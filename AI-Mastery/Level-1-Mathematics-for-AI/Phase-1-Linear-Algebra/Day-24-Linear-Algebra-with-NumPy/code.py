# Day 24 — Linear Algebra with NumPy
import numpy as np
import time

# 1. Performance Benchmark: Python Loop vs NumPy Vectorization
N = 1_000_000
py_list1 = list(range(N))
py_list2 = list(range(N))

np_arr1 = np.array(py_list1, dtype=np.float64)
np_arr2 = np.array(py_list2, dtype=np.float64)

# Pure Python Loop Benchmark
start_py = time.time()
py_result = [py_list1[i] + py_list2[i] for i in range(N)]
end_py = time.time()
py_time = end_py - start_py

# NumPy Vectorized Benchmark
start_np = time.time()
np_result = np_arr1 + np_arr2
end_np = time.time()
np_time = end_np - start_np

print(f"Pure Python Loop Time: {py_time:.4f} seconds")
print(f"NumPy Vectorized Time: {np_time:.4f} seconds")
print(f"Vectorization Speedup: {py_time / np_time:.2f}x Faster!")

# 2. Comprehensive np.linalg Suite Demo
A = np.array([[4.0, 2.0], [1.0, 3.0]])
b = np.array([8.0, 7.0])

print(f"\n--- NumPy np.linalg Suite ---")
print(f"Determinant: {np.linalg.det(A):.2f}")
print(f"Inverse:\n{np.linalg.inv(A)}")
print(f"Linear System Solution (Ax = b): {np.linalg.solve(A, b)}")

evals, evecs = np.linalg.eig(A)
print(f"Eigenvalues: {evals}")
