# Day 108 — DataFrames

## Learning Objectives
- Master the Pandas `DataFrame` 2D tabular data structure.
- Understand DataFrame construction from dicts, lists, NumPy matrices, and Series.
- Inspect attributes (`.shape`, `.columns`, `.index`, `.dtypes`, `.info()`, `.describe()`).

## Prerequisites
- Day 106: Pandas Introduction
- Day 107: Series

## Topics Covered
1. What is a Pandas `DataFrame` (2D Labeled Table)
2. Creating DataFrames from multiple data sources
3. DataFrame attributes (`shape`, `columns`, `index`, `dtypes`, `values`)
4. Structural inspection routines (`df.head()`, `df.tail()`, `df.info()`, `df.describe()`)
5. Renaming and dropping columns/rows (`df.rename()`, `df.drop()`)

## Why This Matters
The DataFrame is the fundamental data structure used throughout data science for cleaning, exploratory data analysis, and feature engineering.

## Real-World Usage
Inspecting raw tabular data schema, checking data types, missing values, and column summaries upon loading a dataset.

## Study Order
1. Read `theory.md`.
2. Review `examples.md`.
3. Complete `practice.md`.
4. Verify using `solution.md`.
5. Run `code.py`.

## Completion Checklist
- [ ] I can create DataFrames from dictionaries, lists, and NumPy arrays.
- [ ] I can inspect DataFrame schema using `.info()` and `.describe()`.
- [ ] I can rename columns using `.rename()`.
- [ ] I can drop columns and rows using `.drop()`.

## Difficulty
Beginner
