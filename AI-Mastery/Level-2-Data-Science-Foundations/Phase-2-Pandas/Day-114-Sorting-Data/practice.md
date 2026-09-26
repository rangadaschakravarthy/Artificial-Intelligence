# Day 114 Practice Questions: Sorting Data

## Level 1 — Basic
1. What method sorts a DataFrame by column values?
2. What method sorts a DataFrame by row index labels?
3. How do you sort a column in descending order (highest to lowest)?
4. What parameter specifies where `NaN` values are placed during sorting?
5. True or False: `df.sort_values()` modifies the DataFrame in-place by default.

## Level 2 — Coding
6. Sort DataFrame `df` by column `'Age'` in ascending order.
7. Sort DataFrame `df` by `'Department'` (ascending) and `'Salary'` (descending).
8. Place missing `NaN` values at the top of sorted output using `na_position='first'`.
9. Extract the 5 smallest values of column `'Price'` using `df.nsmallest(5, 'Price')`.
10. Sort DataFrame `df` by index labels in descending order using `df.sort_index(ascending=False)`.

## Level 3 — Data Analysis
11. Why is `df.nlargest(5, 'col')` faster than `df.sort_values(by='col', ascending=False).head(5)`?
12. What happens to row index labels when you execute `df.sort_values(by='col')`?
13. Explain why `df.sort_values(by='col').reset_index(drop=True)` is frequently used together.
14. Predict output: `s = pd.Series([2, 1, 3]); print(s.sort_values().iloc[0])`.
15. Predict output: `df = pd.DataFrame({'a': [1, 2]}, index=['b', 'a']); print(df.sort_index().index[0])`.

## Level 4 — Debugging
16. Fix error: `ValueError: by option must be a string or list of strings`.
17. Fix bug where sorting multi-columns with `ascending=[True, False]` failed due to list length mismatch with `by=['col1']`.
18. Fix issue where sorting time-series DataFrame failed because `'Date'` column was stored as `object` strings instead of `datetime64`.

## Level 5 — AI/ML Application
19. Why must time-series financial datasets be sorted strictly by date before computing rolling features?
20. In recommendation systems, how do you extract Top-K recommended items per user using `sort_values()`?
21. Connect DataFrame sorting to ranking feature importances after ML model evaluation.

## Level 6 — Interview Questions
22. Compare algorithmic time complexity between `quicksort` ($O(N \log N)$), `mergesort` (stable), and `heapsort`.
23. Why is `mergesort` required if you want a **stable sort** (preserving relative order of equal elements)?
24. Explain how multi-column sorting handles ties in primary sort columns.
25. Demonstrate sorting a DataFrame by the string length of values in a text column.
26. How does memory management execute during large DataFrame sorting operations?
