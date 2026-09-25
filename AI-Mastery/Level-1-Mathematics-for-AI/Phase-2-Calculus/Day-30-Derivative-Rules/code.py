# Day 30 — Derivative Rules
import numpy as np
import sympy as sp

# 1. Symbolic Differentiation using SymPy
x = sp.Symbol('x')

# Define Functions
f_sigmoid = 1 / (1 + sp.exp(-x))
f_product = x**2 * sp.exp(x)
f_quotient = sp.exp(x) / x

print("--- SymPy Symbolic Derivatives ---")
print(f"d/dx [ Sigmoid ]: {sp.simplify(sp.diff(f_sigmoid, x))}")
print(f"d/dx [ x^2 * e^x ]: {sp.simplify(sp.diff(f_product, x))}")
print(f"d/dx [ e^x / x ]: {sp.simplify(sp.diff(f_quotient, x))}")

# 2. Verify Sigmoid Derivative Formula: sigmoid(x) * (1 - sigmoid(x))
def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

def sigmoid_derivative(x):
    s = sigmoid(x)
    return s * (1.0 - s)

# Numerical test at x = 2.0
x_val = 2.0
sig_der_formula = sigmoid_derivative(x_val)

# Numerical central difference check
h = 1e-6
sig_der_num = (sigmoid(x_val + h) - sigmoid(x_val - h)) / (2 * h)

print(f"\nSigmoid Derivative at x=2.0 (Formula):   {sig_der_formula:.6f}")
print(f"Sigmoid Derivative at x=2.0 (Numerical): {sig_der_num:.6f}")
assert np.isclose(sig_der_formula, sig_der_num)
print("Sigmoid Derivative Rule Verified!")
