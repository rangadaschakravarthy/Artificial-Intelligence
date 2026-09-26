# Day 126 Theory: Pivot Tables

### 1. What Is It?
`df.pivot_table()` creates a spreadsheet-style cross-tabulation matrix, aggregating values specified across index row keys and column headers. `pd.melt()` performs the inverse unpivoting operation.

### 2. Why Does It Exist?
Transaction logs store data in "long format" (many rows, few columns). Executive reporting and heatmaps require "wide format" matrices (categories as rows and columns).

### 3. Intuition
- **Pivot Table**: Fold long transaction lists into a 2D grid matrix.
- **Melt**: Unfold 2D grid matrices back into a clean narrow 3-column list (ID, Variable, Value).

### 4. Syntax
```python
# Pivot Table (Long to Wide with aggregation):
df.pivot_table(
    index='RowKey',
    columns='ColKey',
    values='MetricCol',
    aggfunc='mean',
    fill_value=0,
    margins=True
)

# Melt (Wide to Long):
pd.melt(df, id_vars=['ID'], value_vars=['Q1', 'Q2'], var_name='Quarter', value_name='Sales')
```

### 5. Parameters
- `index`: Column(s) for pivot row labels.
- `columns`: Column(s) for pivot column headers.
- `values`: Column(s) to aggregate.
- `aggfunc`: Aggregation function (`'mean'`, `'sum'`, `'count'`, etc.).
- `fill_value`: Value to replace empty missing matrix cells (`NaN`).
- `margins`: bool (default `False`). If `True`, adds All (total) row and column margins.

### 6. How It Works
Pandas groups by `[index, columns]`, applies `aggfunc` to `values`, and unstacks the secondary grouping column to create a 2D matrix layout.

### 7. Simple Example
```python
import pandas as pd
df = pd.DataFrame({'Year': [2021, 2021, 2022], 'Region': ['East', 'West', 'East'], 'Sales': [100, 150, 200]})
print(df.pivot_table(index='Year', columns='Region', values='Sales', aggfunc='sum', fill_value=0))
```

### 8. Intermediate Example
```python
import pandas as pd
df = pd.DataFrame({
    'Date': ['2023-01', '2023-01', '2023-02', '2023-02'],
    'Store': ['S1', 'S2', 'S1', 'S2'],
    'Revenue': [1000, 1200, 1100, 1300]
})
piv = df.pivot_table(index='Date', columns='Store', values='Revenue', margins=True)
print(piv)
```

### 9. Output Interpretation
Produces a multi-column DataFrame where row indices represent unique `index` items, columns represent unique `columns` categories, and cell values contain aggregated metrics.

### 10. Common Mistakes
- Using `df.pivot()` when duplicate `(index, columns)` pairs exist (triggers `ValueError: Index contains duplicate entries`). Use `pivot_table()`!
- Confusing `id_vars` (columns to keep unchanged) and `value_vars` (columns to unpivot) in `pd.melt()`.

### 11. Data Science Connection
Exploratory data analysis cross-tabs, heatmap data generation, financial matrix reports, and dataset tidying.

### 12. AI/ML Connection
Preparing correlation matrices and co-occurrence feature matrices for recommendation systems and collaborative filtering.

### 13. Interview Insight
Question: "Difference between `df.pivot()` and `df.pivot_table()`?"
Answer: `df.pivot()` requires strictly unique `(index, columns)` coordinate pairs and performs NO aggregation. `df.pivot_table()` aggregates non-unique index/column duplicate pairs using `aggfunc`.

### 14. Summary
Pivot tables summarize long data into wide matrices, while `pd.melt()` unpivots wide matrices into tidy long format.
