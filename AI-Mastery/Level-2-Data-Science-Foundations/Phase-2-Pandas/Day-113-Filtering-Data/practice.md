# Day 113 Practice Questions: Filtering Data

## Level 1 — Basic
1. What bitwise operator represents element-wise OR in Pandas filtering?
2. What bitwise operator represents element-wise NOT (negation) in Pandas?
3. What method filters rows based on a list of allowed values?
4. What method checks if values fall within an inclusive numerical range $[A, B]$?
5. True or False: `df.query("Age > 30")` modifies `df` in-place.

## Level 2 — Coding
6. Filter DataFrame `df` where column `'Age'` is $\ge 21$.
7. Filter DataFrame `df` where `'City'` is either `'New York'` or `'London'` using `.isin()`.
8. Filter DataFrame `df` where `'Salary'` is between $50,000 and $100,000 inclusive using `.between()`.
9. Filter DataFrame `df` where `'Department'` is NOT `'Sales'` using `~`.
10. Use `df.query()` to select rows where `'Score'` is $> 80$ and `'Status'` is `'Active'`.

## Level 3 — Data Analysis
11. Why do multiple conditions in `df[(df['A'] > 1) & (df['B'] < 5)]` require enclosing parentheses?
12. Explain what `df[~df['col'].isin(vals)]` extracts.
13. Predict output: `df = pd.DataFrame({'a': [10, 20, 30]}); print(len(df[df['a'] > 15]))`.
14. Compare readability and execution of `df.query()` vs standard boolean masking.
15. Predict output: `df = pd.DataFrame({'x': [1, 2, 3]}); print(len(df[df['x'].between(1, 2)]))`.

## Level 4 — Debugging
16. Fix error: `ValueError: cannot compare a dtyped [float64] array with a scalar of type [bool]`.
17. Fix operator precedence error: `df[df['A'] > 10 & df['B'] == 'Y']`.
18. Fix error in query string accessing Python variable: `df.query("Age > min_age")` (Use `@min_age`).

## Level 5 — AI/ML Application
19. How do you filter out invalid negative values in feature column `df['Price']`?
20. In fraud detection, extract transaction rows where `Amount > 10000` OR `Is_Foreign == True`.
21. Connect boolean filtering to generating evaluation metrics on specific data sub-cohorts.

## Level 6 — Interview Questions
22. Explain how `numexpr` optimizes execution speed and memory in `df.query()`.
23. What is the difference between `.str.contains()` vs `.str.match()` in string pattern filtering?
24. How does index label preservation affect filtered DataFrames?
25. Demonstrate filtering using callable functions inside `.loc[lambda df: ...]`.
26. How do boolean array filters perform memory allocations under the hood?
