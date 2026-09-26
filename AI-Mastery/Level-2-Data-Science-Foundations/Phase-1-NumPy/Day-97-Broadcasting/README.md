# Day 97 — Broadcasting

## Learning Objectives
- Master NumPy's Broadcasting Rules for arithmetic between arrays of different shapes.
- Understand compatible vs incompatible shapes.
- Perform scalar broadcasting, row broadcasting, and column broadcasting efficiently.

## Prerequisites
- Day 88: Array Dimensions
- Day 96: Array Operations

## Topics Covered
1. What is Broadcasting and why it eliminates explicit looping
2. The Two Rules of NumPy Broadcasting
3. Scalar to Array Broadcasting
4. 1D Vector to 2D Matrix Broadcasting (Row vs Column)
5. Debugging `ValueError: operands could not be broadcast together`

## Why This Matters
Broadcasting enables memory-efficient tensor operations in neural networks, such as adding bias vectors to feature matrices without duplicating memory.

## Real-World Usage
Standardizing dataset features by subtracting feature mean vector $\mu$ `(D,)` from feature matrix $X$ `(N, D)`.

## Study Order
1. Read `theory.md`.
2. Review `examples.md`.
3. Complete `practice.md`.
4. Verify using `solution.md`.
5. Run `code.py`.

## Completion Checklist
- [ ] I can state the 2 formal rules of NumPy broadcasting.
- [ ] I can determine whether two array shapes are compatible.
- [ ] I can add a 1D vector to a 2D matrix across rows or columns.
- [ ] I can debug shape broadcasting errors cleanly.

## Difficulty
Intermediate
