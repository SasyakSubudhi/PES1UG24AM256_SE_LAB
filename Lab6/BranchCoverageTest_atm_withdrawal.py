"""Branch and boundary coverage: Sasyak Subudhi, PES1UG24AM256."""
import pytest
from atm_withdrawal import withdraw, pin_check, note_breakup


@pytest.mark.parametrize('amount', [-100, 0, 1, 99, 101, 150])
def test_invalid_amounts(amount):
    with pytest.raises(ValueError, match='^invalid amount$'):
        withdraw(100000, amount, 'savings', True)


def test_unknown_account_checked_first():
    with pytest.raises(ValueError, match='^unknown account$'):
        withdraw(100000, 0, 'other', False)


@pytest.mark.parametrize('account,limit', [('savings', 25000), ('current', 50000)])
def test_daily_limit_boundaries(account, limit):
    assert withdraw(100000, limit - 100, account, True) == 100000 - limit + 100
    assert withdraw(100000, limit, account, True) == 100000 - limit
    assert withdraw(100000, limit + 100, account, True) == 'limit exceeded'


@pytest.mark.parametrize('amount,own_bank,fee', [
    (100, True, 0), (100, False, 20),
    (9900, False, 20), (10000, False, 20), (10100, False, 30),
    (11000, True, 0), (11000, False, 30),
])
def test_fee_and_balance_boundaries(amount, own_bank, fee):
    assert withdraw(amount + fee - 1, amount, 'savings', own_bank) == 'insufficient funds'
    assert withdraw(amount + fee, amount, 'savings', own_bank) == 0
    assert withdraw(amount + fee + 1, amount, 'savings', own_bank) == 1


@pytest.mark.parametrize('entered,attempts,expected', [
    (1234, 0, 'ok'), (1234, 1, 'ok'), (1234, 2, 'ok'),
    (9999, 0, 'retry'), (9999, 1, 'retry'), (9999, 2, 'card blocked'),
    (1234, 3, 'card blocked'), (9999, 3, 'card blocked'),
    (1234, 4, 'card blocked'),
])
def test_pin_boundaries(entered, attempts, expected):
    assert pin_check(entered, 1234, attempts) == expected


@pytest.mark.parametrize('amount,expected', [
    (0, (0, 0, 0)), (100, (0, 0, 1)), (200, (0, 1, 0)),
    (300, (0, 1, 1)), (400, (0, 2, 0)), (500, (1, 0, 0)),
    (600, (1, 0, 1)), (700, (1, 1, 0)), (800, (1, 1, 1)),
    (900, (1, 2, 0)), (1000, (2, 0, 0)), (25100, (50, 0, 1)),
])
def test_note_boundaries(amount, expected):
    result = note_breakup(amount)
    assert result == expected
    assert sum(count * value for count, value in zip(result, [500, 200, 100])) == amount


@pytest.mark.parametrize('amount', [1, 99, 101, 150])
def test_non_multiple_notes(amount):
    with pytest.raises(ValueError, match='^invalid amount$'):
        note_breakup(amount)
