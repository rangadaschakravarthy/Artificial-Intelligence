# Solutions — Linear Algebra with NumPy

## Level 1 — Basic Understanding Solutions
### Question 1
1. `np.eye(n)`.
### Question 2
2. The `@` operator (`A @ B`).
### Question 3
3. `np.linalg.inv()`, `np.linalg.det()`, `np.linalg.eig()`, `np.linalg.svd()`.
### Question 4
4. Python loops iterate sequentially through dynamic PyObject pointers, incurring interpreter overhead, dynamic type checking, and unaligned memory accesses per element.
### Question 5
5. `arr.shape` for shape tuple, `arr.ndim` for dimension rank count.

## Level 2 — Calculation Solutions
### Question 1
1. `A = np.array([[3, 1], [1, 2]]); b = np.array([9, 8]); x = np.linalg.solve(A, b)`. Output: `[2., 3.]`.
### Question 2
2. `v = np.array([3, 4, 12]); norm = np.linalg.norm(v, 2)`. Output: `13.0`.
### Question 3
3. `evals, evecs = np.linalg.eigh(A)`.
### Question 4
4. `arr_2d = arr_1d.reshape(3, 4)`.
### Question 5
5. `A @ B` (or `np.dot`) performs row-by-column matrix multiplication. `A * B` performs element-wise Hadamard product.

## Level 3 — Conceptual Solutions
### Question 1
1. BLAS (Basic Linear Algebra Subprograms) provides low-level C/Fortran vector/matrix routines. LAPACK (Linear Algebra Package) provides high-level solvers (SVD, Eig, LU, QR). Libraries like Intel MKL and OpenBLAS compile these for specific CPU architectures.
### Question 2
2. `solve(A, b)` uses LU decomposition ($PA = LU$) with partial pivoting ($O(n^3)$ with 3x smaller constant factor), avoiding catastrophic loss of precision caused by explicit matrix inversion.
### Question 3
3. C-contiguous stores rows sequentially in memory (last axis changes fastest). Fortran-contiguous stores columns sequentially (first axis changes fastest).
### Question 4
4. `np.ascontiguousarray()` allocates a fresh contiguous memory block and copies array elements in order, setting `c_contiguous` flag to True.
### Question 5
5. `np.einsum` uses Einstein summation notation to specify multi-dimensional index contractions (e.g. `'ij,jk->ik'` for MatMul, `'ii->'` for Trace).

## Level 4 — AI/ML Application Solutions
### Question 1
1. Pure Python 3-loop matmul for 500x500 matrix takes ~60 seconds. NumPy `A @ B` takes ~0.005 seconds (10,000x faster speedup!).
### Question 2
2. `torch.from_numpy(arr)` wraps the underlying C memory pointer of `arr` in a PyTorch Tensor struct without copying memory. Modifying PyTorch tensor mutates NumPy array.
### Question 3
3. `np.memmap('data.bin', dtype='float32', mode='w+', shape=(100000, 1000))` maps a disk file directly into virtual address space, loading chunks into RAM on demand.

## Level 5 — Interview Questions Solutions
### Question 1
1. SIMD registers (e.g. 512-bit AVX-512) load 8 double-precision (64-bit) floats at once and execute a single fused multiply-add instruction across all 8 numbers in 1 clock cycle.
### Question 2
2. CuPy mirrors NumPy API but executes kernel routines on GPU CUDA cores, achieving 50x-100x speedups over CPU NumPy for large matrices ($N > 2000$).
### Question 3
3. BLAS `gemm` divides matrices into sub-blocks fitting into L1/L2 CPU cache (e.g. 64x64 blocks), ensuring data is reused multiple times from high-speed L1 cache before being evicted.
### Question 4
4. For shape $(m, n)$ with float64 (8 bytes): Row stride $s_0 = n \times 8$ bytes, Column stride $s_1 = 8$ bytes. Strides tuple $= (8n, 8)$.
### Question 5
5. NumPy uses IEEE 754 floating-point standards. Overflow produces `Inf`, invalid operations produce `NaN`. Behavior is controlled via `np.errstate(divide='ignore', invalid='ignore')`.
