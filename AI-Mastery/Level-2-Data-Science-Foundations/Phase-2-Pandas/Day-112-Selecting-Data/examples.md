# Day 112 Worked Examples: Selecting Data

## Example 1 — Beginner: Series vs DataFrame Column Selection
```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [70000, 85000, 95000]
})

# Single Column Selection -> Series (1D)
age_series = df['Age']

# Multi-Column Selection -> DataFrame (2D)
sub_df = df[['Name', 'Salary']]

print("Age Series Type:", type(age_series))
print("Sub DataFrame Type:", type(sub_df))
print("
Sub DataFrame:
", sub_df)
```

## Example 2 — Practical: loc vs iloc Selection Comparison
```python
import pandas as pd

df = pd.DataFrame({
    'Score': [88, 92, 79, 95],
    'Grade': ['B', 'A', 'C', 'A']
}, index=['Alice', 'Bob', 'Charlie', 'David'])

# .loc: Label-based selection
bob_score = df.loc['Bob', 'Score']
alice_bob_df = df.loc['Alice':'Bob', :] # INCLUSIVE of 'Bob'!

# .iloc: Positional integer selection
first_row_score = df.iloc[0, 0]
first_two_rows_df = df.iloc[0:2, :]    # EXCLUSIVE of index 2!

print("Bob's Score (loc):", bob_score)
print("Alice to Bob (loc inclusive):
", alice_bob_df)
print("
First 2 Rows (iloc exclusive):
", first_two_rows_df)
```

## Example 3 — Intermediate: Fast Scalar Cell Access with at & iat
```python
import pandas as pd

df = pd.DataFrame({
    'A': [100, 200, 300],
    'B': [400, 500, 600]
}, index=['r1', 'r2', 'r3'])

# Fast scalar lookup using .at (label) and .iat (position)
val_at = df.at['r2', 'B']  # 500
val_iat = df.iat[1, 1]     # 500

print("Value using .at['r2', 'B']:", val_at)
print("Value using .iat[1, 1]:    ", val_iat)
```

## Example 4 — Real Dataset: Slicing Feature Columns by Name Range
```python
import pandas as pd

# Multi-feature dataset
dataset = pd.DataFrame({
    'ID': [1, 2, 3],
    'Feat_A': [1.1, 2.2, 3.3],
    'Feat_B': [10, 20, 30],
    'Feat_C': [0.1, 0.2, 0.3],
    'Target': [0, 1, 0]
})

# Extract all feature columns between 'Feat_A' and 'Feat_C' inclusive
feature_sub = dataset.loc[:, 'Feat_A':'Feat_C']
print("Extracted Features (Feat_A to Feat_C):
", feature_sub)
```

## Example 5 — AI/ML Application: Separating X and y using iloc
```python
import pandas as pd

# ML Dataset with 4 features and target in final column
df_ml = pd.DataFrame({
    'F1': [1, 2, 3], 'F2': [4, 5, 6], 'F3': [7, 8, 9], 'F4': [10, 11, 12],
    'Label': [0, 1, 0]
})

# X: All rows, all columns up to last column (0 to -1)
X = df_ml.iloc[:, :-1]

# y: All rows, last column only
y = df_ml.iloc[:, -1]

print("Feature Matrix X shape:", X.shape) # (3, 4)
print("Target Vector y shape:  ", y.shape) # (3,)
```
