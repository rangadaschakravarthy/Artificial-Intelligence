# Day 102 — Linear Algebra with NumPy

## Learning Objectives
- Master `np.linalg` module functions for matrix operations.
- Compute dot products (`np.dot`, `@`), matrix inverses (`np.inv`), determinants (`np.det`), and norms (`np.norm`).
- Solve linear systems $A x = b$ and compute Eigenvalues/Eigenvectors.

## Prerequisites
- Level 1: Linear Algebra (Matrices, Determinants, Eigenvalues)
- Day 87: NumPy Arrays

## Topics Covered
1. Vector and Matrix Multiplication (`np.dot`, `np.matmul`, `@`)
2. Matrix Transpose, Trace, and Determinant (`np.trace`, `np.linalg.det`)
3. Matrix Inverse (`np.linalg.inv`, `np.linalg.pinv` pseudo-inverse)
4. Vector and Matrix Norms (`np.linalg.norm` L1, L2, Frobenius)
5. Eigenvalues and Eigenvectors (`np.linalg.eig`) & Linear Systems (`np.linalg.solve`)

## Why This Matters
Linear algebra operations form the computational engine for PCA dimensionality reduction, Linear Regression parameter estimation, and Singular Value Decomposition (SVD).

## Real-World Usage
Solving Ordinary Least Squares linear regression closed-form formula $w = (X^T X)^{-1} X^T y$.

## Study Order
1. Read `theory.md`.
2. Review `examples.md`.
3. Complete `practice.md`.
4. Verify using `solution.md`.
5. Run `code.py`.

## Completion Checklist
- [ ] I can compute dot products and matrix multiplications.
- [ ] I can solve linear systems $A x = b$ using `np.linalg.solve()`.
- [ ] I can compute matrix determinants, inverses, and eigenvalues.
- [ ] I can connect `np.linalg` operations to Level 1 Linear Algebra.

## Difficulty
Intermediate
