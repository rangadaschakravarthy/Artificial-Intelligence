# Day 95 Theory: Reshaping

### 1. What Is It?
Reshaping modifies the dimension layout (`shape`) of an array without altering its underlying numerical element values or total element count (`size`).

### 2. Why Does It Exist?
Different mathematical operations and AI algorithms require data structured in specific tensor shapes (e.g. vectors vs matrices vs 4D image batches).

### 3. Intuition
Imagine a deck of 52 playing cards. You can lay them out as 1 line of 52 cards, 4 rows of 13 cards, or 2 piles of 26 cards. The total cards remain 52; only your organizational layout changes.

### 4. Syntax
```python
import numpy as np

arr = np.arange(12)

# Reshape (returns view if contiguous)
r = arr.reshape(3, 4)

# Flattening
f = r.flatten() # 1D Copy
v = r.ravel()   # 1D View

# Transpose
t = r.T # (4, 3)
```

### 5. Parameters
- `newshape`: Integer or tuple of integers.
- `order`: `'C'` (row-major) or `'F'` (column-major memory reading order).

### 6. How It Works
If an array is C-contiguous, `reshape()` simply calculates a new shape and stride tuple without copying RAM bytes ($O(1)$ view). If non-contiguous, `reshape()` allocates a new memory buffer ($O(N)$ copy).

### 7. Simple Example
```python
import numpy as np
a = np.array([1, 2, 3, 4])
b = a.reshape(2, 2)
print(b) # [[1, 2], [3, 4]]
```

### 8. Intermediate Example
```python
import numpy as np
tensor = np.zeros((2, 3, 4))
trans = np.transpose(tensor, (2, 0, 1)) # Permute axes
print("Transposed Shape:", trans.shape) # (4, 2, 3)
```

### 9. Output Interpretation
`np.transpose(tensor, (2, 0, 1))` moves axis 2 to position 0, axis 0 to position 1, and axis 1 to position 2.

### 10. Common Mistakes
- Trying to transpose a 1D vector `v.T` expecting a column vector (transposing a 1D vector `(N,)` does nothing! Use `v[:, np.newaxis]`).
- Confusing in-place `resize()` with `reshape()`.

### 11. Data Science Connection
Pivoting long data tables to wide matrices and flattening multi-index structures in Pandas.

### 12. AI/ML Connection
Flattening 2D feature maps from Convolutional layers before feeding into Dense Fully-Connected layers.

### 13. Interview Insight
Question: "Why does `v.T` fail to convert a 1D vector of shape `(N,)` into a column vector?"
Answer: A 1D vector has only 1 axis (`ndim=1`). Transposing reverses axes order. Since there is only 1 axis, reversing `(0,)` yields `(0,)` unchanged. You must expand dimensions first: `v[:, np.newaxis]`.

### 14. Summary
Reshaping changes shape metadata. `reshape()` and `ravel()` create zero-copy views on contiguous arrays, while `flatten()` makes explicit copies.
