# Day 119 Solutions: String Operations

## Level 1 — Basic
1. `.str`
2. `.str.strip()`
3. `.str.lower()`
4. `expand=True`
5. True.

## Level 2 — Coding
6. `s_clean = s.str.strip().str.lower()`
7. `s_clean = s.str.replace('$', '', regex=False)`
8. `df_split = s.str.split('-', expand=True)`
9. `gmail_df = df[df['Email'].str.contains('@gmail.com', na=False)]`
10. `lengths = s.str.len()`

## Level 3 — Data Analysis
11. String methods cannot be called directly on Series objects. You must use the `.str` accessor: `df['col'].str.lower()`.
12. Instructs Pandas to treat string `'$'` as a literal text character rather than a regex end-of-string anchor.
13. `Series(['A', 'C'])` (Extracts first element `str[0]` from each split list).
14. `1` (Only `'banana'` contains `'an'`).
15. `1` (`.str.upper()` preserves missing `None`/`NaN` entries).

## Level 4 — Debugging
16. Add `.str` accessor prefix: `s.str.strip()`.
17. Pass `regex=False` or escape dot `\.`: `s.str.replace('.', '_', regex=False)`.
18. Cast column to string type first: `df['col'].astype(str).str.method()`.

## Level 5 — AI/ML Application
19. `df['Age_Num'] = pd.to_numeric(df['Text_Age'].str.extract(r'(\d+)')[0], errors='coerce')`
20. `df['Is_Urgent'] = df['Text'].str.contains('urgent', case=False, na=False).astype(int)`
21. Text cleaning (lowercase, stripping punctuation/symbols) standardizes vocabulary tokens, preventing duplicate tokens like `'Apple'` and `'apple'`.

## Level 6 — Interview Solutions
22. Standard object string `.str` methods execute a Python C-loop over PyObject string pointers. It handles `NaN` checks gracefully without crashing.
23. PyArrow string backend (`string[pyarrow]`) uses Apache Arrow zero-copy contiguous memory buffers, enabling 10x-50x faster multithreaded SIMD string operations.
24. `.str.extract()` extracts first regex capture group match as DataFrame. `.str.extractall()` extracts all matches across rows into MultiIndex DataFrame. `.str.findall()` returns a list of matches per row.
25. `single_text = s.str.cat(sep=', ')`
26. `.str.contains()` returns `NaN` for missing rows by default. Pass `na=False` to force missing entries to evaluate to `False` boolean masks.
