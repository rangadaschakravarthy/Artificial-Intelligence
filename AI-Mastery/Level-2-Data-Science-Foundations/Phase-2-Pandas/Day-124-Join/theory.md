# Day 124 Theory: Join

### 1. What Is It?
`df.join()` is a convenience method for combining two or more DataFrames horizontally using row indices as default matching keys.

### 2. Why Does It Exist?
While `pd.merge()` defaults to column keys, `.join()` defaults to index keys, offering a cleaner API when tables are indexed by entity IDs or dates.

### 3. Intuition
Think of `.join()` as gluing columns of two DataFrames together side-by-side, aligning rows by matching index labels.

### 4. Syntax
```python
# Default index-to-index join (defaults to how='left'!):
df1.join(df2, how='inner')

# Joining on caller's column against target's index:
df1.join(df2, on='KeyColumn')

# Multi-DataFrame join:
df1.join([df2, df3])
```

### 5. Parameters
- `other`: DataFrame or list of DataFrames.
- `on`: Column name in caller DataFrame to match against `other`'s index.
- `how`: `'left'` (default for `.join()`), `'right'`, `'inner'`, `'outer'`.
- `lsuffix`, `rsuffix`: String suffixes for overlapping column names.

### 6. How It Works
Pandas inspects index labels of both caller and target DataFrames, performs hash matching across index labels, and combines columns.

### 7. Simple Example
```python
import pandas as pd
df1 = pd.DataFrame({'A': [1, 2]}, index=['r1', 'r2'])
df2 = pd.DataFrame({'B': [3, 4]}, index=['r1', 'r2'])
print(df1.join(df2))
```

### 8. Intermediate Example
```python
import pandas as pd
prices = pd.DataFrame({'AAPL': [150, 152]}, index=['2023-01-01', '2023-01-02'])
volumes = pd.DataFrame({'Vol': [1000, 1200]}, index=['2023-01-01', '2023-01-02'])
print(prices.join(volumes))
```

### 9. Output Interpretation
Columns from `other` are attached horizontally to `df1`. Missing index matches are populated with `NaN` depending on `how`.

### 10. Common Mistakes
- Expecting default `how='inner'` (like `pd.merge()`); `.join()` defaults to `how='left'`!
- Raising `ValueError: columns overlap` by forgetting `lsuffix` / `rsuffix` when DataFrames share column names.

### 11. Data Science Connection
Aligning feature tables indexed by entity timestamps or unique entity IDs.

### 12. AI/ML Connection
Combining multi-view feature DataFrames created independently by parallel feature extraction pipelines.

### 13. Interview Insight
Question: "Difference between `df.join()` and `pd.merge()`?"
Answer: `pd.merge()` defaults to matching on shared **columns** and defaults to `how='inner'`. `df.join()` defaults to matching on row **indices** and defaults to `how='left'`.

### 14. Summary
`df.join()` simplifies horizontal index-aligned table concatenation and multi-DataFrame merging.
