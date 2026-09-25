# Day 10 — Transpose
import numpy as np

# 1. Basic Transpose
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
]) # Shape (2, 3)

A_T = A.T  # Or np.transpose(A)
print(f"Original Matrix A (shape {A.shape}):\n{A}")
print(f"Transposed Matrix A^T (shape {A_T.shape}):\n{A_T}")

# 2. Product Transpose Rule Verification: (A * B)^T = B^T * A^T
B = np.array([
    [7, 8],
    [9, 1],
    [2, 3]
]) # Shape (3, 2)

AB_T = (A @ B).T
BT_AT = B.T @ A.T

print(f"\n(A @ B)^T:\n{AB_T}")
print(f"B^T @ A^T:\n{BT_AT}")
assert np.allclose(AB_T, BT_AT)
print("Product Transpose Rule Verified!")

# 3. Gram Matrix: A^T * A is always symmetric!
Gram = A.T @ A
print(f"\nGram Matrix A^T @ A:\n{Gram}")
print(f"Is Gram matrix symmetric? {np.allclose(Gram, Gram.T)}")
