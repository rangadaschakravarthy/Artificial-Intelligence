# Day 116 — Handling Missing Values

## Learning Objectives
- Master techniques for handling missing data: dropping (`dropna()`) vs imputing (`fillna()`).
- Learn Mean, Median, Mode, Forward Fill (`ffill`), and Backward Fill (`bfill`) imputation strategies.
- Perform group-based statistical imputation.

## Prerequisites
- Day 115: Missing Values

## Topics Covered
1. Dropping missing data (`df.dropna()`, `how`, `thresh`, `subset`)
2. Constant and statistical imputation (`fillna(val)`, `mean`, `median`, `mode`)
3. Sequential propagation (`fillna(method='ffill')`, `bfill`)
4. Group-based imputation using `groupby().transform()`
5. Dangers of careless imputation and data leakage considerations

## Why This Matters
How you handle missing data directly impacts model bias, sample size, and generalization performance.

## Real-World Usage
Imputing missing customer income using group medians based on job title (`df.groupby('Job')['Income'].transform('median')`).

## Study Order
1. Read `theory.md`.
2. Review `examples.md`.
3. Complete `practice.md`.
4. Verify using `solution.md`.
5. Run `code.py`.

## Completion Checklist
- [ ] I can drop missing rows or columns using `dropna()`.
- [ ] I can impute missing values with mean, median, or mode using `fillna()`.
- [ ] I can use forward fill and backward fill for time-series data.
- [ ] I can perform group-based statistical imputation.

## Difficulty
Intermediate
