# Day 123 Solutions: Merge

## Level 1 — Basic
1. Inner, Left (Left Outer), Right (Right Outer), Outer (Full Outer).
2. Unmatched left rows are discarded from the output.
3. `pd.merge(df1, df2, left_on='ID', right_on='User_ID')`.
4. `suffixes=('_left_name', '_right_name')`.
5. It creates a `_merge` Categorical column indicating whether each row came from `left_only`, `right_only`, or `both`.

## Level 2 — Coding
1.
```python
import pandas as pd
res = pd.merge(df1, df2, on='ProductID', how='inner')
```
2.
```python
res = pd.merge(customers_df, orders_df, on='CustomerID', how='left')
```
3.
```python
res = pd.merge(df_a, df_b, on='Date', how='outer', suffixes=('_left', '_right'))
```
4.
```python
res = pd.merge(df_left, df_right, on=['Year', 'Month'], how='inner')
```
5.
```python
merged = pd.merge(df_left, df_right, on='Key', how='outer', indicator=True)
left_only_df = merged[merged['_merge'] == 'left_only']
```

## Level 3 — Data Analysis
1.
```python
merged = customers.merge(orders, on='CustomerID', how='left')
segment_spend = merged.groupby('Segment')['OrderAmount'].sum()
print(segment_spend)
```
2.
```python
audit = inventory.merge(sales, on='SKU', how='outer', indicator=True)
unlisted = audit[audit['_merge'] == 'left_only']
print("Unlisted Products:
", unlisted)
```
3.
```python
emp_dept = emp.merge(depts, on='DeptID')
payroll = emp_dept.groupby('DeptName').agg(
    Total_Payroll=('Salary', 'sum'),
    Budget=('Budget', 'first')
)
over_budget = payroll[payroll['Total_Payroll'] > payroll['Budget']]
print(over_budget)
```
4.
```python
campaign = mktg.merge(conversions, on=['CampaignID', 'Date'], how='left')
```
5.
```python
sensor_maint = sensors.merge(maint, on='Timestamp', how='left')
```

## Level 4 — Debugging
1. The join keys contain non-unique duplicate values in both tables (many-to-many relationship). Deduplicate keys before merging or validate cardinality (`validate='1:m'`).
2. Match key parameter casing: `pd.merge(df1, df2, left_on='id', right_on='ID')`.
3. If both key names match (`on='ID'`), single key column is retained. If using `left_on` and `right_on`, drop redundant right key afterwards: `.drop(columns=['right_key_name'])`.

## Level 5 — AI/ML Application
1.
```python
X_y_dataset = features_df.merge(labels_df, on='Sample_ID', how='inner')
```
2. Many-to-many key duplicates duplicate observations across rows. If split after merge, identical records leak between train and test sets.
3.
```python
ml_matrix = static_users.merge(dynamic_aggregates, on='UserID', how='left').fillna(0)
```

## Level 6 — Interview Questions
1. `pd.merge()` is in-memory Python syntax equivalent to SQL `JOIN ON`. Parameters (`how`, `left_on`, `right_on`) map 1-to-1 to SQL clauses (`INNER JOIN`, `LEFT JOIN ON`).
2. A Cross Join generates the Cartesian product of all rows. Executed using `how='cross'` in Pandas 1.2+.
3. In Pandas merges, `NaN` values do NOT match other `NaN` values (treated as unique missing keys).
4. Merging on indexed columns (`left_index=True`) is significantly faster because Pandas utilizes existing index hash maps.
5. Pass the `validate` parameter: `validate='1:1'`, `validate='1:m'`, or `validate='m:1'`. If validation fails, Pandas raises a `MergeError`.
