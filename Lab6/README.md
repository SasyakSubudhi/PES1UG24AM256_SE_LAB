# Lab 6: Code and Branch Coverage Analysis

**Name:** Sasyak Subudhi  
**SRN:** PES1UG24AM256  
**Assigned application:** 18 - ATM Withdrawal

The supplied assignment spreadsheet maps this SRN to [SETAPESU26/L6_L7_18_atm_withdrawal](https://github.com/SETAPESU26/L6_L7_18_atm_withdrawal). The application and starter tests match the assigned source exactly. Source application blob: `8b7e3a40f7efc3af9588cdc1dd2557478ecbafff`; starter test blob: `52c2a0c59e5d82498258733e7cb53f0fa3c074f1`. The name uses the spelling requested by the student; the spreadsheet spells the surname Subuddhi.

## Measured results

| Suite | Tests passed | Statements covered | Branch outcomes covered | Coverage.py score |
| --- | ---: | ---: | ---: | ---: |
| Starter, line mode | 2 | 14/34 (41.18%) | Not measured | 41% |
| Starter, branch mode | 2 | 14/34 (41.18%) | 7/22 (31.82%) | 38% |
| Code coverage | 15 | 34/34 (100%) | Not measured | 100% |
| Branch coverage | 41 | 34/34 (100%) | 22/22 (100%) | 100% |

All suites together: **58 passed**. Coverage is restricted to `atm_withdrawal.py`. Coverage.py's branch-mode score combines statements and branch outcomes; the branch percentage is reported separately above. There are no exclusions, missing statements, missing branches, or partial branches in the final branch run.

## Submission files

- [CodeCoverageTest_atm_withdrawal.py](CodeCoverageTest_atm_withdrawal.py)
- [BranchCoverageTest_atm_withdrawal.py](BranchCoverageTest_atm_withdrawal.py)
- [Coverage analysis](coverage_analysis.md)
- [Code output image](evidence/code_coverage_output.png) and [command log](evidence/code_terminal_output.txt)
- [Branch output image](evidence/branch_coverage_output.png) and [command log](evidence/branch_terminal_output.txt)
- [Code coverage JSON](evidence/code_coverage.json), [branch coverage JSON](evidence/branch_coverage.json), and [all-tests result](evidence/all_tests.txt)

The images are screenshots of a browser transcript viewer showing verbatim output from real command executions. They are not native terminal-window captures. Initial measurements are provided as text and JSON; only final results above 90% are pictured. Native terminal screenshots can be captured after running the commands below if the evaluator requires that exact presentation.

## Reproduce

Run inside `Lab6` using Python 3.12:

```sh
python -m pip install -r requirements.txt
python -m coverage run --source=atm_withdrawal -m pytest -q CodeCoverageTest_atm_withdrawal.py
python -m coverage report -m --fail-under=90
python -m coverage run --branch --source=atm_withdrawal -m pytest -q BranchCoverageTest_atm_withdrawal.py
python -m coverage report -m --fail-under=90
python -m pytest -q
```

`pytest.ini` enables discovery of both required capitalized filenames. Each coverage run replaces the prior measurement. The submission is split into a code-coverage commit and a branch-coverage commit. This work follows the supplied Lab 6 handout; the spreadsheet also mentions Lab 7, for which no handout was supplied.
