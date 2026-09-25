# Day 21 — Singular Value Decomposition
import numpy as np

# Create Rectangular 3x2 Matrix
A = np.array([
    [3.0, 1.0],
    [1.0, 3.0],
    [0.0, 0.0]
])

print(f"Original Matrix A (shape {A.shape}):\n{A}")

# 1. Compute SVD using np.linalg.svd
U, S_vec, Vt = np.linalg.svd(A, full_matrices=True)

print(f"\nU matrix shape: {U.shape}")
print(f"Singular values vector S: {S_vec}")
print(f"Vt matrix shape: {Vt.shape}")

# Reconstruct full Sigma matrix
Sigma = np.zeros(A.shape)
Sigma[:len(S_vec), :len(S_vec)] = np.diag(S_vec)

# 2. Reconstruct Original Matrix A = U @ Sigma @ Vt
A_reconstructed = U @ Sigma @ Vt
print(f"\nReconstructed Matrix A:\n{np.round(A_reconstructed, 4)}")
assert np.allclose(A, A_reconstructed)

# 3. Truncated SVD (Rank-1 Approximation)
Sigma_rank1 = np.zeros(A.shape)
Sigma_rank1[0, 0] = S_vec[0]
A_rank1 = U @ Sigma_rank1 @ Vt
print(f"\nBest Rank-1 Low-Rank Approximation:\n{np.round(A_rank1, 4)}")
