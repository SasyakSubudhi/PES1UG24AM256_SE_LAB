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

