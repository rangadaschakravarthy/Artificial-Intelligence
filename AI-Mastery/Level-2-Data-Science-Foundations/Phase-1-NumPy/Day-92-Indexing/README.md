# Day 92 — Indexing

## Learning Objectives
- Master basic integer indexing for 1D, 2D, and high-dimensional arrays.
- Understand 0-based indexing and negative index referencing.
- Access specific rows, columns, sub-matrices, and tensor elements.

## Prerequisites
- Day 87: NumPy Arrays

## Topics Covered
1. 1D Array Indexing (`arr[i]`, negative indices `arr[-1]`)
2. 2D Matrix Indexing (`matrix[row, col]`)
3. 3D Tensor Indexing (`tensor[depth, row, col]`)
4. Indexing vs Slicing performance differences
5. Modifying array elements in-place via indexing

## Why This Matters
Accessing specific data samples, feature columns, and target labels is foundational to data manipulation in Pandas and NumPy.

## Real-World Usage
Extracting target prediction labels $y = X[:, -1]$ from a combined dataset matrix $X$.

## Study Order
1. Read `theory.md`.
2. Review `examples.md`.
3. Complete `practice.md`.
4. Verify using `solution.md`.
5. Run `code.py`.

## Completion Checklist
- [ ] I can index 1D, 2D, and 3D array elements.
- [ ] I understand comma-separated indexing `arr[r, c]` vs Python chaining `arr[r][c]`.
- [ ] I can use negative indices to reference elements from the end.
- [ ] I can update individual array elements using indexing.

## Difficulty
Beginner
