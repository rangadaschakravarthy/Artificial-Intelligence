# Day 91 Theory: Array Creation

### 1. What Is It?
NumPy array creation routines are built-in functions that allocate and populate new `ndarray` objects without manually constructing Python lists.

### 2. Why Does It Exist?
Manually converting Python loops or list comprehensions into arrays is slow. Creation routines allocate contiguous RAM buffers instantly at C-speed.

### 3. Intuition
Instead of hand-drawing a grid cell by cell, creation routines are pre-built rubber stamps that instantly print 1,000 zeros, an identity matrix, or a smooth line of numbers.

### 4. Syntax
```python
import numpy as np

z = np.zeros((3, 3))
o = np.ones((2, 4), dtype=np.float32)
f = np.full((2, 2), 7.0)
r = np.arange(0, 10, 2)       # [start, stop), step
l = np.linspace(0, 1, 5)       # [start, stop], num_points
i = np.eye(3)                  # Identity 3x3
```

### 5. Parameters
- `shape`: Tuple of dimensions.
- `step` (in `arange`): Distance between consecutive values.
- `num` (in `linspace`): Total number of evenly spaced samples generated (includes endpoint by default).

### 6. How It Works
- `zeros`/`ones`: Allocates buffer and sets memory bytes using `memset`.
- `empty`: Allocates memory buffer **without** initializing byte values (contains whatever residual garbage was in RAM).

### 7. Simple Example
```python
import numpy as np
seq = np.linspace(0.0, 1.0, 5)
print(seq) # [0.   0.25 0.5  0.75 1.  ]
```

### 8. Intermediate Example
```python
import numpy as np
base = np.array([[1, 2], [3, 4]])
mask = np.zeros_like(base, dtype=bool)
print("Zeros Like Mask:
", mask)
```

### 9. Output Interpretation
`zeros_like` creates an array with identical shape and memory geometry as `base`, but with user-specified boolean dtype.

### 10. Common Mistakes
- Expecting `np.arange(0, 1, 0.1)` to accurately include `1.0` (floating point step issues; use `np.linspace` for floating sequences!).
- Reading values from `np.empty()` assuming they will default to zero (they contain random memory garbage!).

### 11. Data Science Connection
Creating baseline prediction arrays, synthetic test grids, and initial feature matrices during exploratory data analysis.

### 12. AI/ML Connection
Initializing bias vectors $b = \mathbf{0}$, identity regularizers $I$, and evaluation grids for decision boundary contour plots.

### 13. Interview Insight
Question: "When should you use `np.arange` versus `np.linspace`?"
Answer: Use `np.arange` when you know the desired integer **step size**. Use `np.linspace` when you know the exact **number of points** required or when working with floating-point endpoints.

### 14. Summary
Array creation routines quickly generate structured tensors. Match `arange` for step-based ranges and `linspace` for fixed-sample continuous intervals.
