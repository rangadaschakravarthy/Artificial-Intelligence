# Day 116 Worked Examples: Handling Missing Values

## Example 1 — Beginner: Dropping Missing Values with dropna()
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, np.nan, 35, np.nan],
    'Salary': [70000, 85000, np.nan, 95000]
})

# Drop rows where ANY value is NaN
df_drop_any = df.dropna()

# Drop rows where Age is NaN specifically
df_drop_age = df.dropna(subset=['Age'])

print("Original DataFrame:
", df)
print("
Drop Any NaN:
", df_drop_any)
print("
Drop NaN in Age Column:
", df_drop_age)
```

## Example 2 — Practical: Mean, Median, and Mode Imputation
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Income': [50000.0, 60000.0, np.nan, 55000.0, 1000000.0], # Skewed with outlier!
    'City': ['NY', 'LA', np.nan, 'NY', 'NY'] # Categorical
})

# Impute Income with Median (robust to 1M outlier)
income_median = df['Income'].median()
df['Income_Imputed'] = df['Income'].fillna(income_median)

# Impute City with Mode (most frequent)
city_mode = df['City'].mode()[0]
df['City_Imputed'] = df['City'].fillna(city_mode)

print("Imputed DataFrame:
", df)
print(f"Income Median used: {income_median}")
print(f"City Mode used:     {city_mode}")
```

## Example 3 — Intermediate: Time-Series Forward & Backward Fill
```python
import pandas as pd
import numpy as np

# Stock price time series with weekend/holiday missing gaps
time_df = pd.DataFrame({
    'Date': pd.date_range('2026-01-01', periods=5),
    'Price': [100.0, np.nan, np.nan, 105.0, 107.0]
})

# Forward Fill (propagate last valid observation forward)
time_df['Price_FFill'] = time_df['Price'].ffill()

# Backward Fill (propagate next valid observation backward)
time_df['Price_BFill'] = time_df['Price'].bfill()

print("Time-Series Imputation:
", time_df)
```

## Example 4 — Real Dataset: Group-Based Imputation
```python
import pandas as pd
import numpy as np

# Employee dataset with missing salary by Job Title
df = pd.DataFrame({
    'Job_Title': ['Data Scientist', 'Data Scientist', 'Sales', 'Sales', 'Data Scientist'],
    'Experience_Years': [2, 5, 1, 4, 3],
    'Salary': [90000, 130000, 50000, np.nan, np.nan]
})

# Impute Salary using group median of respective Job_Title
df['Salary_Group_Imputed'] = df.groupby('Job_Title')['Salary'].transform(
    lambda group: group.fillna(group.median())
)

print("Group Imputed DataFrame:
", df)
```

## Example 5 — AI/ML Application: Adding Missing Indicator Feature Columns
```python
import pandas as pd
import numpy as np

# Patient medical data
df_med = pd.DataFrame({
    'Age': [25, 40, 60, 30],
    'Glucose_Level': [95.0, np.nan, 140.0, np.nan] # Missing Not At Random!
})

# Step 1: Create binary missingness indicator column
df_med['Glucose_is_missing'] = df_med['Glucose_Level'].isna().astype(int)

# Step 2: Impute Glucose with median
df_med['Glucose_Level'] = df_med['Glucose_Level'].fillna(df_med['Glucose_Level'].median())

print("ML-Ready Imputed Feature Matrix:
", df_med)
```
