# Practice Exercises — Linear Algebra with NumPy

## Level 1 — Basic Understanding
1. What function in NumPy creates an identity matrix?
2. What operator performs matrix multiplication in Python 3.5+?
3. Name 4 core functions inside `np.linalg`.
4. Why are Python `for` loops slow compared to NumPy vectorized operations?
5. How do you check the shape and dimension of a NumPy array `arr`?

## Level 2 — Calculation
1. Write code to solve system \mathbf{A}\mathbf{x} = \mathbf{b} for 

$$\mathbf{A} = \begin{bmatrix} 3 & 1 \\ 1 & 2 \end{bmatrix}$$

 and \mathbf{b} = [9, 8]^T using `np.linalg.solve`.
2. Compute L2 norm of vector `v = np.array([3, 4, 12])` using `np.linalg.norm`.
3. Compute eigenvalues of symmetric matrix using `np.linalg.eigh`.
4. Convert a 1D array of 12 elements into a 3x4 matrix using `.reshape()`.
5. What is the difference between `np.dot(A, B)` and `A * B` in NumPy?

## Level 3 — Conceptual
1. Explain what BLAS and LAPACK are and how NumPy links to them (e.g. OpenBLAS, Intel MKL).
2. Why is `np.linalg.solve(A, b)` numerically more stable and faster than `np.linalg.inv(A) @ b`?
3. Explain C-contiguous memory layout vs Fortran-contiguous memory layout in NumPy arrays (`flags.c_contiguous`).
4. How does `np.ascontiguousarray()` fix non-contiguous array strides after slicing or transpose?
5. What is `np.einsum` and how does it execute arbitrary linear algebra tensor contractions?

## Level 4 — AI/ML Application
1. Write a Python script to benchmark matrix multiplication of two $1000 \times 1000$ matrices comparing pure Python nested loops vs `A @ B`. Record execution times.
2. Explain how PyTorch `torch.from_numpy()` creates a zero-copy tensor sharing memory with NumPy.
3. Demonstrate memory-mapped arrays (`np.memmap`) for processing out-of-core linear algebra datasets larger than RAM.

## Level 5 — Interview Questions
1. Explain CPU SIMD (Single Instruction Multiple Data) instruction sets (AVX-256, AVX-512, ARM Neon) and how BLAS leverages them.
2. Compare NumPy CPU performance against GPU-accelerated array libraries like CuPy and PyTorch.
3. How does cache line prefetching (L1/L2/L3 cache alignment) influence block matrix multiplication algorithms in BLAS `gemm`?
4. Explain Memory Strides math: given 2D array of shape $(m, n)$ and float64 (8 bytes), what are the strides in row-major order?
5. How does NumPy handle IEEE 754 floating-point exceptions (`NaN`, `Inf`, divide-by-zero) in matrix algorithms?
