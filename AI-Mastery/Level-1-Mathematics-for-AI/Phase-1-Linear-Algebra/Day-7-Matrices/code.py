# Day 7 — Matrices
import numpy as np

# Create a 2x3 Matrix
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(f"Matrix A:\n{A}")
print(f"Shape: {A.shape}, Rows: {A.shape[0]}, Cols: {A.shape[1]}")

# Indexing (0-indexed in Python)
print(f"Element A[0, 2] (1st row, 3rd col): {A[0, 2]}")
print(f"2nd Row: {A[1, :]}")
print(f"1st Column: {A[:, 0]}")

# Special Matrices
diag_matrix = np.diag([10, 20, 30])
identity_matrix = np.eye(3)
zeros_matrix = np.zeros((2, 4))

print(f"\nDiagonal Matrix:\n{diag_matrix}")
print(f"Identity Matrix (3x3):\n{identity_matrix}")
