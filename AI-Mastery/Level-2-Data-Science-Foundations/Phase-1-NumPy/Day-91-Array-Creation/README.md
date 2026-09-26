# Day 91 — Array Creation

## Learning Objectives
- Master all built-in NumPy array creation routines (`zeros`, `ones`, `full`, `eye`, `arange`, `linspace`).
- Learn numerical spacing routines (`arange` vs `linspace`).
- Create empty buffers (`empty`, `empty_like`, `zeros_like`, `ones_like`) for optimized memory allocation.

## Prerequisites
- Day 86: NumPy Introduction

## Topics Covered
1. Constant array constructors (`np.zeros`, `np.ones`, `np.full`)
2. Identity and Diagonal constructors (`np.eye`, `np.identity`, `np.diag`)
3. Sequence generation (`np.arange` vs `np.linspace`)
4. Like-constructors (`np.zeros_like`, `np.ones_like`, `np.full_like`)
5. Uninitialized memory buffer allocation (`np.empty`)

## Why This Matters
Creating pre-allocated array memory buffers avoids expensive dynamic array resizing inside loops.

## Real-World Usage
Initializing neural network bias vectors to zeros, weight matrices to small values, or creating evaluation grids for model visualization.

## Study Order
1. Read `theory.md`.
2. Review `examples.md`.
3. Complete `practice.md`.
4. Verify using `solution.md`.
5. Run `code.py`.

## Completion Checklist
- [ ] I can create arrays of zeros, ones, and custom constants.
- [ ] I know when to use `arange` vs `linspace`.
- [ ] I can create identity matrices for linear algebra.
- [ ] I understand why `np.empty()` is faster but contains uninitialized garbage values.

## Difficulty
Beginner
