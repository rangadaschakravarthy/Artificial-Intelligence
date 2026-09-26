# Day 119 Practice Questions: String Operations

## Level 1 — Basic
1. What accessor attribute must precede string methods in Pandas Series?
2. What method strips leading and trailing whitespace from strings?
3. What method converts strings to lowercase?
4. What parameter in `.str.split()` expands split items into separate DataFrame columns?
5. True or False: Vectorized string methods automatically preserve missing `NaN` values.

## Level 2 — Coding
6. Strip whitespace and convert Series `s = pd.Series(['  apple ', ' BANANA '])` to lowercase.
7. Replace dollar sign `$` in `s = pd.Series(['$10', '$20'])` with empty string `''`.
8. Split `s = pd.Series(['NY-USA', 'LA-USA'])` by hyphen `-` into a 2-column DataFrame.
9. Filter rows in DataFrame `df` where column `'Email'` contains `'@gmail.com'`.
10. Calculate character length of each string in `s = pd.Series(['Python', 'Pandas'])` using `.str.len()`.

## Level 3 — Data Analysis
11. Why does `df['col'].lower()` raise an `AttributeError`?
12. Explain what `regex=False` does in `s.str.replace('$', '', regex=False)`.
13. Predict output: `s = pd.Series(['A B', 'C D']); print(s.str.split(' ').str[0])`.
14. Predict output: `s = pd.Series(['apple', 'banana']); print(s.str.contains('an').sum())`.
15. Predict output: `s = pd.Series(['x', None]); print(s.str.upper().isna().sum())`.

## Level 4 — Debugging
16. Fix error: `AttributeError: 'Series' object has no attribute 'strip'`.
17. Fix unexpected regex replacement bug when replacing periods `.` in IP addresses (`s.str.replace('.', '_')`).
18. Fix error when calling `.str` methods on a non-string numeric column.

## Level 5 — AI/ML Application
19. How do you extract numerical digits from messy text strings (e.g. `'25 years'`) using `str.extract(r'(\d+)')`?
20. Create one-hot boolean feature flags for text keywords (e.g. `'Urgent'`, `'Discount'`) using `.str.contains()`.
21. Connect string cleaning to preparing text features for Bag-of-Words or TF-IDF vectorization.

## Level 6 — Interview Questions
22. Explain how Pandas string operations execute under the hood compared to Python list comprehensions.
23. What is the Arrow string backend (`string[pyarrow]`) introduced in Pandas 2.0+ and why is it faster?
24. How do `.str.extract()`, `.str.extractall()`, and `.str.findall()` differ?
25. Demonstrate how `s.str.cat(sep=', ')` concatenates Series string elements into a single text string.
26. How do missing `NaN` values affect regex evaluation in `.str.contains()`?
