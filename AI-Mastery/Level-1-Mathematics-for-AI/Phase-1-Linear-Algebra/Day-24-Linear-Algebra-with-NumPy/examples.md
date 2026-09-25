# Examples — Linear Algebra with NumPy

## Example 1 — Very Easy
Vectorized Addition: `c = a + b` instead of `for i in range(N): c[i] = a[i] + b[i]`.

## Example 2 — Beginner
MatMul: `C = A @ B` calling BLAS `gemm` routine.

## Example 3 — Intermediate
Solving Linear System: `x = np.linalg.solve(A, b)`.

## Example 4 — AI/ML Example
SVD: `U, S, Vt = np.linalg.svd(A)`.

## Example 5 — Real-World Interpretation
Memory Strides Inspection: `arr.strides` showing byte step counts.
