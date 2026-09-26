# Day 111 Solutions: Inspecting Datasets

## Level 1 — Basic
1. `df.info()`
2. `df.sample()`
3. `df.nunique()`
4. True.
5. `df.memory_usage()`

## Level 2 — Coding
6. `sample_df = df.sample(frac=0.1, random_state=42)`
7. `missing_pct = df.isna().mean() * 100`
8. `print(df.memory_usage(deep=True))`
9. `obj_cols = df.select_dtypes(include=['object']).columns`
10. `print(df.columns.is_unique)`

## Level 3 — Data Analysis
11. `.head(5)` only checks top rows which are often sorted or pre-cleaned. `.sample(5)` extracts random rows across the entire dataset, exposing anomalies hidden in middle or tail rows.
12. Parses numeric string values to float/int, and converts unparseable invalid string entries into missing `NaN` values.
13. `1` (Total missing values across all columns).
14. `(50, 10)` (50% of 100 rows).
15. A categorical column with 10,000 unique string categories generates 10,000 sparse columns during one-hot encoding, triggering the curse of dimensionality.

## Level 4 — Debugging
16. Convert to numeric using `pd.to_numeric(df['col'].str.strip(), errors='coerce')`.
17. Reduce sample size $n \le 2$ or set `replace=True` to allow sampling with replacement.
18. Replace string sentinel values with proper `NaN`: `df.replace('N/A', np.nan, inplace=True)`.

## Level 5 — AI/ML Application
19. 
```python
report = {
    'n_samples': len(df),
    'n_features': df.shape[1] - 1,
    'missing_pct': df.isna().mean().to_dict(),
    'dtypes': df.dtypes.astype(str).to_dict()
}
```
20. Low cardinality ($\le 10$) targets One-Hot Encoding; high cardinality targets Target/Frequency Encoding or Embedding representations.
21. Inspecting correlation `df.corr()` during EDA reveals if a feature has $ho = 1.0$ with target $y$, flagging target leakage.

## Level 6 — Interview Solutions
22. `df.info()` iterates column Series blocks, inspecting underlying 1D NumPy boolean null-bitmaps (`isna`) and summing valid entries.
23. `df.nunique()` returns a Series of unique counts for all columns. `df['col'].unique()` returns a 1D NumPy array of the actual unique values for a single column.
24. Object string columns store 64-bit pointers to scattered PyObject string locations in Python heap memory. Categorical columns store 8-bit integer codes mapped to a single dictionary array.
25. `mem_mb = df.memory_usage(deep=True) / (1024 ** 2)`
26. Pseudo-random number generators seeded with `random_state=42` produce deterministic, reproducible sample index permutations across runs.
