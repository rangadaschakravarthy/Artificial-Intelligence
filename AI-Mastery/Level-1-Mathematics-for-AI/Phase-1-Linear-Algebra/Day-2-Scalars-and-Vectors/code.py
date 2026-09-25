# Day 2 — Scalars and Vectors
import numpy as np

# Scalar
s = 42.5
print(f"Scalar: {s}, Type: {type(s)}")

# Vector (1D NumPy array)
v = np.array([3.0, 4.0, -1.5])
print(f"Vector v: {v}")
print(f"Vector shape: {v.shape}, Dimension: {v.ndim}, Size: {v.size}")

# Column Vector vs Row Vector
col_v = np.array([[3.0], [4.0], [-1.5]])
row_v = np.array([[3.0, 4.0, -1.5]])

print(f"Column vector shape: {col_v.shape}")
print(f"Row vector shape: {row_v.shape}")

# Scalar multiplication
scaled_v = 2.0 * v
print(f"Scaled vector (2 * v): {scaled_v}")
