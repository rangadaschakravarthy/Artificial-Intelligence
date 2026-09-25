# Day 36 — Loss Functions
import numpy as np

# 1. Regression Losses: MSE, MAE, Huber Loss
def mse_loss(y_true, y_pred):
    return np.mean((y_true - y_pred)**2)

def mae_loss(y_true, y_pred):
    return np.mean(np.abs(y_true - y_pred))

def huber_loss(y_true, y_pred, delta=1.0):
    error = y_true - y_pred
    is_small_error = np.abs(error) <= delta
    squared_loss = 0.5 * (error**2)
    linear_loss = delta * (np.abs(error) - 0.5 * delta)
    return np.mean(np.where(is_small_error, squared_loss, linear_loss))

# Test Regression Data
y_real = np.array([10.0, 20.0, 30.0, 100.0])  # Note outlier at 100!
y_hat  = np.array([12.0, 18.0, 31.0, 40.0])   # Prediction error 60 on outlier

print("--- Regression Loss Comparison ---")
print(f"MSE Loss (Outlier Sensitive): {mse_loss(y_real, y_hat):.2f}")
print(f"MAE Loss (Robust):            {mae_loss(y_real, y_hat):.2f}")
print(f"Huber Loss (Balanced):        {huber_loss(y_real, y_hat):.2f}")

# 2. Classification Losses: BCE and CCE
def binary_cross_entropy(y_true, y_pred, eps=1e-7):
    y_pred = np.clip(y_pred, eps, 1.0 - eps)
    return -np.mean(y_true * np.log(y_pred) + (1.0 - y_true) * np.log(1.0 - y_pred))

y_class = np.array([1.0, 0.0, 1.0])
p_class = np.array([0.9, 0.1, 0.8])
bce = binary_cross_entropy(y_class, p_class)
print(f"\nBinary Cross-Entropy Loss: {bce:.4f}")
