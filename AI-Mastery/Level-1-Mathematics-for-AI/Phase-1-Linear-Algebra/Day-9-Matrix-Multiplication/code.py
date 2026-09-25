# Day 9 — Matrix Multiplication
import numpy as np

# 1. Dimensions Check: (2x3) * (3x2) -> (2x2)
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
]) # Shape (2, 3)

B = np.array([
    [7, 8],
    [9, 1],
    [2, 3]
]) # Shape (3, 2)

# Manual implementation (Triple Loop)
def manual_matmul(M1, M2):
    m, k1 = M1.shape
    k2, n = M2.shape
    assert k1 == k2, "Inner dimensions must match!"
    C = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            for p in range(k1):
                C[i, j] += M1[i, p] * M2[p, j]
    return C

C_manual = manual_matmul(A, B)
print(f"Manual MatMul Output:\n{C_manual}")

# 2. NumPy matmul / @ Operator
C_numpy = A @ B
print(f"\nNumPy @ Operator Output:\n{C_numpy}")

# Verify equivalence
assert np.allclose(C_manual, C_numpy)

# 3. Neural Network Layer Forward Pass: Y = X * W + b
X = np.array([[1.0, 2.0], [3.0, 4.0]])   # Batch of 2 samples, 2 features
W = np.array([[0.5, -0.5], [1.0, 1.5]])  # Weights 2x2
b = np.array([0.1, 0.2])                  # Bias

Y = X @ W + b
print(f"\nNeural Network Layer Output Y:\n{Y}")
