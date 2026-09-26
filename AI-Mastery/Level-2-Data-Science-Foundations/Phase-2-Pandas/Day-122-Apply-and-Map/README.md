# Day 122 — Apply and Map

## Learning Objectives
- Transform Series data using `.map()` and `.replace()`.
- Apply custom functions across Series and DataFrames using `.apply()`.
- Perform group-wise vectorized feature transformations using `.transform()`.

## Prerequisites
- Day 107: Series
- Day 108: DataFrames
- Python Functions & Lambda Expressions

## Topics Covered
- `Series.map()` for element-wise dictionary and function mapping
- `Series.apply()` vs `DataFrame.apply()`
- Row-wise (`axis=1`) vs Column-wise (`axis=0`) operations
- `GroupBy.transform()` for broadcasted group-level calculations
- Vectorized alternatives vs `.apply()` performance tradeoffs

## Why This Matters
Data transformation often requires custom business logic (e.g. converting temperature units, categorizing continuous variables into discrete risk tiers, scaling variables within groups).

## Real-World Usage
Credit scoring engines apply complex non-linear mathematical transformations and custom risk rules across applicant records.

## Study Order
1. Read `theory.md` to understand `.map()`, `.apply()`, and `.transform()`.
2. Study `examples.md` for `axis=1` row transformations.
3. Run `code.py` to compare execution outputs.
4. Complete `practice.md` and review `solution.md`.

## Practical Work
- Map categorical string keys to numerical integer codes.
- Apply a custom row-level row calculation computing BMI from Height and Weight columns.

## Interview Preparation
- What is the crucial difference between `.apply()` and `.transform()` on a GroupBy object?
- Why is `.map()` faster than `.apply()` for element-wise dictionary substitutions on a Series?

## Completion Checklist
- [ ] I can map dictionary keys to Series values using `.map()`.
- [ ] I can apply custom functions across rows using `df.apply(..., axis=1)`.
- [ ] I understand `GroupBy.transform()`.
- [ ] I know when to avoid `.apply()` in favor of vectorized operations.

## Difficulty
Intermediate
