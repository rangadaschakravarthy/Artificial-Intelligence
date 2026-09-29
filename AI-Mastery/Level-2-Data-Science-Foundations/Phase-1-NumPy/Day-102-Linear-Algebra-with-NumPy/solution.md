# Day 102 Solutions: Linear Algebra with NumPy

## Level 1 — Basic
1. `np.linalg.det()`
2. `np.linalg.solve(A, b)`
3. `np.linalg.norm(v, ord=2)` (or `np.linalg.norm(v)` as default).
4. False (Standard matrix inverse is strictly defined for square matrices; use `np.linalg.pinv()` for rectangular matrices).
5. `np.linalg.eig()` (or `np.linalg.eigh()` for symmetric matrices).

## Level 2 — Coding
6. 
```python
A = np.array([[1, 2], [3, 4]])
print("Transpose:
", A.T)
print("Trace:", np.trace(A)) # 1 + 4 = 5
```
7. 
```python
A = np.array([[2, 3], [4, 1]]); b = np.array([8, 6])
x = np.linalg.solve(A, b) # [1.0, 2.0]
```
8. `A_pinv = np.linalg.pinv(rect_matrix)`
9. `l1 = np.linalg.norm(v, 1)` ($1+2+3+4=10$); `l2 = np.linalg.norm(v, 2)` ($\sqrt{1+4+9+16} = \sqrt{30} pprox 5.477$).
10. `np.allclose(A @ np.linalg.inv(A), np.eye(2))` -> `True`.

## Level 3 — Data Analysis
11. A matrix with determinant 0 is singular (non-invertible); dividing by zero determinant raises `LinAlgError`.
12. `solve()` uses LU decomposition ($O(\frac{2}{3} N^3)$ time, stable). `inv() @ b` computes full inverse first ($O(2 N^3)$ time, introduces rounding error).
13. `5.0` ($\sqrt{3^2 + 4^2} = 5$).
14. `(5, 5)` (Eigenvectors stored as columns).
15. `1.0` (Determinant of Identity matrix is 1).

## Level 4 — Debugging
16. Inversion/Determinant operations require square 2D matrices. Ensure shape is `(N, N)`.
17. Correct Normal Equation parenthesis ordering: `w = np.linalg.inv(X.T @ X) @ (X.T @ y)`.
18. Replace `np.linalg.inv(A)` with robust SVD pseudo-inverse `np.linalg.pinv(A)`.

## Level 5 — AI/ML Application
19. `w = np.linalg.inv(X.T @ X) @ X.T @ y`
20. 
```python
cov = (X.T @ X) / (len(X) - 1)
evals, evecs = np.linalg.eig(cov)
```
21. L1 norm $\|w\|_1$ drives weight coefficients to zero (feature sparsity in Lasso). L2 norm $\|w\|_2^2$ shrinks weight magnitude smoothly (Ridge regularization).

## Level 6 — Interview Solutions
22. LU decomposition factors $A = L U$ into lower and upper triangular matrices, allowing $A x = b \implies L (U x) = b$ to be solved instantly via forward and back substitution.
23. $A^+ = V \Sigma^+ U^T$ where $A = U \Sigma V^T$ is SVD. Computes minimal norm least-squares solution for rectangular singular matrices.
24. Condition number $\kappa(A) = \frac{\sigma_{\max}}{\sigma_{\min}}$ measures sensitivity of $x$ to small perturbations in $b$. Large $\kappa(A)$ means matrix is ill-conditioned.
25. `U, S, Vt = np.linalg.svd(A)`
26. BLAS Level 3 matrix-matrix operations ($O(N^3)$ ops on $O(N^2)$ data) partition matrices into cache-sized sub-blocks, maximizing CPU SIMD register compute density.
