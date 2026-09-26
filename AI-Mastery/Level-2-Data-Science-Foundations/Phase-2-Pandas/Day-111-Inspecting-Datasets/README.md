# Day 111 — Inspecting Datasets

## Learning Objectives
- Perform comprehensive structural inspection of newly loaded DataFrames.
- Master `.info()`, `.describe()`, `.head()`, `.tail()`, `.sample()`, `.shape`, `.dtypes`, `.isna().sum()`.
- Identify memory usage, missing value proportions, and unexpected data types.

## Prerequisites
- Day 108: DataFrames
- Day 110: Loading Datasets

## Topics Covered
1. Random sampling for auditing (`df.sample()`)
2. Memory profiling (`df.info(memory_usage='deep')`)
3. Checking missing value counts & percentages (`df.isna().sum()`)
4. Inspecting unique value distributions (`df.nunique()`)
5. Identifying data corruption and type anomalies

## Why This Matters
Inspecting dataset schema prior to modeling catches data corruption, missing fields, and type misclassifications early.

## Real-World Usage
Creating automated dataset audit reports during initial exploratory data analysis.

## Study Order
1. Read `theory.md`.
2. Review `examples.md`.
3. Complete `practice.md`.
4. Verify using `solution.md`.
5. Run `code.py`.

## Completion Checklist
- [ ] I can audit DataFrame memory usage and dtypes.
- [ ] I can compute missing value counts and missing percentages per column.
- [ ] I can randomly sample dataset rows using `.sample()`.
- [ ] I can identify non-numeric objects disguised in numerical columns.

## Difficulty
Beginner
