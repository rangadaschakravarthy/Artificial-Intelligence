# Day 23 — Linear Algebra for Machine Learning
# Implementation of Linear Regression OLS using Pure Matrix Algebra

import numpy as np

# 1. Generate Synthetic Dataset (y = 2*x1 + 3*x2 + 5 + noise)
np.random.seed(42)
N = 100
x1 = np.random.randn(N)
x2 = np.random.randn(N)
noise = np.random.randn(N) * 0.1
y = 2.0 * x1 + 3.0 * x2 + 5.0 + noise

# 2. Build Augmented Design Matrix X (Column of 1s for bias + features)
X_raw = np.column_stack([x1, x2])
ones = np.ones((N, 1))
X = np.hstack([ones, X_raw])  # Shape (100, 3)

print(f"Augmented Design Matrix X shape: {X.shape}")
print(f"Target Vector y shape: {y.shape}")

# 3. Solve OLS Normal Equation: w* = (X^T * X)^-1 * X^T * y
X_T = X.T
Gram_matrix = X_T @ X
X_T_y = X_T @ y

w_ols = np.linalg.inv(Gram_matrix) @ X_T_y

print(f"\nEstimated Parameters [Bias, w1, w2]:\n{w_ols}")
print(f"True Parameters [Bias=5.0, w1=2.0, w2=3.0]")

# 4. Predict & Compute Mean Squared Error (MSE)
y_pred = X @ w_ols
mse_loss = np.mean((y - y_pred)**2)
print(f"\nOLS Model Mean Squared Error (MSE): {mse_loss:.6f}")
