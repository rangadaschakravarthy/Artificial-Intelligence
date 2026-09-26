# Day 121 Solutions: Aggregation

## Level 1 — Basic
1. Strings (`'sum'`), built-in functions (`np.mean`), lists of functions/strings (`['mean', 'std']`), or dicts (`{'Col': 'sum'}`).
2. `df['Col'].agg(['mean', 'std', 'min', 'max'])`.
3. `df.groupby('Key').agg(New_Col_Name=('Source_Col', 'agg_func'))`.
4. False. `.agg()` can also be called directly on DataFrames for column-wise aggregations.
5. `'std'` or `np.std`.

## Level 2 — Coding
1.
```python
import pandas as pd
res = df.groupby('Category')['Price'].agg(['min', 'max', 'median'])
```
2.
```python
res = df.groupby('Department').agg({'Sales': 'sum', 'Rating': 'mean'})
```
3.
```python
res = df.groupby('City').agg(
    Total_Rev=('Revenue', 'sum'),
    Avg_Discount=('Discount', 'mean')
)
```
4.
```python
range_agg = df.groupby('City')['Temperature'].agg(lambda x: x.max() - x.min())
```
5.
```python
grouped_df.columns = ['_'.join(col).strip() for col in grouped_df.columns.values]
```

## Level 3 — Data Analysis
1.
```python
branch_kpis = df.groupby('Branch')['Sales'].agg(['mean', 'sum', 'count'])
print(branch_kpis)
```
2.
```python
agent_perf = tickets.groupby('AgentID').agg(
    Avg_Res_Time=('ResolutionTime', 'mean'),
    Total_Tickets=('TicketID', 'count')
)
print(agent_perf)
```
3.
```python
risk_summary = loans.groupby('CreditTier').agg(
    Default_Rate=('IsDefault', 'mean'),
    Total_Loans=('LoanID', 'count')
)
print(risk_summary)
```
4.
```python
pct_df = tx.groupby('Country')['Amount'].agg(
    P25=lambda x: x.quantile(0.25),
    P75=lambda x: x.quantile(0.75)
)
print(pct_df)
```
5.
```python
prod_metrics = df.groupby('Category')['Revenue'].agg(['sum', 'std'])
print(prod_metrics)
```

## Level 4 — Debugging
1. In dictionary syntax, map columns to lists of functions: `df.groupby('Dept').agg({'Sales': ['sum', 'mean']})`.
2. Use Named Aggregation syntax, or flatten headers: `df.columns = ['_'.join(c) for c in df.columns]`.
3. Add parentheses to call methods on Series `x`: `lambda x: x.max() - x.min()`.

## Level 5 — AI/ML Application
1.
```python
customer_features = orders.groupby('CustomerID').agg(
    Total_Orders=('OrderID', 'count'),
    Mean_Order_Value=('Amount', 'mean'),
    Max_Order_Value=('Amount', 'max')
)
```
2. Computing group-level mean and std dev allows identifying individual sensor readings that deviate by > 3 standard deviations from their subgroup baseline.
3. High transaction frequency or standard deviation of spend indicates volatile transaction patterns characteristic of fraudulent card activity.

## Level 6 — Interview Questions
1. Named Aggregation cleanly assigns single-level column titles directly, whereas dictionary aggregation can create MultiIndex column headers when multiple functions apply to one column.
2. Built-in string aggregations call Cython-optimized C code internally (fast). Custom lambda functions invoke Python interpreter loops for every group (significantly slower).
3. Built-in aggregations ignore `NaN` values by default (`skipna=True`).
4. Returning a Series converts the operation into a transformation or multi-row expansion, which may trigger a `ValueError` or result in a DataFrame with tuple indices.
5. Pass `lambda x: x.mode()[0]` or `pd.Series.mode` inside `.agg()`.
