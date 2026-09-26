# Day 155 Solutions: Categorical and Numerical Features

## Level 1 — Basic
1. `df.select_dtypes()`.
2. ZIP codes are nominal spatial identifiers. Subtracting or averaging ZIP codes is mathematically meaningless, so they must be treated as categorical features.
3. Cardinality refers to the number of unique distinct values present in a categorical column.

## Level 2 — Coding
1. `num_cols = df.select_dtypes(include=[np.number]).columns.tolist()`
2. `df['Status'] = df['Status'].astype('category')`

## Level 3 — Data Analysis
1. One-Hot Encoding a feature with 5,000 unique levels generates 5,000 new sparse binary columns, creating extreme memory consumption and high-dimensional sparsity (Curse of Dimensionality).
