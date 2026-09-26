# Day 126 — Pivot Tables

## Learning Objectives
- Reshape long DataFrames into wide summary matrices using `df.pivot_table()`.
- Compare `.pivot()` vs `.pivot_table()`.
- Unpivot wide DataFrames into long format using `pd.melt()`.

## Prerequisites
- Day 120: GroupBy
- Day 121: Aggregation

## Topics Covered
- `df.pivot()` vs `df.pivot_table()`
- `index`, `columns`, `values`, and `aggfunc` parameters
- Adding row and column margins (`margins=True`)
- Reshaping wide to long with `pd.melt()`
- Handling missing cells in pivot tables

## Why This Matters
Pivot tables transform dense multi-dimensional transaction logs into executive summary heatmaps and cross-tabulations.

## Real-World Usage
Creating monthly sales reports showing Product Category along rows and Sales Region across columns with total margins.

## Study Order
1. Read `theory.md` for pivoting and melting concepts.
2. Study `examples.md` for syntax patterns.
3. Run `code.py` to view table transformations.
4. Complete `practice.md` and check `solution.md`.

## Practical Work
- Construct a pivot table of customer churn rates grouped by plan type and region.
- Melt a wide financial dataset into tidy format.

## Interview Preparation
- What is the difference between `df.pivot()` and `df.pivot_table()`?
- How does `pd.melt()` unpivot a DataFrame?

## Completion Checklist
- [ ] I can create pivot tables using `df.pivot_table()`.
- [ ] I can calculate row/column subtotals using `margins=True`.
- [ ] I can convert wide tables to tidy long format using `pd.melt()`.
- [ ] I understand how pivot tables relate to multi-index `groupby()`.

## Difficulty
Intermediate
