# Day 107 Practice Questions: Series

## Level 1 — Basic
1. What is the fundamental difference between a 1D NumPy array and a Pandas Series?
2. How do you assign a name to a Series during creation?
3. What property extracts the underlying NumPy array from a Series?
4. What method counts the occurrences of each unique value in a Series?
5. True or False: Converting a Python dictionary to a Series uses dictionary keys as Index labels.

## Level 2 — Coding
6. Create a Series with values `[100, 200, 300]` and index `['Jan', 'Feb', 'Mar']`.
7. Compute the 90th percentile of Series `s = pd.Series(range(100))`.
8. Find unique values and their frequencies for `s = pd.Series(['A', 'B', 'A', 'C', 'B', 'A'])`.
9. Convert Series `s = pd.Series([1.5, 2.5, 3.5])` to a integer Series using `.astype(int)`.
10. Extract values from Series `s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])` where values are $> 15$.

## Level 3 — Data Analysis
11. Predict output of adding `s1 = pd.Series([1, 2], index=['a', 'b'])` and `s2 = pd.Series([10, 20], index=['b', 'c'])`.
12. How does `s.value_counts(dropna=False)` handle missing `NaN` values?
13. Predict output: `s = pd.Series([1, 2, 3], index=['x', 'y', 'z']); print(s['y'])`.
14. Predict output: `s = pd.Series([10, 20, 30]); print(s.mean())`.
15. Explain why `s.describe()` outputs different summary metrics for string Series vs numerical Series.

## Level 4 — Debugging
16. Fix error: `KeyError: 'd'` when trying to index `s['d']` on Series indexed `['a', 'b', 'c']`.
17. Fix bug where adding two Series returned all `NaN` values due to completely non-matching index labels.
18. Fix issue where `s.value_counts()` ignored missing `NaN` values during data auditing.

## Level 5 — AI/ML Application
19. How do you check if a target Series `y` has a severe class imbalance problem?
20. Implement boolean masking on feature Series `df['Income']` to filter out values below $0.
21. Connect Series index alignment to combining prediction Series from multiple models.

## Level 6 — Interview Questions
22. Explain how Pandas Series index alignment handles non-unique/duplicate index labels.
23. What is the difference between `.loc[]` and `.iloc[]` when indexing a Series with integer index labels `[10, 20, 30]`?
24. How does `Series.map()` differ from `Series.apply()`?
25. Demonstrate how `pd.concat()` combines multiple Series into a DataFrame.
26. How does memory alignment execute when operating on two Series with 1,000,000 labeled rows?
