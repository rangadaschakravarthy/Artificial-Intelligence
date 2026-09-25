# Day 40 — Calculus for Neural Networks
# 2-Layer Neural Network Forward and Backward Pass in Pure NumPy

import numpy as np

# Sigmoid Activation & Derivative
def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

def sigmoid_prime(z):
    s = sigmoid(z)
    return s * (1.0 - s)

# 1. Network Architecture: Input (2) -> Hidden (3) -> Output (1)
np.random.seed(42)
W1 = np.random.randn(3, 2)  # Shape (3, 2)
b1 = np.zeros((3, 1))       # Shape (3, 1)

W2 = np.random.randn(1, 3)  # Shape (1, 3)
b2 = np.zeros((1, 1))       # Shape (1, 1)

# Training Sample (XOR input)
x = np.array([[1.0], [0.0]])  # Shape (2, 1)
y = np.array([[1.0]])         # Shape (1, 1)

print("--- Forward Pass ---")
# Layer 1 Forward
z1 = W1 @ x + b1
a1 = sigmoid(z1)

# Layer 2 Forward
z2 = W2 @ a1 + b2
a2 = sigmoid(z2)
loss = 0.5 * (a2 - y)**2

print(f"Prediction a2: {a2[0,0]:.4f}, Target y: {y[0,0]:.1f}, Loss: {loss[0,0]:.6f}")

print("\n--- Backward Pass (Calculus Error Deltas) ---")
# 1. Output Layer Delta: delta2 = (a2 - y) * sigmoid_prime(z2)
delta2 = (a2 - y) * sigmoid_prime(z2)

# Gradients for Layer 2
dW2 = delta2 @ a1.T
db2 = delta2

# 2. Hidden Layer Delta Recurrence: delta1 = (W2^T * delta2) * sigmoid_prime(z1)
delta1 = (W2.T @ delta2) * sigmoid_prime(z1)

# Gradients for Layer 1
dW1 = delta1 @ x.T
db1 = delta1

print(f"Output Delta (delta2):\n{delta2}")
print(f"Layer 2 Weight Gradient dW2 (shape {dW2.shape}):\n{dW2}")
print(f"Hidden Delta (delta1):\n{delta1}")
print(f"Layer 1 Weight Gradient dW1 (shape {dW1.shape}):\n{dW1}")
