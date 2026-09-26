# Day 106 Solutions: Pandas Introduction

## Level 1 — Basic
1. `pd` (`import pandas as pd`).
2. `Series` (1D) and `DataFrame` (2D).
3. `pd.__version__`
4. False (Each column has its own dtype, but all values within a single column share the same dtype).
5. `.to_numpy()` (or `.values`).

## Level 2 — Coding
6. `import pandas as pd; print(pd.__version__)`
7. `df = pd.DataFrame({'City': ['NY', 'LA'], 'Population': [8000000, 4000000]})`
8. `print(df.shape)`
9. `print(df.columns.tolist())`
10. `print(df.dtypes)`

## Level 3 — Data Analysis
11. A DataFrame is a collection of separate 1D Series columns. Each column wraps its own independent 1D NumPy array with its own specific dtype.
12. A Series is a 1D labeled array (single column). A DataFrame is a 2D tabular data structure composed of multiple Series aligned on a shared Index.
13. `(10, 4)` (10 rows, 4 columns).
14. `<class 'pandas.core.series.Series'>`
15. Pandas stores additional metadata structures (index labels, column names, pandas BlockManager pointers) which consume small extra memory overhead over raw NumPy bytes.

## Level 4 — Debugging
16. Add missing import statement: `import pandas as pd`.
17. Ensure all lists in dictionary have identical length (number of elements).
18. Remove string entry or clean missing value placeholder so column can cast back to numeric type (`pd.to_numeric()`).

## Level 5 — AI/ML Application
19. `X = df[['feat1', 'feat2']].to_numpy(dtype=np.float32)`
20. DataFrames excel at EDA, data cleaning, string handling, and labelled alignment. NumPy arrays deliver maximum hardware matrix multiplication throughput required by ML algorithms.
21. DataFrame columns represent feature variables $X_1, X_2, \dots, X_p$ and target labels $Y$ in dataset matrices.

## Level 6 — Interview Solutions
22. Pandas uses `BlockManager` internally to group columns of identical data types into consolidated 2D NumPy arrays (e.g. FloatBlock, IntBlock) for memory efficiency.
23. `df.values` is legacy code that can return inconsistent types or views. `df.to_numpy()` is the modern, explicit NumPy conversion method.
24. Pandas performs additional label-based indexing checks and index alignment, incurring small Python overhead compared to raw NumPy integer stride offsets.
25. 
```python
# Dict of lists: keys=cols
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
# List of dicts: keys=row entries
df2 = pd.DataFrame([{'A': 1, 'B': 3}, {'A': 2, 'B': 4}])
```
26. When operating on two Series/DataFrames, Pandas automatically aligns data based on index labels rather than element positions, filling non-matching index positions with `NaN`.
