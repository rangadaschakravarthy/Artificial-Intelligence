# Day 20 — Projections
import numpy as np

# 1. Projection of vector v onto line u
u = np.array([1.0, 0.0])  # x-axis
v = np.array([3.0, 4.0])

proj_v_on_u = (np.dot(u, v) / np.dot(u, u)) * u
residual_e = v - proj_v_on_u

print(f"Vector v: {v}")
print(f"Projection of v onto x-axis: {proj_v_on_u}")
print(f"Residual Error e: {residual_e}")
print(f"Residual e perpendicular to u? Dot product = {np.dot(residual_e, u):.4f}")

# 2. Projection Matrix P onto Column Space of A
A = np.array([
    [1.0, 0.0],
    [0.0, 1.0],
    [0.0, 0.0]
]) # xy-plane in 3D space

P = A @ np.linalg.inv(A.T @ A) @ A.T
print(f"\nProjection Matrix P (shape {P.shape}):\n{P}")

# Test Projection on 3D Point b = [5, 7, 9]
b = np.array([5.0, 7.0, 9.0])
b_hat = P @ b
print(f"\nOriginal 3D point b: {b}")
print(f"Projected point b_hat onto xy-plane: {b_hat}")

# 3. Check Properties: P^T = P and P^2 = P
print(f"Is P symmetric (P^T == P)? {np.allclose(P, P.T)}")
print(f"Is P idempotent (P^2 == P)? {np.allclose(P @ P, P)}")
