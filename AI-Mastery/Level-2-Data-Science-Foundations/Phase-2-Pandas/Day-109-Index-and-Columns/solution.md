# Day 109 Solutions: Index and Columns

## Level 1 — Basic
1. `df.index`
2. `df.columns`
3. `df.set_index('ID')`
4. `drop=True` (`df.reset_index(drop=True)`).
5. False (Index objects are immutable).

## Level 2 — Coding
6. `df.set_index('Date', inplace=True)`
7. `df.reset_index(drop=True, inplace=True)`
8. `df.index.is_unique` -> Returns `True` or `False`.
9. `df.rename(index={'r1': 'Row1'}, columns={'A': 'Alpha'})`
10. `df.columns = df.columns.str.upper()`

## Level 3 — Data Analysis
11. Immutability guarantees index hash maps remain consistent across shared DataFrames without risk of side-effect mutations.
12. Row filtering preserves original index labels of matching rows, creating gaps in integer sequences (e.g. 0, 2, 5).
13. Broken non-consecutive indices cause position-based iteration bugs. `reset_index(drop=True)` restores clean 0-based range indexing.
14. `'a'`
15. `(10, 4)` (Old index is promoted to a new column, adding 1 column).

## Level 4 — Debugging
16. Do not assign directly to index items. Replace full index: `df.index = new_list` or use `.rename(index=...)`.
17. Add `drop=True` parameter: `df.reset_index(drop=True, inplace=True)`.
18. Verify column exists in `df.columns` before calling `set_index()`.

## Level 5 — AI/ML Application
19. Non-matching or broken index labels between $X$ and $y$ cause `pd.concat([X, y], axis=1)` to generate `NaN` rows due to label mismatch.
20. Unique index labels ensure each sample record is tracked uniquely, preventing accidental duplicate sample assignment across train/test splits.
21. `DatetimeIndex` enables time-based operations (e.g. extracting `df.index.dayofweek`, `df.index.month`) for temporal feature engineering.

## Level 6 — Interview Solutions
22. Pandas builds an internal C hash table mapping label keys to integer row positions, delivering $O(1)$ fast lookups for `.loc['label']`.
23. A `MultiIndex` allows multiple levels of row or column labels (e.g. `[State, City]`), structuring multi-dimensional data in 2D DataFrames.
24. `RangeIndex` is a memory-efficient generator `(start, stop, step)` consuming $O(1)$ RAM. `Int64Index` stores an explicit int array. `CategoricalIndex` uses memory-mapped category codes.
25. `df.reindex(new_index_list)` aligns DataFrame rows to `new_index_list`, inserting `NaN` for missing labels.
26. `RangeIndex` stores 3 integers (start, stop, step) consuming negligible RAM. String `Index` stores arrays of string pointers, consuming significantly more memory.
