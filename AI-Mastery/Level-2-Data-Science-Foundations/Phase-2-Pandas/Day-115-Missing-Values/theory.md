# Day 115 Theory: Missing Values

### 1. What Is It?
Missing values represent absent, unobserved, or unrecorded data entries in a dataset, represented in Pandas as `NaN` (Not a Number), `None`, `pd.NA`, or `NaT` (Not a Time).

### 2. Why Does It Exist?
Data acquisition fails due to skipped survey questions, faulty sensors, corrupted data pipelines, or unrecorded events.

### 3. Intuition
A missing value is a blank space on a printed paper form. You know a question was asked, but the answer slot was left completely empty.

### 4. Syntax
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Age': [25, np.nan, 35],
    'Name': ['Alice', None, 'Charlie']
})

# Detect missing entries
mask = df.isna()
missing_counts = df.isna().sum()
missing_pcts = df.isna().mean() * 100
```

### 5. Parameters
- `df.isna()` / `df.isnull()`: Synonymous functions returning boolean DataFrame indicating `True` where values are missing.
- `df.notna()` / `df.notnull()`: Logical inverse returning `True` for valid existing data.

### 6. How It Works
`np.nan` is an IEEE 754 floating-point special value. By IEEE definition, `np.nan != np.nan`. Pandas provides `.isna()` to check for missingness reliably.

### 7. Simple Example
```python
import pandas as pd
import numpy as np
print("np.nan == np.nan:", np.nan == np.nan) # False!
print("pd.isna(np.nan): ", pd.isna(np.nan))  # True
```

### 8. Intermediate Example
```python
import pandas as pd
import numpy as np
df = pd.DataFrame({'A': [1, np.nan, 3], 'B': [np.nan, np.nan, 6]})
print("Missing Total:", df.isna().sum().sum()) # 3 total missing cells
```

### 9. Output Interpretation
`df.isna().sum().sum()` totals all missing `NaN` cells across all rows and columns.

### 10. Common Mistakes
- Checking missingness using `if val == np.nan:` (Always evaluates to `False`! Use `pd.isna(val)`).
- Assuming integer columns can hold standard `np.nan` without upcasting to `float64` (Standard integer columns upcast to float when `NaN` is inserted unless nullable `Int64` dtype is used).

### 11. Data Science Connection
Auditing missing data patterns during initial EDA and creating missingness heatmaps.

### 12. AI/ML Connection
Most Scikit-Learn models (`LinearRegression`, `SVM`) crash if fed `NaN` values. Missing data must be handled during preprocessing.

### 13. Interview Insight
Question: "What are the 3 statistical mechanisms of missing data (MCAR, MAR, MNAR)?"
Answer:
1. **MCAR (Missing Completely at Random)**: Missingness is purely random, unrelated to any observed or unobserved variable (e.g. random sensor glitch).
2. **MAR (Missing at Random)**: Missingness depends systematically on *observed* variables (e.g. older people skipping income questions).
3. **MNAR (Missing Not at Random)**: Missingness depends on the *unobserved missing value itself* (e.g. high earners hiding high incomes).

### 14. Summary
Missing data is represented by `NaN`/`None`/`pd.NA`. Detect missingness using `isna()`, and audit missing percentages before choosing imputation strategies.
