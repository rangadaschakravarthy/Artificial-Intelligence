# Day 98 Worked Examples: Vectorization

## Example 1 — Beginner: Loop vs Vectorized Square Operation
```python
import numpy as np
import time

size = 5_000_000
data_list = list(range(size))
data_arr = np.arange(size)

# Non-vectorized Python Loop
t0 = time.time()
loop_res = [x**2 for x in data_list]
t_loop = time.time() - t0

# Vectorized NumPy Operation
t0 = time.time()
vec_res = data_arr ** 2
t_vec = time.time() - t0

print(f"Loop Time:       {t_loop:.4f}s")
print(f"Vectorized Time: {t_vec:.4f}s")
print(f"Vectorization Speedup: {t_loop / t_vec:.1f}x faster!")
```

## Example 2 — Practical: Vectorized Conditional Mapping (np.where)
```python
import numpy as np

values = np.array([-5, 10, -15, 20, -25, 30])

# Non-vectorized: [x if x > 0 else 0 for x in values]
# Vectorized using np.where(condition, if_true, if_false)
relu_values = np.where(values > 0, values, 0)

print("Original Values:  ", values)
print("Vectorized ReLU:  ", relu_values)
```

## Example 3 — Intermediate: Vectorized Pairwise Distance Matrix
```python
import numpy as np

# 3 points in 2D space
P = np.array([[0, 0], [3, 0], [0, 4]])

# Compute pairwise Euclidean distance matrix without loops!
# Shape (3, 1, 2) - Shape (1, 3, 2) -> (3, 3, 2)
diff = P[:, np.newaxis, :] - P[np.newaxis, :, :]
dist_matrix = np.sqrt(np.sum(diff ** 2, axis=-1))

print("Pairwise Distance Matrix:
", np.round(dist_matrix, 2))
```

## Example 4 — Real Dataset: Vectorized Categorical Binning
```python
import numpy as np

# Customer Credit Scores
scores = np.array([550, 720, 640, 810, 590, 750])

# Vectorized binning using np.select
conditions = [
    scores < 600,
    (scores >= 600) & (scores < 700),
    (scores >= 700) & (scores < 800),
    scores >= 800
]
choices = ['Poor', 'Fair', 'Good', 'Excellent']

categories = np.select(conditions, choices, default='Unknown')

print("Scores:    ", scores)
print("Categories:", categories)
```

## Example 5 — AI/ML Application: Vectorized Softmax Function
```python
import numpy as np

# Logits output from final neural network layer for 3 samples, 3 classes
logits = np.array([
    [2.0, 1.0, 0.1],
    [1.0, 3.0, 0.2],
    [0.5, 0.5, 2.0]
])

# Vectorized Softmax: exp(z) / sum(exp(z))
# Subtract max for numerical stability
exp_logits = np.exp(logits - np.max(logits, axis=1, keepdims=True))
softmax_probs = exp_logits / np.sum(exp_logits, axis=1, keepdims=True)

print("Vectorized Softmax Probabilities:
", np.round(softmax_probs, 4))
print("Row Sums (must be 1.0):", np.sum(softmax_probs, axis=1))
```
