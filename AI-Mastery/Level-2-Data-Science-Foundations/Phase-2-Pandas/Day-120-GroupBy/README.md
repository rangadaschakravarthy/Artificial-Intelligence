# Day 120 — GroupBy

## Learning Objectives
- Master the Split-Apply-Combine paradigm in Pandas using `.groupby()`.
- Perform single-column and multi-column grouping on categorical attributes.
- Inspect group structures, access individual groups, and extract group keys.

## Prerequisites
- Day 108: DataFrames
- Day 113: Filtering Data

## Topics Covered
- Split-Apply-Combine concept
- `df.groupby()` syntax
- Grouping by single vs multiple columns
- `DataFrameGroupBy` and `SeriesGroupBy` objects
- Accessing groups with `.get_group()` and `.groups` attribute

## Why This Matters
Grouping allows data scientists to segment data into meaningful buckets (e.g., revenue by region, churn rate by customer tier) and perform targeted cohort analysis.

## Real-World Usage
E-commerce platforms group sales data by product category and region to analyze seasonal buying trends and calculate regional average order values (AOV).

## Study Order
1. Read `theory.md` for Split-Apply-Combine intuition.
2. Examine `examples.md` for syntax patterns.
3. Run `code.py` to observe grouping outputs.
4. Attempt `practice.md` exercises and verify with `solution.md`.

## Practical Work
- Group a retail dataset by store branch and compute branch-wise metrics.
- Perform multi-level grouping by Department and Job Title.

## Interview Preparation
- Explain the Split-Apply-Combine strategy.
- What is returned when you call `df.groupby('col')` without an aggregation function?

## Completion Checklist
- [ ] I understand Split-Apply-Combine.
- [ ] I can group data by single and multiple columns.
- [ ] I can access specific groups using `.get_group()`.
- [ ] I can connect grouping to SQL `GROUP BY` and cohort analysis.

## Difficulty
Intermediate
