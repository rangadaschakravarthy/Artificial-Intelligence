# Day 12 — Matrix Inverse
import numpy as np

# 1. Manual 2x2 Matrix Inversion
def manual_inverse_2x2(M):
    assert M.shape == (2, 2), "Must be 2x2 matrix"
    a, b = M[0, 0], M[0, 1]
    c, d = M[1, 0], M[1, 1]
    det = a * d - b * c
    assert det != 0, "Matrix is singular (non-invertible)!"
    return (1.0 / det) * np.array([[d, -b], [-c, a]])

A = np.array([[4.0, 7.0], [2.0, 6.0]])
A_inv_manual = manual_inverse_2x2(A)
print(f"Manual 2x2 Inverse:\n{A_inv_manual}")

# 2. NumPy np.linalg.inv
A_inv_numpy = np.linalg.inv(A)
print(f"\nNumPy np.linalg.inv:\n{A_inv_numpy}")

# Verify A @ A_inv = Identity
I_check = A @ A_inv_numpy
print(f"\nA @ A_inv (Identity Check):\n{np.round(I_check, 4)}")

# 3. Solving Linear System A * x = b
# 2x + 1y = 5
# 1x + 1y = 3
A_sys = np.array([[2.0, 1.0], [1.0, 1.0]])
b_sys = np.array([5.0, 3.0])

# Preferred numerical solver: np.linalg.solve
x_sol = np.linalg.solve(A_sys, b_sys)
print(f"\nLinear System Solution (x, y): {x_sol}")
