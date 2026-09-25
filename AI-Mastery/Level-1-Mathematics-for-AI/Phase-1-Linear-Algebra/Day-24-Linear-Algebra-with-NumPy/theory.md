# Theory — Linear Algebra with NumPy

### 1. Simple Definition
NumPy is a Python library that executes linear algebra operations in compiled C/Fortran code using optimized hardware vector instructions (SIMD) and BLAS libraries.

### 2. Intuition
Python loops are like a single worker inspecting each item one-by-one. NumPy vectorization is like an automated factory assembly line loading and processing entire arrays simultaneously in memory.

### 3. Mathematical Definition
NumPy arrays (`ndarray`) store homogenous typed data in contiguous memory blocks. Array shape and stride tuples $(s_0, s_1, \dots, s_d)$ define byte offsets needed to step between elements across dimensions.

### 4. Notation
`np.array()`, `np.dot()`, `A @ B`, `np.linalg.solve(A, b)`, `np.linalg.svd(A)`.

### 5. Formula
$$\text{Speedup} = \frac{\text{Execution Time}_{Python Loop}}{\text{Execution Time}_{NumPy Vectorized}} \approx 50x - 200x$$

### 6. Symbol-by-Symbol Explanation
- `ndarray`: Homogeneous N-dimensional array
- `strides`: Tuple of bytes to step along each dimension
- BLAS: Basic Linear Algebra Subprograms (C/Fortran backend)

### 7. Step-by-Step Calculation
Benchmark vector addition of 1,000,000 numbers:
- Pure Python `for` loop: ~120 ms
- NumPy `a + b` vectorized: ~0.8 ms
$$\text{Speedup} = \frac{120}{0.8} = 150x \text{ faster!}$$

### 8. Second Example
Solve $A x = b$ using `np.linalg.solve(A, b)`: Uses LAPACK `gesv` (LU decomposition with partial pivoting) in $O(n^3)$ operations with optimal CPU cache usage.

### 9. Common Mistakes
Writing explicit Python `for` loops over NumPy arrays (completely defeats vectorization benefits!); using `np.matrix` class instead of standard 2D `ndarray`.

### 10. AI Connection
PyTorch tensors share memory layouts and array syntax directly with NumPy (`torch.from_numpy()`, `tensor.numpy()`). Modern LLM libraries interface seamlessly with NumPy memory buffers.

### 11. Algorithm Connection
NumPy, PyTorch, SciPy, Scikit-Learn, Pandas, CuPy (GPU NumPy).

### 12. Practical Interpretation
Vectorization removes Python interpreter loop overhead, type checking, and object boxing per element.

### 13. Interview Insight
Q: 'How does NumPy achieve C-like performance in Python?' A: 1) Contiguous memory allocation, 2) Homogeneous data types avoiding dynamic dispatch, 3) Compiled C loops leveraging CPU SIMD vector units, 4) Multithreaded BLAS/MKL libraries.

### 14. Summary
NumPy vectorizes linear algebra operations via contiguous C arrays and BLAS/LAPACK libraries, executing operations 100x+ faster than pure Python.
