# Day 108 Worked Examples: DataFrames

## Example 1 — Beginner: Creating DataFrame from Multiple Sources
```python
import pandas as pd
import numpy as np

# Source 1: Dict of Lists
df1 = pd.DataFrame({'Age': [20, 30], 'City': ['NY', 'LA']})

# Source 2: 2D NumPy Array
matrix = np.array([[10, 20], [30, 40]])
df2 = pd.DataFrame(matrix, columns=['Col_1', 'Col_2'], index=['Row_A', 'Row_B'])

print("DataFrame 1:
", df1)
print("
DataFrame 2:
", df2)
```

## Example 2 — Practical: Structural Auditing with info() and describe()
```python
import pandas as pd

df = pd.DataFrame({
    'CustomerID': [1, 2, 3, 4, 5],
    'Age': [25, 45, 35, 50, 28],
    'Spend_USD': [150.5, 420.0, 280.25, 600.0, 95.0],
    'Tier': ['Gold', 'Silver', 'Gold', 'Platinum', 'Silver']
})

print("--- DataFrame Info ---")
df.info()

print("
--- Numerical Describe ---")
print(df.describe())

print("
--- Object Describe ---")
print(df.describe(include=['object']))
```

## Example 3 — Intermediate: Renaming & Dropping Columns
```python
import pandas as pd

df = pd.DataFrame({
    'old_col1': [1, 2, 3],
    'old_col2': [4, 5, 6],
    'temp_col': [0, 0, 0]
})

# Rename columns
df_renamed = df.rename(columns={'old_col1': 'feature_1', 'old_col2': 'feature_2'})

# Drop unneeded column
df_clean = df_renamed.drop(columns=['temp_col'])

print("Clean DataFrame:
", df_clean)
```

## Example 4 — Real Dataset: Inspecting Top and Bottom Rows
```python
import pandas as pd
import numpy as np

# Synthetic sensor dataset of 1,000 rows
rng = np.random.default_rng(42)
sensor_df = pd.DataFrame({
    'Timestamp_Sec': np.arange(1000),
    'Temperature': rng.normal(25.0, 2.0, 1000),
    'Pressure': rng.normal(1013.0, 10.0, 1000)
})

print("First 3 rows:
", sensor_df.head(3))
print("
Last 3 rows:
", sensor_df.tail(3))
```

## Example 5 — AI/ML Application: Preparing X (Features) and y (Target)
```python
import pandas as pd

# Credit Default Dataset
credit_df = pd.DataFrame({
    'Income': [50000, 80000, 30000, 120000],
    'Credit_Score': [650, 720, 580, 790],
    'Debt_Ratio': [0.4, 0.2, 0.6, 0.1],
    'Defaulted': [0, 0, 1, 0] # Target Label
})

# Separate Feature Matrix X and Target Vector y
X = credit_df.drop(columns=['Defaulted'])
y = credit_df['Defaulted']

print("Features X:
", X)
print("
Target y:
", y)
```
