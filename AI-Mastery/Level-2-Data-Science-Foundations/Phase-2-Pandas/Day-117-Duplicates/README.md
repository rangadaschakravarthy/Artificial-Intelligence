# Day 117 — Duplicates

## Learning Objectives
- Master detecting duplicate rows (`duplicated()`) and dropping duplicates (`drop_duplicates()`).
- Understand exact full-row duplicates vs column-subset duplicates.
- Learn duplicate retention strategies (`keep='first'`, `keep='last'`, `keep=False`).

## Prerequisites
- Day 108: DataFrames
- Day 111: Inspecting Datasets

## Topics Covered
1. Detecting duplicate rows (`df.duplicated()`)
2. Multi-column subset duplicate detection (`subset=['col1', 'col2']`)
3. Retention rules (`keep='first'`, `keep='last'`, `keep=False`)
4. Dropping duplicate rows (`df.drop_duplicates()`)
5. Identifying duplicate primary keys and index labels

## Why This Matters
Duplicate records distort statistical aggregations, artificially inflate sample sizes, and cause data leakage between training and evaluation splits.

## Real-World Usage
Deduplicating transaction logs or user registration tables based on unique `User_ID` or `Email`.

## Study Order
1. Read `theory.md`.
2. Review `examples.md`.
3. Complete `practice.md`.
4. Verify using `solution.md`.
5. Run `code.py`.

## Completion Checklist
- [ ] I can detect duplicate rows using `df.duplicated()`.
- [ ] I can drop duplicate rows using `df.drop_duplicates()`.
- [ ] I understand `keep='first'`, `keep='last'`, and `keep=False`.
- [ ] I can check for duplicate primary keys in ID columns.

## Difficulty
Beginner
