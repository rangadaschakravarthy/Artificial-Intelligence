# Day 34 — Jacobians
import numpy as np
import sympy as sp

# 1. Symbolic Jacobian with SymPy
x, y = sp.symbols('x y')
f1 = x**2 * y
f2 = x + 3*y

f_vec = sp.Matrix([f1, f2])
x_vec = sp.Matrix([x, y])

J_symbolic = f_vec.jacobian(x_vec)
print("--- SymPy Symbolic Jacobian Matrix ---")
print(f"Vector Function f(x, y) = [x^2*y, x + 3*y]^T")
print(f"Jacobian Matrix J:\n{J_symbolic}")

# Evaluate Jacobian at (2, 1)
J_eval = J_symbolic.subs({x: 2, y: 1})
print(f"\nJacobian at (2, 1):\n{J_eval}")
print(f"Jacobian Determinant at (2, 1): {J_eval.det()}")

# 2. Numerical Jacobian Function (2D Input -> 2D Output)
def vector_func(vec):
    x_in, y_in = vec[0], vec[1]
    return np.array([x_in**2 * y_in, x_in + 3.0 * y_in])

def num_jacobian(func, vec, h=1e-5):
    n = len(vec)
    f0 = func(vec)
    m = len(f0)
    J = np.zeros((m, n))
    for j in range(n):
        vec_plus = vec.copy()
        vec_minus = vec.copy()
        vec_plus[j] += h
        vec_minus[j] -= h
        J[:, j] = (func(vec_plus) - func(vec_minus)) / (2 * h)
    return J

pt = np.array([2.0, 1.0])
J_num = num_jacobian(vector_func, pt)
print(f"\nNumerical Jacobian at (2, 1):\n{J_num}")
