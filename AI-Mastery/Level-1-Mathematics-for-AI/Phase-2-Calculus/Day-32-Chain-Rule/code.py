# Day 32 — Chain Rule
import numpy as np

# 1. Chain Rule for Composite Function: f(x) = (3x^2 + 1)^4
# Let u = 3x^2 + 1  => du/dx = 6x
# Let y = u^4       => dy/du = 4u^3
# dy/dx = dy/du * du/dx = 4(3x^2 + 1)^3 * (6x)

def u(x):
    return 3.0 * x**2 + 1.0

def y(u):
    return u**4

def dy_dx_analytic(x):
    return 4.0 * (3.0 * x**2 + 1.0)**3 * (6.0 * x)

x_val = 2.0
analytic_grad = dy_dx_analytic(x_val)

# Numerical derivative check
h = 1e-6
num_grad = (y(u(x_val + h)) - y(u(x_val - h))) / (2 * h)

print(f"Analytical Chain Rule Derivative at x=2.0: {analytic_grad:.2f}")
print(f"Numerical Derivative at x=2.0:             {num_grad:.2f}")
assert np.isclose(analytic_grad, num_grad)
print("Chain Rule Verified Successfully!")

# 2. Simple Neural Network 1-Neuron Backprop Chain Rule
# L = 0.5 * (sigmoid(w * x + b) - target)^2
def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

x_in = 1.5
w_in = 0.8
b_in = 0.2
target = 1.0

# Forward Pass
z = w_in * x_in + b_in
a = sigmoid(z)
loss = 0.5 * (a - target)**2

# Backward Pass via Chain Rule
# dL/dw = dL/da * da/dz * dz/dw
dL_da = a - target
da_dz = a * (1.0 - a)
dz_dw = x_in

dL_dw = dL_da * da_dz * dz_dw
print(f"\nNeural Pass Loss: {loss:.6f}")
print(f"Weight Gradient dL/dw via Chain Rule: {dL_dw:.6f}")
