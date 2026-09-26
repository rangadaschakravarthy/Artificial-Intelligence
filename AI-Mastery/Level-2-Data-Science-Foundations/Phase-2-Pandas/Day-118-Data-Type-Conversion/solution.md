# Day 118 Solutions: Data Type Conversion

## Level 1 — Basic
1. `.astype()`
2. `pd.to_numeric()`
3. `pd.to_datetime()`
4. `errors='coerce'`
5. False (Categorical dtype is only memory-efficient for low-cardinality columns with repeated category strings).

## Level 2 — Coding
6. `df['Price'] = df['Price'].astype(float)`
7. `s_clean = pd.to_numeric(s, errors='coerce')`
8. `df['Date'] = pd.to_datetime(df['Date'])`
9. `df['Gender'] = df['Gender'].astype('category')`
10. `df[col] = pd.to_numeric(df[col], downcast='integer')`

## Level 3 — Data Analysis
11. Standard `int64` cannot represent `NaN`. Attempting to convert float `NaN` to standard integer raises a `ValueError`.
12. Unparseable invalid date strings are converted into missing timestamp `NaT` (Not a Time).
13. `2.0`
14. If every string is unique (10,000 unique strings for 10,000 rows), `category` creates 10,000 unique dictionary entries plus 10,000 integer codes, consuming more RAM than raw strings.
15. `int8` (Automatically picks smallest integer byte size capable of holding values 1, 2, 3).

## Level 4 — Debugging
16. Use Pandas Nullable integer type: `df['col'].astype('Int64')` or fill missing values before casting.
17. Strip thousands comma separator first: `pd.to_numeric(df['col'].str.replace(',', ''), errors='coerce')`.
18. String `'False'` is a non-empty string; Python `.astype(bool)` evaluates any non-empty string as `True`! Map explicitly: `df['col'].map({'True': True, 'False': False})`.

## Level 5 — AI/ML Application
19. `df[df.select_dtypes('float64').columns] = df.select_dtypes('float64').astype(np.float32)`
20. `df['Tier'] = pd.Categorical(df['Tier'], categories=['Low', 'Medium', 'High'], ordered=True)`
21. Downcasting float64 to float32 halves RAM usage, allowing double the batch size $B$ during GPU training without out-of-memory crashes.

## Level 6 — Interview Solutions
22. `category` dtype creates an internal dictionary array of unique categories (e.g. `['NY', 'LA']`) and stores column values as an array of compact 8-bit integer codes (`[0, 1, 0]`).
23. `int64` is standard NumPy 64-bit integer (cannot hold `NaN`). `Int64` is Pandas Nullable integer (uses an auxiliary boolean mask to hold `NaN`).
24. `float64` uses 8 bytes (53-bit mantissa, 15-17 decimal digits precision). `float32` uses 4 bytes (24-bit mantissa, 6-9 decimal digits precision).
25. `num_df = df.select_dtypes(include=[np.number]); cat_df = df.select_dtypes(include=['category', 'object'])`.
26. Matching optimal small dtypes (`float32`, `int8`) allows CPU SIMD registers to pack and process 2x-8x more element operations per clock cycle.
