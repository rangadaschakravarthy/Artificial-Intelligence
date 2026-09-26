# Day 110 Practice Questions: Loading Datasets

## Level 1 — Basic
1. What Pandas function reads a comma-separated text file?
2. How do you specify a tab `	` separator in `pd.read_csv()`?
3. What parameter restricts CSV loading to specific column names?
4. What parameter specifies custom string indicators for missing values?
5. True or False: `pd.read_csv()` can read files directly from web URLs.

## Level 2 — Coding
6. Write code to read a CSV file `'data.csv'` ignoring the first row header (`header=None`).
7. Load only columns `['Age', 'Salary']` from `'employees.csv'`.
8. Parse a TSV (tab-separated) file `'sensor.tsv'` into a DataFrame.
9. Treat strings `'MISSING'` and `'-99'` as `NaN` during CSV import.
10. Read a JSON file string into a DataFrame using `pd.read_json()`.

## Level 3 — Data Analysis
11. Why does specifying `dtype={'Col': 'float32'}` during CSV import optimize RAM memory?
12. Explain how `chunksize=5000` alters the return type of `pd.read_csv()`.
13. Predict output: `pd.read_csv(io.StringIO("a,b\n1,2"), names=['x', 'y'])` (Why are names duplicated?).
14. How does `pd.read_csv()` handle trailing spaces in column header strings?
15. Compare memory consumption when parsing a 1GB file with vs without `usecols`.

## Level 4 — Debugging
16. Fix error: `FileNotFoundError: [Errno 2] No such file or directory: 'data.csv'`.
17. Fix error: `ParserError: Error tokenizing data. C error: Expected 3 fields in line 4, saw 4`.
18. Fix issue where numeric ID column `'00123'` was auto-converted to integer `123`, stripping leading zeros.

## Level 5 — AI/ML Application
19. How do you load a 50GB dataset iteratively to extract target label distribution using `chunksize`?
20. Why specify `float32` dtypes upon dataset loading for GPU ML training pipelines?
21. Connect dataset parsing options (`na_values`, `dtype`) to downstream ML data quality.

## Level 6 — Interview Questions
22. Explain the architectural difference between C-engine (`engine='c'`) vs Python engine (`engine='python'`) in `read_csv`.
23. How do you handle encoding issues (`UnicodeDecodeError`) when loading non-UTF-8 CSV files?
24. Explain how `pyarrow` engine speeds up CSV reading in modern Pandas (Pandas 2.0+).
25. Demonstrate reading multiple CSV files into a single concatenated DataFrame.
26. Compare performance between CSV format vs Parquet binary storage format (`read_parquet`).
