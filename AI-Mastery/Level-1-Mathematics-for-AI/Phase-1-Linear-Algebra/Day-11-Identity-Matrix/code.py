# Day 11 — Identity Matrix
import numpy as np

# 1. Create Identity Matrices
I2 = np.eye(2)
I3 = np.eye(3)

print(f"2x2 Identity Matrix:\n{I2}")
print(f"\n3x3 Identity Matrix:\n{I3}")

# 2. Verify Multiplicative Identity: A * I = A
A = np.array([
    [5, -2],
    [3,  8]
])

A_I = A @ I2
I_A = I2 @ A

print(f"\nOriginal A:\n{A}")
print(f"A @ I:\n{A_I}")
print(f"I @ A:\n{I_A}")

assert np.array_equal(A, A_I) and np.array_equal(A, I_A)
print("Identity Multiplication Verified!")

# 3. Ridge Regularization Identity Addition: (X^T X + lambda * I)
X_TX = np.array([[4.0, 2.0], [2.0, 1.0]])  # Singular matrix!
lam = 0.5
regularized_matrix = X_TX + lam * I2

print(f"\nRegularized Matrix (X^T X + lambda * I):\n{regularized_matrix}")
