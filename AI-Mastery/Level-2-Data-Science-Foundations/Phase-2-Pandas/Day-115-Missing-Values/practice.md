# Day 115 Practice Questions: Missing Values

## Level 1 — Basic
1. What special floating-point object represents missing numbers in NumPy/Pandas?
2. What method returns a boolean DataFrame indicating `True` where values are missing?
3. What is the logical inverse method of `df.isna()`?
4. True or False: `np.nan == np.nan` evaluates to `True`.
5. How do you total all missing values across an entire DataFrame?

## Level 2 — Coding
6. Calculate the count of missing values per column for DataFrame `df`.
7. Calculate the percentage of missing values per column for DataFrame `df`.
8. Filter rows from DataFrame `df` where column `'Age'` is missing (`isna()`).
9. Filter rows from DataFrame `df` where column `'Age'` is NOT missing (`notna()`).
10. Extract row indices where at least one missing value exists using `df.isna().any(axis=1)`.

## Level 3 — Data Analysis
11. Why does inserting `np.nan` into an integer array upcast its data type to `float64`?
12. Explain the difference between `NaN` (Not a Number), `None` (Python NoneType), and `NaT` (Not a Time).
13. Predict output: `s = pd.Series([1, np.nan, 2]); print(s.sum())` (Explain skipna default).
14. Predict output: `print(np.nan in [np.nan])`.
15. Predict output: `df = pd.DataFrame({'a': [None, None]}); print(df['a'].dtype)`.

## Level 4 — Debugging
16. Fix bug where checking missing values `if val == np.nan:` failed to detect missing items.
17. Fix issue where `df.dropna()` unexpectedly deleted all rows because every row contained at least 1 NaN.
18. Fix issue where string `'null'` in a CSV was parsed as text instead of missing value `NaN`.

## Level 5 — AI/ML Application
19. Define MCAR, MAR, and MNAR missing data mechanisms and their impact on ML data imputation.
20. Write code to drop features from dataset `df` if missing value percentage exceeds 40%.
21. Connect missing value detection to automated data validation in ML inference pipelines.

## Level 6 — Interview Questions
22. Why does IEEE 754 standard define `NaN != NaN`?
23. What is Pandas Nullable Integer type (`Int64`, `boolean`) and how does it handle missing values without upcasting to float?
24. How does `df.isna()` handle Python `None` objects vs `np.nan`?
25. Demonstrate creating a missingness indicator binary feature column `df['Col_is_missing']`.
26. How do missing values affect distance-based algorithms (KNN, SVM) vs tree-based algorithms (XGBoost)?
