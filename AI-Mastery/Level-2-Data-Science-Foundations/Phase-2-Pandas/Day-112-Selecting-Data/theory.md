# Day 112 Theory: Selecting Data

### 1. What Is It?
Data selection refers to extracting specific rows, columns, sub-tables, or scalar values from a DataFrame using bracket syntax (`[]`), `.loc[]`, `.iloc[]`, `.at[]`, or `.iat[]`.

### 2. Why Does It Exist?
DataFrames contain large 2D grids of information. Selection tools enable precise retrieval of relevant feature subsets or specific data observations.

### 3. Intuition
- `df['col']`: Pull a single column out as a 1D Series.
- `df.loc['RowA', 'ColB']`: Navigate to a cell by row label name and column header name.
- `df.iloc[0, 1]`: Navigate to a cell by 0-based row position and column position.

### 4. Syntax
```python
import pandas as pd

df = pd.DataFrame({'Age': [25, 30], 'Income': [50k, 80k]}, index=['r1', 'r2'])

# Single Column (Series) vs Multiple Columns (DataFrame)
s = df['Age']           # Series (1D)
sub_df = df[['Age']]     # DataFrame (2D)

# .loc (Label-based: inclusive stop!)
val_loc = df.loc['r1', 'Income']

# .iloc (Positional integer: exclusive stop!)
val_iloc = df.iloc[0, 1]
```

### 5. Parameters
- `loc[row_labels, col_labels]`: Accepts label strings, lists of labels, or label slices. Note: `.loc` slices are **inclusive** of the stop label!
- `iloc[row_indices, col_indices]`: Accepts integers, integer lists, or integer slices. `.iloc` slices are **exclusive** of the stop index!

### 6. How It Works
`.loc[]` queries the index hash map for label matches. `.iloc[]` bypasses label lookups, executing fast 0-based integer offset array indexing over underlying BlockManager buffers.

### 7. Simple Example
```python
import pandas as pd
df = pd.DataFrame({'A': [10, 20], 'B': [30, 40]}, index=['x', 'y'])
print(df.loc['x', 'A'])  # 10
print(df.iloc[0, 0])     # 10
```

### 8. Intermediate Example
```python
import pandas as pd
df = pd.DataFrame({'A': [10, 20, 30], 'B': [40, 50, 60]})
# Extract rows 0 to 1, all columns
sub = df.iloc[0:2, :]
print(sub)
```

### 9. Output Interpretation
`df.iloc[0:2, :]` extracts row positions 0 and 1 (exclusive of 2), returning a 2-row DataFrame.

### 10. Common Mistakes
- Confusing `.loc` slice inclusivity (`'a':'c'` includes `'c'`) with `.iloc` slice exclusivity (`0:2` excludes `2`).
- Chained indexing (`df['Col'][0] = 5`) which triggers `SettingWithCopyWarning` (Use `df.loc[0, 'Col'] = 5`!).

### 11. Data Science Connection
Subsetting columns for feature engineering and splitting datasets by observation indices.

### 12. AI/ML Connection
Separating feature matrix $X = 	ext{df.iloc[:, :-1]}$ from target vector $y = 	ext{df.iloc[:, -1]}$.

### 13. Interview Insight
Question: "What is the difference between `df['Col']` and `df[['Col']]`?"
Answer: `df['Col']` selects a single column as a 1D Pandas **Series**. `df[['Col']]` passes a list of column names, selecting the column while preserving 2D **DataFrame** structure.

### 14. Summary
Use `df['col']` for column selection, `.loc[]` for label-based selection (inclusive stop), `.iloc[]` for positional integer selection (exclusive stop), and `.at[]`/`.iat[]` for fast scalar access.
