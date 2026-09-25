# Day 38 — Learning Rate
import numpy as np

# Loss function L(w) = 5 * w^2 (Minimum at w = 0)
# Derivative L'(w) = 10 * w
def grad_loss(w):
    return 10.0 * w

def run_gd(w_start, lr, steps=10):
    w = w_start
    history = [w]
    for _ in range(steps):
        w = w - lr * grad_loss(w)
        history.append(w)
    return history

w_init = 1.0

# 1. Under-shooting (lr too small = 0.01)
w_small = run_gd(w_init, lr=0.01, steps=10)

# 2. Optimal Learning Rate (lr = 0.1)
w_optimal = run_gd(w_init, lr=0.1, steps=10)

# 3. Over-shooting / Divergence (lr too large = 0.22)
w_large = run_gd(w_init, lr=0.22, steps=10)

print(f"Initial Weight: {w_init}")
print(f"Small LR (0.01) after 10 steps:   w = {w_small[-1]:.4f} (Slow convergence)")
print(f"Optimal LR (0.10) after 10 steps: w = {w_optimal[-1]:.4f} (Reached Minimum!)")
print(f"Large LR (0.22) after 10 steps:   w = {w_large[-1]:.4f} (Exploded/Diverged!)")

# 4. Cosine Annealing Learning Rate Schedule
def cosine_annealing_lr(eta_max, eta_min, total_epochs):
    epochs = np.arange(total_epochs)
    lrs = eta_min + 0.5 * (eta_max - eta_min) * (1.0 + np.cos(epochs / total_epochs * np.pi))
    return lrs

lrs = cosine_annealing_lr(eta_max=0.1, eta_min=0.001, total_epochs=10)
print(f"\nCosine Annealing LRs (Epoch 0 to 9):\n{np.round(lrs, 4)}")
