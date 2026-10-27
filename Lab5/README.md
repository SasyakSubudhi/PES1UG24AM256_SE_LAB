# Lab 5: Static Code Analysis

**Name:** Sasyak Subudhi  
**SRN:** PES1UG24AM256

## Deliverables

- [Updated Python source](supplier_orders.py)
- [PDF report](report.pdf) and [editable report](report.md)
- [Issue table](issues.md)
- [Reflections](reflection.md)
- [Before-analysis reports](reports/before)
- [After-analysis reports](reports/after)
- [Executed tests](reports/tests.txt) and [demo output](reports/demo.txt)
- [Regression test source](test_supplier_orders.py)
- [Tool versions](requirements-tools.txt)

## Verified results

| Tool | Before | After |
|---|---|---|
| Pylint | 2.41/10 | 10.00/10 |
| Bandit | 3 findings | 0 findings |
| Flake8 | 4 findings | 0 findings |

All eight regression tests passed. The empty final Flake8 report is expected; its recorded exit code is 0.

## Three fix commits

The three Lab 5 commits on this repository's main branch separately record Bandit security fixes, Pylint code-quality fixes, and Flake8 formatting plus final deliverables. They reproduce the three local preparation stages within this repository's existing history.

The PDF, report.md and SUBMISSION_README.md were prepared before this upload; their statements about local commits and no remote upload describe that preparation stage. The submission is now available in this Lab5 folder. The local ZIP and its embedded original Git history remain an offline copy. No LMS submission was performed.

## Reproduce

Create and activate a Python 3.12 virtual environment, then run from this folder:

```text
python -m pip install -r requirements-tools.txt
python supplier_orders.py
python -m pylint --rcfile= --persistent=no supplier_orders.py
python -m bandit -r supplier_orders.py
python -m flake8 --isolated supplier_orders.py
python -m unittest -v
```

The supplied handout omitted the reflection questions referenced in the assignment README. reflection.md clearly labels the four learning-outcome prompts used instead.

[Original assignment README](ASSIGNMENT_README.md)
