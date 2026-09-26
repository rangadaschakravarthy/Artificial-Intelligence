# Day 97 Worked Examples: Broadcasting

## Example 1 — Beginner: Scalar Broadcasting
```python
import numpy as np

matrix = np.array([[10, 20], [30, 40]])
scalar = 5

# Scalar 5 is broadcast across all elements of matrix
result = matrix + scalar
print("Matrix + Scalar 5:
", result)
```

## Example 2 — Practical: Row-wise vs Column-wise Broadcasting
```python
import numpy as np

M = np.zeros((3, 3)) # (3, 3)
v = np.array([1, 2, 3]) # (3,)

# Row-wise Broadcasting (adds v to each row)
row_broad = M + v
print("Row-wise Broadcasting:
", row_broad)

# Column-wise Broadcasting (adds v as column)
v_col = v[:, np.newaxis] # (3, 1)
col_broad = M + v_col
print("Column-wise Broadcasting:
", col_broad)
```

## Example 3 — Intermediate: Creating a Distance Grid via Outer Addition
```python
import numpy as np

x = np.array([0, 1, 2])     # Shape (3,)
y = np.array([10, 20, 30])  # Shape (3,)

# Expand dimensions to (3, 1) and (1, 3)
grid = x[:, np.newaxis] + y[np.newaxis, :]
print("Outer Grid Addition Shape:", grid.shape) # (3, 3)
print("Outer Grid Matrix:
", grid)
```

## Example 4 — Real Dataset: Feature Standardization (Z-score Normalization)
```python
import numpy as np

# Feature matrix X: 4 samples, 3 features
X = np.array([
    [150.0, 2.0, 30.0],
    [180.0, 3.0, 45.0],
    [120.0, 1.0, 25.0],
    [200.0, 4.0, 50.0]
])

mu = X.mean(axis=0) # Feature means: Shape (3,)
sigma = X.std(axis=0) # Feature stds: Shape (3,)

# Broadcasting (4, 3) - (3,) / (3,)
X_standardized = (X - mu) / sigma

print("Feature Means:", mu)
print("Standardized Feature Matrix (Mean=0, Std=1):
", np.round(X_standardized, 2))
```

## Example 5 — AI/ML Application: Neural Network Bias Addition
```python
import numpy as np

# Batch output activations from matrix multiplication XW: Shape (3, 4) -> 3 samples, 4 neurons
XW = np.array([
    [1.5, -0.2, 3.0, 0.5],
    [2.1,  0.8, 1.2, 0.1],
    [0.4, -1.5, 2.2, 1.8]
])

# Bias vector b for 4 neurons: Shape (4,)
b = np.array([0.1, 0.2, 0.3, 0.4])

# Broadcast bias vector across all batch sample rows
Z = XW + b
print("Z = XW + b Output Shape:", Z.shape) # (3, 4)
print("Activated Output Z:
", np.round(Z, 2))
```
