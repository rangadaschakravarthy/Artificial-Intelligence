# Day 121 Worked Examples: Aggregation

## Example 1 — Beginner: Multiple Functions on a Single Column
```python
import pandas as pd

df = pd.DataFrame({
    'Dept': ['IT', 'IT', 'HR', 'HR', 'IT'],
    'Salary': [80000, 95000, 60000, 65000, 110000]
})

res = df.groupby('Dept')['Salary'].agg(['min', 'mean', 'max', 'std'])
print("Salary Statistics by Dept:
", res)
```

## Example 2 — Practical: Dictionary Mapping Aggregation
```python
import pandas as pd

df = pd.DataFrame({
    'Store': ['North', 'North', 'South', 'South'],
    'Sales': [5000, 7000, 3000, 4000],
    'Customers': [120, 150, 90, 110]
})

agg_dict = {
    'Sales': 'sum',
    'Customers': ['mean', 'max']
}
res = df.groupby('Store').agg(agg_dict)
print("Store Metrics:
", res)
```

## Example 3 — Intermediate: Named Aggregation (Clean Output)
```python
import pandas as pd

df = pd.DataFrame({
    'Region': ['East', 'East', 'West', 'West'],
    'Revenue': [100, 200, 150, 300],
    'Cost': [40, 70, 50, 110]
})

clean_agg = df.groupby('Region').agg(
    Total_Revenue=('Revenue', 'sum'),
    Avg_Cost=('Cost', 'mean'),
    Max_Profit=('Revenue', lambda x: (x - df.loc[x.index, 'Cost']).max())
)
print("Clean Named Aggregation Table:
", clean_agg)
```

## Example 4 — Real Dataset: E-Commerce Metrics
```python
import pandas as pd

orders = pd.DataFrame({
    'Category': ['Electronics', 'Electronics', 'Clothing', 'Clothing', 'Electronics'],
    'Price': [299.99, 899.99, 49.99, 89.99, 149.99],
    'Quantity': [1, 1, 3, 2, 2]
})

cat_metrics = orders.groupby('Category').agg(
    Total_Units=('Quantity', 'sum'),
    Average_Price=('Price', 'mean'),
    Price_Spread=('Price', lambda x: x.max() - x.min())
)
print("E-Commerce Category Summary:
", cat_metrics)
```

## Example 5 — AI/ML Application: Feature Engineering via Named Aggregation
```python
import pandas as pd

user_logs = pd.DataFrame({
    'User_ID': [1, 1, 2, 2, 2],
    'Session_Time_Sec': [300, 450, 120, 600, 240],
    'Purchased': [0, 1, 0, 1, 0]
})

user_features = user_logs.groupby('User_ID').agg(
    Total_Session_Time=('Session_Time_Sec', 'sum'),
    Avg_Session_Time=('Session_Time_Sec', 'mean'),
    Purchase_Conversion=('Purchased', 'mean')
)
print("Engineered ML User Features:
", user_features)
```
