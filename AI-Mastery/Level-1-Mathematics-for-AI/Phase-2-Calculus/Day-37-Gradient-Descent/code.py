# Day 37 — Gradient Descent
import numpy as np

# 1. Synthetic Linear Regression Data
np.random.seed(42)
N = 300
X = np.random.randn(N, 1)
y = 3.0 * X + 2.0 + np.random.randn(N, 1) * 0.2
X_b = np.hstack([np.ones((N, 1)), X])  # Add bias column

# 2. Mini-Batch SGD Implementation
def mini_batch_sgd(X_data, y_data, batch_size=32, lr=0.05, epochs=20):
    N_samples, n_features = X_data.shape
    w = np.zeros((n_features, 1))  # Initialize weights to 0
    
    loss_history = []
    for epoch in range(epochs):
        # Shuffle dataset at start of epoch
        indices = np.random.permutation(N_samples)
        X_shuffled = X_data[indices]
        y_shuffled = y_data[indices]
        
        for i in range(0, N_samples, batch_size):
            X_batch = X_shuffled[i:i+batch_size]
            y_batch = y_shuffled[i:i+batch_size]
            
            # Compute Gradient: 2/B * X_batch^T * (X_batch * w - y_batch)
            B_curr = len(X_batch)
            error = X_batch @ w - y_batch
            grad = (2.0 / B_curr) * (X_batch.T @ error)
            
            # Update Weights
            w -= lr * grad
            
        # Record Loss at end of epoch
        total_loss = np.mean((X_data @ w - y_data)**2)
        loss_history.append(total_loss)
        
    return w, loss_history

w_trained, losses = mini_batch_sgd(X_b, y, batch_size=32, lr=0.05, epochs=20)

print(f"Trained Parameters [Bias, Slope]: [{w_trained[0,0]:.4f}, {w_trained[1,0]:.4f}]")
print(f"True Parameters [Bias=2.0000, Slope=3.0000]")
print(f"Initial Epoch Loss: {losses[0]:.4f} -> Final Epoch Loss: {losses[-1]:.4f}")
