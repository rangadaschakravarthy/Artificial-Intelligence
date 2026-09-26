# Day 108 Practice Questions: DataFrames

## Level 1 — Basic
1. What attribute returns a tuple of `(n_rows, n_cols)` for a DataFrame?
2. What method displays concise summary info including column names, non-null counts, and dtypes?
3. How do you inspect the first 5 rows of a DataFrame?
4. What parameter in `.drop()` specifies column names to remove?
5. True or False: `df.describe()` includes string columns by default.

## Level 2 — Coding
6. Create a 3x3 DataFrame from a 2D NumPy array with column names `['A', 'B', 'C']`.
7. Print the last 4 rows of a DataFrame `df` using `.tail()`.
8. Rename column `'old_name'` to `'new_name'` in DataFrame `df`.
9. Drop column `'Unneeded'` from DataFrame `df` without mutating original `df`.
10. Display summary statistics for categorical columns using `df.describe(include=['object'])`.

## Level 3 — Data Analysis
11. Explain what `df.info()` reveals about missing data in a DataFrame.
12. Predict output of `len(df)` for a DataFrame with shape `(500, 20)`.
13. Explain why `df.drop('ColA')` raises a `KeyError` if `axis=1` or `columns=` is omitted.
14. Predict output shape of `df.drop(columns=['c1', 'c2'])` for `df` of shape `(10, 5)`.
15. Predict output: `df = pd.DataFrame({'a': [1, 2]}); df.columns = ['x']; print(df.columns.tolist())`.

## Level 4 — Debugging
16. Fix error: `KeyError: "['ColA'] not found in axis"` when attempting to drop a column.
17. Fix bug where dropping columns failed to update `df` because `inplace=True` was omitted and return value wasn't assigned.
18. Fix issue where `.describe()` returned blank output because all columns were strings (`include='all'`).

## Level 5 — AI/ML Application
19. How do you separate target column `'target'` from DataFrame `df` into `X` and `y`?
20. Why is inspecting `df.dtypes` critical before passing feature DataFrames to Scikit-Learn models?
21. Connect DataFrame column manipulation to feature engineering.

## Level 6 — Interview Questions
22. Explain how Pandas `BlockManager` stores DataFrame columns in memory under the hood.
23. What is the performance penalty of appending rows one-by-one to a DataFrame inside a loop?
24. How do `.memory_usage(deep=True)` and standard `.memory_usage()` differ?
25. Demonstrate how `pd.DataFrame.from_dict()` constructs DataFrames from nested dictionaries.
26. How do non-unique column names affect DataFrame operations?
