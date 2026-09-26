# Day 124 — Join

## Learning Objectives
- Combine DataFrames based on row index keys using `.join()`.
- Distinguish between index-based `.join()` and column-based `.merge()`.
- Perform multi-DataFrame index joins cleanly.

## Prerequisites
- Day 109: Index and Columns
- Day 123: Merge

## Topics Covered
- `df.join()` syntax and default parameters
- Index-to-index and index-to-column joining
- Joining on MultiIndex structures
- Joining multiple DataFrames simultaneously (`df1.join([df2, df3])`)
- Comparing `.join()` vs `.merge()` performance and syntax

## Why This Matters
When DataFrames already use meaningful row indices (such as timestamps, stock tickers, or entity IDs), `.join()` provides a cleaner, more concise API than `.merge()`.

## Real-World Usage
Combining financial time series tables indexed by Date (`DatetimeIndex`) across multiple asset symbols.

## Study Order
1. Read `theory.md` for index-join mechanics.
2. Review `examples.md` for syntax patterns.
3. Run `code.py` to compare join methods.
4. Complete `practice.md` and check `solution.md`.

## Practical Work
- Join two financial price DataFrames using `Date` index.
- Join a list of 3 separate DataFrames sharing identical row indices in one call.

## Interview Preparation
- What is the main default operational difference between `df.join()` and `pd.merge()`?
- How do you join on a column key using `.join()`?

## Completion Checklist
- [ ] I can use `df.join()` to combine DataFrames on row indices.
- [ ] I know how to join on index vs column using `on='col_name'`.
- [ ] I can join more than two DataFrames in a single call.
- [ ] I understand when to use `.join()` vs `.merge()`.

## Difficulty
Intermediate
