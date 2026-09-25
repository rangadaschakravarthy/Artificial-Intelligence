# Day 31 — Partial Derivatives
import numpy as np
import sympy as sp

# 1. Symbolic Partial Derivatives with SymPy
x, y = sp.symbols('x y')
f_symbolic = 3*x**2 * y + 5*y**3 - 4*x

df_dx = sp.diff(f_symbolic, x)
df_dy = sp.diff(f_symbolic, y)

print("--- SymPy Partial Derivatives ---")
print(f"f(x, y) = 3*x^2*y + 5*y^3 - 4*x")
print(f"df/dx = {df_dx}")
print(f"df/dy = {df_dy}")

# Verify Clairaut's Theorem (f_xy == f_yx)
f_xy = sp.diff(df_dx, y)
f_yx = sp.diff(df_dy, x)
print(f"f_xy = {f_xy}, f_yx = {f_yx} (Equal: {f_xy == f_yx})")

# 2. Numerical Partial Derivative Function
def f_num(x, y):
    return 3.0*x**2 * y + 5.0*y**3 - 4.0*x

def num_partial_x(f, x, y, h=1e-5):
    return (f(x + h, y) - f(x - h, y)) / (2 * h)

def num_partial_y(f, x, y, h=1e-5):
    return (f(x, y + h) - f(x, y - h)) / (2 * h)

x0, y0 = 2.0, 3.0
print(f"\nNumerical Partial df/dx at (2, 3): {num_partial_x(f_num, x0, y0):.4f}")
print(f"Numerical Partial df/dy at (2, 3): {num_partial_y(f_num, x0, y0):.4f}")
