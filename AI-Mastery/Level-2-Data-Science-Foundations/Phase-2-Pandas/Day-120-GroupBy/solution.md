# Day 120 Solutions: GroupBy

## Level 1 — Basic
1. **Split** (partitioning data by key), **Apply** (computing function on groups), **Combine** (assembling output table).
2. A `pandas.core.groupby.generic.DataFrameGroupBy` lazy object.
3. Set parameter `as_index=False` in `df.groupby('col', as_index=False)`.
4. `grouped = df.groupby('City')`.
5. Access the `.groups` dictionary attribute: `df.groupby('City').groups`.

## Level 2 — Coding
1.
```python
import pandas as pd
dept_sales = df.groupby('Department')['Sales'].sum()
```
2.
```python
profit_series = df.groupby(['Year', 'Quarter'])['Profit']
```
3.
```python
electronics_df = df.groupby('Category').get_group('Electronics')
```
4.
```python
status_counts = df.groupby('Status').size()
```
5.
```python
cat_grouped = df.groupby('Category', dropna=False)
```

## Level 3 — Data Analysis
1.
```python
country_aov = sales_df.groupby('Country')['OrderAmount'].mean()
print(country_aov)
```
2.
```python
dept_gender = emp_df.groupby(['Department', 'Gender'])['Salary'].mean()
print(dept_gender)
```
3.
```python
best_store = store_df.groupby('StoreLocation')['Revenue'].sum().idxmax()
print("Top Store:", best_store)
```
4.
```python
prod_qty = orders_df.groupby('ProductID')['Quantity'].sum()
print(prod_qty)
```
5.
```python
tier_activity = users_df.groupby('SubscriptionTier')['ActivityHours'].mean()
print(tier_activity)
```

## Level 4 — Debugging
1. Select numeric columns explicitly before aggregation: `df.groupby('Category')[['Sales', 'Profit']].mean()` or pass `numeric_only=True`.
2. `.get_group()` accepts a single key string (or tuple for multi-keys). Correct syntax: `g.get_group('Sales')`.
3. Use `as_index=False` in groupby or add `.reset_index()` before calling `.to_csv('output.csv', index=False)`.

## Level 5 — AI/ML Application
1. `groupby()` allows computing entity-level aggregations (e.g. historical average spend per user) to append as predictive features for ML models.
2.
```python
purchase_freq = transactions.groupby('CustomerID')['TransactionID'].count()
```
3. Group-based feature calculation captures localized sub-population baseline norms without blurring distinct domain groups into a single global mean.

## Level 6 — Interview Questions
1. Both follow identical logical partitioning semantics. Pandas GroupBy operates in-memory on DataFrames and allows custom Python lambda execution, whereas SQL operates on relational engine tables.
2. `['B']` returns a 1D Pandas Series with index `A`. `[['B']]` returns a 2D Pandas DataFrame with index `A` and column `B`.
3. High-cardinality keys create many small subgroups, increasing dictionary lookup overhead and memory footprint for group indexing.
4. `.agg()` reduces each group to a single summary row, shrinking output size. `.transform()` returns a vector aligned with the original DataFrame shape.
5. Set `dropna=False` in `df.groupby('col', dropna=False)` so rows with `NaN` keys form their own group instead of being discarded.
