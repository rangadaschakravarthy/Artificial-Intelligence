# Day 19 — Eigenvalues and Eigenvectors
import numpy as np

# Symmetric Matrix A
A = np.array([
    [4.0, 1.0],
    [1.0, 3.0]
])

# 1. Compute Eigenvalues & Eigenvectors
# np.linalg.eigh is optimized for real symmetric matrices!
eigenvalues, eigenvectors = np.linalg.eigh(A)

print(f"Matrix A:\n{A}")
print(f"\nEigenvalues: {eigenvalues}")
print(f"Eigenvectors (columns):\n{eigenvectors}")

# 2. Verify A * v = lambda * v for 1st eigenvector
v1 = eigenvectors[:, 0]
lambda1 = eigenvalues[0]

Av1 = A @ v1
lambda1_v1 = lambda1 * v1

print(f"\nA @ v1: {Av1}")
print(f"lambda1 * v1: {lambda1_v1}")
assert np.allclose(Av1, lambda1_v1)
print("Eigenvalue Equation A * v = lambda * v Verified!")

# 3. Verify Trace and Determinant properties
print(f"\nTrace Check: Sum of Eigenvalues = {np.sum(eigenvalues):.2f}, Trace(A) = {np.trace(A):.2f}")
print(f"Det Check: Product of Eigenvalues = {np.prod(eigenvalues):.2f}, Det(A) = {np.linalg.det(A):.2f}")
