# Day 120 Practice Questions: GroupBy

## Level 1 — Basic
1. What three steps constitute the Split-Apply-Combine paradigm?
2. What object type is returned by `df.groupby('col')` before applying an aggregation?
3. How do you retain key columns as regular DataFrame columns during grouping?
4. Write syntax to group a DataFrame by column `'City'`.
5. How can you view all row indices corresponding to each group key?

## Level 2 — Coding
1. Group `df` by `'Department'` and calculate total sales for each department.
2. Group `df` by `['Year', 'Quarter']` and select the `'Profit'` column.
3. Use `.get_group()` to extract all rows corresponding to group `'Electronics'`.
4. Group by `'Status'` without resetting index, and find group sizes.
5. Create a GroupBy object on `'Category'` keeping `NaN` keys intact (`dropna=False`).

## Level 3 — Data Analysis
1. Load sales data and calculate average order value (AOV) per country.
2. Analyze employee salaries by department and gender simultaneously.
3. Identify which store location achieved the highest total revenue.
4. Calculate total quantity sold per product ID.
5. Compare mean user activity hours across free vs premium subscription tiers.

## Level 4 — Debugging
1. Fix the error: `df.groupby('Category').mean()` throws `TypeError: Could not convert string to float`.
2. Correct code: `g = df.groupby('Dept'); g.get_group('Sales', 'HR')`.
3. Fix unexpected index loss when exporting grouped data to CSV.

## Level 5 — AI/ML Application
1. Explain how `groupby()` can be used to engineer historical user features for a recommendation algorithm.
2. Group customer transaction logs by `CustomerID` to calculate purchase frequency.
3. How does group-based feature calculation help prevent global distribution distortion?

## Level 6 — Interview Questions
1. Compare Pandas `groupby()` with SQL `GROUP BY`.
2. What is the difference between `df.groupby('A')['B'].mean()` and `df.groupby('A')[['B']].mean()`?
3. How does memory usage behave during grouping on high-cardinality categorical keys?
4. Explain how `.transform()` differs from standard `.agg()` inside a GroupBy pipeline.
5. How do you handle missing values in key columns during grouping?
