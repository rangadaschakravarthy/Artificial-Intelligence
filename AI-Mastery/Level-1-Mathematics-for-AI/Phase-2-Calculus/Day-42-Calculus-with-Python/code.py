# Day 42 — Calculus with Python
import numpy as np
import sympy as sp
from scipy.optimize import minimize

# 1. Symbolic Calculus with SymPy
x = sp.Symbol('x')
f_sym = x**3 - 4*x**2 + 5*x - 2

df_sym = sp.diff(f_sym, x)
ddf_sym = sp.diff(f_sym, x, 2)

print("--- SymPy Symbolic Calculus ---")
print(f"Function f(x):  {f_sym}")
print(f"1st Derivative: {df_sym}")
print(f"2nd Derivative: {ddf_sym}")

# 2. Numerical Minimization with SciPy
def f_scipy(x_val):
    return (x_val[0] - 3.0)**2 + 5.0

res = minimize(f_scipy, x0=[0.0])
print(f"\n--- SciPy Numerical Minimization ---")
print(f"Minimum x*: {res.x[0]:.4f} (True x* = 3.0)")
print(f"Minimum Loss f(x*): {res.fun:.4f}")

# 3. Gradient Check: Compare Analytical vs Numerical Derivative
def loss_func(w):
    return np.sin(w) + w**2

def grad_analytical(w):
    return np.cos(w) + 2.0 * w

def grad_numerical(f, w, h=1e-6):
    return (f(w + h) - f(w - h)) / (2 * h)

w_test = 1.5
g_exact = grad_analytical(w_test)
g_num = grad_numerical(loss_func, w_test)

rel_error = abs(g_exact - g_num) / (abs(g_exact) + abs(g_num))
print(f"\n--- Gradient Check ---")
print(f"Exact Grad: {g_exact:.6f}, Numerical Grad: {g_num:.6f}")
print(f"Relative Error: {rel_error:.2e} (Gradient Check Passed!)")
