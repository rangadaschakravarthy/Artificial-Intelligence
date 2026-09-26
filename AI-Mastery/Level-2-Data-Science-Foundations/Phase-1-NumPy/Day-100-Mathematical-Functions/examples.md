# Day 100 Worked Examples: Mathematical Functions

## Example 1 — Beginner: Exponential, Logarithmic, and Square Root
```python
import numpy as np

x = np.array([1.0, 2.0, 4.0, 10.0])

print("Input x:       ", x)
print("exp(x):        ", np.round(np.exp(x), 2))
print("Natural Log:   ", np.round(np.log(x), 2))
print("Log Base 10:   ", np.round(np.log10(x), 2))
print("Square Root:   ", np.round(np.sqrt(x), 2))
```

## Example 2 — Practical: Rounding Methods Comparison
```python
import numpy as np

vals = np.array([-1.7, -1.2, 0.5, 1.2, 1.7])

print("Original Values:", vals)
print("Floor (down):   ", np.floor(vals))
print("Ceil (up):      ", np.ceil(vals))
print("Trunc (towards 0):", np.trunc(vals))
print("Round (nearest):", np.round(vals))
```

## Example 3 — Intermediate: Implementing Tanh Activation Function
```python
import numpy as np

z = np.array([-2.0, -1.0, 0.0, 1.0, 2.0])

# Method 1: Built-in ufunc
tanh_builtin = np.tanh(z)

# Method 2: Mathematical formula (exp(z) - exp(-z)) / (exp(z) + exp(-z))
tanh_formula = (np.exp(z) - np.exp(-z)) / (np.exp(z) + np.exp(-z))

print("Built-in Tanh:", np.round(tanh_builtin, 4))
print("Formula Tanh: ", np.round(tanh_formula, 4))
```

## Example 4 — Real Dataset: Log Transformation of Right-Skewed Data
```python
import numpy as np

# Right-skewed feature (e.g. Income in dollars)
incomes = np.array([20000, 35000, 50000, 120000, 1500000])

# Apply log1p transform to compress right-skewed tail
log_incomes = np.log1p(incomes)

print("Original Incomes:", incomes)
print("Log1p Incomes:   ", np.round(log_incomes, 2))
```

## Example 5 — AI/ML Application: Numerically Stable Log-Sum-Exp
```python
import numpy as np

# Large logits that would overflow standard exp(z)
logits = np.array([1000.0, 1001.0, 1002.0])

# Standard exp(logits) overflows to [inf, inf, inf]
# Log-Sum-Exp Trick: max_z + log(sum(exp(z - max_z)))
max_z = np.max(logits)
lse = max_z + np.log(np.sum(np.exp(logits - max_z)))

print("Numerically Stable Log-Sum-Exp:", lse)
```
