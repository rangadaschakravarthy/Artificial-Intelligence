# Day 108 Solutions: DataFrames

## Level 1 — Basic
1. `df.shape`
2. `df.info()`
3. `df.head()` (or `df.head(5)`).
4. `columns=['col1', 'col2']` (or `labels=['col1'], axis=1`).
5. False (By default `.describe()` only summarizes numerical columns).

## Level 2 — Coding
6. `df = pd.DataFrame(np.arange(9).reshape(3, 3), columns=['A', 'B', 'C'])`
7. `df.tail(4)`
8. `df.rename(columns={'old_name': 'new_name'})`
9. `df_clean = df.drop(columns=['Unneeded'])`
10. `df.describe(include=['object'])` (or `include='all'`).

## Level 3 — Data Analysis
11. `df.info()` displays non-null row counts for each column; comparing non-null count against total row count immediately identifies missing values.
12. `500` (`len(df)` returns number of rows).
13. `.drop()` defaults to `axis=0` (row index drop). Since `'ColA'` is not a row index label, Pandas throws a `KeyError`.
14. `(10, 3)` (2 columns dropped from 5 columns).
15. `['x']`

## Level 4 — Debugging
16. Add `axis=1` or use explicit `columns=['ColA']` keyword argument: `df.drop(columns=['ColA'])`.
17. Reassign returned DataFrame: `df = df.drop(columns=['ColA'])` or pass `inplace=True`.
18. Pass `include='all'` or `include=['object']` parameter to `.describe()`.

## Level 5 — AI/ML Application
19. `X = df.drop(columns=['target']); y = df['target']`
20. Scikit-Learn models require strictly numerical inputs (`float32`/`float64`). Non-numerical `object` string columns cause model fitting errors.
21. Feature engineering creates new columns (e.g. `df['Ratio'] = df['A'] / df['B']`) directly on DataFrame structures.

## Level 6 — Interview Solutions
22. `BlockManager` consolidates columns sharing identical dtypes into single 2D NumPy arrays (e.g. 1 FloatBlock for all float columns), minimizing memory allocations.
23. Appending rows one-by-one re-allocates new memory blocks for the entire DataFrame on every loop iteration ($O(N^2)$ memory copying cost). Pre-allocate a list of dicts or NumPy array first.
24. `.memory_usage()` reports fixed pointer block sizes for `object` columns. `deep=True` inspects actual string lengths in memory heap.
25. `pd.DataFrame.from_dict(nested_dict, orient='index')` parses dict keys as row index labels.
26. Duplicate column names cause column selection `df['Dup']` to return a 2D DataFrame instead of a 1D Series, potentially causing downstream shape mismatch errors.
