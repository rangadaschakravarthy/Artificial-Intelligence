# Day 14 — Rank
import numpy as np

# 1. Full Rank Matrix (2x2)
A_full = np.array([
    [1.0, 2.0],
    [3.0, 4.0]
])
rank_full = np.linalg.matrix_rank(A_full)
print(f"Matrix A:\n{A_full}")
print(f"Rank of A: {rank_full} (Full Rank!)")

# 2. Rank Deficient Matrix (Row 2 = 2 * Row 1)
A_def = np.array([
    [1.0, 2.0],
    [2.0, 4.0]
])
rank_def = np.linalg.matrix_rank(A_def)
print(f"\nRank Deficient Matrix:\n{A_def}")
print(f"Rank: {rank_def} (Rank Deficient!)")

# 3. Low-Rank Matrix Factorization (LoRA concept)
# Original 1000x1000 matrix factorized into (1000x4) @ (4x1000)
U = np.random.randn(1000, 4)
V = np.random.randn(4, 1000)
W_low_rank = U @ V

rank_W = np.linalg.matrix_rank(W_low_rank)
print(f"\nLow-Rank Factorized Matrix Shape: {W_low_rank.shape}")
print(f"Rank of W_low_rank: {rank_W} (Compressed to Rank 4!)")
