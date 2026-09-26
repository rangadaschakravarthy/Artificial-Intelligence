# Day 183 Worked Examples: Deep Learning

## Example 1 — Practical: Simulating Artificial Neuron Calculation
```python
import numpy as np

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

# Inputs x, Weights w, Bias b
x = np.array([0.5, 0.8, -0.2])
w = np.array([1.2, -0.5, 2.0])
b = 0.1

z = np.dot(w, x) + b
output = sigmoid(z)

print(f"Weighted Sum z: {z:.4f}")
print(f"Neuron Sigmoid Output: {output:.4f}")
```
