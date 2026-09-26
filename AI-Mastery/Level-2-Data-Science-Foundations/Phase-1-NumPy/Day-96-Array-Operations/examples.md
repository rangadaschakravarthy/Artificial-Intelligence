# Day 96 Worked Examples: Array Operations

## Example 1 — Beginner: Basic Element-wise Arithmetic
```python
import numpy as np

a = np.array([10, 20, 30, 40])
b = np.array([2, 4, 5, 8])

print("Addition (a + b):       ", a + b)
print("Subtraction (a - b):    ", a - b)
print("Multiplication (a * b): ", a * b)
print("Division (a / b):       ", a / b)
print("Power (a ** 2):         ", a ** 2)
```

## Example 2 — Practical: Comparison & Boolean Mask Generation
```python
import numpy as np

temperatures = np.array([18.5, 22.0, 31.5, 29.0, 15.0, 34.0])

is_hot = temperatures > 30.0
print("Temperature array:", temperatures)
print("Is Hot Mask ( > 30.0):", is_hot)
print("Hot Temperatures:", temperatures[is_hot])
```

## Example 3 — Intermediate: In-Place Memory Optimization (`out` parameter)
```python
import numpy as np

X = np.ones((1000, 1000), dtype=np.float64)
Y = np.full((1000, 1000), 2.0, dtype=np.float64)

# Out-of-place: Allocates new 8MB array
Z = X + Y 

# In-place using ufunc out parameter: No RAM allocation!
np.add(X, Y, out=X)
print("X updated in-place, top-left element:", X[0, 0]) # 3.0
```

## Example 4 — Real Dataset: Normalizing Feature Values (Min-Max Scaling)
```python
import numpy as np

# Feature vector (e.g., house prices in $k)
prices = np.array([150.0, 200.0, 350.0, 500.0, 100.0])

min_val = prices.min()
max_val = prices.max()

# Element-wise Min-Max Scaling formula: (x - min) / (max - min)
scaled_prices = (prices - min_val) / (max_val - min_val)

print("Original Prices:", prices)
print("Min-Max Scaled [0, 1]:", np.round(scaled_prices, 4))
```

## Example 5 — AI/ML Application: Calculating Mean Squared Error (MSE) Loss
```python
import numpy as np

y_true = np.array([1.0, 0.0, 1.0, 1.0, 0.0])
y_pred = np.array([0.9, 0.1, 0.8, 0.95, 0.2])

# Step 1: Element-wise error
errors = y_pred - y_true

# Step 2: Element-wise squared error
squared_errors = errors ** 2

# Step 3: Mean loss reduction
mse_loss = np.mean(squared_errors)

print("Element-wise Errors:  ", np.round(errors, 2))
print("Squared Errors:       ", np.round(squared_errors, 4))
print(f"Mean Squared Error:   {mse_loss:.4f}")
```
