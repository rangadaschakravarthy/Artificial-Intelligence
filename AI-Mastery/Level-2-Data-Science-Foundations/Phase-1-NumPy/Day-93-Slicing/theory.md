# Day 93 Theory: Slicing

### 1. What Is It?
Slicing extracts a contiguous or step-strided sub-region of an `ndarray` without copying underlying memory bytes.

### 2. Why Does It Exist?
Copying large sub-matrices during data preparation is slow and RAM-intensive. Slicing constructs an $O(1)$ zero-copy memory view with updated shape and stride parameters.

### 3. Intuition
Imagine a photo frame placed over a large newspaper page. Moving or shrinking the frame doesn't reprint the page—it just changes what window of text you are looking at.

### 4. Syntax
```python
import numpy as np

# 1D Slicing: arr[start:stop:step]
arr = np.array([10, 20, 30, 40, 50])
sub1d = arr[1:4] # [20, 30, 40]

# 2D Slicing: matrix[row_slice, col_slice]
m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
sub2d = m[0:2, 1:3] # Top-right 2x2 sub-matrix
```

### 5. Parameters
- `start`: Inclusive starting index (defaults to `0`).
- `stop`: Exclusive stopping index (defaults to length of axis).
- `step`: Increment step size (defaults to `1`).

### 6. How It Works
Slicing updates array metadata:

$$
ext{New Offset} = 	ext{Base Offset} + (	ext{start} 	imes 	ext{stride})
$$

$$	ext{New Shape}_i = \left\lceil \frac{	ext{stop} - 	ext{start}}{	ext{step}} 
ight
ceil, \quad 	ext{New Stride}_i = 	ext{stride}_i 	imes 	ext{step}$$

### 7. Simple Example
```python
import numpy as np
a = np.arange(10)
print(a[::2]) # Even indices: [0, 2, 4, 6, 8]
```

### 8. Intermediate Example
```python
import numpy as np
m = np.arange(12).reshape(3, 4)
col1 = m[:, 1] # Extract column index 1 as 1D array
col1_2d = m[:, 1:2] # Extract column index 1 as 2D column matrix!
print("1D Col Shape:", col1.shape)    # (3,)
print("2D Col Shape:", col1_2d.shape) # (3, 1)
```

### 9. Output Interpretation
Slicing with integer `1` reduces rank (1D). Slicing with range `1:2` preserves matrix rank (2D).

### 10. Common Mistakes
- Expecting `matrix[:, 0]` to return a 2D column vector (it returns a 1D vector of shape `(N,)`!).
- Modifying a slice without realizing it mutates the parent array.

### 11. Data Science Connection
Pandas `.loc[row_slice, col_slice]` and `.iloc[row_slice, col_slice]` rely directly on NumPy 2D slicing semantics.

### 12. AI/ML Connection
Cropping images, extracting temporal time-series windows $[t-k : t]$, and separating $X = 	ext{data}[:, :-1]$ and $y = 	ext{data}[:, -1]$.

### 13. Interview Insight
Question: "What is the difference between `arr[:, 0]` and `arr[:, 0:1]`?"
Answer: `arr[:, 0]` performs integer indexing on column dimension, dropping rank to 1D `(N,)`. `arr[:, 0:1]` performs slice indexing, preserving 2D rank `(N, 1)`.

### 14. Summary
Slicing uses `[start:stop:step]` across dimensions to construct zero-copy views over sub-regions of arrays.
