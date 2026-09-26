# Day 118 Practice Questions: Data Type Conversion

## Level 1 — Basic
1. What method converts a DataFrame column to a specified data type?
2. What function safely converts text strings to numbers, turning invalid text into `NaN`?
3. What function parses string dates into `datetime64` objects?
4. What parameter in `pd.to_numeric()` converts invalid string entries to `NaN`?
5. True or False: Converting high-cardinality unique string IDs to `category` saves memory.

## Level 2 — Coding
6. Convert column `df['Price']` from string to float using `.astype(float)`.
7. Robustly parse `s = pd.Series(['10', '20', 'bad', '30'])` into numeric values using `pd.to_numeric()`.
8. Convert string column `df['Date']` to datetime using `pd.to_datetime()`.
9. Convert low-cardinality string column `df['Gender']` to `'category'` data type.
10. Automatically downcast integer columns in `df` using `pd.to_numeric(downcast='integer')`.

## Level 3 — Data Analysis
11. Why does `s.astype(int)` raise `ValueError` when `s` contains missing `NaN` values?
12. Explain what `errors='coerce'` does in `pd.to_datetime('invalid_date', errors='coerce')`.
13. Predict output: `s = pd.Series(['1.5', '2.5']); print(s.astype(float).mean())`.
14. Explain why `category` data type is ineffective for high-cardinality columns (e.g. Unique User UUIDs).
15. Predict output dtype of `pd.to_numeric(pd.Series([1, 2, 3]), downcast='integer')`.

## Level 4 — Debugging
16. Fix error: `ValueError: cannot convert float NaN to integer` when casting column containing NaNs to int.
17. Fix error: `ValueError: Unable to parse string "1,000.50" at position 0` (Strip commas first).
18. Fix issue where converting boolean column `'True'`/`'False'` strings using `.astype(bool)` parsed `'False'` as `True`!

## Level 5 — AI/ML Application
19. How do you convert all `float64` columns in a 100-feature DataFrame to `float32` for PyTorch?
20. Convert categorical column `df['Tier']` (`['Low', 'Medium', 'High']`) to ordered category type.
21. Connect type conversion to reducing dataset RAM footprint before distributed ML training.

## Level 6 — Interview Questions
22. Explain how Pandas `category` dtype stores categories and integer codes under the hood.
23. What is the difference between `astype('int64')` vs Pandas Nullable `astype('Int64')`?
24. Explain floating-point precision differences between `float64` (double) and `float32` (single).
25. Demonstrate how `df.select_dtypes()` filters columns by data type family (`include=[np.number]`).
26. How do data type conversions affect vectorized C-loop computational throughput?
