# Day 123 Worked Examples: Merge

## Example 1 — Beginner: Basic Inner Join
```python
import pandas as pd

employees = pd.DataFrame({
    'Emp_ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David']
})

salaries = pd.DataFrame({
    'Emp_ID': [1, 2, 3, 5],
    'Salary': [70000, 80000, 90000, 65000]
})

inner_df = pd.merge(employees, salaries, on='Emp_ID', how='inner')
print("Inner Merge Result:
", inner_df)
```

## Example 2 — Practical: Left Outer Join with Differing Keys
```python
import pandas as pd

customers = pd.DataFrame({
    'Cust_ID': [101, 102, 103],
    'Customer_Name': ['Acme Corp', 'Beta LLC', 'Gamma Inc']
})

orders = pd.DataFrame({
    'Client_ID': [101, 101],
    'Order_Amount': [5000, 3200]
})

left_df = pd.merge(
    customers, orders,
    left_on='Cust_ID', right_on='Client_ID',
    how='left'
)
print("Left Join Result:
", left_df)
```

## Example 3 — Intermediate: Handling Column Suffix Collisions
```python
import pandas as pd

df2022 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Revenue': [100, 200, 300],
    'Status': ['Active', 'Active', 'Pending']
})

df2023 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Revenue': [150, 220, 310],
    'Status': ['Active', 'Closed', 'Active']
})

merged_str = pd.merge(
    df2022, df2023,
    on='ID',
    suffixes=('_2022', '_2023')
)
print("Merged with Custom Suffixes:
", merged_str)
```

## Example 4 — Real Dataset: Audit Mismatches with indicator=True
```python
import pandas as pd

inventory = pd.DataFrame({
    'SKU': ['A1', 'B2', 'C3'],
    'Stock': [50, 0, 100]
})

sales = pd.DataFrame({
    'SKU': ['A1', 'C3', 'D4'],
    'Qty_Sold': [5, 10, 2]
})

audit_df = pd.merge(inventory, sales, on='SKU', how='outer', indicator=True)
print("Outer Join with Merge Indicator:
", audit_df)
```

## Example 5 — AI/ML Application: Feature Matrix Construction via Merging
```python
import pandas as pd

# Primary ML Entities
users = pd.DataFrame({'User_ID': [1, 2, 3], 'Age': [25, 40, 35]})
user_stats = pd.DataFrame({'User_ID': [1, 2, 3], 'Avg_Spend': [120.5, 450.0, 89.0]})
user_labels = pd.DataFrame({'User_ID': [1, 2, 3], 'Churned': [0, 1, 0]})

# Chain Merges to build complete ML feature table
ml_data = users.merge(user_stats, on='User_ID').merge(user_labels, on='User_ID')
print("Assembled ML Training Dataset:
", ml_data)
```
