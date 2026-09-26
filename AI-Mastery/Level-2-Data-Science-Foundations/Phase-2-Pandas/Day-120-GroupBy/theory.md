# Day 120 Theory: GroupBy

### 1. What Is It?
`df.groupby()` splits a DataFrame into distinct groups based on matching values in one or more key columns, enabling segment-wise analysis.

### 2. Why Does It Exist?
Aggregate metrics across an entire dataset (like overall mean salary) mask valuable sub-population patterns. GroupBy allows calculating metrics per category.

### 3. Intuition
Imagine sorting a stack of customer invoices into piles by Country (Split), calculating the total invoice amount for each pile (Apply), and summarizing the totals in a new table (Combine).

### 4. Syntax
```python
grouped = df.groupby('CategoryColumn')
# Multi-column grouping:
grouped_multi = df.groupby(['Category1', 'Category2'])
```

### 5. Parameters
- `by`: Column name(s) or function to group by.
- `as_index`: bool (default `True`). If `False`, key columns remain regular columns instead of DataFrame index.
- `drop_missing` / `dropna`: bool (default `True`). Whether to drop missing values (`NaN`) in group keys.

### 6. How It Works
1. **Split**: Rows with identical group keys are mapped to common indices.
2. **Apply**: An aggregation/transformation function is executed on each subgroup independently.
3. **Combine**: Results from all groups are concatenated into a single output DataFrame or Series.

### 7. Simple Example
```python
import pandas as pd
df = pd.DataFrame({'Dept': ['HR', 'IT', 'HR', 'IT'], 'Salary': [50, 80, 60, 90]})
print(df.groupby('Dept')['Salary'].mean())
# HR: 55.0, IT: 85.0
```

### 8. Intermediate Example
```python
import pandas as pd
df = pd.DataFrame({
    'Region': ['East', 'East', 'West', 'West', 'East'],
    'Product': ['A', 'B', 'A', 'B', 'A'],
    'Sales': [100, 150, 200, 120, 180]
})
print(df.groupby(['Region', 'Product'])['Sales'].sum())
```

### 9. Output Interpretation
Grouping returns a `DataFrameGroupBy` lazy object. Aggregating it produces a Series (if single column selected) or DataFrame indexed by the unique values of the grouping key(s).

### 10. Common Mistakes
- Expecting `df.groupby('Col')` to print a table directly without calling an aggregation/action method.
- Forgetting `as_index=False` when preparing grouped results for visualization or ML export.

### 11. Data Science Connection
Cohort analysis, customer segmentation, regional performance benchmarking, and category-level feature engineering.

### 12. AI/ML Connection
Group-based feature creation (e.g., `user_mean_purchase_amount` feature for recommendation systems).

### 13. Interview Insight
Question: "What happens to `NaN` values in the grouping column by default?"
Answer: By default, Pandas drops `NaN` keys from groups (`dropna=True`). Set `dropna=False` to retain a group for missing key values.

### 14. Summary
GroupBy implements Split-Apply-Combine to break data into subgroups for targeted analytical evaluation and cohort metrics.
