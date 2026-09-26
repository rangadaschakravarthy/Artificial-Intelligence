# Day 109 — Index and Columns

## Learning Objectives
- Master Pandas `Index` objects for row labels and column headers.
- Learn setting, resetting, and manipulating index structures (`set_index`, `reset_index`).
- Understand multi-indexing concepts and index alignment.

## Prerequisites
- Day 108: DataFrames

## Topics Covered
1. What is a Pandas `Index` object (`df.index`, `df.columns`)
2. Setting a column as Index (`df.set_index()`)
3. Resetting Index back to default integer range (`df.reset_index()`)
4. Index modification and immutability rules
5. Introduction to MultiIndex (Hierarchical Indexing)

## Why This Matters
Index labels enable fast row selection, automatic dataset merging/joining, and time-series alignment.

## Real-World Usage
Setting timestamp columns or unique ID columns (e.g., `Date` or `User_ID`) as the primary DataFrame index.

## Study Order
1. Read `theory.md`.
2. Review `examples.md`.
3. Complete `practice.md`.
4. Verify using `solution.md`.
5. Run `code.py`.

## Completion Checklist
- [ ] I can set a column as index using `set_index()`.
- [ ] I can reset an index back to default using `reset_index()`.
- [ ] I understand that Pandas Index objects are immutable.
- [ ] I can check index properties like `.is_unique`.

## Difficulty
Beginner
