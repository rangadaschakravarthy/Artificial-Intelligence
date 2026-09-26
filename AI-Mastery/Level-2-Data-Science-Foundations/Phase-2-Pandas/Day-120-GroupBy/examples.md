# Day 120 Worked Examples: GroupBy

## Example 1 — Beginner: Basic Single-Column Grouping
```python
import pandas as pd

df = pd.DataFrame({
    'Team': ['Alpha', 'Beta', 'Alpha', 'Beta', 'Alpha'],
    'Points': [10, 20, 15, 25, 30]
})

grouped = df.groupby('Team')
print("Group Names and Indices:", grouped.groups)
print("Alpha Mean Points:", grouped['Points'].mean()['Alpha'])
```

## Example 2 — Practical: Inspecting Groups with get_group
```python
import pandas as pd

df = pd.DataFrame({
    'Category': ['Tech', 'Health', 'Tech', 'Finance', 'Health'],
    'Stock': ['AAPL', 'JNJ', 'GOOG', 'JPM', 'PFE'],
    'Price': [150, 170, 2800, 140, 160]
})

g = df.groupby('Category')
health_df = g.get_group('Health')
print("Health Category Sub-DataFrame:
", health_df)
```

## Example 3 — Intermediate: Multi-Column Grouping
```python
import pandas as pd

df = pd.DataFrame({
    'Store': ['S1', 'S1', 'S2', 'S2', 'S1'],
    'Shift': ['Day', 'Night', 'Day', 'Night', 'Night'],
    'Revenue': [1000, 800, 1200, 950, 850]
})

grouped_multi = df.groupby(['Store', 'Shift'])['Revenue'].mean()
print("Mean Revenue by Store and Shift:
", grouped_multi)
```

## Example 4 — Real Dataset: E-Commerce Customer Grouping
```python
import pandas as pd

orders = pd.DataFrame({
    'CustomerID': [101, 102, 101, 103, 102, 101],
    'OrderValue': [250.0, 450.0, 120.0, 89.0, 310.0, 95.0],
    'PaymentMethod': ['Credit', 'PayPal', 'Credit', 'Credit', 'PayPal', 'Credit']
})

cust_summary = orders.groupby('CustomerID')['OrderValue'].sum()
print("Total Spend Per Customer:
", cust_summary)
```

## Example 5 — AI/ML Application: Group-Level Mean Imputation Preprocessing
```python
import pandas as pd

# Group-level feature creation for ML inputs
df_ml = pd.DataFrame({
    'Occupation': ['Eng', 'Eng', 'Doc', 'Doc', 'Eng'],
    'Income': [90000, 110000, 180000, 210000, 95000]
})

df_ml['Group_Avg_Income'] = df_ml.groupby('Occupation')['Income'].transform('mean')
print("Dataset with Group Average Feature:
", df_ml)
```
