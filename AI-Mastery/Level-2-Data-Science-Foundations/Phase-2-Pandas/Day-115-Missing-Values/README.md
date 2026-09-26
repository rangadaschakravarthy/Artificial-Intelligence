# Day 115 — Missing Values

## Learning Objectives
- Understand how missing data is represented in Pandas (`NaN`, `None`, `pd.NA`).
- Master detecting missing data (`isna()`, `notna()`, `.sum()`, `.mean()`).
- Learn the causes and patterns of missing data (MCAR, MAR, MNAR).

## Prerequisites
- Day 108: DataFrames
- Day 111: Inspecting Datasets

## Topics Covered
1. Missing value representations (`np.nan`, `None`, `pd.NA`, `NaT`)
2. IEEE 754 Floating point `NaN` behavior (`np.nan != np.nan`)
3. Detecting missing values (`df.isna()`, `df.notna()`)
4. Aggregating missing metrics (Counts, Percentages per column)
5. Statistical taxonomy of missing data (MCAR, MAR, MNAR)

## Why This Matters
Real-world datasets are littered with missing data. Detecting and understanding missingness patterns is mandatory before data cleaning.

## Real-World Usage
Auditing missing data percentages across a 100-feature medical dataset before deciding which features to drop or impute.

## Study Order
1. Read `theory.md`.
2. Review `examples.md`.
3. Complete `practice.md`.
4. Verify using `solution.md`.
5. Run `code.py`.

## Completion Checklist
- [ ] I understand `NaN`, `None`, and `pd.NA` representations.
- [ ] I can explain why `np.nan == np.nan` evaluates to `False`.
- [ ] I can calculate missing value counts and percentages per column.
- [ ] I understand MCAR, MAR, and MNAR missing data patterns.

## Difficulty
Intermediate
