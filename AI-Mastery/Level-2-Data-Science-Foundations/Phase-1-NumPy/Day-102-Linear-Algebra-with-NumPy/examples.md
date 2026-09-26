# Day 102 Worked Examples: Linear Algebra with NumPy

## Example 1 — Beginner: Matrix Product, Determinant, and Inverse
```python
import numpy as np

A = np.array([[4, 7],
              [2, 6]])

det_A = np.linalg.det(A)
inv_A = np.linalg.inv(A)

print("Matrix A:
", A)
print(f"Determinant: {det_A:.2f}") # (4*6 - 7*2) = 10
print("Inverse A^-1:
", np.round(inv_A, 2))
print("Verification A @ A^-1 = I:
", np.round(A @ inv_A, 2))
```

## Example 2 — Practical: Solving Linear System Ax = b
```python
import numpy as np

# System of equations:
# 3x + 1y = 9
# 1x + 2y = 8
A = np.array([[3.0, 1.0],
              [1.0, 2.0]])
b = np.array([9.0, 8.0])

x = np.linalg.solve(A, b)

print("Solution vector [x, y]:", x) # [2.0, 3.0]
print("Verification A @ x = b:", A @ x)
```

## Example 3 — Intermediate: Eigenvalues and Eigenvectors
```python
import numpy as np

# Symmetric Matrix
A = np.array([[2.0, 1.0],
              [1.0, 2.0]])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues) # [3., 1.]
print("Eigenvectors (columns):
", eigenvectors)

# Verification: A v = λ v
v0 = eigenvectors[:, 0]
lambda0 = eigenvalues[0]
print("A @ v0:    ", A @ v0)
print("lambda0 * v0:", lambda0 * v0)
```

## Example 4 — Real Dataset: Computing Vector & Matrix Norms
```python
import numpy as np

v = np.array([3.0, 4.0]) # 2D Vector
M = np.array([[1, 2], [3, 4]])

# L1 Norm (Manhattan): sum(|x_i|)
l1_norm = np.linalg.norm(v, ord=1)

# L2 Norm (Euclidean): sqrt(sum(x_i^2))
l2_norm = np.linalg.norm(v, ord=2)

# Frobenius Norm of Matrix: sqrt(sum(M_ij^2))
fro_norm = np.linalg.norm(M, ord='fro')

print("L1 Norm of v:", l1_norm)  # 7.0
print("L2 Norm of v:", l2_norm)  # 5.0
print("Frobenius Norm of M:", np.round(fro_norm, 2)) # sqrt(1+4+9+16) = 5.48
```

## Example 5 — AI/ML Application: Closed-Form OLS Linear Regression
```python
import numpy as np

# Synthetic Dataset: 4 samples, 2 features (plus bias column of 1s)
# Target equation: y = 2*x1 + 3*x2 + 5
X = np.array([
    [1.0, 1.0, 1.0],
    [1.0, 2.0, 1.0],
    [1.0, 1.0, 2.0],
    [1.0, 3.0, 3.0]
])
y = np.array([10.0, 12.0, 13.0, 20.0])

# Normal Equation: w = (X^T X)^-1 X^T y
w = np.linalg.inv(X.T @ X) @ X.T @ y

print("OLS Estimated Weights [bias, w1, w2]:", np.round(w, 2))
```
