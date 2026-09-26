# Day 88 Theory: Array Dimensions

### 1. What Is It?
Array dimensions (axes) specify the orthogonal directions along which array elements are indexed and aggregated. An array's rank is its total number of dimensions (`ndim`).

### 2. Why Does It Exist?
Data naturally has different dimensionality. A single number is 0D, a list of features is 1D, a table is 2D, a video or image batch is 3D/4D. Dimensions provide axis-aligned structure.

### 3. Intuition
In a 2D table:
- `axis=0`: Collapse across Rows (move vertically downwards).
- `axis=1`: Collapse across Columns (move horizontally rightwards).

### 4. Syntax
```python
import numpy as np

# Expanding dimensions
v = np.array([1, 2, 3]) # Shape (3,)
col_vec = v[:, np.newaxis] # Shape (3, 1)
row_vec = v[np.newaxis, :] # Shape (1, 3)

# Squeezing dimensions
sq = np.squeeze(col_vec) # Shape (3,)
```

### 5. Parameters
- `axis`: Integer or tuple of integers specifying target reduction axes.
- `np.newaxis`: Alias for `None` used in slicing to insert a new length-1 axis.

### 6. How It Works
When you perform `arr.sum(axis=0)` on a 2D shape `(R, C)` array, NumPy iterates down the rows, collapsing dimension 0 and outputting a 1D result of shape `(C,)`.

### 7. Simple Example
```python
import numpy as np
arr = np.array([[1, 2], [3, 4]])
print("Sum axis 0 (down rows):", arr.sum(axis=0)) # [4, 6]
print("Sum axis 1 (across cols):", arr.sum(axis=1)) # [3, 7]
```

### 8. Intermediate Example
```python
import numpy as np
x = np.ones((2, 3, 4))
print("Summing over axis=(0, 2):", x.sum(axis=(0, 2)).shape) # Shape (3,)
```

### 9. Output Interpretation
Summing over axes `(0, 2)` collapses dimensions 0 and 2, leaving only dimension 1 (size 3).

### 10. Common Mistakes
- Confusing 1D vector shape `(N,)` with 2D column vector shape `(N, 1)`.
- Reversing axis indices when computing row vs column means.

### 11. Data Science Connection
Grouping, aggregating, and pivot table operations in Pandas operate directly along specified axis dimensions.

### 12. AI/ML Connection
Broadcasting matrix-vector operations $Y = XW + b$ requires matching feature dimensions between 2D matrices $(N, D)$ and 1D bias vectors $(D,)$.

### 13. Interview Insight
Question: "What is the difference between an array of shape `(5,)` and an array of shape `(5, 1)`?"
Answer: `(5,)` is a 1D vector with 1 axis. `(5, 1)` is a 2D matrix (column vector) with 2 axes. Linear algebra operations treat them differently during matrix multiplication.

### 14. Summary
Dimensions structure tensor axes. Master `axis=0` (rows) vs `axis=1` (columns) and dimension expansion (`newaxis`) to ensure seamless ML model compatibility.
