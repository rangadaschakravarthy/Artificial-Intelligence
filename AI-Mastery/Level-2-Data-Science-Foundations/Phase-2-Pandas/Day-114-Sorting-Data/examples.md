# Day 114 Worked Examples: Sorting Data

## Example 1 — Beginner: Basic Single Column Sorting
```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Score': [88, 95, 72, 91]
})

# Sort ascending by Score
df_asc = df.sort_values(by='Score')

# Sort descending by Score
df_desc = df.sort_values(by='Score', ascending=False)

print("Ascending Order:
", df_asc)
print("
Descending Order:
", df_desc)
```

## Example 2 — Practical: Multi-Column Sorting with Mixed Directions
```python
import pandas as pd

df = pd.DataFrame({
    'Department': ['IT', 'HR', 'IT', 'HR', 'IT'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Salary': [90000, 65000, 110000, 60000, 95000]
})

# Primary Sort: Department (A-Z Ascending)
# Secondary Sort: Salary (High to Low Descending)
df_sorted = df.sort_values(
    by=['Department', 'Salary'],
    ascending=[True, False]
)

print("Multi-Column Sorted DataFrame:
", df_sorted)
```

## Example 3 — Intermediate: Handling Missing Values (na_position)
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Product': ['P1', 'P2', 'P3', 'P4'],
    'Rating': [4.5, np.nan, 3.8, np.nan]
})

# Place NaNs at the beginning
df_na_first = df.sort_values(by='Rating', na_position='first')

print("Sorted with NaNs First:
", df_na_first)
```

## Example 4 — Real Dataset: Extracting Top 3 Highest Earners using nlargest()
```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Revenue': [45000, 82000, 29000, 95000, 61000, 88000]
})

# Extract top 3 highest revenues using nlargest
top_3 = df.nlargest(3, 'Revenue')

print("Top 3 Revenue Earners:
", top_3)
```

## Example 5 — AI/ML Application: Sorting Time-Series Index
```python
import pandas as pd

# Unsorted time series data
df_time = pd.DataFrame({
    'Date': pd.to_datetime(['2026-01-03', '2026-01-01', '2026-01-02']),
    'Price': [103.5, 100.0, 101.2]
}).set_index('Date')

print("Unsorted Time Series:
", df_time)

# Sort strictly by DatetimeIndex
df_time_sorted = df_time.sort_index(ascending=True)

print("
Sorted Time Series:
", df_time_sorted)
```
