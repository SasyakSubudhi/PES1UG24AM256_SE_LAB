# Coverage analysis

Sasyak Subudhi | PES1UG24AM256

## Coverage concepts

Statement coverage asks whether executable statements ran. Branch coverage checks alternative control-flow outcomes of decisions. Executing every statement does not necessarily exercise both outcomes of every decision. Path coverage concerns full sequences of decisions; function coverage concerns invoking functions. Statement and branch coverage are quantified here; neither complete path coverage nor condition coverage is claimed.

## Initial tests

The two supplied cases check an own-bank withdrawal and a correct PIN on the first attempt. They execute 14/34 statements (41.18%) and 7/22 branch outcomes (31.82%). The branch-mode combined score is 38%. Missing behavior includes invalid account/amount handling, daily limits, other-bank fees, insufficient balances, blocked or incorrect PINs, and note breakup.

## Code coverage suite

Five withdrawal scenarios cover success, ordinary other-bank fees, high-value other-bank fees, the daily limit and insufficient funds. Three invalid cases reach unknown-account and invalid-amount exceptions. Four PIN cases reach every return. Two valid note cases cover the remainder decision and a third checks invalid notes.

The 15 cases execute 34/34 statements: 100% statement coverage.

## Branch coverage suite

| Area | Cases and expected behavior |
| --- | --- |
| Account validation | Unknown account raises ValueError before amount validation |
| Amount validation | Negative, zero, and positive nonmultiples of 100 are rejected |
| Daily limits | Savings 25000 and current 50000, each tested at limit-100, limit, and limit+100 |
| Fee threshold | Other-bank amounts 9900 and 10000 charge 20; 10100 and 11000 charge 30; own-bank transactions charge zero |
| Funds including fees | Balance equals amount+fee-1, amount+fee, and amount+fee+1; expected insufficient funds, zero balance, and balance one |
| PIN decisions | Correct and wrong PINs at attempts 0, 1, 2 and 3; already-blocked attempts override even a correct PIN |
| Note breakup | 0 through 1000 in 100 increments, plus 25100; each exact tuple and reconstructed total are asserted |
| Invalid note amount | 1, 99, 101 and 150 raise ValueError |

The 41 cases cover 34/34 statements and 22/22 branch outcomes, with zero partial branches. All 58 tests, including the supplied starter cases, pass together.

## Interpretation

Both final coverage measures exceed the handout's 90% thresholds. Equality tests check limit and fee boundaries. Balance assertions verify that fees participate in affordability checks. Correct-PIN tests at attempts 2 and 3 verify the distinction between a final allowed attempt and an already blocked card. Note tests verify denominations and conservation of the requested amount.

The `amount <= 0 or amount % 100 != 0` condition is exercised with each reason for invalidity and with a valid amount, although coverage.py reports control-flow branches rather than independent Boolean-condition coverage. All three functions are invoked, but a separate function-coverage percentage is not reported.

No application changes or coverage exclusions were used. Full measured coverage does not prove all possible paths or arbitrary input types correct. The supplied note function does not explicitly reject negative multiples of 100; that design limitation is documented without redefining its contract. Evidence PNGs display real command output through a transcript viewer; text logs and JSON retain inspectable measurements.
