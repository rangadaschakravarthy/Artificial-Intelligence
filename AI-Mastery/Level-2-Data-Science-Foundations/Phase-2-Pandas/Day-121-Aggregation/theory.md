# Day 121 Theory: Aggregation

### 1. What Is It?
`df.agg()` computes summary metrics (like sum, mean, std) across rows or columns, either globally or per group created by `groupby()`.

### 2. Why Does It Exist?
Basic methods like `.mean()` apply a single function to all columns. `.agg()` allows applying multiple different functions to different specific columns simultaneously.

### 3. Intuition
Instead of calculating average salary in one query and max experience in another, `.agg()` generates a single consolidated executive metric report.

### 4. Syntax
```python
# Multiple aggregations on selected column:
df.groupby('Group')['Col'].agg(['mean', 'std', 'count'])

# Column-specific dictionary mapping:
df.groupby('Group').agg({'Sales': 'sum', 'Rating': 'mean'})

# Named Aggregation (flattens column names):
df.groupby('Group').agg(
    Avg_Sales=('Sales', 'mean'),
    Max_Rating=('Rating', 'max')
)
```

### 5. Parameters
- `func`: Function, string function name, list of functions, or dictionary mapping column names to functions.
- `*args`, `**kwargs`: Passed through to specified functions.

### 6. How It Works
Pandas iterates over each specified column group, evaluates the designated statistical functions vectorially, and constructs an aggregated table.

### 7. Simple Example
```python
import pandas as pd
df = pd.DataFrame({'A': [10, 20, 30], 'B': [1, 2, 3]})
print(df.agg(['sum', 'mean']))
```

### 8. Intermediate Example
```python
import pandas as pd
df = pd.DataFrame({
    'Category': ['A', 'A', 'B', 'B'],
    'Sales': [100, 200, 150, 250],
    'Profit': [10, 30, 20, 40]
})
print(df.groupby('Category').agg({'Sales': ['sum', 'mean'], 'Profit': 'max'}))
```

### 9. Output Interpretation
Aggregating multiple functions creates hierarchical (MultiIndex) column headers unless Named Aggregation or column flattening is applied.

### 10. Common Mistakes
- Using non-vectorized Python loops inside custom lambda functions, degrading performance on large datasets.
- Getting confused by MultiIndex column tuples in downstream code.

### 11. Data Science Connection
Creating summary tables, KPI dashboards, cohort comparison reports, and EDA statistical summaries.

### 12. AI/ML Connection
Aggregating historical transactional features per user entity (e.g. `total_spend`, `avg_basket_size`, `max_discount_used`).

### 13. Interview Insight
Question: "How do you avoid MultiIndex column names when calling `.agg()`?"
Answer: Use Named Aggregation: `df.groupby('Key').agg(new_col_name=('target_col', 'agg_func'))`.

### 14. Summary
`.agg()` offers flexible, multi-metric statistical summary capabilities across groups using string names, custom functions, or dictionary mappings.
