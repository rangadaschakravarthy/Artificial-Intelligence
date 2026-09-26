# Day 126 Solutions: Pivot Tables

## Level 1 — Basic
1. `index`, `columns`, `values` (and optional `aggfunc`).
2. `df.pivot()` fails on duplicate `(index, columns)` pairs and does not aggregate. `df.pivot_table()` aggregates duplicate pairs using `aggfunc`.
3. `margins=True`.
4. `pd.melt()`.
5. Pass `fill_value=0` parameter to `pivot_table()`.

## Level 2 — Coding
1.
```python
import pandas as pd
res = df.pivot_table(index='Region', columns='Quarter', values='Sales', aggfunc='sum')
```
2.
```python
res = df.pivot_table(index='City', columns='Month', values='Temperature', aggfunc=['mean', 'max'], margins=True)
```
3.
```python
long_df = pd.melt(df, id_vars=['ID'], value_vars=['Q1_Score', 'Q2_Score'], var_name='Question', value_name='Score')
```
4.
```python
res = df.pivot_table(index='Region', columns='Category', values=['Sales', 'Profit'], aggfunc={'Sales': 'sum', 'Profit': 'mean'})
```
5.
```python
pivot_df = multi_series.unstack()
```

## Level 3 — Data Analysis
1.
```python
churn_matrix = df.pivot_table(index='PlanTier', columns='TenureGroup', values='Churned', aggfunc='mean')
print(churn_matrix)
```
2.
```python
sales_matrix = df.pivot_table(index='DayOfWeek', columns='Branch', values='Sales', aggfunc='sum')
print(sales_matrix)
```
3.
```python
gdp_long = pd.melt(gdp_df, id_vars=['Country'], value_vars=['2020', '2021', '2022'], var_name='Year', value_name='GDP')
```
4.
```python
default_crosstab = df.pivot_table(index='IncomeBracket', columns='LoanType', values='Default', aggfunc='mean')
```
5.
```python
session_piv = df.pivot_table(index='TrafficSource', columns='Device', values='SessionDuration', aggfunc='mean')
```

## Level 4 — Debugging
1. Replace `df.pivot()` with `df.pivot_table(..., aggfunc='mean')` to resolve duplicate index entries.
2. Specify `var_name` and `value_name` explicitly in `pd.melt(..., var_name='Metric', value_name='Val')`.
3. Set `fill_value=0` in `pivot_table()`.

## Level 5 — AI/ML Application
1.
```python
user_item = ratings.pivot_table(index='User_ID', columns='Item_ID', values='Rating', fill_value=0)
```
2. Seaborn visualization APIs expect Tidy Data format (each column a variable, each row an observation), easily produced via `pd.melt()`.
3.
```python
co_occurrence = basket.pivot_table(index='Item_A', columns='Item_B', values='Count', fill_value=0)
```

## Level 6 — Interview Questions
1. `df.pivot_table()` is syntactic sugar for `df.groupby(['index_col', 'col_col'])['val'].agg().unstack()`. Both produce identical outputs.
2. Tidy Data principle states: 1) Each variable is a column, 2) Each observation is a row, 3) Each observational unit forms a table. `pd.melt()` converts untidy wide tables into tidy long format.
3. `pivot_table()` converts grouping categories to Categorical dtypes internally to minimize RAM usage during matrix construction.
4. Pass a list to `values=['Sales', 'Profit']`; Pandas creates hierarchical MultiIndex columns for each value metric.
5. Call `.reset_index()` on the resulting pivot table DataFrame.
