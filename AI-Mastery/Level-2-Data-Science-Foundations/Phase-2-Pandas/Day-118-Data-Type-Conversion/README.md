# Day 118 — Data Type Conversion

## Learning Objectives
- Master type casting techniques in Pandas (`astype()`, `pd.to_numeric()`, `pd.to_datetime()`).
- Understand categorical data types (`category`) and memory optimization.
- Convert dirty text numerical strings into clean numeric columns.

## Prerequisites
- Day 90: Array Data Types
- Day 108: DataFrames

## Topics Covered
1. Explicit casting with `.astype()`
2. Robust numerical conversion using `pd.to_numeric(errors='coerce')`
3. Date string conversion using `pd.to_datetime()`
4. Categorical Data Type conversion (`astype('category')`)
5. Memory reduction profiling through type downcasting

## Why This Matters
Raw datasets read numeric data as strings or float64. Converting strings to numbers and text categories to `category` dtypes cuts RAM usage and unlocks model compatibility.

## Real-World Usage
Downcasting large DataFrames from `float64` to `float32` and `object` strings to `category` to reduce dataset memory footprint by up to 80%.

## Study Order
1. Read `theory.md`.
2. Review `examples.md`.
3. Complete `practice.md`.
4. Verify using `solution.md`.
5. Run `code.py`.

## Completion Checklist
- [ ] I can cast column dtypes using `.astype()`.
- [ ] I can handle invalid string entries using `pd.to_numeric(errors='coerce')`.
- [ ] I can convert string dates using `pd.to_datetime()`.
- [ ] I can optimize memory by converting low-cardinality strings to `category`.

## Difficulty
Intermediate
