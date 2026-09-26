# Day 114 — Sorting Data

## Learning Objectives
- Master sorting DataFrames and Series by values (`sort_values()`) and by index (`sort_index()`).
- Perform multi-column sorting with mixed ascending/descending directions.
- Understand sorting algorithms (quicksort, mergesort) and NaN placement options.

## Prerequisites
- Day 108: DataFrames
- Day 109: Index and Columns

## Topics Covered
1. Sorting Series by values (`s.sort_values()`)
2. Sorting DataFrames by one or multiple columns (`df.sort_values(by=...)`)
3. Multi-column sort directions (`ascending=[True, False]`)
4. Sorting by Index labels (`df.sort_index()`)
5. Missing value placement (`na_position='first'` vs `'last'`)

## Why This Matters
Sorting orders data for rank analysis, top-K selection, time-series alignment, and clean visual presentation.

## Real-World Usage
Identifying top 10 highest-spending customers (`df.sort_values(by='Spend', ascending=False).head(10)`).

## Study Order
1. Read `theory.md`.
2. Review `examples.md`.
3. Complete `practice.md`.
4. Verify using `solution.md`.
5. Run `code.py`.

## Completion Checklist
- [ ] I can sort DataFrames by single and multiple columns.
- [ ] I can control ascending vs descending sort order per column.
- [ ] I can sort DataFrames by index labels using `sort_index()`.
- [ ] I can specify `na_position` to place missing values at start or end.

## Difficulty
Beginner
