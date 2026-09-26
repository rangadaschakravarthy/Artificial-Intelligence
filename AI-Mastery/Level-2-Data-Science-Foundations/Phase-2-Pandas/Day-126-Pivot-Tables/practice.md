# Day 126 Practice Questions: Pivot Tables

## Level 1 — Basic
1. What parameters are required by `df.pivot_table()`?
2. How does `df.pivot()` differ from `df.pivot_table()`?
3. What parameter adds summary row and column totals to a pivot table?
4. What function performs the opposite transformation of `pivot_table()` (wide to long)?
5. How do you replace `NaN` cell values in a pivot table with `0`?

## Level 2 — Coding
1. Create a pivot table showing total `'Sales'` grouped by `'Region'` (rows) and `'Quarter'` (columns).
2. Compute mean and max `'Temperature'` by `'City'` and `'Month'` with `margins=True`.
3. Use `pd.melt()` to convert a wide survey DataFrame with columns `['ID', 'Q1_Score', 'Q2_Score']` to long format.
4. Create a multi-metric pivot table using `aggfunc={'Sales': 'sum', 'Profit': 'mean'}`.
5. Unstack a MultiIndex Series into a pivot DataFrame structure.

## Level 3 — Data Analysis
1. Reshape customer churn data into a matrix showing churn rate by plan tier and tenure group.
2. Analyze store sales performance across day of week and store branch locations.
3. Melt multi-year GDP columns (`'2020'`, `'2021'`, `'2022'`) into a tidy time series dataset.
4. Construct a cross-tabulation table of credit default frequency across income bracket and loan type.
5. Create a pivot table summarizing average website session duration by traffic source and user device.

## Level 4 — Debugging
1. Fix error: `ValueError: Index contains duplicate entries, cannot reshape` when using `df.pivot()`.
2. Fix unexpected column titles after `pd.melt()` where default names `'variable'` and `'value'` overwrite clear metadata.
3. Correct pivot output where missing combinations appear as `NaN` instead of integer zero count.

## Level 5 — AI/ML Application
1. Demonstrate constructing a sparse User-Item rating matrix using `pivot_table()` for recommender systems.
2. Explain how tidy long data format (via `pd.melt()`) simplifies seaborn visualization inputs.
3. Convert co-occurrence transaction logs into a pivot correlation matrix for market basket analysis.

## Level 6 — Interview Questions
1. Compare `df.pivot_table()` with `df.groupby().unstack()`.
2. Explain the concept of Tidy Data (Wickham 2014) and how `pd.melt()` helps enforce it.
3. How does `pivot_table()` handle memory optimization when reshaping large DataFrames?
4. How do you handle multiple values columns in `pivot_table()`?
5. How do you reset index labels on a pivot table DataFrame to return it to flat table format?
