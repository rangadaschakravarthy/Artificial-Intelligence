# Day 91 Worked Examples: Array Creation

## Example 1 — Beginner: Basic Constant Creation Functions
```python
import numpy as np

z = np.zeros((2, 3))
o = np.ones((2, 3))
f = np.full((2, 3), 99)

print("Zeros:
", z)
print("Ones:
", o)
print("Full (99):
", f)
```

## Example 2 — Practical: arange vs linspace Comparison
```python
import numpy as np

# arange: start=0, stop=10, step=2 -> [0, 10)
a = np.arange(0, 10, 2)

# linspace: start=0, stop=10, num=5 -> [0, 10] inclusive
l = np.linspace(0, 10, 5)

print("arange (step=2):", a)
print("linspace (num=5):", l)
```

## Example 3 — Intermediate: Creating Identity & Diagonal Matrices
```python
import numpy as np

# 3x3 Identity Matrix I
I = np.eye(3)

# Custom Diagonal Matrix
diag_vals = np.array([10, 20, 30])
D = np.diag(diag_vals)

print("Identity Matrix:
", I)
print("Diagonal Matrix:
", D)
```

## Example 4 — Real Dataset: Generating Synthetic Time Axis
```python
import numpy as np

# Simulate 1 second of audio recorded at 44.1 kHz sampling rate
sample_rate = 44100
time_axis = np.linspace(0.0, 1.0, sample_rate, endpoint=False)

print("Time axis shape:", time_axis.shape)
print("First 5 time stamps:", time_axis[:5])
print("Last 5 time stamps:", time_axis[-5:])
```

## Example 5 — AI/ML Application: Pre-allocating Output Array for Iterative Computation
```python
import numpy as np

# Pre-allocate output buffer for 1,000 epoch loss history
num_epochs = 1000
loss_history = np.empty(num_epochs, dtype=np.float64)

# Simulation loop writing directly to allocated buffer
for epoch in range(num_epochs):
    loss_history[epoch] = 1.0 / (epoch + 1)

print("First 3 epoch losses:", loss_history[:3])
print("Final loss:", loss_history[-1])
```
