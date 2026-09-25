# Day 8 — Matrix Operations
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# 1. Addition and Subtraction
print(f"A + B:\n{A + B}")
print(f"A - B:\n{A - B}")

# 2. Scalar Multiplication
print(f"3 * A:\n{3 * A}")

# 3. Element-wise (Hadamard) Multiplication
print(f"Hadamard Product (A * B):\n{A * B}")

# 4. NumPy Broadcasting
# Add 1D bias vector to 2D matrix
bias = np.array([10, 20])  # Shape (2,)
broadcast_sum = A + bias   # Adds [10, 20] to each row of A

print(f"\nMatrix A (shape {A.shape}):\n{A}")
print(f"Bias vector (shape {bias.shape}): {bias}")
print(f"Broadcasted Sum:\n{broadcast_sum}")
