# Day 118 Worked Examples: Data Type Conversion

## Example 1 — Beginner: Basic astype() Casting
```python
import pandas as pd

df = pd.DataFrame({
    'Val_Str': ['10', '20', '30'],
    'Val_Float': [1.1, 2.8, 3.9]
})

df['Val_Int'] = df['Val_Str'].astype(int)
df['Val_Float_to_Int'] = df['Val_Float'].astype(int) # Truncates!

print(df)
print("Data Types:
", df.dtypes)
```

## Example 2 — Practical: Robust Numeric Conversion with pd.to_numeric
```python
import pandas as pd

# Dirty column containing currency symbols and corrupted text 'ERROR'
raw_series = pd.Series(['$100.50', '$250.00', 'ERROR', '$175.25'])

# Step 1: Clean string currency symbol
clean_str = raw_series.str.replace('$', '', regex=False)

# Step 2: Coerce unparseable 'ERROR' into NaN float
numeric_series = pd.to_numeric(clean_str, errors='coerce')

print("Raw Series:
", raw_series)
print("
Cleaned Numeric Series:
", numeric_series)
print("Dtype:", numeric_series.dtype)
```

## Example 3 — Intermediate: Converting Dates with pd.to_datetime
```python
import pandas as pd

df = pd.DataFrame({
    'Date_Str': ['2026-01-01', '02/15/2026', '2026.03.20']
})

df['Date_Parsed'] = pd.to_datetime(df['Date_Str'])
df['Year'] = df['Date_Parsed'].dt.year
df['Month_Name'] = df['Date_Parsed'].dt.day_name()

print("Parsed Datetime DataFrame:
", df)
```

## Example 4 — Real Dataset: Memory Reduction via Categorical Downcasting
```python
import pandas as pd

# 10,000 customer region records with only 4 unique categories
regions = ['North', 'South', 'East', 'West'] * 2500
df = pd.DataFrame({'Region': regions})

mem_obj = df['Region'].memory_usage(deep=True)

# Convert to category
df['Region'] = df['Region'].astype('category')
mem_cat = df['Region'].memory_usage(deep=True)

print(f"Object String Memory:     {mem_obj / 1024:.2f} KB")
print(f"Categorical Dtype Memory: {mem_cat / 1024:.2f} KB")
print(f"Memory Saved: {((mem_obj - mem_cat) / mem_obj) * 100:.1f}%!")
```

## Example 5 — AI/ML Application: Automatic Numeric Downcasting for ML Pipelines
```python
import pandas as pd
import numpy as np

# DataFrame with standard float64 and int64 columns
df_ml = pd.DataFrame({
    'A': np.array([1.0, 2.0, 3.0], dtype=np.float64),
    'B': np.array([10, 20, 30], dtype=np.int64)
})

# Downcast to float32 and int32
for col in df_ml.select_dtypes(include=['float64']).columns:
    df_ml[col] = df_ml[col].astype(np.float32)

for col in df_ml.select_dtypes(include=['int64']).columns:
    df_ml[col] = pd.to_numeric(df_ml[col], downcast='integer')

print("Downcasted ML DataFrame Dtypes:
", df_ml.dtypes)
```
