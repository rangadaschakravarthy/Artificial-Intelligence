# Day 94 Worked Examples: Boolean and Fancy Indexing

## Example 1 — Beginner: Basic Boolean Masking
```python
import numpy as np

scores = np.array([55, 88, 42, 95, 73, 61])

# Create boolean mask for passing grades (>= 70)
mask = scores >= 70
passing_scores = scores[mask]

print("Mask:", mask)
print("Passing Scores:", passing_scores)
```

## Example 2 — Practical: Complex Multi-Condition Queries
```python
import numpy as np

ages = np.array([22, 45, 60, 35, 18, 50])
incomes = np.array([30, 85, 120, 65, 20, 95]) # in $k

# Query: Age >= 30 AND Income > 70k
cond = (ages >= 30) & (incomes > 70)
high_earners_ages = ages[cond]

print("Matching Indices:", np.where(cond)[0])
print("High Earners Ages:", high_earners_ages)
```

## Example 3 — Intermediate: Fancy Indexing for Row Reordering
```python
import numpy as np

matrix = np.array([
    [10, 20], # Row 0
    [30, 40], # Row 1
    [50, 60], # Row 2
    [70, 80]  # Row 3
])

# Reorder rows: Row 3, then Row 0, then Row 2
reordered = matrix[[3, 0, 2]]
print("Reordered Matrix:
", reordered)
```

## Example 4 — Real Dataset: Outlier Clipping via Masking
```python
import numpy as np

# Feature vector with extreme outliers
data = np.array([12.0, 15.0, 14.0, 150.0, 13.0, -99.0, 16.0])

# Clip outliers outside range [0.0, 50.0]
data[data < 0.0] = 0.0
data[data > 50.0] = 50.0

print("Clipped Clean Data:", data)
```

## Example 5 — AI/ML Application: Implementing ReLU Activation Function
```python
import numpy as np

# Linear activation outputs before non-linearity
z = np.array([-2.5, 1.2, -0.1, 4.8, 0.0])

# Rectified Linear Unit (ReLU): f(z) = max(0, z)
relu_out = z.copy()
relu_out[relu_out < 0] = 0.0

print("Raw Layer Activations: ", z)
print("ReLU Output Activations:", relu_out)
```
