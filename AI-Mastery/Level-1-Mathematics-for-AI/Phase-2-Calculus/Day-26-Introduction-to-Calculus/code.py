# Day 26 — Introduction to Calculus
import numpy as np

# Define quadratic function f(x) = x^2
def f(x):
    return x**2

# 1. Secant Line Slope (Average Rate of Change)
def secant_slope(f, x1, x2):
    return (f(x2) - f(x1)) / (x2 - x1)

print("--- Secant Slope Approaching Tangent at x = 2 ---")
intervals = [1.0, 0.5, 0.1, 0.01, 0.0001]
for h in intervals:
    slope = secant_slope(f, 2.0, 2.0 + h)
    print(f"Interval h = {h:<7}: Secant Slope = {slope:.6f}")

# 2. Numerical Derivative Approximation at x = 2
def numerical_derivative(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)  # Central Difference Formula

deriv_x2 = numerical_derivative(f, 2.0)
print(f"\nInstantaneous Derivative at x = 2.0: {deriv_x2:.4f} (True mathematical derivative = 4.0)")
