# Day 4 — Dot Product
import numpy as np

# Define vectors
u = np.array([2.0, 3.0])
v = np.array([4.0, -1.0])

# 1. Manual Dot Product
def manual_dot_product(vec1, vec2):
    assert len(vec1) == len(vec2), "Dimensions must match!"
    dot_sum = 0.0
    for i in range(len(vec1)):
        dot_sum += vec1[i] * vec2[i]
    return dot_sum

manual_res = manual_dot_product(u, v)
print(f"Manual Dot Product: {manual_res}")

# 2. NumPy np.dot and @ Operator
numpy_res1 = np.dot(u, v)
numpy_res2 = u @ v  # Modern Python matrix/vector multiplication operator

print(f"NumPy np.dot: {numpy_res1}")
print(f"NumPy @ operator: {numpy_res2}")

# 3. Neural Network Layer Neuron Calculation: z = w^T * x + b
x = np.array([0.8, 0.2, 0.5])
w = np.array([2.0, -1.0, 3.0])
b = 0.5

z = np.dot(w, x) + b
print(f"Neuron Activation Pre-state z: {z:.2f}")
