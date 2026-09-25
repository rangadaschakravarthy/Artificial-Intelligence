# Day 15 — Linear Independence
import numpy as np

# 1. Test Linearly Independent Vectors
# v1 = [1, 0], v2 = [0, 1]
V_ind = np.array([
    [1.0, 0.0],
    [0.0, 1.0]
])

rank_ind = np.linalg.matrix_rank(V_ind)
det_ind = np.linalg.det(V_ind)

print("--- Independent Vector Set ---")
print(f"Rank: {rank_ind} (Equals num vectors 2 -> INDEPENDENT!)")
print(f"Determinant: {det_ind:.2f} (Non-zero!)")

# 2. Test Linearly Dependent Vectors
# u1 = [1, 2], u2 = [3, 6] (u2 = 3 * u1)
V_dep = np.array([
    [1.0, 3.0],
    [2.0, 6.0]
])

rank_dep = np.linalg.matrix_rank(V_dep)
det_dep = np.linalg.det(V_dep)

print("\n--- Dependent Vector Set ---")
print(f"Rank: {rank_dep} (Less than num vectors 2 -> DEPENDENT!)")
print(f"Determinant: {det_dep:.2f} (Zero!)")

# 3. Automated Linear Independence Checker Function
def check_independence(vector_list):
    matrix = np.column_stack(vector_list)
    r = np.linalg.matrix_rank(matrix)
    num_vecs = len(vector_list)
    is_ind = (r == num_vecs)
    return is_ind, r

v1 = np.array([1, 2, 0])
v2 = np.array([0, 1, 1])
v3 = np.array([1, 3, 1]) # v3 = v1 + v2

is_indep, r = check_independence([v1, v2, v3])
print(f"\nSet [v1, v2, v3] Independent? {is_indep} (Rank = {r})")
