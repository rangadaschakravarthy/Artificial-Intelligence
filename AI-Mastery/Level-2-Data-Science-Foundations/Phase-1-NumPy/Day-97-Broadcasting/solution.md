# Day 97 Solutions: Broadcasting

## Level 1 — Basic
1. 1) Pad 1s to left of smaller rank array. 2) Dimensions match if equal OR if one of them is `1`.
2. Yes (Scalar is padded to `(1, 1)` and expanded to `(4, 3)`).
3. `(5, 4)`
4. False (Broadcasting sets stride to 0 for length-1 dimensions, performing zero-copy arithmetic).
5. Right-to-left (trailing dimensions first).

## Level 2 — Coding
6. `res = M - v`
7. `res = M - v[:, np.newaxis]`
8. `(10, 5, 1)` and `(1, 5, 4)` -> Dim 2: $1 \to 4$; Dim 1: $5 == 5$; Dim 0: $1 \to 10$. Compatible! Output `(10, 5, 4)`.
9. 
```python
a = np.arange(1, 6)
grid = a[:, None] * a[None, :]
```
10. `res = tensor + v` -> Output shape `(2, 4, 3)`.

## Level 3 — Data Analysis
11. `(4, 3, 5)`
12. Trailing dimensions check $3 
\neq 4$. NumPy checks right-to-left, attempting to match 3 with 4.
13. Reshape `(4,)` to column vector `(4, 1)` using `vec[:, np.newaxis]`.
14. `(10, 20)`
15. `array([[11, 21], [12, 22]])`

## Level 4 — Debugging
16. Convert 1D vector `(4,)` to column vector shape `(4, 1)` using `v[:, np.newaxis]`.
17. Ensure `keepdims=True` is set on sums: `row_sums = M.sum(axis=1, keepdims=True); M / row_sums`.
18. Replace `np.tile(v, (N, 1))` with simple zero-copy broadcasting `M + v`.

## Level 5 — AI/ML Application
19. `normalized_batch = batch - channel_means` (Where `channel_means` has shape `(3,)` matching trailing dimension 3).
20. `x_stable = x - x.max(axis=1, keepdims=True)` (keepdims maintains 2D shape `(N, 1)` for row-wise broadcasting).
21. Expand $X$ to `(N, 1, D)` and $Y$ to `(1, M, D)`. Difference `X[:, None, :] - Y[None, :, :]` broadcasts to `(N, M, D)`.

## Level 6 — Interview Solutions
22. NumPy sets the stride of the expanded dimension to `0`. When iterating, the pointer index increments by $0 	imes 	ext{bytes} = 0$, reusing the same RAM memory cell.
23. `np.broadcast_to()` creates a zero-copy read-only view. `np.tile()` physically duplicates RAM bytes to construct a new array copy.
24. Right-to-left alignment aligns with C-contiguous row-major layout where the last axis index changes fastest in contiguous memory addresses.
25. `np.ogrid[0:3, 0:3]` returns column `(3, 1)` and row `(1, 3)` arrays that broadcast together to form 2D coordinate grids.
26. Memory usage remains $O(1)$ overhead, but total floating-point operations scale to the full broadcast output shape size.
