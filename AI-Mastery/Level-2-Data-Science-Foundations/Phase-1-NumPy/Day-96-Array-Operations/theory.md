# Day 96 Theory: Array Operations

### 1. What Is It?
Array operations are vectorized mathematical, comparison, or logical functions applied simultaneously to every individual element in an `ndarray`.

### 2. Why Does It Exist?
Iterating element-by-element using Python `for` loops is slow. Array operations execute C-compiled SIMD vector instructions across contiguous RAM blocks.

### 3. Intuition
Instead of adding numbers one by one by hand, an element-wise array operation is like pressing a single button that instantly adds 5 to every cell in a 1,000-row spreadsheet.

### 4. Syntax
```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise addition
c = a + b # [5, 7, 9]

# Element-wise Hadamard multiplication
d = a * b # [4, 10, 18]

# In-place addition
a += 10 # [11, 12, 13]
```

### 5. Parameters
- `out`: Optional output array parameter in ufuncs to store results without allocating new memory.

### 6. How It Works
NumPy delegates operations to C ufuncs (Universal Functions). The C loop iterates down the contiguous array buffer, applying hardware instruction registers directly.

### 7. Simple Example
```python
import numpy as np
x = np.array([10, 20, 30])
print(x / 10) # [1. 2. 3.]
```

### 8. Intermediate Example
```python
import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Hadamard Product (A * B):
", A * B)
print("Matrix Product (A @ B):   
", A @ B)
```

### 9. Output Interpretation
`A * B` multiplies matching entries $(1	imes 5=5, 2	imes 6=12)$. `A @ B` computes formal linear algebra matrix dot product.

### 10. Common Mistakes
- Using `*` when matrix dot product `@` is intended.
- Mixing incompatible array shapes that fail broadcasting rules.

### 11. Data Science Connection
Column-wise math in Pandas DataFrames (e.g. `df['total'] = df['price'] * df['qty']`) compiles directly to NumPy ufunc array operations.

### 12. AI/ML Connection
Computing Mean Squared Error (MSE) loss: $	ext{MSE} = \frac{1}{N} \sum (y_{	ext{pred}} - y_{	ext{true}})^2$ uses element-wise subtraction, squaring, and mean reduction.

### 13. Interview Insight
Question: "What is the difference between `A * B` and `np.dot(A, B)` in NumPy?"
Answer: `A * B` performs element-wise (Hadamard) multiplication requiring matching shapes. `np.dot(A, B)` or `A @ B` performs formal linear algebra matrix multiplication requiring matching inner dimensions.

### 14. Summary
NumPy operators perform element-wise ufunc execution. Use `*` for Hadamard element-wise multiplication and `@` for matrix multiplication.
