# Day 3 — Vector Operations
import numpy as np

u = np.array([2.0, 5.0])
v = np.array([3.0, -1.0])

# 1. Vector Addition & Subtraction
add_uv = u + v
sub_uv = u - v

print(f"u + v = {add_uv}")
print(f"u - v = {sub_uv}")

# 2. Scalar Multiplication
scalar = 4.0
scaled_u = scalar * u
print(f"4 * u = {scaled_u}")

# 3. Element-wise (Hadamard) Product
hadamard_uv = u * v  # Note: * in NumPy is element-wise!
print(f"Hadamard product (u * v) = {hadamard_uv}")

# 4. Linear Combination: 2*u - 3*v
lin_comb = 2.0 * u - 3.0 * v
print(f"2*u - 3*v = {lin_comb}")
