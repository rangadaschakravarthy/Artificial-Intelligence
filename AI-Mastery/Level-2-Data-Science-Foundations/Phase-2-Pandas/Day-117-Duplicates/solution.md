# Day 117 Solutions: Duplicates

## Level 1 — Basic
1. `df.duplicated()`
2. `df.drop_duplicates()`
3. `subset=['col1', 'col2']`
4. Keeps the final (last) occurrence of duplicate records and drops earlier occurrences.
5. True.

## Level 2 — Coding
6. `dups = df[df.duplicated()]`
7. `df_clean = df.drop_duplicates(subset=['User_ID'], keep='last')`
8. `df_unique = df.drop_duplicates(keep=False)`
9. `count = df.duplicated(subset=['First_Name', 'Last_Name']).sum()`
10. `print(df['UUID'].is_unique)`

## Level 3 — Data Analysis
11. Displays all rows involved in duplication (including both original and duplicate copies), allowing full inspection of repeated records.
12. `drop_duplicates()` leaves gaps in row index labels (e.g. 0, 2, 5). Resetting index restores clean consecutive integer row labels.
13. `1` (Keeps 1 single copy of value 1).
14. `0` (`keep=False` deletes all occurrences of value 1).
15. `False` (All elements are unique).

## Level 4 — Debugging
16. Verify column string spelling in `df.columns` before passing to `subset=`.
17. Pass explicit business key columns to `subset=['User_ID', 'Action']` to ignore millisecond timestamp variations.
18. Assign back: `df = df.drop_duplicates()` or use `df.drop_duplicates(inplace=True)`.

## Level 5 — AI/ML Application
19. Duplicates in dataset split across train and validation folds cause validation samples to be identical to training samples, producing artificially high validation scores that fail in production.
20. `X_clean = X.drop_duplicates().reset_index(drop=True)`
21. Verifying primary key uniqueness prevents duplicate entity records from distorting entity aggregation metrics.

## Level 6 — Interview Solutions
22. Pandas uses C-level hash tables (`khash`). It hashes row tuple values into 64-bit integer hash keys, checking key existence in $O(1)$ lookup time.
23. Time complexity is $O(N \cdot D)$ expected time where $N$ is number of rows and $D$ is number of subset columns.
24. Repeated rows weight certain data points multiple times, shifting the sample mean towards duplicated values and falsely shrinking/expanding sample variance.
25. Sort secondary column descending first, then drop duplicates keeping first: `df.sort_values(by='Score', ascending=False).drop_duplicates(subset=['User_ID'], keep='first')`.
26. Integer hashing operates directly on 32/64-bit C-ints in registers ($O(1)$ memory). String hashing must traverse string heap pointers, incurring higher memory overhead.
