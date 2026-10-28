# Lab 5: Static Code Analysis — Issue Report

## Project: Pharmacy Stock Management System

### PES2UG24CS015

The original Python program was analyzed using Pylint, Bandit, and Flake8 to identify code quality issues, potential security vulnerabilities, and formatting violations.

## Issue Table

| Issue | Type | Original Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| SQL injection risk | Security | 21 | The SQL query used string formatting to insert the patient name, potentially allowing SQL injection. | Replaced string formatting with a parameterized SQL query using a placeholder and a tuple of parameters. |
| Mutable default argument | Bug | 24 | The `add_stock()` function used `batch_log=[]`, which could share a mutable list across function calls. | Changed the default value to `None` and initialized a new list inside the function. |
| Bare exception handling | Code Quality / Security | 38, 58 | Bare `except` blocks caught unspecified exceptions, and one silently ignored errors. | Replaced bare exceptions with specific exception types and added explicit error handling. |
| Unsafe file handling | Code Quality | 50, 57 | Files were opened without context managers or explicit encoding. | Used `with open()` and specified UTF-8 encoding. |
| Missing docstrings | Code Quality | Multiple | The module and functions lacked documentation explaining their purpose. | Added a module docstring and function docstrings. |
| Unused import | Code Quality | 3 | The `os` module was imported but never used. | Removed the unused import. |
| Non-snake-case function name | Style | 61 | The function `printStock()` did not follow Python's snake_case naming convention. | Renamed the function to `print_stock()` and updated its call. |
| Formatting violations | Style | Multiple | The original code contained long lines, incorrect blank-line spacing, and a missing final newline. | Reformatted the code according to Python style conventions and ensured the file ended with a newline. |

## Analysis Results

| Tool | Before Fixes | After Fixes |
|---|---|---|
| Pylint | 6.90/10 | 10.00/10 |
| Bandit | 2 findings: 1 medium severity and 1 low severity | 0 findings |
| Flake8 | Multiple formatting and code style violations | 0 violations |

## Conclusion

Static code analysis identified security, reliability, documentation, and formatting issues in the pharmacy stock management program. After applying the fixes, the program achieved a Pylint score of 10.00/10, Bandit reported no issues, and Flake8 reported no violations. These improvements demonstrate the value of static analysis tools in maintaining secure, readable, and maintainable Python code.
