# Day 102 Practice Questions: Linear Algebra with NumPy

## Level 1 — Basic
1. What function computes the determinant of a matrix?
2. What function solves a linear system of equations $A x = b$?
3. How do you compute the L2 norm (Euclidean length) of a vector using `np.linalg.norm()`?
4. True or False: `np.linalg.inv(A)` works for non-square matrices.
5. What function computes eigenvalues and eigenvectors of a square matrix?

## Level 2 — Coding
6. Compute matrix transpose $A^T$ and trace $	ext{Tr}(A)$ for $A = egin{bmatrix} 1 & 2 \ 3 & 4 \end{bmatrix}$.
7. Solve system $2x + 3y = 8$ and $4x + 1y = 6$ using `np.linalg.solve()`.
8. Compute pseudo-inverse of non-square matrix of shape `(4, 2)` using `np.linalg.pinv()`.
9. Calculate L1 norm and L2 norm of vector `v = np.array([1, -2, 3, -4])`.
10. Verify that $A \cdot A^{-1} = I$ for matrix $A = egin{bmatrix} 5 & 2 \ 2 & 1 \end{bmatrix}$.

## Level 3 — Data Analysis
11. Why does `np.linalg.inv(A)` raise `LinAlgError` when $\det(A) = 0$?
12. Compare memory and execution time of `np.linalg.solve(A, b)` vs `np.linalg.inv(A) @ b`.
13. Predict output: `np.linalg.norm(np.array([3, 4]), ord=2)`.
14. Predict output shape of `eigenvectors` from `np.linalg.eig(M)` where `M` has shape `(5, 5)`.
15. Predict output: `A = np.eye(3); print(np.linalg.det(A))`.

## Level 4 — Debugging
16. Fix error: `numpy.linalg.LinAlgError: Last 2 dimensions of the array must be square`.
17. Fix shape mismatch bug when executing Normal Equation `X.T @ X @ X.T @ y`.
18. Fix numerical stability error when inverting near-singular matrix by switching to `np.linalg.pinv()`.

## Level 5 — AI/ML Application
19. Implement closed-form Linear Regression weight equation $w = (X^T X)^{-1} X^T y$.
20. Implement Principal Component Analysis (PCA) eigenvector extraction on covariance matrix $C = \frac{1}{N-1} X^T X$.
21. Connect vector norms (L1 and L2) to Lasso and Ridge regularization penalties in Machine Learning.

## Level 6 — Interview Questions
22. Explain LU Decomposition used internally by `np.linalg.solve()`.
23. What is the Moore-Penrose Pseudo-Inverse (`pinv`) and how is it derived using Singular Value Decomposition (SVD)?
24. Explain why the condition number `np.linalg.cond(A)` predicts numerical instability in matrix inversion.
25. Demonstrate Singular Value Decomposition `U, S, Vt = np.linalg.svd(A)`.
26. How do BLAS (Basic Linear Algebra Subprograms) Level 3 routines accelerate matrix multiplication on CPUs?
