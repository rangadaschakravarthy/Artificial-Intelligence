# Day 39 — Gradient Descent in Machine Learning
import numpy as np

# 1. Synthetic Classification Data
np.random.seed(42)
N = 200
X1 = np.random.randn(N) * 100.0  # Large scale feature (e.g. Income)
X2 = np.random.randn(N) * 0.1    # Small scale feature (e.g. Interest Rate)

# True decision rule: y = 1 if 0.05*X1 + 20*X2 > 0 else 0
logits_true = 0.05 * X1 + 20.0 * X2
y_true = (1.0 / (1.0 + np.exp(-logits_true)) > 0.5).astype(np.float64)

X_raw = np.column_stack([X1, X2])

# 2. Feature Standardization: z = (x - mean) / std
X_mean = np.mean(X_raw, axis=0)
X_std = np.std(X_raw, axis=0)
X_scaled = (X_raw - X_mean) / X_std

print(f"Raw Feature Stds:    {np.std(X_raw, axis=0)}")
print(f"Scaled Feature Stds: {np.std(X_scaled, axis=0)} (Standardized!)")

# 3. Logistic Regression SGD Trainer
def train_logistic_sgd(X_data, y_data, lr=0.1, epochs=50):
    N_samples, n_feats = X_data.shape
    w = np.zeros(n_feats)
    b = 0.0
    
    for epoch in range(epochs):
        # Forward pass
        z = X_data @ w + b
        p = 1.0 / (1.0 + np.exp(-z))
        
        # Gradients
        error = p - y_data
        dw = (1.0 / N_samples) * (X_data.T @ error)
        db = np.mean(error)
        
        # Updates
        w -= lr * dw
        b -= lr * db
        
    loss = -np.mean(y_data * np.log(p + 1e-7) + (1 - y_data) * np.log(1 - p + 1e-7))
    return loss

loss_unscaled = train_logistic_sgd(X_raw, y_true, lr=1e-5, epochs=50)
loss_scaled   = train_logistic_sgd(X_scaled, y_true, lr=0.1,  epochs=50)

print(f"\nFinal BCE Loss (Unscaled Features): {loss_unscaled:.4f}")
print(f"Final BCE Loss (Scaled Features):   {loss_scaled:.4f} (Converged much faster!)")
