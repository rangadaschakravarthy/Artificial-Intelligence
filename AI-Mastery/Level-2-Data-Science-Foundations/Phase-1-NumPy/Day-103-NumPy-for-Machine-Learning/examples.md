# Day 103 Worked Examples: NumPy for Machine Learning

## Example 1 — Beginner: Vectorized Activation Functions
```python
import numpy as np

# Sample Linear Logits
z = np.array([-3.0, -1.0, 0.0, 2.0, 5.0])

# 1. Sigmoid: 1 / (1 + exp(-z))
sigmoid = 1.0 / (1.0 + np.exp(-z))

# 2. ReLU: max(0, z)
relu = np.maximum(0, z)

# 3. Leaky ReLU: max(0.01*z, z)
leaky_relu = np.where(z > 0, z, 0.01 * z)

print("Input Logits: ", z)
print("Sigmoid:      ", np.round(sigmoid, 4))
print("ReLU:         ", relu)
print("Leaky ReLU:   ", leaky_relu)
```

## Example 2 — Practical: Binary Cross-Entropy (BCE) Loss
```python
import numpy as np

y_true = np.array([1, 0, 1, 1, 0])
y_prob = np.array([0.9, 0.1, 0.85, 0.95, 0.05])

# Clip probabilities to prevent log(0)
eps = 1e-15
y_prob_clipped = np.clip(y_prob, eps, 1 - eps)

# BCE Loss Formula
bce_loss = -np.mean(y_true * np.log(y_prob_clipped) + (1 - y_true) * np.log(1 - y_prob_clipped))

print("Target Labels:       ", y_true)
print("Model Probabilities: ", y_prob)
print(f"Binary Cross-Entropy Loss: {bce_loss:.4f}")
```

## Example 3 — Intermediate: Softmax Classifier Function
```python
import numpy as np

# Logits for 2 samples, 3 classes
logits = np.array([
    [2.0, 1.0, 0.1],
    [0.5, 3.0, 1.5]
])

# Numerically stable Softmax
exp_z = np.exp(logits - np.max(logits, axis=1, keepdims=True))
probs = exp_z / np.sum(exp_z, axis=1, keepdims=True)

print("Output Probabilities (Softmax):
", np.round(probs, 4))
print("Predicted Classes:", np.argmax(probs, axis=1))
```

## Example 4 — Real Dataset: One-Hot Encoding Labels in Pure NumPy
```python
import numpy as np

# Class labels for 5 samples (3 classes: 0, 1, 2)
labels = np.array([0, 2, 1, 0, 2])

num_classes = 3
one_hot = np.zeros((len(labels), num_classes))
one_hot[np.arange(len(labels)), labels] = 1.0

print("Original Labels:", labels)
print("One-Hot Matrix:
", one_hot)
```

## Example 5 — AI/ML Application: Complete Linear Regression in Pure NumPy
```python
import numpy as np

# Synthetic Dataset: Y = 3*X + 5 + noise
rng = np.random.default_rng(42)
X = rng.uniform(0, 10, size=(100, 1))
y = 3.0 * X.flatten() + 5.0 + rng.normal(0, 1, size=100)

# Initialize Weights and Bias
w = 0.0
b = 0.0
lr = 0.01
epochs = 500
N = len(X)

# Gradient Descent Loop
for epoch in range(epochs):
    y_pred = (X.flatten() * w) + b
    
    # Gradients
    dw = (2 / N) * np.sum((y_pred - y) * X.flatten())
    db = (2 / N) * np.sum(y_pred - y)
    
    # Updates
    w -= lr * dw
    b -= lr * db

print(f"Trained Weight w: {w:.4f} (Target: 3.0)")
print(f"Trained Bias b:   {b:.4f} (Target: 5.0)")
```
