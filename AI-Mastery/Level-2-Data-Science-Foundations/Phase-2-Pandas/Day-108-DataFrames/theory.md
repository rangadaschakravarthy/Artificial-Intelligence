# Day 108 Theory: DataFrames

### 1. What Is It?
A Pandas `DataFrame` is a 2D size-mutable, potentially heterogeneous tabular data structure with labelled axes (rows and columns).

### 2. Why Does It Exist?
Real-world data is multi-column and tabular. DataFrames align heterogeneous Series columns (numbers, strings, dates) on a shared row Index.

### 3. Intuition
A DataFrame is a digital spreadsheet or SQL table. Columns represent variables (features); rows represent observations (samples).

### 4. Syntax
```python
import pandas as pd

# Creating DataFrame from Dictionary
df = pd.DataFrame({
    'Feature_A': [1.0, 2.0, 3.0],
    'Feature_B': ['X', 'Y', 'Z']
})

# Dropping a column
df_dropped = df.drop(columns=['Feature_B'])

# Renaming a column
df_renamed = df.rename(columns={'Feature_A': 'Target'})
```

### 5. Parameters
- `data`: 2D ndarray, dict of Series/lists, or DataFrame.
- `index`: Row labels.
- `columns`: Column header labels.
- `inplace`: If `True`, mutates original DataFrame in-place without returning a copy.

### 6. How It Works
A DataFrame maintains an internal column dictionary mapping column names to 1D Series data blocks aligned on a shared `Index` object.

### 7. Simple Example
```python
import pandas as pd
df = pd.DataFrame({'x': [1, 2], 'y': [3, 4]})
print(df.describe())
```

### 8. Intermediate Example
```python
import pandas as pd
df = pd.DataFrame({'A': [10, 20], 'B': [30, 40]})
df.rename(columns={'A': 'Alpha'}, inplace=True)
print(df.columns.tolist()) # ['Alpha', 'B']
```

### 9. Output Interpretation
`inplace=True` mutates column names directly within the existing `df` object.

### 10. Common Mistakes
- Forgetting `axis=1` or `columns=` when dropping columns (`df.drop('ColA')` defaults to `axis=0` row drop, raising `KeyError`!).
- Misinterpreting `.describe()` for non-numerical object columns.

### 11. Data Science Connection
The central container for data pipelines: loading, auditing, filtering, transforming, and saving processed tables.

### 12. AI/ML Connection
DataFrame represents complete tabular dataset $D = [X \mid y]$. Features $X$ are extracted via `df.drop(columns=['target'])` and target $y$ via `df['target']`.

### 13. Interview Insight
Question: "What is the difference between `df.drop('Col', axis=1)` and `df.drop('Col', axis=1, inplace=True)`?"
Answer: Without `inplace=True`, `.drop()` returns a **new DataFrame copy** with the column removed, leaving the original `df` unchanged. With `inplace=True`, it mutates the existing `df` directly and returns `None`.

### 14. Summary
DataFrames are labelled 2D tables. Use `head()`, `info()`, and `describe()` to audit schema and `drop()` / `rename()` to modify column structure.
