# Day 117 Practice Questions: Duplicates

## Level 1 — Basic
1. What method returns a boolean Series indicating duplicate rows?
2. What method removes duplicate rows from a DataFrame?
3. What parameter restricts duplicate checking to a specific list of columns?
4. What does `keep='last'` specify during deduplication?
5. True or False: `df.duplicated().sum()` counts the total number of duplicate rows.

## Level 2 — Coding
6. Detect duplicate rows in DataFrame `df` using `df.duplicated()`.
7. Remove duplicate rows from DataFrame `df` based on column `'User_ID'`, keeping the last occurrence.
8. Remove ALL rows that have duplicates using `df.drop_duplicates(keep=False)`.
9. Count duplicate rows in DataFrame `df` based on subset `['First_Name', 'Last_Name']`.
10. Check if column `'UUID'` contains any duplicate values using `.is_unique`.

## Level 3 — Data Analysis
11. Explain what `df[df.duplicated(keep=False)]` displays.
12. Why should you reset index after executing `df.drop_duplicates()`?
13. Predict output: `df = pd.DataFrame({'a': [1, 1, 1]}); print(len(df.drop_duplicates()))`.
14. Predict output: `df = pd.DataFrame({'a': [1, 1, 1]}); print(len(df.drop_duplicates(keep=False)))`.
15. Predict output: `df = pd.DataFrame({'a': [1, 2, 3]}); print(df.duplicated().any())`.

## Level 4 — Debugging
16. Fix error: `KeyError: 'user_id'` when passing column name to `subset=`.
17. Fix bug where `drop_duplicates()` failed to remove duplicates because timestamp columns varied by milliseconds.
18. Fix issue where deduplication was accidentally executed on a copy without assigning back or using `inplace=True`.

## Level 5 — AI/ML Application
19. Why does duplicate data in a training dataset cause artificial model overfitting during cross-validation?
20. Write a function that audits and removes exact feature vector duplicates $X$ before model fitting.
21. Connect primary key uniqueness verification to data integrity in ML pipelines.

## Level 6 — Interview Questions
22. How does Pandas compute row hashes under the hood in `duplicated()` C routines?
23. What is the time complexity of `drop_duplicates()` for $N$ rows and $D$ columns?
24. Explain why duplicate rows can corrupt statistical metrics like Mean and Variance.
25. Demonstrate how to keep the duplicate record with the highest value in a secondary score column.
26. Compare memory overhead of checking duplicates on integer columns vs string columns.
