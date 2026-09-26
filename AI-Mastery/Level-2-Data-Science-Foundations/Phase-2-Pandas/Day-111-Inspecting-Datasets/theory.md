# Day 111 Theory: Inspecting Datasets

### 1. What Is It?
Inspecting datasets is the initial data auditing step where a Data Scientist examines the size, schema, column data types, missing value frequencies, and statistical distributions of a DataFrame.

### 2. Why Does It Exist?
Real-world datasets contain corrupt data, inconsistent sentinel values, unexpected strings, missing entries, and bad data types. Auditing discovers these issues before downstream processing.

### 3. Intuition
Dataset inspection is like an initial architectural inspection of a newly purchased house—checking foundation walls (shape), plumbing (dtypes), and leaks (missing NaNs).

### 4. Syntax
```python
import pandas as pd

df = pd.read_csv('data.csv')

# Random sample of 5 rows
sample_df = df.sample(n=5, random_state=42)

# Missing value summary
missing_count = df.isna().sum()
missing_pct = (df.isna().mean()) * 100

# Unique value count per column
unique_counts = df.nunique()
```

### 5. Parameters
- `n` / `frac`: Number or fraction of rows to sample in `.sample()`.
- `deep`: Boolean in `.memory_usage(deep=True)` to inspect heap string sizes.

### 6. How It Works
Pandas iterates down internal C-array column blocks, scanning null-bitmaps (`isna`), computing summary statistics (`describe`), and summing byte allocations (`memory_usage`).

### 7. Simple Example
```python
import pandas as pd
df = pd.DataFrame({'Age': [25, 30, None], 'City': ['NY', 'LA', 'NY']})
print("Missing Count:
", df.isna().sum())
```

### 8. Intermediate Example
```python
import pandas as pd
df = pd.DataFrame({'A': range(100), 'B': ['x'] * 100})
print("Memory Usage (Deep):
", df.memory_usage(deep=True))
```

### 9. Output Interpretation
`df.memory_usage(deep=True)` reports exact RAM bytes consumed by row indices, integer blocks, and string pointer heaps.

### 10. Common Mistakes
- Relying solely on `df.head()` (Head rows may appear clean while tail rows contain missing values or corrupted strings!).
- Forgetting to check `df.dtypes` and failing to notice that a numeric column was parsed as `object` (string).

### 11. Data Science Connection
Generating data quality health checks and automated EDA baseline reports.

### 12. AI/ML Connection
Verifying feature matrix dimension alignment $X$ `(N, D)` and target label $y$ `(N,)` before training algorithms.

### 13. Interview Insight
Question: "What steps do you take in your initial 5-minute dataset inspection?"
Answer: 1) `df.shape` for size bounds. 2) `df.info()` for dtypes and missing values. 3) `df.isna().mean() * 100` for missing percentages. 4) `df.describe()` for numerical distributions. 5) `df.nunique()` and `.value_counts()` for categorical cardinality.

### 14. Summary
Dataset inspection audits data health. Use `.info()`, `.sample()`, `.isna().sum()`, and `.nunique()` to discover missing values and data type anomalies.
