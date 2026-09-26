# Day 88 — Array Dimensions

## Learning Objectives
- Master working with array axes, dimensions (`ndim`), and rank.
- Learn how dimensions map to real-world data structures (scalars, vectors, matrices, tensors).
- Understand axis-based operations (`axis=0`, `axis=1`, `axis=2`).

## Prerequisites
- Day 87: NumPy Arrays

## Topics Covered
1. Rank and Dimension Definition (`ndim`)
2. Axis 0, Axis 1, Axis 2 geometry and directional movement
3. Expanding dimensions (`np.newaxis`, `np.expand_dims`)
4. Squeezing single-dimensional entries (`np.squeeze`)
5. High-dimensional data representation in Deep Learning

## Why This Matters
Mismatched dimensions are the #1 cause of bugs when building machine learning pipelines and neural network layers.

## Real-World Usage
Converting 1D feature vectors `(N,)` to 2D column matrices `(N, 1)` for matrix multiplication in Linear Regression.

## Study Order
1. Read `theory.md`.
2. Review `examples.md`.
3. Complete `practice.md`.
4. Verify using `solution.md`.
5. Run `code.py`.

## Completion Checklist
- [ ] I can state the difference between shape and dimension.
- [ ] I know which direction `axis=0` and `axis=1` operate on in 2D matrices.
- [ ] I can add dimensions using `np.newaxis` and `np.expand_dims`.
- [ ] I can remove dummy dimensions using `np.squeeze`.

## Difficulty
Beginner
