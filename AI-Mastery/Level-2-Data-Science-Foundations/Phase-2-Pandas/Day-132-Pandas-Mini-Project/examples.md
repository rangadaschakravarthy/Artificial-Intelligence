# Day 132 Worked Examples: Pandas Mini Project

## Full Workflow Code Structure Overview
```python
import pandas as pd
import numpy as np

# Stage 1: Ingestion
raw = pd.DataFrame({...})

# Stage 2: Cleaning
df = raw.copy()
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
df.drop_duplicates(inplace=True)
df['amount'] = pd.to_numeric(df['amount'].str.replace('$', '', regex=False), errors='coerce')
df['amount'].fillna(df['amount'].median(), inplace=True)
df['date'] = pd.to_datetime(df['date'])

# Stage 3: EDA
print(df.describe())
print(df.corr(numeric_only=True))

# Stage 4: Reporting
monthly_piv = df.pivot_table(index=df['date'].dt.to_period('M'), columns='category', values='amount', aggfunc='sum', fill_value=0)

# Stage 5: Pre-ML
y = (df['amount'] > 100).astype(int)
X = pd.get_dummies(df.drop(columns=['amount']), drop_first=True, dtype=int)

# Stage 6: Validation
assert X.isna().sum().sum() == 0
print("Project Execution Completed Successfully!")
```
