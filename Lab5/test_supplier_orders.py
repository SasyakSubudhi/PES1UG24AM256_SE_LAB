"""Behavior and security regression checks for the lab solution."""
import contextlib
import importlib
import io
import sqlite3
import unittest
from unittest.mock import patch

import supplier_orders as orders


class SupplierOrdersTests(unittest.TestCase):
    def setUp(self):
        self.connection = orders.create_database()
        self.addCleanup(self.connection.close)

    def test_demo_output(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            orders.main()
        self.assertEqual(output.getvalue(),
                         'notifying warehouse about Acme\n1 540\n')

    def test_sql_payload_is_stored_as_data(self):
        supplier = "O'Reilly'); DROP TABLE orders; --"
        orders.place_order(self.connection, supplier, "bolt's", 4)
        row = self.connection.execute(
            'SELECT supplier, item, quantity FROM orders'
        ).fetchone()
        self.assertEqual(row, (supplier, "bolt's", 4))
        self.assertEqual(orders.pending_count(self.connection), 1)

    def test_notification_does_not_call_shell(self):
        supplier = 'Acme & echo INJECTED'
        output = io.StringIO()
        with patch('os.system') as shell, \
                contextlib.redirect_stdout(output):
            orders.notify_warehouse(supplier)
        shell.assert_not_called()
        self.assertEqual(output.getvalue(),
                         'notifying warehouse about ' + supplier + '\n')

    def test_received_cleanup_preserves_pending_orders(self):
        orders.place_order(self.connection, 'Acme', 'rods', 40)
        orders.place_order(self.connection, 'Bolt Co', 'bolts', 500, 40)
        orders.mark_received(self.connection, 1)
        self.assertEqual(orders.pending_count(self.connection), 1)
        orders.cleanup(self.connection)
        self.assertEqual(self.connection.execute(
            'SELECT supplier FROM orders').fetchall(), [('Bolt Co',)])
        orders.cleanup(self.connection)
        self.assertEqual(orders.pending_count(self.connection), 1)

    def test_database_errors_are_visible(self):
        self.connection.execute('DROP TABLE orders')
        with self.assertRaises(sqlite3.OperationalError):
            orders.cleanup(self.connection)

    def test_total_stays_cumulative_after_cleanup(self):
        total = orders.place_order(self.connection, 'Acme', 'rods', 40)
        orders.mark_received(self.connection, 1)
        orders.cleanup(self.connection)
        total = orders.place_order(self.connection, 'Bolt Co', 'bolts',
                                   500, total)
        self.assertEqual(total, 540)

    def test_new_database_has_independent_state(self):
        orders.place_order(self.connection, 'Acme', 'rods', 40)
        with contextlib.closing(orders.create_database()) as other:
            self.assertEqual(orders.pending_count(other), 0)
            self.assertEqual(orders.place_order(other, 'Bolt', 'nuts', 5), 5)

    def test_import_has_no_demo_side_effects(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            importlib.reload(orders)
        self.assertEqual(output.getvalue(), '')
        self.assertFalse(hasattr(orders, 'conn'))


if __name__ == '__main__':
    unittest.main()
