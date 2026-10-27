# Identified issues and fixes

Line numbers refer to the original source unless marked final. Bandit severity is tool-reported; Pylint and Flake8 categories are descriptive, not Bandit risk ratings.

| Issue | Type / severity | Line(s) | Description | Fix approach |
|---|---|---|---|---|
| B605 / Bandit | High | 21 | Supplier input was concatenated into os.system(), allowing shell metacharacters to run commands. | Replace the shell call with print(); supplier text is treated literally (final 35-37). |
| B608 / Bandit | Medium | 11 | String interpolation built an INSERT statement from supplier and item input. Quotes could break the query or alter its meaning. | Bind supplier, item and quantity with SQLite ? placeholders (final 19-23). |
| B110 / Bandit; W0718 / Pylint | Low / quality | 25-28 | A broad except Exception followed by pass hid failed cleanup operations. | Remove the catch so sqlite3 errors propagate; verify with a missing-table test (final 40-42). |
| W0603 / Pylint | Quality | 6, 10, 12 | The cumulative order quantity depended on mutable global state. | Keep the total in main and explicitly pass the prior total to place_order (final 17-25, 56-59). |
| W0621 / Pylint | Quality | 4, 9, 16, 24, 31 | Function parameters shadowed the module-level connection. | Create the connection inside a factory; pass a local connection explicitly and close it in main (final 7-14, 54-55). |
| W0613 / Pylint | Quality | 16 | remarks was accepted but never stored or used. | Remove the unused parameter and update the demonstration call (final 28, 60). |
| C0103 / Pylint | Convention | 9, 16, 20, 31 | Mixed-case function names violated Python naming conventions. | Rename functions and call sites to snake_case. |
| C0114, C0116 / Pylint | Convention | 1, 9, 16, 20, 24, 31, 35 | Module and public functions lacked docstrings. | Add module and function docstrings describing purpose and return values. |
| C0301 / Pylint; E501 / Flake8 | Style | 5, 11, 32 | SQL statements and query expressions exceeded line-length limits. | Use parenthesized multiline expressions and adjacent SQL string literals, keeping lines within 79 characters. |
| E225 / Flake8 | Style | 12 | order_total+=quantity lacked operator spacing. | Use order_total += quantity (final 24). |
| C0209 / Pylint | Convention | 11 | The original string-formatting expression also triggered a formatting suggestion. | Parameterized SQL removes the formatting expression; an f-string would retain the injection risk. |
