# Day 115 Solutions: Missing Values

## Level 1 — Basic
1. `np.nan` (or `pd.NA`).
2. `df.isna()` (or `df.isnull()`).
3. `df.notna()` (or `df.notnull()`).
4. False (IEEE 754 standard specifies `NaN != NaN`).
5. `df.isna().sum().sum()`

## Level 2 — Coding
6. `missing_counts = df.isna().sum()`
7. `missing_pcts = df.isna().mean() * 100`
8. `missing_age_rows = df[df['Age'].isna()]`
9. `valid_age_rows = df[df['Age'].notna()]`
10. `any_missing_rows = df[df.isna().any(axis=1)]`

## Level 3 — Data Analysis
11. Standard C integers cannot represent IEEE 754 `NaN`. Pandas upcasts integer arrays to `float64` so `np.nan` bit-patterns can be stored.
12. `NaN` is float missing value. `None` is Python object missing value. `NaT` is missing timestamp value in datetime Series.
13. `3.0` (Pandas aggregators skip `NaN` by default: `skipna=True`).
14. `True` (Python `in` checks object identity/equality in container list).
15. `object` (Series of `None` defaults to generic object dtype).

## Level 4 — Debugging
16. Replace `== np.nan` with `pd.isna(val)`.
17. Pass threshold parameter `thresh` or specify subset of critical columns: `df.dropna(subset=['Critical_Col'])`.
18. Pass sentinel values to `read_csv`: `na_values=['null', 'NULL', 'N/A']`.

## Level 5 — AI/ML Application
19. MCAR: Safe to drop/impute. MAR: Impute using observed features. MNAR: Imputation introduces bias; must add explicit missing indicator feature column.
20. `drop_cols = df.columns[df.isna().mean() > 0.40]; df_clean = df.drop(columns=drop_cols)`
21. Real-time inference pipelines check `isna()` to flag invalid API payloads before passing tensors to model `.predict()`.

## Level 6 — Interview Solutions
22. IEEE 754 floating-point standard defines `NaN` as an un-comparable invalid numerical signal (e.g. $0/0$ or $\sqrt{-1}$). Any equality check involving `NaN` evaluates to `False`.
23. Nullable dtypes (`Int64`, `boolean`) store an additional internal boolean mask array tracking missing entries without altering the primary integer/boolean data block.
24. Pandas automatically coerces Python `None` into `np.nan` in numeric Series, treating both as missing `True` in `.isna()`.
25. `df['Feature_isna'] = df['Feature'].isna().astype(int)`
26. Distance algorithms (KNN, SVM) compute Euclidean distances $\sqrt{\sum (x_i - y_i)^2}$ which fail on `NaN`. Tree algorithms (XGBoost) learn default split directions for `NaN` values natively.
