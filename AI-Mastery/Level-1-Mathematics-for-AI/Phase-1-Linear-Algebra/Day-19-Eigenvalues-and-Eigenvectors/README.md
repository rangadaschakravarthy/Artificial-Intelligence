# Day 19 — Eigenvalues and Eigenvectors

## Learning Objectives
- Master the Eigenvalue equation $\mathbf{A}\mathbf{v} = \lambda \mathbf{v}$
- Understand geometric intuition of eigenvectors as invariant directional axes
- Solve the characteristic equation $\det(\mathbf{A} - \lambda \mathbf{I}) = 0$ to find eigenvalues
- Calculate eigenvectors by solving $(\mathbf{A} - \lambda \mathbf{I})\mathbf{v} = \mathbf{0}$
- Connect eigenvectors to Principal Component Analysis (PCA) and Spectral Clustering

## Prerequisites
Day 9 — Matrix Multiplication, Day 13 — Determinants

## Topics Covered
- Eigenvalue Equation: $\mathbf{A}\mathbf{v} = \lambda \mathbf{v}$
- Geometric Intuition (Vectors whose direction does NOT change under linear transform)
- Characteristic Polynomial: $\det(\mathbf{A} - \lambda \mathbf{I}) = 0$
- Trace and Determinant properties: $\sum \lambda_i = \text{Tr}(\mathbf{A})$, $\prod \lambda_i = \det(\mathbf{A})$
- Eigendecomposition of Symmetric Matrices (Spectral Theorem $\mathbf{A} = \mathbf{Q} \mathbf{\Lambda} \mathbf{Q}^T$)

## Why This Matters for AI
Eigenvectors represent the principal axes of data variance (PCA), Google's PageRank algorithm, Spectral Graph Neural Networks, and structural stability of dynamical AI models.

## Study Order
1. Read theory.md
2. Study examples.md
3. Run code.py
4. Complete practice.md
5. Verify with solution.md

## Practical Work
Compute eigenvalues and eigenvectors in Python using `np.linalg.eig()` and `np.linalg.eigh()`.

## Interview Preparation
Explain $\mathbf{A}\mathbf{v} = \lambda \mathbf{v}$ geometrically, Spectral Theorem for symmetric matrices, and PCA connections.

## Completion Checklist
- [ ] I can state the eigenvalue equation $Av = \lambda v$
- [ ] I can solve $\det(A - \lambda I) = 0$ for 2x2 matrices
- [ ] I know that trace equals sum of eigenvalues and det equals product
- [ ] I can compute eigenvalues in Python

## Estimated Difficulty
Advanced
