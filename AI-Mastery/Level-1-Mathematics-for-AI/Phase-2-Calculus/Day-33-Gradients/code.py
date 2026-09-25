# Day 33 — Gradients
import numpy as np

# Scalar Loss Function L(w1, w2) = w1^2 + 3*w2^2
def loss_func(w):
    return w[0]**2 + 3.0 * w[1]**2

# Analytical Gradient Vector grad L = [2*w1, 6*w2]^T
def grad_exact(w):
    return np.array([2.0 * w[0], 6.0 * w[1]])

# Numerical Gradient Function (Central Difference)
def grad_numerical(f, w, h=1e-5):
    grad = np.zeros_like(w)
    for i in range(len(w)):
        w_plus = w.copy()
        w_minus = w.copy()
        w_plus[i] += h
        w_minus[i] -= h
        grad[i] = (f(w_plus) - f(w_minus)) / (2 * h)
    return grad

w_curr = np.array([3.0, 2.0])
exact_g = grad_exact(w_curr)
num_g = grad_numerical(loss_func, w_curr)

print(f"Current Weights (w1, w2): {w_curr}")
print(f"Analytical Gradient Vector:  {exact_g}")
print(f"Numerical Gradient Vector:   {num_g}")
assert np.allclose(exact_g, num_g)

# 1 Step of Gradient Descent (Steepest Descent)
eta = 0.1  # Learning rate
w_next = w_curr - eta * exact_g
print(f"\nUpdated Weights after 1 GD step (eta=0.1): {w_next}")
print(f"Previous Loss: {loss_func(w_curr):.2f} -> New Loss: {loss_func(w_next):.2f} (Reduced!)")
