# Day 92 Theory: Indexing

### 1. What Is It?
Indexing is the process of accessing or mutating individual scalar elements or sub-tensors within an `ndarray` using coordinate index tuples.

### 2. Why Does It Exist?
Data items are located at specific coordinate addresses inside multidimensional tensors. Indexing allows instant $O(1)$ random-access retrieval.

### 3. Intuition
Think of 2D indexing `arr[row, col]` as a grid map coordinate like Battleship (e.g. Row 3, Column 2).

### 4. Syntax
```python
import numpy as np

arr1d = np.array([10, 20, 30])
v = arr1d[0] # First element
last = arr1d[-1] # Last element

arr2d = np.array([[1, 2], [3, 4]])
val = arr2d[1, 0] # Row index 1, Column index 0 -> Value 3
```

### 5. Parameters
- `index`: Integer or tuple of integers corresponding to axes.

### 6. How It Works
For a 2D matrix with strides $(s_0, s_1)$, indexing `arr[i, j]` calculates RAM pointer address directly:
$$	ext{Address} = 	ext{Base} + i \cdot s_0 + j \cdot s_1$$

### 7. Simple Example
```python
import numpy as np
m = np.array([[10, 20], [30, 40]])
print("Top-Right Element:", m[0, 1]) # 20
```

### 8. Intermediate Example
```python
import numpy as np
t = np.arange(8).reshape(2, 2, 2)
print("Tensor Element [1, 0, 1]:", t[1, 0, 1]) # Value 5
```

### 9. Output Interpretation
`t[1, 0, 1]` selects depth 1, row 0, column 1 in the 3D tensor grid.

### 10. Common Mistakes
- Using Python chained indexing `arr[r][c]` instead of efficient NumPy multi-axis indexing `arr[r, c]`. (Chained indexing creates intermediate temporary array objects!).
- Forgetting that index bounds are zero-indexed (`0` to `N-1`).

### 11. Data Science Connection
Pandas `.iloc[row_idx, col_idx]` uses integer indexing identical to NumPy multi-axis indexing syntax.

### 12. AI/ML Connection
Extracting batch sample $i$, channel $c$, pixel $(h, w)$ from image tensors during neural network feature visualization.

### 13. Interview Insight
Question: "Why is `arr[r, c]` preferred over `arr[r][c]` in NumPy?"
Answer: `arr[r, c]` passes a single index tuple to C code, performing a single pointer arithmetic calculation. `arr[r][c]` creates a temporary Python array object for `arr[r]` first, then indexes `[c]`, causing unnecessary object creation overhead.

### 14. Summary
NumPy supports multi-axis comma-separated indexing `arr[i, j, k]`. Negative indices count backward from the array bounds.
