# Day 125 — Concatenation

## Learning Objectives
- Stacking DataFrames vertically (row-wise) and horizontally (column-wise) using `pd.concat()`.
- Control index behavior using `ignore_index=True`.
- Handle overlapping and non-overlapping column structures during concatenation.

## Prerequisites
- Day 108: DataFrames
- Day 123: Merge

## Topics Covered
- `pd.concat()` function syntax
- Vertical concatenation (`axis=0`) vs Horizontal concatenation (`axis=1`)
- Index management with `ignore_index=True`
- Handling column mismatches (`join='outer'` vs `join='inner'`)
- Adding hierarchical keys with `keys=['batch1', 'batch2']`
- Performance best practices for appending data

## Why This Matters
Data is frequently delivered in batch files (e.g., monthly CSV logs). Data scientists must stack vertical batches or concatenate horizontal feature blocks cleanly.

## Real-World Usage
Combining 12 monthly sales log files into a single unified yearly master sales DataFrame.

## Study Order
1. Read `theory.md` for stacking mechanics.
2. Examine `examples.md` for axis variations.
3. Run `code.py` to observe concat outputs.
4. Complete `practice.md` and check `solution.md`.

## Practical Work
- Combine a list of 5 daily log DataFrames vertically with `ignore_index=True`.
- Stack feature blocks horizontally along `axis=1`.

## Interview Preparation
- Why is calling `df.append()` or `pd.concat()` inside a loop bad for performance?
- What is the difference between `join='inner'` and `join='outer'` in `pd.concat()`?

## Completion Checklist
- [ ] I can concatenate DataFrames vertically (`axis=0`).
- [ ] I can concatenate DataFrames horizontally (`axis=1`).
- [ ] I know how to reset row indices using `ignore_index=True`.
- [ ] I can build a list of DataFrames and concatenate once for speed.

## Difficulty
Intermediate
