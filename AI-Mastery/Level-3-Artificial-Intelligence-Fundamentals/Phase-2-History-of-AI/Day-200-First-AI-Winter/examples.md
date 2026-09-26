# Day 200 Worked Examples: First AI Winter

## Example 1 — Practical: The XOR Linearly Non-Separable Problem
```python
# XOR Truth Table: (0,0)->0, (0,1)->1, (1,0)->1, (1,1)->0
# Cannot be separated by a single straight decision line w1*x1 + w2*x2 + b = 0!
import numpy as np

xor_inputs = np.array([[0,0], [0,1], [1,0], [1,1]])
xor_targets = np.array([0, 1, 1, 0])

print("XOR Inputs:
", xor_inputs)
print("XOR Targets:", xor_targets)
print("Requires Multi-Layer Perceptrons (MLP) with non-linear activations to solve!")
```
