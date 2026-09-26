# Day 115 Worked Examples: Missing Values

## Example 1 — Beginner: Demonstrating IEEE 754 NaN Behavior
```python
import pandas as pd
import numpy as np

val1 = np.nan
val2 = np.nan

print("val1 == val2:     ", val1 == val2)       # False!
print("val1 is val2:     ", val1 is val2)       # True (same object)
print("pd.isna(val1):    ", pd.isna(val1))      # True
print("pd.notna(val1):   ", pd.notna(val1))     # False
```

## Example 2 — Practical: Auditing Missing Data Counts & Percentages
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Patient_ID': [101, 102, 103, 104, 105],
    'Blood_Pressure': [120, np.nan, 140, np.nan, 115],
    'Cholesterol': [180, 220, np.nan, np.nan, np.nan], # 60% missing
    'Target_Disease': [0, 1, 0, 1, 0]
})

missing_summary = pd.DataFrame({
    'Missing_Count': df.isna().sum(),
    'Missing_Percentage': np.round(df.isna().mean() * 100, 2)
})

print("Missing Audit Table:
", missing_summary)
```

## Example 3 — Intermediate: Nullable Integer Dtypes (`Int64`)
```python
import pandas as pd
import numpy as np

# Standard int array upcasts to float64 when NaN is inserted
s_float = pd.Series([1, 2, np.nan])

# Pandas Nullable Integer Dtype (capital 'I') retains integer type!
s_int64 = pd.Series([1, 2, np.nan], dtype='Int64')

print("Standard Series Dtype: ", s_float.dtype) # float64
print("Nullable Series Dtype: ", s_int64.dtype) # Int64
print("Nullable Series Content:
", s_int64)
```

## Example 4 — Real Dataset: Visualizing Missingness Pattern across Rows
```python
import pandas as pd
import numpy as np

# Filter rows where AT LEAST ONE feature is missing
df = pd.DataFrame({
    'A': [1.0, 2.0, np.nan, 4.0],
    'B': [10.0, np.nan, np.nan, 40.0],
    'C': [100.0, 200.0, 300.0, 400.0]
})

# Rows with any missing values
rows_with_nan = df[df.isna().any(axis=1)]
print("Rows with at least 1 missing value:
", rows_with_nan)
```

## Example 5 — AI/ML Application: Flagging High-Missingness Features for Removal
```python
import pandas as pd
import numpy as np

# Dataset with 4 features
df_ml = pd.DataFrame({
    'F1': [1, 2, 3, 4, 5],
    'F2': [np.nan, 2, np.nan, 4, 5],
    'F3': [np.nan, np.nan, np.nan, np.nan, 5], # 80% missing!
    'Label': [0, 1, 0, 1, 0]
})

# Threshold: Drop features with > 50% missing values
missing_pct = df_ml.isna().mean()
cols_to_drop = missing_pct[missing_pct > 0.50].index.tolist()

df_filtered = df_ml.drop(columns=cols_to_drop)

print("Missing Percentages:
", missing_pct * 100)
print("Columns Flagged for Removal:", cols_to_drop)
print("Filtered ML Feature Matrix:
", df_filtered)
```
