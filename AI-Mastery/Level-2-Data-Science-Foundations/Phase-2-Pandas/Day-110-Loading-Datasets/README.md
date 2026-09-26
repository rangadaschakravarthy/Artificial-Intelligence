# Day 110 — Loading Datasets

## Learning Objectives
- Master reading external data formats into Pandas DataFrames (`read_csv`, `read_excel`, `read_json`, `read_sql`).
- Understand parsing options (separators, headers, dtypes, missing value specifiers).
- Handle large files using chunking (`chunksize`).

## Prerequisites
- Day 108: DataFrames

## Topics Covered
1. Reading CSV files (`pd.read_csv()`) and key parameters
2. Reading Excel spreadsheets (`pd.read_excel()`)
3. Reading JSON data (`pd.read_json()`)
4. Delimiters, headers, missing value handling (`sep`, `header`, `na_values`, `usecols`)
5. Memory efficient large file parsing using `chunksize`

## Why This Matters
Real-world data lives in CSV files, databases, and APIs. Reading datasets cleanly is the first step of every data science workflow.

## Real-World Usage
Loading large multi-gigabyte CSV files in chunks to avoid out-of-memory crashes.

## Study Order
1. Read `theory.md`.
2. Review `examples.md`.
3. Complete `practice.md`.
4. Verify using `solution.md`.
5. Run `code.py`.

## Completion Checklist
- [ ] I can read CSV, Excel, and JSON files into DataFrames.
- [ ] I can specify custom delimiters, column subsets, and dtypes during loading.
- [ ] I can handle custom missing value strings using `na_values`.
- [ ] I can process large datasets in chunks using `chunksize`.

## Difficulty
Beginner
