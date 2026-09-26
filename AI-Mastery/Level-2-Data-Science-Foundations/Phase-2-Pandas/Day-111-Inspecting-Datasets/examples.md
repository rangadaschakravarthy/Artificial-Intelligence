# Day 111 Worked Examples: Inspecting Datasets

## Example 1 — Beginner: Basic Dataset Auditing Toolkit
```python
import pandas as pd

df = pd.DataFrame({
    'ID': [101, 102, 103, 104, 105],
    'Age': [25, 40, None, 35, 50],
    'Department': ['HR', 'IT', 'IT', None, 'Finance'],
    'Salary': [60000.0, 95000.0, 80000.0, 72000.0, 110000.0]
})

print("Shape:", df.shape)
print("
First 2 Rows:
", df.head(2))
print("
Random 2 Rows:
", df.sample(2, random_state=42))
print("
Missing Count per Column:
", df.isna().sum())
```

## Example 2 — Practical: Calculating Missing Percentage Summary Table
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Feat_1': [1, 2, np.nan, 4, 5, np.nan, 7, 8, 9, 10],
    'Feat_2': [np.nan] * 6 + [1, 2, 3, 4], # 60% missing
    'Target': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
})

# Missing Summary DataFrame
missing_df = pd.DataFrame({
    'Missing_Count': df.isna().sum(),
    'Missing_Percent': np.round(df.isna().mean() * 100, 2)
})

print("Missing Audit Table:
", missing_df)
```

## Example 3 — Intermediate: Memory Footprint Profiling
```python
import pandas as pd

df = pd.DataFrame({
    'Int_Col': range(1000),
    'Float_Col': [1.5] * 1000,
    'String_Col': ['Large_Category_Name_String'] * 1000
})

mem = df.memory_usage(deep=True)
print("Memory Usage per Column (Bytes):
", mem)
print(f"Total Memory: {mem.sum() / 1024:.2f} KB")
```

## Example 4 — Real Dataset: Identifying Type Corruptions in Numerical Columns
```python
import pandas as pd

# Raw dataset where 'Income' contains a string error 'UNKNOWN'
raw_df = pd.DataFrame({
    'Age': [25, 30, 35, 40],
    'Income': ['50000', '65000', 'UNKNOWN', '90000']
})

print("Inferred Dtypes:
", raw_df.dtypes)
print("Notice how 'Income' is parsed as 'object' due to 'UNKNOWN'!")

# Convert Income to numeric, turning 'UNKNOWN' into NaN
raw_df['Income'] = pd.to_numeric(raw_df['Income'], errors='coerce')
print("
Cleaned Dtypes:
", raw_df.dtypes)
print("Cleaned DataFrame:
", raw_df)
```

## Example 5 — AI/ML Application: Feature Cardinality Audit
```python
import pandas as pd

# Dataset with 5 columns
df = pd.DataFrame({
    'User_ID': range(100),
    'Gender': ['M', 'F'] * 50,
    'Country': ['USA', 'Canada', 'UK', 'USA'] * 25,
    'High_Cardinality_Zip': [f'Zip_{i}' for i in range(100)],
    'Target': [0, 1] * 50
})

# Cardinality audit (number of unique values)
cardinality = df.nunique()
print("Feature Cardinality (Unique Values):
", cardinality)

# Flag high-cardinality categorical features
high_card_cols = cardinality[(cardinality > 20) & (df.dtypes == 'object')].index.tolist()
print("
High-Cardinality Categorical Features to Watch Out For:", high_card_cols)
```
