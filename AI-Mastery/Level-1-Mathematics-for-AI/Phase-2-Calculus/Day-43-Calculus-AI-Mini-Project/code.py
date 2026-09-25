# Day 43 — Calculus AI Mini-Project
# Building a Deep Neural Network Engine from Scratch in Pure NumPy

import numpy as np

# 1. Activation Functions & Derivatives
def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

def sigmoid_prime(z):
    s = sigmoid(z)
    return s * (1.0 - s)

def relu(z):
    return np.maximum(0.0, z)

def relu_prime(z):
    return (z > 0).astype(np.float64)

# 2. XOR Non-Linear Dataset
X = np.array([
    [0.0, 0.0],
    [0.0, 1.0],
    [1.0, 0.0],
    [1.0, 1.0]
]) # Shape (4, 2)

Y = np.array([
    [0.0],
    [1.0],
    [1.0],
    [0.0]
]) # Shape (4, 1)

# 3. Initialize Neural Network (2 -> 4 -> 1)
np.random.seed(42)
input_dim = 2
hidden_dim = 4
output_dim = 1

# He Normal Weight Initialization
W1 = np.random.randn(hidden_dim, input_dim) * np.sqrt(2.0 / input_dim)
b1 = np.zeros((hidden_dim, 1))

W2 = np.random.randn(output_dim, hidden_dim) * np.sqrt(2.0 / hidden_dim)
b2 = np.zeros((output_dim, 1))

# Hyperparameters
lr = 0.5
epochs = 2000
B = X.shape[0]

print("--- Training Pure Calculus Neural Network on XOR ---")

# 4. Training Loop
for epoch in range(epochs):
    # Forward Pass
    Z1 = X @ W1.T + b1.T              # Shape (4, 4)
    A1 = relu(Z1)                     # Shape (4, 4)
    
    Z2 = A1 @ W2.T + b2.T             # Shape (4, 1)
    A2 = sigmoid(Z2)                  # Shape (4, 1)
    
    # Binary Cross-Entropy Loss
    loss = -np.mean(Y * np.log(A2 + 1e-7) + (1.0 - Y) * np.log(1.0 - A2 + 1e-7))
    
    # Backward Pass (Calculus Chain Rule)
    # Output Delta: Delta2 = A2 - Y
    Delta2 = A2 - Y                   # Shape (4, 1)
    
    # Hidden Delta: Delta1 = (Delta2 @ W2) * relu_prime(Z1)
    Delta1 = (Delta2 @ W2) * relu_prime(Z1) # Shape (4, 4)
    
    # Compute Gradients
    dW2 = (1.0 / B) * (Delta2.T @ A1) # Shape (1, 4)
    db2 = (1.0 / B) * np.sum(Delta2, axis=0, keepdims=True).T
    
    dW1 = (1.0 / B) * (Delta1.T @ X)  # Shape (4, 2)
    db1 = (1.0 / B) * np.sum(Delta1, axis=0, keepdims=True).T
    
    # SGD Weight Updates
    W2 -= lr * dW2
    b2 -= lr * db2
    W1 -= lr * dW1
    b1 -= lr * db1
    
    if epoch % 400 == 0 or epoch == epochs - 1:
        print(f"Epoch {epoch:<4}: BCE Loss = {loss:.6f}")

# 5. Final Evaluation on XOR
print("\n--- Final Trained Predictions ---")
Z1_final = X @ W1.T + b1.T
A1_final = relu(Z1_final)
Z2_final = A1_final @ W2.T + b2.T
A2_final = sigmoid(Z2_final)

for i in range(4):
    print(f"Input: {X[i]} -> True Target: {Y[i,0]:.0f} | Neural Prediction: {A2_final[i,0]:.4f} (Binary: {int(A2_final[i,0] > 0.5)})")
