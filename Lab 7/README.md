# LAB 7 SE – Fuzz Testing with Hypothesis

## About
This lab focuses on **Fuzz Testing (Property-Based Testing)** using the Hypothesis library in Python.

The objective is to test the Pet Walking Service application with automatically generated inputs to identify unexpected errors, crashes and input-validation issues.

## Functions Tested

1. **parse_walk_schedule()** – Parses pet walking schedules and calculates the total fee.
2. **compute_pace_per_pet()** – Calculates the walking time per pet.
3. **lookup_temperament_surcharge()** – Returns additional charges based on pet temperament.

## Tools & Technologies
- Python 3.13
- Hypothesis
- Pytest

## Project Structure

```text
LAB7/
│
├── processor.py
├── test_processor.py
└── README.md
```

## Implementation
- Used Hypothesis `@given()` and strategies to generate random inputs, including strings and None values.
- Identified input-validation issues through fuzz testing.
- Added exception handling and input validation to prevent unexpected crashes.
- Implemented additional functional tests for valid and invalid inputs.

## How to Run

Install dependencies:

```bash
pip install hypothesis pytest
```

Run the application:

```bash
python processor.py
```

Run the test suite:

```bash
python -m pytest test_processor.py
```

## Test Results
The final test suite contains **9 tests**, including 3 property-based fuzz tests and 6 functional/validation tests.

**Result: 9 passed.**

## Conclusion
This lab demonstrates how property-based fuzz testing helps identify edge cases and improve software reliability by testing functions against a wide range of automatically generated inputs.
