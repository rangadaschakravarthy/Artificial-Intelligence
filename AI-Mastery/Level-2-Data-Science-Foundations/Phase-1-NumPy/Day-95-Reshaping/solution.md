# Day 95 Solutions: Reshaping

## Level 1 — Basic
1. Returns a new reshaped array object (view if possible).
2. `arr.ravel()`
3. `m.T`
4. False (`(5,)` transposed remains `(5,)`).
5. `np.swapaxes(arr, axis1, axis2)`

## Level 2 — Coding
6. `arr = np.arange(12).reshape(2, 2, 3)`
7. `v = tensor.ravel()`
8. `m_t = m.T`
9. `col = v.reshape(-1, 1)`
10. `permuted = tensor.transpose(0, 2, 3, 1)`

## Level 3 — Data Analysis
11. `(1, 10)`
12. Total elements must match ($5 	imes 5 = 25 
eq 20$).
13. `flatten()` explicitly allocates a new independent memory buffer copy.
14. `(2, 4, 3)`
15. `[1, 2, 3, 4]`

## Level 4 — Debugging
16. You called `.reshape()` on a Python tuple. Convert tuple to NumPy array first: `np.array(tup).reshape(...)`.
17. Call `np.ascontiguousarray(arr).reshape(2, 3)` or allow copying.
18. Expand 1D vector to 2D first: `v = v[:, np.newaxis]` or `v = v.reshape(-1, 1)`.

## Level 5 — AI/ML Application
19. `flat_batch = features.reshape(features.shape[0], -1)`
20. Hardware accelerator memory access patterns. PyTorch optimizes for channels-first (`NCHW`) CUDA memory indexing; TensorFlow CPU optimized for `NHWC`.
21. Batched matrix multiplication requires aligning sample inputs into uniform 2D/3D tensor grids.

## Level 6 — Interview Solutions
22. `order='C'` fills elements row-by-row (last axis index changes fastest). `order='F'` fills elements column-by-column (first axis index changes fastest).
23. Transposing swaps stride tuple values without moving memory bytes. Consecutive elements in rows are no longer contiguous in RAM bytes.
24. `np.ascontiguousarray()` allocates a new C-contiguous memory buffer and copies non-contiguous element data into sequential RAM addresses.
25. For $N$-dim tensor, `swapaxes(a1, a2)` is equivalent to `transpose(perm)` where `perm` swaps indices `a1` and `a2` in range `0..N-1`.
26. Transposition updates shape and stride metadata tuples in $O(1)$ time while leaving underlying byte addresses untouched.
