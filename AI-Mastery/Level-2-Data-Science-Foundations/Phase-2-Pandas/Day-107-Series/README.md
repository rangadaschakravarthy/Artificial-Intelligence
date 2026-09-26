# Day 107 — Series

## Learning Objectives
- Master the Pandas `Series` 1D data structure.
- Understand explicit Index labels vs default positional integer indices.
- Perform Series indexing, slicing, alignment, and vector operations.

## Prerequisites
- Day 106: Pandas Introduction

## Topics Covered
1. What is a Pandas `Series` (1D Labeled Array)
2. Creating Series from Lists, Dictionaries, and NumPy Arrays
3. Series attributes (`.values`, `.index`, `.dtype`, `.name`, `.shape`)
4. Index-based alignment during Series operations
5. Essential Series methods (`head()`, `tail()`, `value_counts()`, `unique()`, `describe()`)

## Why This Matters
Individual columns in a Pandas DataFrame are Series objects. Mastering Series operations is essential for feature manipulation.

## Real-World Usage
Calculating value distributions of categorical columns (e.g. `df['Category'].value_counts()`).

## Study Order
1. Read `theory.md`.
2. Review `examples.md`.
3. Complete `practice.md`.
4. Verify using `solution.md`.
5. Run `code.py`.

## Completion Checklist
- [ ] I can create Series with default and custom index labels.
- [ ] I understand how Series automatically align data by index label during operations.
- [ ] I can use `value_counts()` and `unique()` to explore categorical features.
- [ ] I can extract the underlying NumPy array from a Series using `.to_numpy()`.

## Difficulty
Beginner
