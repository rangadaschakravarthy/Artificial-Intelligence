# Day 109 Worked Examples: Index and Columns

## Example 1 — Beginner: Setting and Resetting Index
```python
import pandas as pd

df = pd.DataFrame({
    'Emp_ID': ['E101', 'E102', 'E103'],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Salary': [70000, 85000, 95000]
})

# Set Emp_ID as row index
df_id = df.set_index('Emp_ID')
print("DataFrame with Emp_ID Index:
", df_id)

# Reset index back to 0-based range
df_reset = df_id.reset_index()
print("
Reset DataFrame:
", df_reset)
```

## Example 2 — Practical: Inspecting Index Uniqueness and Properties
```python
import pandas as pd

df = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'C'], # Non-unique values
    'Value': [10, 20, 30, 40]
})

df.set_index('Category', inplace=True)

print("Index Values:", df.index.tolist())
print("Is Index Unique?", df.index.is_unique)
print("Index Name:", df.index.name)
```

## Example 3 — Intermediate: Renaming Index and Columns
```python
import pandas as pd

df = pd.DataFrame([[1, 2], [3, 4]], columns=['a', 'b'], index=['r1', 'r2'])

# Rename row index labels and column headers simultaneously
df_renamed = df.rename(index={'r1': 'Row_1'}, columns={'a': 'Col_A'})

print("Renamed DataFrame:
", df_renamed)
```

## Example 4 — Real Dataset: Setting Datetime Index for Time-Series Data
```python
import pandas as pd

stock_df = pd.DataFrame({
    'Date': pd.date_range(start='2026-01-01', periods=4, freq='D'),
    'Close_Price': [150.2, 152.5, 151.0, 155.8]
})

stock_df.set_index('Date', inplace=True)

print("Time Series DataFrame:
", stock_df)
print("Index Type:", type(stock_df.index))
```

## Example 5 — AI/ML Application: Resetting Index After Row Filtering
```python
import pandas as pd

# Filtering rows leaves broken non-consecutive index labels (e.g. 0, 2, 4)
df = pd.DataFrame({'Age': [20, 15, 30, 12, 45], 'Score': [80, 50, 90, 40, 85]})
filtered_df = df[df['Age'] >= 18]

print("Filtered DataFrame (Broken Index):
", filtered_df)

# Reset index cleanly (drop=True prevents creating extra 'index' column)
filtered_df_clean = filtered_df.reset_index(drop=True)
print("
Clean Reset DataFrame:
", filtered_df_clean)
```
