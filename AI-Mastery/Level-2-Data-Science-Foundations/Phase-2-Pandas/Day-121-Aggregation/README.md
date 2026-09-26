# Day 121 — Aggregation

## Learning Objectives
- Master multi-metric and custom aggregations using `.agg()` and `.aggregate()`.
- Apply column-specific aggregation dictionaries to grouped DataFrames.
- Execute named aggregations and handle multi-level column headers.

## Prerequisites
- Day 120: GroupBy
- Level 1 Statistics: Mean, Variance, Standard Deviation

## Topics Covered
- `df.agg()` and `df.groupby().agg()`
- Built-in aggregation strings (`'sum'`, `'mean'`, `'std'`, `'count'`, `'min'`, `'max'`)
- Applying multiple aggregations simultaneously
- Column-specific aggregation mapping dictionaries
- Named Aggregation syntax in Pandas
- Custom lambda functions in aggregation

## Why This Matters
Data science decisions require multiple perspective metrics simultaneously (e.g. min, max, average, and std dev of customer spend) rather than just a single mean.

## Real-World Usage
Financial risk modeling requires computing mean return along with standard deviation (volatility) and minimum return across asset portfolios.

## Study Order
1. Study `theory.md` for `.agg()` syntax patterns.
2. Work through `examples.md` for named aggregations.
3. Execute `code.py` to see multi-metric tables.
4. Complete `practice.md` exercises and check `solution.md`.

## Practical Work
- Compute mean, median, min, max, and std for product prices grouped by category.
- Apply named aggregation to flatten multi-index output columns cleanly.

## Interview Preparation
- What is named aggregation in Pandas, and how does it prevent multi-level column indexes?
- How do custom lambda functions affect aggregation computational performance?

## Completion Checklist
- [ ] I can apply multiple aggregation functions in a single call.
- [ ] I can map different aggregations to different columns using dictionaries.
- [ ] I can use Named Aggregation syntax.
- [ ] I can apply custom lambda aggregation functions.

## Difficulty
Intermediate
