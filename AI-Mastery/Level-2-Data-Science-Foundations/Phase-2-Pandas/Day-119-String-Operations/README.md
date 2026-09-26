# Day 119 — String Operations

## Learning Objectives
- Master vectorized string accessor `.str` methods in Pandas.
- Learn text cleaning operations (`lower()`, `strip()`, `replace()`, `split()`, `contains()`).
- Use Regular Expressions (regex) for advanced pattern extraction.

## Prerequisites
- Day 107: Series
- Day 118: Data Type Conversion

## Topics Covered
1. Vectorized String Accessor `.str`
2. Case conversion and whitespace stripping (`lower()`, `upper()`, `strip()`)
3. Substring replacement and splitting (`replace()`, `split()`, `cat()`)
4. Pattern detection and extraction (`contains()`, `extract()`)
5. Data cleaning workflows for messy text columns

## Why This Matters
Real-world categorical text columns contain leading spaces, mixed casing, currency symbols, and extra characters that corrupt grouping and modeling.

## Real-World Usage
Cleaning dirty product names or user email addresses before categorical feature encoding.

## Study Order
1. Read `theory.md`.
2. Review `examples.md`.
3. Complete `practice.md`.
4. Verify using `solution.md`.
5. Run `code.py`.

## Completion Checklist
- [ ] I can use `.str` accessor methods on Series.
- [ ] I can clean text casing and strip whitespace.
- [ ] I can split string columns into multiple feature columns.
- [ ] I can extract text patterns using regular expressions.

## Difficulty
Intermediate
