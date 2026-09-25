# Day 41 — Backpropagation Mathematics
# Complete 4-Equation Backpropagation Proof & Verification Code

import numpy as np

# Sigmoid & Derivative
def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

def sigmoid_prime(z):
    s = sigmoid(z)
    return s * (1.0 - s)

# 1. Setup 2-Layer Neural Network (Hand-Calculation Test Case)
# Inputs x (2x1), Hidden w1 (2x2), Output w2 (1x2)
x = np.array([[1.0], [1.0]])
y = np.array([[1.0]])

W1 = np.array([[0.1, 0.2], [0.3, 0.4]])
b1 = np.array([[0.0], [0.0]])

W2 = np.array([[0.5, 0.6]])
b2 = np.array([[0.0]])

# 2. Forward Pass
z1 = W1 @ x + b1                  # [[0.3], [0.7]]
a1 = sigmoid(z1)                   # [[0.574443], [0.668188]]

z2 = W2 @ a1 + b2                  # [[0.688137]]
a2 = sigmoid(z2)                   # [[0.665538]]
loss = 0.5 * (a2[0,0] - y[0,0])**2 # 0.055932

print(f"--- Forward Pass ---")
print(f"Predicted Output a2: {a2[0,0]:.6f}")
print(f"Target Output y:     {y[0,0]:.6f}")
print(f"MSE Loss:            {loss:.6f}")

# 3. Backward Pass (4 Fundamental Backpropagation Equations)
# Eq 1: Output Layer Delta delta2 = (a2 - y) * sigmoid_prime(z2)
delta2 = (a2 - y) * sigmoid_prime(z2)

# Eq 3 & 4 for Layer 2: dW2 = delta2 * a1^T, db2 = delta2
dW2 = delta2 @ a1.T
db2 = delta2

# Eq 2: Hidden Layer Delta Recurrence delta1 = (W2^T * delta2) * sigmoid_prime(z1)
delta1 = (W2.T @ delta2) * sigmoid_prime(z1)

# Eq 3 & 4 for Layer 1: dW1 = delta1 * x^T, db1 = delta1
dW1 = delta1 @ x.T
db1 = delta1

print(f"\n--- 4 Fundamental Equations Output ---")
print(f"Eq 1 (Output Delta delta2): {delta2[0,0]:.6f}")
print(f"Eq 2 (Hidden Delta delta1):\n{delta1}")
print(f"Eq 4 (Layer 2 Weight Grad dW2): {dW2}")
print(f"Eq 4 (Layer 1 Weight Grad dW1):\n{dW1}")
