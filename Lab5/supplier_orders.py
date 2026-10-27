"""Track supplier purchase orders in an in-memory SQLite database."""

from contextlib import closing
import sqlite3


def create_database():
    """Create a database connection and initialize the orders table."""
    connection = sqlite3.connect(":memory:")
    connection.execute(
        "CREATE TABLE orders (id INTEGER PRIMARY KEY, supplier TEXT, "
        "item TEXT, quantity INTEGER, received INTEGER)"
    )
    return connection


def place_order(connection, supplier, item, quantity, order_total=0):
    """Insert an order and return the caller's updated cumulative quantity."""
    connection.execute(
        "INSERT INTO orders (supplier, item, quantity, received) "
        "VALUES (?, ?, ?, 0)",
        (supplier, item, quantity),
    )
    order_total += quantity
    return order_total


def mark_received(connection, order_id):
    """Mark an existing order as received."""
    connection.execute(
        "UPDATE orders SET received = 1 WHERE id = ?", (order_id,)
    )


def notify_warehouse(supplier):
    """Print a warehouse notification without interpreting shell commands."""
    print("notifying warehouse about " + supplier)


def cleanup(connection):
    """Delete received orders, allowing database errors to reach the caller."""
    connection.execute("DELETE FROM orders WHERE received = 1")


def pending_count(connection):
    """Return the number of orders awaiting delivery."""
    return connection.execute(
        "SELECT COUNT(*) FROM orders WHERE received = 0"
    ).fetchone()[0]


def main():
    """Demonstrate placing orders, receiving a delivery, and cleaning up."""
    with closing(create_database()) as connection:
        with connection:
            order_total = place_order(connection, "Acme Steel", "rods", 40)
            order_total = place_order(
                connection, "Bolt Co", "bolts", 500, order_total
            )
            mark_received(connection, 1)
            notify_warehouse("Acme")
            print(pending_count(connection), order_total)
            cleanup(connection)


if __name__ == "__main__":
    main()
