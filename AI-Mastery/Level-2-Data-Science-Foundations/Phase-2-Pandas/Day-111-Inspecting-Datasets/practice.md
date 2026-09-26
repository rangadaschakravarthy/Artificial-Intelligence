# Day 111 Practice Questions: Inspecting Datasets

## Level 1 — Basic
1. What function displays concise summary info including non-null counts and column dtypes?
2. What method returns a random sample of rows from a DataFrame?
3. What method calculates the number of unique values in each column?
4. True or False: `df.isna().sum()` returns the total number of missing values per column.
5. What attribute reports total RAM bytes consumed by a DataFrame?

## Level 2 — Coding
6. Write code to sample 10% of rows randomly from DataFrame `df` using `.sample(frac=0.1)`.
7. Calculate the percentage of missing values per column in DataFrame `df`.
8. Inspect memory consumption of DataFrame `df` including deep string inspection.
9. Filter columns from DataFrame `df` that have a data type of `object`.
10. Check if all column names in `df` are unique using `df.columns.is_unique`.

## Level 3 — Data Analysis
11. Why is `.sample(5)` often better than `.head(5)` for inspecting real-world datasets?
12. Explain what `pd.to_numeric(df['col'], errors='coerce')` does when encountering string invalid entries.
13. Predict output: `df = pd.DataFrame({'a': [1, None, 3]}); print(df.isna().sum().sum())`.
14. Predict output shape of `df.sample(frac=0.5)` for `df` of shape `(100, 10)`.
15. Why does high cardinality in a categorical column create problems during one-hot encoding?

## Level 4 — Debugging
16. Fix bug where `.head()` showed numbers but column dtype was `object` due to hidden space characters.
17. Fix error: `ValueError: Cannot sample3 rows from a dataset of 2 rows` (Set `replace=True` or reduce `n`).
18. Fix issue where `df.isna().sum()` returned `0` despite missing values being present as string `'N/A'`.

## Level 5 — AI/ML Application
19. How do you construct an automated dataset inspection report dictionary for an ML pipeline?
20. Why audit feature cardinality prior to applying categorical encoding transformations?
21. Connect dataset inspection to identifying data leakage indicators (e.g. 100% target correlation).

## Level 6 — Interview Questions
22. Explain how `df.info()` computes non-null counts under the hood.
23. What is the difference between `df.nunique()` and `len(df.unique())`?
24. Explain why string object columns consume substantially more memory than categorical columns.
25. Demonstrate how to profile memory usage of each DataFrame column in megabytes (MB).
26. How do random seed states (`random_state`) ensure deterministic row sampling in data pipelines?
