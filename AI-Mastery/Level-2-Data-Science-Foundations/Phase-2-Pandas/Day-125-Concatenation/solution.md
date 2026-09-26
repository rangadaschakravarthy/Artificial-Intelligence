# Day 125 Solutions: Concatenation

## Level 1 — Basic
1. `axis=0` (default) stacks rows vertically; `axis=1` appends columns horizontally.
2. It discards original non-unique row indices and generates a clean sequential `RangeIndex(0, N)`.
3. `join='outer'` (keeps all columns/rows and fills missing values with `NaN`).
4. `pd.concat([df, s], axis=1)`.
5. Missing values in non-overlapping columns are filled with `NaN`.

## Level 2 — Coding
1.
```python
import pandas as pd
res = pd.concat([df1, df2], axis=0, ignore_index=True)
```
2.
```python
res = pd.concat([df_left, df_right], axis=1, join='inner')
```
3.
```python
res = pd.concat([df1, df2, df3, df4], axis=0, ignore_index=True)
```
4.
```python
res = pd.concat([df1, df2], keys=['Q1', 'Q2'])
```
5.
```python
res = pd.concat([df1, df2], axis=0, join='inner', ignore_index=True)
```

## Level 3 — Data Analysis
1.
```python
monthly_dfs = [pd.read_csv(f"sales_{m}.csv") for m in range(1, 13)]
yearly_df = pd.concat(monthly_dfs, ignore_index=True)
print(yearly_df.shape)
```
2.
```python
master_features = pd.concat([feat_a, feat_b, feat_c], axis=1)
```
3.
```python
history = pd.concat([df_2021, df_2022, df_2023], ignore_index=True)
```
4.
```python
all_results = pd.concat(scraped_pages_list, ignore_index=True)
```
5.
```python
all_telemetry = pd.concat(batch_list, ignore_index=True)
```

## Level 4 — Debugging
1. Accumulate DataFrames into a Python list and concatenate once outside the loop:
   `dfs = [pd.read_csv(f) for f in files]; master_df = pd.concat(dfs, ignore_index=True)`.
2. Add `ignore_index=True` parameter to `pd.concat()`, or run `df.reset_index(drop=True)` post-concatenation.
3. Reset row indices or ensure index alignment before calling `pd.concat(..., axis=1)`.

## Level 5 — AI/ML Application
1.
```python
combined = pd.concat([train_df, test_df], axis=0, keys=['train', 'test'])
combined_encoded = pd.get_dummies(combined)
train_encoded = combined_encoded.loc['train']
test_encoded = combined_encoded.loc['test']
```
2. `pd.concat()` preserves sequential row index ordering strictly, ensuring row $i$ in $X$ corresponds exactly to target label $y_i$.
3.
```python
meta_features = pd.concat([pred_model1, pred_model2, pred_model3], axis=1)
```

## Level 6 — Interview Questions
1. Repeated `.append()` reallocates memory and copies full data on every iteration ($O(N^2)$ complexity). `pd.concat()` computes total memory requirements upfront and performs a single copy pass ($O(N)$ complexity).
2. `pd.concat()` glues DataFrames along a physical axis (stacking rows/cols based on index/column alignment). `pd.merge()` performs value-matching joins on specified relational keys (SQL-style joins).
3. `pd.concat()` pre-allocates a contiguous block of RAM matching total output dimensions before copying underlying NumPy arrays.
4. Unaligned indices fill missing cells with `NaN` if `join='outer'`, or drop non-matching row indices if `join='inner'`.
5. The `keys` parameter constructs an outer MultiIndex level using the provided key strings, allowing tracking of source batch origin.
