# Day 109 Practice Questions: Index and Columns

## Level 1 — Basic
1. What attribute accesses row labels of a DataFrame?
2. What attribute accesses column header labels of a DataFrame?
3. How do you set column `'ID'` as the DataFrame row index?
4. What parameter in `.reset_index()` prevents the old index from becoming a new column?
5. True or False: You can modify an index element directly via `df.index[0] = 'X'`.

## Level 2 — Coding
6. Set column `'Date'` as index for DataFrame `df` in-place.
7. Reset index of DataFrame `df` and drop the old index.
8. Check if DataFrame index has duplicate values using `.is_unique`.
9. Rename column `'A'` to `'Alpha'` and row index `'r1'` to `'Row1'`.
10. Convert DataFrame column headers to a list of uppercase strings using `.columns.str.upper()`.

## Level 3 — Data Analysis
11. Why are Pandas Index objects designed to be immutable?
12. What happens to the index when you perform row filtering `df[df['age'] > 30]`?
13. Explain why `df.reset_index(drop=True)` is recommended after filtering rows.
14. Predict output: `df = pd.DataFrame({'a': [1, 2]}); df.set_index('a', inplace=True); print(df.index.name)`.
15. Predict output shape of `df.reset_index()` for `df` of shape `(10, 3)` with single index column.

## Level 4 — Debugging
16. Fix error: `TypeError: Index does not support mutable operations`.
17. Fix bug where `reset_index()` created an annoying duplicate column named `'index'`.
18. Fix issue where `set_index('ColA')` failed because `'ColA'` was already dropped or mispelled.

## Level 5 — AI/ML Application
19. Why should you reset index before combining target vector `y` with feature matrix `X`?
20. How does a unique index prevent duplicate sample matching bugs during train/test splits?
21. Connect `DatetimeIndex` to sequential time-series feature engineering.

## Level 6 — Interview Questions
22. Explain how hash tables optimize row lookups for Pandas Index objects.
23. What is a `MultiIndex` (Hierarchical Indexing) and how is it created in Pandas?
24. Explain the difference between `RangeIndex`, `Int64Index`, and `CategoricalIndex`.
25. Demonstrate how `df.reindex()` aligns DataFrames to a new set of index labels.
26. How does memory management differ between default `RangeIndex` vs explicit string `Index`?
