# Day 13 — Determinants
import numpy as np

# 1. 2x2 Determinant
A = np.array([
    [4.0, 2.0],
    [1.0, 5.0]
])

det_A_manual = A[0,0]*A[1,1] - A[0,1]*A[1,0]
det_A_numpy = np.linalg.det(A)

print(f"Manual 2x2 Determinant: {det_A_manual:.2f}")
print(f"NumPy Determinant: {det_A_numpy:.2f}")

# 2. Singular Matrix (Det = 0)
B = np.array([
    [2.0, 4.0],
    [1.0, 2.0]
])
det_B = np.linalg.det(B)
print(f"Singular Matrix Determinant: {det_B:.4f} (Area Collapsed to 0!)")

# 3. Product Property: det(A @ C) = det(A) * det(C)
C = np.array([[1, 3], [2, 4]])
det_AC = np.linalg.det(A @ C)
det_A_times_det_C = np.linalg.det(A) * np.linalg.det(C)

print(f"\ndet(A @ C): {det_AC:.2f}")
print(f"det(A) * det(C): {det_A_times_det_C:.2f}")
assert np.isclose(det_AC, det_A_times_det_C)
