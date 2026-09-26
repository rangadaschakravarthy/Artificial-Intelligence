# Day 123 Practice Questions: Merge

## Level 1 — Basic
1. Name the four primary join types supported by `pd.merge()`.
2. What happens to unmatched left table rows during an Inner join?
3. How do you merge two DataFrames where the key column is named `'ID'` in the left DF and `'User_ID'` in the right DF?
4. What parameter adds string suffixes to overlapping column titles?
5. What does the `indicator=True` parameter do?

## Level 2 — Coding
1. Perform an Inner join on `df1` and `df2` using key column `'ProductID'`.
2. Perform a Left join keeping all records from `customers_df` matched against `orders_df`.
3. Perform an Outer join on `df_a` and `df_b` on key `'Date'` with suffixes `('_left', '_right')`.
4. Merge `df_left` and `df_right` using multi-keys `['Year', 'Month']`.
5. Filter rows after an outer join to extract records present ONLY in the left DataFrame using `_merge`.

## Level 3 — Data Analysis
1. Merge customer demographics with order history and calculate total spend per customer segment.
2. Perform a full audit of product inventory versus website sales listings to identify unlisted products.
3. Merge employee records with department budgets to find departments exceeding target payroll.
4. Combine monthly marketing spend with campaign conversion logs.
5. Merge sensor readings with maintenance logs on timestamps.

## Level 4 — Debugging
1. Fix unexpected row explosion: merging two DataFrames of 1,000 rows results in 500,000 rows.
2. Fix KeyError: `pd.merge(df1, df2, on='ID')` where `df1` has `'id'` (lowercase) and `df2` has `'ID'`.
3. Fix error where key column is dropped or duplicated after merge.

## Level 5 — AI/ML Application
1. Demonstrate building an ML training dataset by merging primary features with target labels on `Sample_ID`.
2. How can an unexpected row expansion during merging invalidate ML train/test splitting?
3. Merge static user attributes with dynamic aggregate behavioral features for churn prediction.

## Level 6 — Interview Questions
1. Compare Pandas `pd.merge()` with SQL `JOIN` syntax.
2. What is a Cross Join, and how is it executed in Pandas?
3. How does Pandas handle `NaN` values in join keys during a merge?
4. Compare performance of merging on indexed columns versus regular data columns.
5. How do you validate join cardinality (e.g. enforcing 1-to-1 or 1-to-many joins) in `pd.merge()`?
