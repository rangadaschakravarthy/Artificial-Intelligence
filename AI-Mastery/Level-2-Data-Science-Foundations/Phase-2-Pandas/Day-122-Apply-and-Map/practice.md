# Day 122 Practice Questions: Apply and Map

## Level 1 — Basic
1. Which Pandas method is used for dictionary element replacement on a Series?
2. What does `axis=1` signify when passed to `df.apply()`?
3. What is the output shape of `df.groupby('Key')['Col'].transform('mean')` relative to `df`?
4. What happens if a key is missing from a `.map()` dictionary?
5. Write a lambda function to double each element in a Series using `.apply()`.

## Level 2 — Coding
1. Map values in `df['Grade']` (`'A'`, `'B'`, `'C'`) to points (`4.0`, `3.0`, `2.0`).
2. Use `df.apply(..., axis=1)` to create a column `'Full_Name'` from `'First_Name'` and `'Last_Name'`.
3. Use `.transform()` to add a column `'City_Avg_Temp'` to a weather DataFrame.
4. Apply a custom function to round all numeric columns in a DataFrame to 2 decimal places.
5. Create a binary flag column `'Is_High_Earner'` using `.apply()` based on age and income conditions.

## Level 3 — Data Analysis
1. Calculate the percentage contribution of each transaction relative to its regional sales total using `.transform()`.
2. Normalize employee salaries within their respective departments to a 0–1 scale using `.transform()`.
3. Apply custom tax rules across state rows based on state code and income level.
4. Categorize product price continuous values into `'Budget'`, `'Mid-Range'`, and `'Premium'`.
5. Transform raw datetime strings into custom formatted financial quarter strings.

## Level 4 — Debugging
1. Fix error: `df['Total'] = df.apply(lambda r: r['A'] + r['B'])` throwing `KeyError: 'A'`.
2. Fix unmapped NaN values: `s.map({'Y': 1})` resulting in `NaN` for `'N'` values.
3. Correct performance bottleneck: replacing vectorized `df['A'] * df['B']` with `df.apply(lambda r: r['A']*r['B'], axis=1)`.

## Level 5 — AI/ML Application
1. Demonstrate computing group-wise z-score scaling using `.transform()` for non-stationary time series ML data.
2. Encode target labels into integer classes using `.map()`.
3. Explain why `GroupBy.transform()` prevents data leakage during localized feature engineering.

## Level 6 — Interview Questions
1. Compare execution speed: Vectorized NumPy math vs `Series.map()` vs `DataFrame.apply(axis=1)`.
2. How does `.applymap()` (or `.map()` in Pandas 2.1+) differ from `.apply()` on DataFrames?
3. What happens if a function passed to `df.apply()` returns a Series instead of a scalar value?
4. How do you implement parallelized apply for large DataFrames?
5. When should you choose `.replace()` over `.map()` on a Pandas Series?
