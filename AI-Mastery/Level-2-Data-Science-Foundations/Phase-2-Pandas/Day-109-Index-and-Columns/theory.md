# Day 109 Theory: Index and Columns

### 1. What Is It?
Pandas `Index` and `Columns` are specialized 1D immutable array-like objects holding row labels and column headers for DataFrames and Series.

### 2. Why Does It Exist?
Data needs meaningful row and column labels. Index objects act as hash maps for fast $O(1)$ row lookups and automatic alignment during merging and join operations.

### 3. Intuition
Think of row index labels as the page numbers of a textbook and column names as the chapter titles. They allow you to turn directly to specific content.

### 4. Syntax
```python
import pandas as pd

df = pd.DataFrame({'ID': ['A1', 'A2'], 'Val': [10, 20]})

# Set column as Index
df_indexed = df.set_index('ID')

# Reset Index back to default integer range
df_reset = df_indexed.reset_index()
```

### 5. Parameters
- `drop`: Boolean in `reset_index()`. If `True`, drops the old index instead of inserting it as a column.
- `inplace`: Mutates DataFrame in-place.

### 6. How It Works
Pandas `Index` objects store internal C-level hash tables. When calling `.loc['A1']`, Pandas looks up `'A1'` in the hash table to locate exact row integer memory offsets.

### 7. Simple Example
```python
import pandas as pd
df = pd.DataFrame({'x': [1, 2]}, index=['r1', 'r2'])
print("Index:", df.index.tolist()) # ['r1', 'r2']
```

### 8. Intermediate Example
```python
import pandas as pd
df = pd.DataFrame({'ID': [101, 102], 'Score': [85, 90]})
df.set_index('ID', inplace=True)
print("Is Index Unique?", df.index.is_unique) # True
```

### 9. Output Interpretation
`df.index.is_unique` verifies that all index labels in `'ID'` are unique without duplicates.

### 10. Common Mistakes
- Trying to mutate an Index element directly (`df.index[0] = 'New'` raises `TypeError` because Index objects are immutable!).
- Forgetting `drop=True` in `reset_index()` when resetting index, adding unwanted `'index'` columns.

### 11. Data Science Connection
Setting timestamp columns as `DatetimeIndex` for time-series resampling and date filtering.

### 12. AI/ML Connection
Ensuring `df.index.is_unique` before splitting feature matrices to prevent data duplication or alignment mismatch during model evaluation.

### 13. Interview Insight
Question: "Why are Pandas Index objects immutable?"
Answer: Immutability guarantees that index hash tables remain consistent across multiple Series and DataFrames sharing the index, allowing zero-copy sharing of index objects without risk of unintended mutation bugs.

### 14. Summary
Index objects store row and column labels. Use `set_index()` to promote columns to index and `reset_index()` to restore range index.
