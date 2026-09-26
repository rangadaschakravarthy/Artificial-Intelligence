# Day 113 Worked Examples: Filtering Data

## Example 1 — Beginner: Single & Multi-Condition Filtering
```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 45, 35, 50, 28],
    'Salary': [70000, 120000, 85000, 95000, 62000]
})

# Single Condition: Salary > 80,000
high_salary = df[df['Salary'] > 80000]

# Multiple Conditions: Age < 35 AND Salary > 65,000
young_well_paid = df[(df['Age'] < 35) & (df['Salary'] > 65000)]

print("High Salary Employees:
", high_salary)
print("
Young Well-Paid Employees:
", young_well_paid)
```

## Example 2 — Practical: Category Membership with isin()
```python
import pandas as pd

df = pd.DataFrame({
    'Product': ['Laptop', 'Shirt', 'Phone', 'Book', 'Tablet'],
    'Category': ['Electronics', 'Apparel', 'Electronics', 'Media', 'Electronics'],
    'Price': [1200, 35, 800, 15, 500]
})

# Filter for Electronics or Media
target_cats = ['Electronics', 'Media']
tech_media_df = df[df['Category'].isin(target_cats)]

print("Tech & Media Products:
", tech_media_df)
```

## Example 3 — Intermediate: Numerical Range Filtering with between()
```python
import pandas as pd

df = pd.DataFrame({
    'Employee': ['E1', 'E2', 'E3', 'E4', 'E5'],
    'Score': [55, 72, 88, 64, 95]
})

# Filter scores in range [60, 80] inclusive
mid_scores = df[df['Score'].between(60, 80)]

print("Scores between 60 and 80:
", mid_scores)
```

## Example 4 — Real Dataset: String Matching Pattern Filtering
```python
import pandas as pd

df = pd.DataFrame({
    'Email': ['alice@gmail.com', 'bob@yahoo.com', 'charlie@gmail.com', 'david@corp.org'],
    'Role': ['Admin', 'User', 'User', 'Admin']
})

# Filter users with gmail.com domain
gmail_users = df[df['Email'].str.contains('gmail.com')]

print("Gmail Users:
", gmail_users)
```

## Example 5 — AI/ML Application: SQL-Style Querying with df.query()
```python
import pandas as pd

credit_df = pd.DataFrame({
    'Age': [25, 45, 35, 52, 29],
    'Debt_Ratio': [0.2, 0.6, 0.4, 0.7, 0.1],
    'Default': [0, 1, 0, 1, 0]
})

# Query: High-risk default candidates (Age > 30 and Debt_Ratio > 0.5)
high_risk = credit_df.query("Age > 30 and Debt_Ratio > 0.5")

print("High Risk Query Output:
", high_risk)
```
