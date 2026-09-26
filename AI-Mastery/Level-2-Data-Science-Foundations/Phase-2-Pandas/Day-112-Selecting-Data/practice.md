# Day 112 Practice Questions: Selecting Data

## Level 1 — Basic
1. What is the return type of selecting a single column using `df['Col']`?
2. What is the return type of selecting a column using double brackets `df[['Col']]`?
3. Which selector uses explicit row and column labels: `.loc[]` or `.iloc[]`?
4. True or False: Slicing with `.loc['A':'C']` includes label `'C'`.
5. Which accessor provides fastest scalar cell lookup by integer position?

## Level 2 — Coding
6. Select columns `'Age'` and `'Income'` from DataFrame `df`.
7. Extract the first 5 rows and first 3 columns of DataFrame `df` using `.iloc[]`.
8. Select row with index label `'User_42'` and column `'Email'` using `.loc[]`.
9. Modify value at row position `0` and column position `1` to `99` using `.iat[]`.
10. Extract all rows where column range is from `'feat_1'` to `'feat_5'` inclusive using `.loc[]`.

## Level 3 — Data Analysis
11. Explain why `df.loc[0:2]` behaves differently depending on whether the DataFrame index is default integer vs string.
12. Predict output shape of `df.iloc[:, -1]` for `df` of shape `(100, 10)`.
13. Predict output shape of `df.iloc[:, -1:]` for `df` of shape `(100, 10)`.
14. Predict output: `df = pd.DataFrame({'a': [10, 20]}, index=['x', 'y']); print(df.loc['x', 'a'])`.
15. Explain why `.at[]` is faster than `.loc[]` for single scalar value lookup.

## Level 4 — Debugging
16. Fix error: `KeyError: 0` when using `df.loc[0]` on a DataFrame indexed with string labels `['r1', 'r2']` (Use `.iloc[0]`).
17. Fix warning: `SettingWithCopyWarning: A value is trying to be set on a copy of a slice from a DataFrame`.
18. Fix error when passing a 1D slice string list to `.iloc[]`: `TypeError: Cannot index by location index with a non-integer`.

## Level 5 — AI/ML Application
19. How do you extract all feature columns except the target label column using `.iloc[]`?
20. Extract a single test sample row as a 2D DataFrame of shape `(1, n_features)` for model prediction.
21. Connect `.loc[]` feature selection to preparing training subsets for cross-validation.

## Level 6 — Interview Questions
22. Explain why chained indexing `df['A'][0] = 5` triggers `SettingWithCopyWarning` in Pandas.
23. How does `.loc[]` evaluate boolean Series masks vs explicit label arrays?
24. Explain how `.iloc[]` translates positional integer coordinates into C-buffer block offsets.
25. Demonstrate how `df.xs()` selects cross-sections from a MultiIndex DataFrame.
26. Compare performance between `df.at[r, c]`, `df.loc[r, c]`, and `df.iloc[r, c]`.
