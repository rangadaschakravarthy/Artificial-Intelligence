# Day 102 Theory: Linear Algebra with NumPy

### 1. What Is It?
`np.linalg` is NumPy's sub-module for executing linear algebra computations (matrix multiplication, inversion, decomposition, system solving) backed by optimized LAPACK / BLAS C-libraries.

### 2. Why Does It Exist?
Hand-writing C loops for matrix inversion ($O(N^3)$) or eigenvalue decomposition is mathematically complex and numerically unstable. LAPACK routines provide production-grade numerical precision.

### 3. Intuition
`np.linalg` is a high-performance linear algebra super-calculator that solves systems of 1,000 simultaneous equations in milliseconds.

### 4. Syntax
```python
import numpy as np

A = np.array([[1, 2], [3, 4]])
b = np.array([5, 11])

# Matrix Product
C = A @ A

# Inverse & Determinant
A_inv = np.linalg.inv(A)
det_A = np.linalg.det(A)

# Solve Ax = b
x = np.linalg.solve(A, b)

# Eigenvalues & Eigenvectors
eigenvals, eigenvecs = np.linalg.eig(A)
```

### 5. Parameters
- `ord`: Order of the norm in `np.linalg.norm` (`1` for L1, `2` for L2, `'fro'` for Frobenius).

### 6. How It Works
NumPy delegates `linalg` functions to OpenBLAS, MKL, or LAPACK C/Fortran libraries compiled with CPU AVX vector instructions.

### 7. Simple Example
```python
import numpy as np
A = np.array([[2, 1], [1, 3]])
print("Determinant:", np.linalg.det(A)) # 2*3 - 1*1 = 5.0
```

### 8. Intermediate Example
```python
import numpy as np
# Solve 2x + y = 5, x + 3y = 10
A = np.array([[2, 1], [1, 3]])
b = np.array([5, 10])
x = np.linalg.solve(A, b)
print("Solution [x, y]:", x) # [1., 3.]
```

### 9. Output Interpretation
`np.linalg.solve(A, b)` computes exact solution vector $x = [1.0, 3.0]$ satisfying both equations simultaneously.

### 10. Common Mistakes
- Using `np.linalg.inv(A) @ b` to solve $A x = b$ instead of `np.linalg.solve(A, b)` (computing explicit inverse is slower and numerically unstable!).
- Attempting to invert a singular matrix ($\det(A) = 0$), raising a `LinAlgError: Singular matrix`.

### 11. Data Science Connection
Computing covariance matrix inverses and Mahalanobis distances during multivariate outlier detection.

### 12. AI/ML Connection
Principal Component Analysis (PCA) computes eigenvectors of covariance matrix $X^T X$. Ordinary Least Squares solves $w = (X^T X)^{-1} X^T y$.

### 13. Interview Insight
Question: "Why should you use `np.linalg.solve(A, b)` instead of `np.linalg.inv(A) @ b`?"
Answer: `np.linalg.solve` uses LU decomposition which is $3	imes$ faster and far more numerically stable. Explicitly computing $A^{-1}$ introduces floating-point rounding errors and fails if $A$ is nearly singular.

### 14. Summary
`np.linalg` handles linear algebra operations. Use `@` for matrix products, `solve()` for systems $Ax=b$, and `eig()` for eigenvalues.
