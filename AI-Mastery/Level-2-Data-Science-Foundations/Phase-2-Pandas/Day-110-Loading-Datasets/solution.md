# Day 110 Solutions: Loading Datasets

## Level 1 — Basic
1. `pd.read_csv()`
2. `sep='	'` (or `delimiter='	'`).
3. `usecols=['col1', 'col2']`
4. `na_values=['string1', 'string2']`
5. True (`pd.read_csv('https://example.com/data.csv')`).

## Level 2 — Coding
6. `df = pd.read_csv('data.csv', header=None)`
7. `df = pd.read_csv('employees.csv', usecols=['Age', 'Salary'])`
8. `df = pd.read_csv('sensor.tsv', sep='	')`
9. `df = pd.read_csv('data.csv', na_values=['MISSING', '-99'])`
10. `df = pd.read_json(json_string)`

## Level 3 — Data Analysis
11. Prevents default C-parser upcasting to double-precision `float64`, cutting array memory footprint in half (4 bytes vs 8 bytes per cell).
12. `read_csv` returns a `TextFileReader` iterator yielding 5,000-row DataFrame chunks instead of loading the whole file as a single DataFrame.
13. If `names` is supplied without `header=0`, the original header line `'a,b'` is treated as the first data row under new headers `['x', 'y']`. Pass `header=0, names=['x', 'y']`.
14. Trailing spaces become part of the column string name (e.g. `'Age '`). Strip spaces using `df.columns = df.columns.str.strip()`.
15. Loading 2 relevant columns out of 50 using `usecols` reduces RAM usage by ~96%.

## Level 4 — Debugging
16. Verify current working directory or provide absolute file path string: `os.path.exists('data.csv')`.
17. Line 4 contains extra delimiter characters. Set `on_bad_lines='skip'` to bypass corrupt rows, or fix delimiter `sep`.
18. Force column to be parsed as string: `dtype={'ID': str}` to preserve leading zeros.

## Level 5 — AI/ML Application
19. 
```python
label_counts = pd.Series(dtype=int)
for chunk in pd.read_csv('large_data.csv', chunksize=10000, usecols=['target']):
    label_counts = label_counts.add(chunk['target'].value_counts(), fill_value=0)
```
20. Directly allocates `float32` RAM buffers required by PyTorch/TensorFlow CUDA kernels, eliminating secondary conversion steps.
21. Proper parser flags prevent corrupted string types and uncaptured sentinel missing strings from polluting ML feature matrices.

## Level 6 — Interview Solutions
22. `engine='c'` is written in C for high-speed parsing. `engine='python'` is slower but supports complex multi-character regex delimiters and custom Python callbacks.
23. Specify character encoding parameter: `encoding='latin1'`, `encoding='iso-8859-1'`, or `encoding='utf-8'`.
24. PyArrow engine uses multithreaded SIMD C++ parsing with zero-copy memory mapping, reading CSVs 5x-10x faster than standard C-engine.
25. 
```python
import glob
files = glob.glob('data_*.csv')
df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
```
26. CSV is uncompressed plain text (slow $O(N)$ text parsing). Parquet is columnar binary format with snappy compression, supporting fast column-pruning reads up to 50x faster.
