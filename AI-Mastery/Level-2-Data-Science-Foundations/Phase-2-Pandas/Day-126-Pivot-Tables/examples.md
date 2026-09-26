# Day 126 Worked Examples: Pivot Tables

## Example 1 — Beginner: Simple pivot_table
```python
import pandas as pd

df = pd.DataFrame({
    'Category': ['Tech', 'Tech', 'Furniture', 'Furniture'],
    'Region': ['North', 'South', 'North', 'South'],
    'Sales': [500, 700, 300, 400]
})

piv = df.pivot_table(index='Category', columns='Region', values='Sales', aggfunc='sum')
print("Pivot Table (Sales by Category & Region):
", piv)
```

## Example 2 — Practical: Pivot Table with Margins and Fill Value
```python
import pandas as pd

df = pd.DataFrame({
    'Department': ['IT', 'IT', 'HR', 'Sales', 'Sales'],
    'Gender': ['M', 'F', 'F', 'M', 'F'],
    'Salary': [90000, 95000, 60000, 70000, 75000]
})

piv_margins = df.pivot_table(
    index='Department',
    columns='Gender',
    values='Salary',
    aggfunc='mean',
    fill_value=0,
    margins=True
)
print("Department Salary Pivot with Totals:
", piv_margins)
```

## Example 3 — Intermediate: Unpivoting Wide Tables using pd.melt
```python
import pandas as pd

wide_df = pd.DataFrame({
    'Employee': ['Alice', 'Bob'],
    'Q1_Sales': [10000, 15000],
    'Q2_Sales': [12000, 18000]
})

long_df = pd.melt(
    wide_df,
    id_vars=['Employee'],
    value_vars=['Q1_Sales', 'Q2_Sales'],
    var_name='Quarter',
    value_name='Sales_Amount'
)
print("Melted Tidy Long DataFrame:
", long_df)
```

## Example 4 — Real Dataset: E-Commerce Product Category Heatmap Matrix
```python
import pandas as pd

orders = pd.DataFrame({
    'Month': ['Jan', 'Jan', 'Feb', 'Feb', 'Jan', 'Feb'],
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Clothing', 'Clothing', 'Electronics'],
    'Revenue': [1500, 800, 1800, 950, 700, 2100]
})

matrix = orders.pivot_table(
    index='Month',
    columns='Category',
    values='Revenue',
    aggfunc='sum',
    fill_value=0
)
print("Monthly Category Revenue Matrix:
", matrix)
```

## Example 5 — AI/ML Application: User-Item Interaction Matrix for Collaborative Filtering
```python
import pandas as pd

ratings = pd.DataFrame({
    'User_ID': [1, 1, 2, 2, 3, 3],
    'Movie_ID': [101, 102, 101, 103, 102, 103],
    'Rating': [5.0, 3.0, 4.0, 2.0, 4.5, 5.0]
})

user_item_matrix = ratings.pivot_table(
    index='User_ID',
    columns='Movie_ID',
    values='Rating',
    fill_value=0
)
print("User-Item Interaction Matrix for Recommendation Engine:
", user_item_matrix)
```
