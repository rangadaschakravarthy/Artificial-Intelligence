# Day 114 Solutions: Sorting Data

## Level 1 — Basic
1. `df.sort_values()`
2. `df.sort_index()`
3. Pass `ascending=False` parameter.
4. `na_position` (`'last'` or `'first'`).
5. False (It returns a new sorted DataFrame copy).

## Level 2 — Coding
6. `df_sorted = df.sort_values(by='Age')`
7. `df_sorted = df.sort_values(by=['Department', 'Salary'], ascending=[True, False])`
8. `df_sorted = df.sort_values(by='Rating', na_position='first')`
9. `smallest_5 = df.nsmallest(5, 'Price')`
10. `df_sorted_idx = df.sort_index(ascending=False)`

## Level 3 — Data Analysis
11. `nlargest` uses a min-heap algorithm ($O(N \log k)$), avoiding a full dataset sort ($O(N \log N)$).
12. Row index labels move along with their respective rows, resulting in non-consecutive scrambled index labels.
13. `sort_values` orders rows by value, and `reset_index(drop=True)` restores clean consecutive 0-based integer row indices.
14. `1`
15. `'a'`

## Level 4 — Debugging
16. Pass column name string or list of strings to `by=` parameter: `df.sort_values(by='ColName')`.
17. Ensure `ascending` boolean list length matches `by` column list length exactly: `by=['C1', 'C2'], ascending=[True, False]`.
18. Convert date string column to datetime type first: `df['Date'] = pd.to_datetime(df['Date'])` before sorting.

## Level 5 — AI/ML Application
19. Unsorted time series data causes rolling window calculations (e.g. 7-day moving average) to compute over out-of-order dates, causing severe temporal data leakage.
20. `top_k = user_predictions.groupby('user_id').apply(lambda g: g.sort_values('score', ascending=False).head(K))`
21. Sorting feature importance Series `importance.sort_values(ascending=False)` ranks features from most predictive to least predictive.

## Level 6 — Interview Solutions
22. `quicksort` is fast $O(N \log N)$ average time but unstable and $O(N^2)$ worst case. `mergesort` is stable $O(N \log N)$ time but requires $O(N)$ extra memory. `heapsort` is $O(N \log N)$ in-place but unstable.
23. A stable sort preserves the original relative row order of records that have identical values in the sort column.
24. When primary sort column values are equal (ties), Pandas compares values in the secondary sort column to determine relative row order.
25. `df.sort_values(by='TextCol', key=lambda col: col.str.len())`
26. Sorting computes an internal integer position array (`argsort`), allocating temporary RAM buffers to construct the newly ordered DataFrame.
