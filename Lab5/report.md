# Lab 5: Static Code Analysis

**Name:** Sasyak Subudhi  
**SRN:** PES1UG24AM256  
**Date:** 27 October 2026  
**Program:** Supplier Purchase Order Tracker  
**Assigned repository:** https://github.com/SETAPESU26/L5_18_supplier_orders  
**Original revision:** 9b72a43356daac383db067724cb5cdccd7dccd4b

## Results

| Tool | Before | After |
|---|---|---|
| Pylint 4.1.3 | 2.41/10; 22 messages; exit 20 | 10.00/10; no messages; exit 0 |
| Bandit 1.9.4 | 3 findings: 1 high, 1 medium, 1 low; exit 1 | 0 findings; exit 0 |
| Flake8 7.4.1 | 4 findings (3 E501, 1 E225); exit 1 | 0 findings; exit 0 |

Python 3.12.14 on Windows. The original and final demonstrations both print:

```
notifying warehouse about Acme
1 540
```

## Method and evidence

The SRN was matched to row 19 of the supplied assignment workbook. Original code was cloned from the assigned repository and retained in reports/before/original_source.txt. The original demonstration was run, followed by all three tools. Fixes were grouped into three local commits: Bandit security fixes; Pylint quality fixes; Flake8 style fixes and final evidence. No findings were disabled or suppressed.

Commands run from the repository directory (with the lab environment activated):

```
python supplier_orders.py
python -m pylint --rcfile= --persistent=no supplier_orders.py
python -m bandit -r supplier_orders.py
python -m flake8 --isolated supplier_orders.py
python -m unittest -v
```

Pylint uses an empty configuration selection and disables its historical cache; Flake8 uses isolated mode. The raw standard output, standard error and command exit codes are retained under reports/before and reports/after. Flake8's empty final report is expected: its exit code is zero. All results refer to supplier_orders.py only. The test file is a separate behavior-checking artifact.

## Behavior verification and scope

Eight tests passed (reports/tests.txt). They cover preserved demo output, quoted/SQL-like supplier input, literal notification output without os.system, received-order cleanup that retains pending orders, database error propagation, cumulative totals after cleanup, independent database state, and import without running the demo. reports/demo.txt records the final demonstration.

The code still uses a transient SQLite database and prints a warehouse notification. The refactor changes function names to snake_case and removes the unused remarks parameter. Cumulative quantity is now explicitly passed and returned; callers must pass the previous total when accumulating orders. main() manages the transaction and closes its database. Importing the module no longer runs the demonstration. These API changes are reflected in all call sites and tests; no external callers are present in the assigned repository.

## Submission notes

The repository contains three new local commits on lab5-pes1ug24am256, with the upstream history preserved. The local Git identity is Sasyak Subudhi <PES1UG24AM256@localhost>; the address is an SRN-based local placeholder, not a verified email or GitHub identity. No remote push or LMS submission was performed. The ZIP preserves the .git directory so the three commits can be inspected after extraction.

The supplied handout has no explicit reflection questions despite the README referring to four. reflection.md provides four clearly labeled learning-outcome reflections. Review them for alignment with any questions supplied separately in class.

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

# Reflections

The supplied three-page handout does not contain the four reflection questions referenced by the repository README. The following four prompts cover the stated learning outcomes and are not quoted official questions.

## 1. How do the three tools complement one another?

Pylint identifies maintainability and likely programming problems, such as global state, shadowed names, unused arguments and missing documentation. Bandit focuses on security patterns, including SQL construction and shell execution. Flake8 checks Python style and related coding mistakes. Their findings overlap, but none covers the entire program.

## 2. Which issues should be fixed first, and why?

The high-severity shell-injection finding B605 takes priority, followed by the medium-severity SQL-injection finding B608. Both involve interpreting supplier-controlled text as executable syntax. Printing notifications and binding SQL parameters remove those interpretation steps. Silent exception handling should then be removed so failures remain visible.

## 3. How were the changes verified?

All three tools were run against the original file and the final file with the same versions. Pylint improved from 2.41/10 to 10.00/10; Bandit fell from three findings to zero; Flake8 fell from four findings to zero. Eight regression tests check demonstration output, SQL payload handling, notification behavior, cleanup, visible errors, cumulative totals, independent databases and safe imports.

## 4. What are the limitations and lessons of static analysis?

A clean tool report does not prove correctness or security. Static tools did not directly flag the unguarded main() call or the missing explicit connection close; those were found by inspection. Runtime tests were needed to verify behavior. The practical lesson is to combine static analysis, source review and targeted tests, and to fix the underlying problem instead of suppressing warnings.

