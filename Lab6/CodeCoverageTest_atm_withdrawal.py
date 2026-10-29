"""Line coverage: Sasyak Subudhi, PES1UG24AM256."""
import pytest
from atm_withdrawal import withdraw, pin_check, note_breakup


@pytest.mark.parametrize('balance,amount,account,own_bank,expected', [
    (5000, 1000, 'savings', True, 4000),
    (5000, 1000, 'current', False, 3980),
    (20000, 11000, 'savings', False, 8970),
    (50000, 25100, 'savings', True, 'limit exceeded'),
    (1000, 1000, 'savings', False, 'insufficient funds'),
])
def test_withdrawal_statements(balance, amount, account, own_bank, expected):
    assert withdraw(balance, amount, account, own_bank) == expected


@pytest.mark.parametrize('amount,account,message', [
    (100, 'other', 'unknown account'), (0, 'savings', 'invalid amount'),
    (150, 'savings', 'invalid amount'),
])
def test_invalid_withdrawal(amount, account, message):
    with pytest.raises(ValueError, match='^' + message + '$'):
        withdraw(5000, amount, account, True)


@pytest.mark.parametrize('entered,attempts,expected', [
    (1234, 0, 'ok'), (1234, 3, 'card blocked'),
    (9999, 2, 'card blocked'), (9999, 1, 'retry'),
])
def test_pin_statements(entered, attempts, expected):
    assert pin_check(entered, 1234, attempts) == expected


@pytest.mark.parametrize('amount,expected', [(0, (0, 0, 0)), (800, (1, 1, 1))])
def test_note_statements(amount, expected):
    assert note_breakup(amount) == expected


def test_invalid_notes():
    with pytest.raises(ValueError, match='^invalid amount$'):
        note_breakup(150)
