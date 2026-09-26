# Day 89 Theory: Array Shape

### 1. What Is It?
Array `.shape` is a tuple of integers that describes the size (number of elements) along each dimension of an `ndarray`.

### 2. Why Does It Exist?
It defines the geometric boundaries of the tensor grid, dictating how 1D memory indices map to multi-dimensional coordinate spaces.

### 3. Intuition
Shape is the blueprint or footprint of your data container. Shape `(3, 4)` means a building with 3 floors (rows) and 4 rooms per floor (columns).

### 4. Syntax
```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape) # (2, 3)

# Reshaping
reshaped = arr.reshape(3, 2)
```

### 5. Parameters
- `shape`: Tuple of integers.
- `-1` in reshape: Automatic dimension inference parameter.

### 6. How It Works
The total number of elements (`size`) in an array is equal to the product of all elements in its shape tuple:
$$	ext{size} = \prod_{i=0}^{N-1} 	ext{shape}[i]$$

### 7. Simple Example
```python
import numpy as np
a = np.zeros((4, 5))
print("Shape:", a.shape) # (4, 5)
print("Total Size:", a.size) # 20
```

### 8. Intermediate Example
```python
import numpy as np
b = np.arange(12) # Size 12
b_2d = b.reshape(3, -1) # Infers 12 / 3 = 4 columns!
print("Inferred Shape:", b_2d.shape) # (3, 4)
```

### 9. Output Interpretation
Using `-1` allows NumPy to automatically compute the missing dimension such that total size remains constant ($3 	imes 4 = 12$).

### 10. Common Mistakes
- Reshaping to an incompatible size (e.g., trying to reshape 10 elements into `(3, 3)` which requires 9 elements).
- Confusing shape mutation `arr.shape = (3, 2)` (in-place) with `arr.reshape(3, 2)` (returns a view).

### 11. Data Science Connection
DataFrame `.shape` returns `(n_rows, n_cols)` representing observations and feature variables.

### 12. AI/ML Connection
Matrix multiplication $A_{(m 	imes n)} \cdot B_{(n 	imes p)} = C_{(m 	imes p)}$ strictly requires matching inner shape dimensions ($n$).

### 13. Interview Insight
Question: "How does NumPy handle the `-1` wildcard in `reshape()`?"
Answer: NumPy calculates the product of all specified dimensions $P$, divides the array total `size` $S$ by $P$, and assigns the quotient $S / P$ to the wildcard dimension.

### 14. Summary
Array shape defines tensor geometry. Total size must be preserved during shape transformations, and matrix operations require strict shape alignment.
