# Day 5 — Norms and Distances
import numpy as np

v = np.array([3.0, -4.0])

# 1. Manual Norms
l1_manual = np.sum(np.abs(v))
l2_manual = np.sqrt(np.sum(v**2))
linf_manual = np.max(np.abs(v))

print(f"Manual L1 Norm: {l1_manual}")
print(f"Manual L2 Norm: {l2_manual}")
print(f"Manual Inf Norm: {linf_manual}")

# 2. NumPy Norms via np.linalg.norm
l1_np = np.linalg.norm(v, ord=1)
l2_np = np.linalg.norm(v, ord=2)
linf_np = np.linalg.norm(v, ord=np.inf)

print(f"NumPy L1: {l1_np}, L2: {l2_np}, Inf: {linf_np}")

# 3. Vector Normalization (Unit Vector)
unit_v = v / l2_np
print(f"Unit vector v_hat: {unit_v}")
print(f"Length of unit vector: {np.linalg.norm(unit_v, 2):.4f}")

# 4. Distances
p1 = np.array([1.0, 2.0])
p2 = np.array([4.0, 6.0])

euclidean_dist = np.linalg.norm(p1 - p2, 2)
manhattan_dist = np.linalg.norm(p1 - p2, 1)

print(f"Euclidean distance: {euclidean_dist:.2f}")
print(f"Manhattan distance: {manhattan_dist:.2f}")
