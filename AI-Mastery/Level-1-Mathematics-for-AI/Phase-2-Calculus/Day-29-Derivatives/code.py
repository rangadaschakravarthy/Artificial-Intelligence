# Day 29 — Derivatives
import numpy as np

# Function f(x) = x^3 - 3x
def f(x):
    return x**3 - 3.0 * x

# Analytical Exact Derivative f'(x) = 3x^2 - 3
def f_prime_exact(x):
    return 3.0 * x**2 - 3.0

# 1. Numerical Derivatives Comparison
def forward_diff(f, x, h=0.01):
    return (f(x + h) - f(x)) / h

def central_diff(f, x, h=0.01):
    return (f(x + h) - f(x - h)) / (2.0 * h)

x_test = 2.0
exact = f_prime_exact(x_test)
fwd = forward_diff(f, x_test, h=0.01)
cnt = central_diff(f, x_test, h=0.01)

print(f"Exact Derivative at x=2.0:   {exact:.6f}")
print(f"Forward Difference (h=0.01): {fwd:.6f} (Error: {abs(fwd - exact):.6f})")
print(f"Central Difference (h=0.01): {cnt:.6f} (Error: {abs(cnt - exact):.6f})")
