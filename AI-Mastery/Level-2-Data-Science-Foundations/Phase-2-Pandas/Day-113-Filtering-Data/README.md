# Day 113 — Filtering Data

## Learning Objectives
- Master conditional row filtering in Pandas (`df[condition]`, `df.query()`).
- Combine multi-condition queries using bitwise operators (`&`, `|`, `~`).
- Filter data using membership (`isin()`), range checks (`between()`), and string masks.

## Prerequisites
- Day 94: Boolean and Fancy Indexing
- Day 112: Selecting Data

## Topics Covered
1. Boolean Mask Filtering (`df[df['col'] > val]`)
2. Multi-Condition Filtering (`&` AND, `|` OR, `~` NOT)
3. Membership Filtering with `.isin([])`
4. Numerical Range Filtering with `.between(left, right)`
5. String Pattern Filtering (`df['col'].str.contains()`) & `df.query()`

## Why This Matters
Filtering data enables extracting target sub-populations (e.g. active users, specific categories, valid transactions) during data cleaning and EDA.

## Real-World Usage
Filtering fraudulent transactions where `Amount > 5000` AND `Country != 'Home'`.

## Study Order
1. Read `theory.md`.
2. Review `examples.md`.
3. Complete `practice.md`.
4. Verify using `solution.md`.
5. Run `code.py`.

## Completion Checklist
- [ ] I can filter DataFrames using single and multiple conditions.
- [ ] I know how to use `.isin()` for multi-category matching.
- [ ] I can use `.between()` for numerical range queries.
- [ ] I can query DataFrames using `df.query()`.

## Difficulty
Beginner
