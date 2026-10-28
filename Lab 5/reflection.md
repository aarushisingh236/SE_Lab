# Reflection
### PES2UG24CS015

## 1. What is static code analysis, and why is it important?

Static code analysis is the process of examining source code without executing it to identify potential bugs, security vulnerabilities, and coding standard violations. It helps improve code quality, security, readability, and maintainability by detecting problems early in development.

## 2. What are the differences between Pylint, Bandit, and Flake8?

Pylint checks code quality, logical issues, naming conventions, and documentation. Bandit identifies potential security vulnerabilities and unsafe coding practices. Flake8 checks Python code for formatting errors and violations of PEP 8 style guidelines. Using all three tools provides a more comprehensive analysis of the code.

## 3. What issues were identified in the pharmacy stock management program, and how were they fixed?

The analysis identified a potential SQL injection vulnerability, a mutable default argument, broad exception handling, unsafe file handling, missing docstrings, and formatting violations. These issues were addressed by using parameterized SQL queries, replacing the mutable default with `None`, specifying exception types, using context managers for file operations, adding docstrings, and correcting formatting issues.

## 4. How did static code analysis improve the quality and security of the program?

Static code analysis helped identify and resolve issues that could affect the program's security, reliability, and maintainability. After the fixes, the Pylint score improved from 6.90/10 to 10.00/10, Bandit reported zero issues, and Flake8 reported no violations. This demonstrated how static analysis tools can help developers produce cleaner, safer, and more maintainable code.

## 5. What challenges did you encounter while performing static code analysis on the pharmacy stock management program?

The pharmacy stock management program contained several issues, including an SQL injection risk in the patient lookup function, a mutable default argument in the stock management function, and broad exception handling in the prescription dispensing and stock loading functions. The program also had file-handling and code formatting issues. I resolved these by using parameterized SQL queries, initializing mutable values safely, handling specific exceptions, using context managers for file operations, and following Python naming and documentation conventions. After applying the fixes, Pylint achieved a score of 10.00/10, Bandit reported no security issues, and Flake8 reported no formatting violations. This exercise helped me understand how static analysis tools can improve the reliability, security, and maintainability of an existing application.