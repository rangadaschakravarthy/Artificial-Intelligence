# Day 123 — Merge

## Learning Objectives
- Combine separate DataFrames using database-style join keys via `pd.merge()`.
- Master Inner, Left, Right, and Outer merge types.
- Handle single-key, multi-key, and mismatched key merges effectively.

## Prerequisites
- Day 108: DataFrames
- Level 1 Set Theory (Intersections, Unions)

## Topics Covered
- `pd.merge()` syntax and function parameters
- Merge types: Inner, Left, Right, Outer
- Joining on matching column names (`on='key'`) vs differing names (`left_on`, `right_on`)
- Multi-key joins (`on=['key1', 'key2']`)
- Overlapping column names and custom `suffixes` (`_left`, `_right`)
- Identifying merge origins with `indicator=True`

## Why This Matters
Real-world enterprise data is normalized across multiple database tables. Data scientists must merge relational tables to assemble analytical datasets.

## Real-World Usage
Joining e-commerce Order tables with Customer profile tables and Product catalog tables using primary-foreign key relationships.

## Study Order
1. Read `theory.md` for Venn diagram join intuitions.
2. Review `examples.md` for merge variations.
3. Run `code.py` to see joined outputs.
4. Complete `practice.md` and verify with `solution.md`.

## Practical Work
- Perform Left join on Customer and Transaction DataFrames.
- Use `indicator=True` to audit missing records across tables.

## Interview Preparation
- What is the difference between an Inner Join and a Left Outer Join?
- How does `pd.merge()` handle duplicate key values in both DataFrames (many-to-many join)?

## Completion Checklist
- [ ] I can perform Inner, Left, Right, and Outer merges.
- [ ] I can merge DataFrames with different key column names.
- [ ] I can handle overlapping non-key column names using `suffixes`.
- [ ] I understand how many-to-many merges expand row counts.

## Difficulty
Intermediate
