# Day 87 Theory: NumPy Arrays

### 1. What Is It?
An `ndarray` is a multidimensional container holding homogeneous elements. Structurally, it consists of a contiguous 1D raw memory buffer paired with metadata (shape, dtype, strides) that dictates how the multi-dimensional structure is interpreted.

### 2. Why Does It Exist?
It allows high-dimensional mathematical data (tensors) to be manipulated efficiently without copying underlying memory bytes during operations like transpose, slicing, or reshaping.

### 3. Intuition
Imagine a long ribbon of numbers printed on paper (the 1D memory buffer). The `ndarray` metadata is a pair of 3D glasses that projects that ribbon into a 3D cube or 2D spreadsheet without moving the physical numbers on the ribbon.

### 4. Syntax
```python
import numpy as np

# 0D Scalar
s = np.array(42)

# 1D Vector
v = np.array([1, 2, 3])

# 2D Matrix
m = np.array([[1, 2], [3, 4]])

# 3D Tensor
t = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
```

### 5. Parameters
- `flags`: Metadata attributes describing memory alignment (`c_contiguous`, `owndata`).
- `strides`: Tuple indicating byte steps needed to move one index forward in each dimension.

### 6. How It Works
Index calculation for element $A[i, j]$ in a 2D matrix of shape $(R, C)$ with strides $(s_0, s_1)$:
$$	ext{Byte Address} = 	ext{Base Address} + (i 	imes s_0) + (j 	imes s_1)$$

### 7. Simple Example
```python
import numpy as np
a = np.array([[10, 20], [30, 40]], dtype=np.int64)
print("Strides:", a.strides) # (16, 8) bytes
```

### 8. Intermediate Example
```python
import numpy as np
b = a.T # Transpose creates a view with swapped strides!
print("Original Strides:", a.strides) # (16, 8)
print("Transposed Strides:", b.strides) # (8, 16)
print("Shares Memory?", np.shares_memory(a, b)) # True
```

### 9. Output Interpretation
Transposing an array swaps strides without modifying the raw C-buffer, executing an instantaneous $O(1)$ operation!

### 10. Common Mistakes
- Modifying a slice thinking it is an isolated copy (`b = a[0]; b[0] = 999` mutates `a`!).
- Creating non-contiguous arrays that slow down downstream linear algebra libraries.

### 11. Data Science Connection
Pandas DataFrames manage 2D collections of column ndarrays. Data views make column selection zero-copy fast.

### 12. AI/ML Connection
Deep Learning tensors in PyTorch (`torch.Tensor`) mirror NumPy ndarray stride and memory layout architecture exactly (`torch.from_numpy`).

### 13. Interview Insight
Question: "What is the difference between an array view and an array copy?"
Answer: A view shares the underlying memory buffer with the original array (zero memory cost, mutations reflect in both). A copy allocates a fresh memory buffer (allocates RAM, independent modifications).

### 14. Summary
An `ndarray` pairs a 1D contiguous memory buffer with shape and stride metadata to deliver flexible zero-copy multidimensional tensor transformations.
