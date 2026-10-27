# Submission contents

- report.pdf: readable lab report with results, issue table and reflections.
- report.md: editable report source; issues.md and reflection.md are separate required sections.
- supplier_orders.py: cleaned assigned source.
- reports/before and reports/after: all three raw tool reports, stderr and run metadata.
- reports/tests.txt and reports/demo.txt: executed behavior checks.
- test_supplier_orders.py: eight regression tests.
- requirements-tools.txt: exact versions of the three analysis tools.
- .git: original repository history plus three lab commits.

## Reproduce

Use Python 3.12. Create a virtual environment with `python -m venv .venv`, activate it, then run `python -m pip install -r requirements-tools.txt`.
Run the commands in report.md. Inspect the three lab commits with `git log -3 --oneline`.
The empty reports/after/flake8_report.txt means Flake8 found no issues; run_metadata.json confirms exit code 0.
The local Git email is an SRN-based placeholder. Nothing has been uploaded or submitted remotely.
