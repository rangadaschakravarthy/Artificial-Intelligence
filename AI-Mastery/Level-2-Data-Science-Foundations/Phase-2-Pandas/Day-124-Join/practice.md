# Day 124 Practice Questions: Join

## Level 1 — Basic
1. What key structure does `df.join()` align by default?
2. What is the default join type (`how` parameter) for `df.join()`?
3. How do you resolve a `ValueError: columns overlap` error in `.join()`?
4. How do you join DataFrame `df2` onto `df1` using column `'User_ID'` in `df1` against `df2`'s index?
5. True or False: `df.join()` can accept a list of multiple DataFrames.

## Level 2 — Coding
1. Join `df1` and `df2` on index using `how='inner'`.
2. Perform a `.join()` with custom column suffixes `'_2022'` and `'_2023'`.
3. Set column `'ID'` as index of `df2`, then join it onto `df1`.
4. Join 3 DataFrames `df_a`, `df_b`, `df_c` sharing identical row index keys.
5. Perform a Right join using `.join()`.

## Level 3 — Data Analysis
1. Combine monthly sales DataFrames from 4 regional offices indexed by `Date`.
2. Align patient demographic data with lab test results using `PatientID` index.
3. Merge financial balance sheets with income statements using `CompanyTicker` index.
4. Align multi-sensor telemetry streams on timestamp index.
5. Create a unified customer profile matrix by joining risk, activity, and demographic tables.

## Level 4 — Debugging
1. Fix `ValueError: columns overlap with no suffix specified`.
2. Fix unexpected `NaN` values resulting from joining DataFrames with mismatched index data types (e.g. string vs int).
3. Fix KeyError when calling `df1.join(df2, on='Key')` where `'Key'` does not exist in `df1`.

## Level 5 — AI/ML Application
1. Demonstrate joining separate feature extraction outputs on sample ID index to construct a master ML matrix.
2. Why is index joining safer than sequential column concatenation for ML feature alignment?
3. How does index alignment prevent row order mismatch errors during target label joining?

## Level 6 — Interview Questions
1. When would you prefer `df.join()` over `pd.merge()`?
2. How does `.join()` handle duplicate index values in either DataFrame?
3. What is the computational complexity of index-based joins in Pandas?
4. How can you convert a column-based merge problem into an index-based join problem?
5. How does `.join()` operate on MultiIndex DataFrames?
