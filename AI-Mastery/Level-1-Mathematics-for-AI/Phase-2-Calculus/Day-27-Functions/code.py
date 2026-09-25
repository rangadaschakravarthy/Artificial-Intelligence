# Day 27 — Functions
import numpy as np

# 1. Common AI Activation Functions
def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

def relu(x):
    return np.maximum(0.0, x)

def softmax(z):
    exp_z = np.exp(z - np.max(z))  # Numerically stable subtraction
    return exp_z / np.sum(exp_z)

# Test Inputs
x_vals = np.array([-3.0, -1.0, 0.0, 1.0, 3.0])

print("Input Values:", x_vals)
print("Sigmoid Outputs:", np.round(sigmoid(x_vals), 4))
print("ReLU Outputs:   ", relu(x_vals))

# Test Softmax
logits = np.array([2.0, 1.0, 0.1])
probs = softmax(logits)
print(f"\nRaw Logits: {logits}")
print(f"Softmax Probabilities: {np.round(probs, 4)} (Sum = {np.sum(probs):.1f})")
