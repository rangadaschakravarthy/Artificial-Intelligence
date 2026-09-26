# Day 125 Theory: Concatenation

### 1. What Is It?
`pd.concat()` glues multiple DataFrames or Series together along a specified axis (vertically stacking rows or horizontally appending columns).

### 2. Why Does It Exist?
When data is split across multiple files (e.g. daily logs) or separate feature generation routines, `pd.concat()` stitches them into a single consolidated structure.

### 3. Intuition
- **`axis=0` (Default)**: Stacking sheets of paper on top of each other (adding rows).
- **`axis=1`**: Placing sheets of paper side by side (adding columns).

### 4. Syntax
```python
# Vertical Concatenation (stack rows):
pd.concat([df1, df2, df3], axis=0, ignore_index=True)

# Horizontal Concatenation (append columns):
pd.concat([df1, df2], axis=1, join='inner')
```

### 5. Parameters
- `objs`: List or dictionary of DataFrame / Series objects.
- `axis`: `0` / `'index'` (rows), `1` / `'columns'` (columns).
- `join`: `'outer'` (keep all columns/rows, fill missing with `NaN`), `'inner'` (keep only shared columns/rows).
- `ignore_index`: bool. If `True`, discards original index labels and builds a new `RangeIndex(0, N)`.
- `keys`: Sequence to build MultiIndex headers identifying source origins.

### 6. How It Works
Pandas allocates a memory buffer for the combined dimensions, aligns axis labels (columns for `axis=0`, rows for `axis=1`), and copies arrays efficiently.

### 7. Simple Example
```python
import pandas as pd
df1 = pd.DataFrame({'A': [1, 2]})
df2 = pd.DataFrame({'A': [3, 4]})
print(pd.concat([df1, df2], ignore_index=True))
```

### 8. Intermediate Example
```python
import pandas as pd
df_q1 = pd.DataFrame({'Sales': [100, 120]}, index=['Jan', 'Feb'])
df_q2 = pd.DataFrame({'Sales': [140, 150]}, index=['Mar', 'Apr'])
print(pd.concat([df_q1, df_q2]))
```

### 9. Output Interpretation
Vertical concat creates a taller DataFrame. Horizontal concat creates a wider DataFrame. Missing aligned elements fill with `NaN` under `join='outer'`.

### 10. Common Mistakes
- Appending DataFrames inside a Python `for` loop, causing $O(N^2)$ memory copying overhead.
- Forgetting `ignore_index=True` during vertical concat, producing duplicate index values (`0, 1, 0, 1`).

### 11. Data Science Connection
Merging monthly/daily log files, assembling feature matrices, and combining web-scraped data batches.

### 12. AI/ML Connection
Combining training and test sets temporarily for uniform feature preprocessing, then re-splitting.

### 13. Interview Insight
Question: "How do you efficiently combine 100 CSV files into a single Pandas DataFrame?"
Answer: Read all CSVs into a list of DataFrames first: `dfs = [pd.read_csv(f) for f in files]`, then call `pd.concat(dfs, ignore_index=True)` once.

### 14. Summary
`pd.concat()` provides fast, axis-configurable vertical and horizontal DataFrame stitching.
