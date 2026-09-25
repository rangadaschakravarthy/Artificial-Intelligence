# Day 28 — Limits
import numpy as np

# 1. Numerical Evaluation of Indeterminate Limit: lim_{x->2} (x^2 - 4) / (x - 2)
def f(x):
    return (x**2 - 4.0) / (x - 2.0)

print("--- Approaching x = 2 from left and right ---")
x_vals = [1.9, 1.99, 1.9999, 2.0001, 2.01, 2.1]
for x in x_vals:
    print(f"x = {x:<7}: f(x) = {f(x):.6f}")

# 2. Numerical Stability Guard for Log Loss: preventing log(0)
def safe_log_loss(y_true, y_pred, eps=1e-7):
    # Clip predictions to range [eps, 1 - eps]
    y_pred_clipped = np.clip(y_pred, eps, 1.0 - eps)
    return - (y_true * np.log(y_pred_clipped) + (1 - y_true) * np.log(1.0 - y_pred_clipped))

# Test zero probability prediction (would crash standard np.log(0))
y_true = 1.0
y_pred_zero = 0.0

loss = safe_log_loss(y_true, y_pred_zero)
print(f"\nSafe Log Loss with p=0.0 clipped: {loss:.4f} (Avoided -Inf / NaN crash!)")
