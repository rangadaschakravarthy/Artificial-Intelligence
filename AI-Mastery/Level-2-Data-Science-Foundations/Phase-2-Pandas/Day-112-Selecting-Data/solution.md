# Day 112 Solutions: Selecting Data

## Level 1 — Basic
1. `Series` (1D).
2. `DataFrame` (2D).
3. `.loc[]`
4. True (`.loc` label slicing is inclusive of the stop label).
5. `.iat[]`

## Level 2 — Coding
6. `sub_df = df[['Age', 'Income']]`
7. `sub_df = df.iloc[0:5, 0:3]`
8. `val = df.loc['User_42', 'Email']`
9. `df.iat[0, 1] = 99`
10. `features = df.loc[:, 'feat_1':'feat_5']`

## Level 3 — Data Analysis
11. If the index is default integer `0,1,2`, `df.loc[0:2]` matches labels `0, 1, 2` (inclusive, returning 3 rows). If index is string, integer `.loc[0:2]` falls back or raises error. `.iloc[0:2]` always selects 0-based positions 0, 1 (exclusive, returning 2 rows).
12. `(100,)` (1D Series).
13. `(100, 1)` (2D DataFrame).
14. `10`
15. `.at[]` bypasses general index slicing checks and returns scalar values directly via fast-path lookup.

## Level 4 — Debugging
16. `.loc[]` expects matching string label `'r1'`. Use `.iloc[0]` for 0-based positional lookup.
17. Replace chained indexing `df['A'][0] = val` with combined `.loc`: `df.loc[0, 'A'] = val`.
18. `.iloc[]` requires positional integer indices. Use column integer positions (e.g. `df.iloc[:, 0:3]`) or use `.loc[]` for string names.

## Level 5 — AI/ML Application
19. `X = df.iloc[:, :-1]` (Assuming target is final column).
20. `sample_2d = df.iloc[[sample_idx], :-1]` (Double brackets `[[sample_idx]]` preserve 2D DataFrame shape `(1, n_features)`).
21. `.loc[train_indices, feature_names]` extracts specific sample subsets and feature subsets cleanly for model folds.

## Level 6 — Interview Solutions
22. Chained indexing `df['A'][0]` calls `__getitem__` twice. Pandas cannot determine if `df['A']` returned a view or copy, rendering `[0]` assignment unreliable. `.loc[0, 'A']` executes a single atomic operation.
23. `.loc[mask]` passes a boolean Series where `True` entries select corresponding rows matching index labels.
24. `.iloc[i, j]` maps directly to 0-based C-array integer index offsets `[i, j]` in underlying BlockManager arrays.
25. `df.xs(key='2026', level='Year')` extracts cross-sectional slices from a specified level of a MultiIndex.
26. Execution speed: `.at` / `.iat` is fastest ($O(1)$ fast-path scalar lookup). `.iloc` is fast (positional block offset). `.loc` is slightly slower (hash table label lookup).
