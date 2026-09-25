# Day 35 — Optimization
import numpy as np
import sympy as sp

# 1. Critical Point Finding & Hessian Classification with SymPy
x, y = sp.symbols('x y')
f = x**2 + 2*y**2 - 4*x + 8*y + 5

# Gradient Vector
grad_x = sp.diff(f, x)
grad_y = sp.diff(f, y)

print("--- SymPy Optimization ---")
print(f"Function: f(x, y) = x^2 + 2*y^2 - 4*x + 8*y + 5")
print(f"Gradient: [{grad_x}, {grad_y}]^T")

# Solve for Critical Point grad f = [0, 0]
crit_points = sp.solve([grad_x, grad_y], (x, y))
print(f"Critical Point: {crit_points}")

# Hessian Matrix
H_symbolic = sp.Matrix([
    [sp.diff(grad_x, x), sp.diff(grad_x, y)],
    [sp.diff(grad_y, x), sp.diff(grad_y, y)]
])
print(f"\nHessian Matrix H:\n{H_symbolic}")

# Hessian Eigenvalues for Classification
H_eval = np.array(H_symbolic, dtype=np.float64)
evals = np.linalg.eigvals(H_eval)
print(f"Hessian Eigenvalues: {evals}")

if np.all(evals > 0):
    print("Classification: STRICT LOCAL MINIMUM (Positive Definite H > 0)")
elif np.all(evals < 0):
    print("Classification: STRICT LOCAL MAXIMUM (Negative Definite H < 0)")
else:
    print("Classification: SADDLE POINT (Mixed Eigenvalue Signs)")
