# Day 89 Solutions: Array Shape

## Level 1 — Basic
1. Tuple of integers.
2. `arr.size` (or `np.prod(arr.shape)`).
3. NumPy automatically infers the length of that dimension based on remaining elements.
4. False (Total size must remain strictly identical).
5. No (Only one unknown dimension can be inferred).

## Level 2 — Coding
6. `arr = np.arange(24).reshape(2, 3, 4)`
7. `v = matrix.reshape(-1)`
8. `np.prod((3,4,5)) == 60 == a.size` -> `True`.
9. 
```python
def can_multiply(A, B):
    return A.ndim == 2 and B.ndim == 2 and A.shape[1] == B.shape[0]
```
10. `t_trans = t.transpose(2, 1, 0)`

## Level 3 — Data Analysis
11. `(10, 2)`
12. 1,000 samples and 30 feature variables.
13. 10 is not divisible by 3 ($10 / 3 = 3.33$, not an integer).
14. `(5, 10)`
15. `(3, 1)`

## Level 4 — Debugging
16. Total size must match: $4 	imes 4 = 16 
\neq 15$. Use compatible dimensions e.g. `(3, 5)` or resize array.
17. Remove second `-1` wildcard parameter in `reshape()` call; specify all other dimensions explicitly.
18. Transpose second matrix: `A @ B.T` so shapes align: `(5, 3) @ (3, 5)` -> `(5, 5)`.

## Level 5 — AI/ML Application
19. `images.reshape(50, -1)` ($64 	imes 64 	imes 3 = 12,288$).
20. Matrix multiplication $(B 	imes I) \cdot (I 	imes O)$ collapses inner dimension $I$, producing output predictions batch $(B 	imes O)$.
21. Flattening bridges 3D feature-map spatial representations from conv layers to 1D linear classification layers.

## Level 6 — Interview Solutions
22. `ravel()` returns a zero-copy 1D view if possible. `flatten()` always allocates a new 1D memory copy.
23. Element index offset = $\sum 	ext{idx}_i 	imes 	ext{stride}_i$. Shape sets index bounds $0 \le 	ext{idx}_i < 	ext{shape}_i$.
24. In-place: `arr.shape = (3, 2)` (mutates original). View: `b = arr.reshape(3, 2)` (returns new view).
25. `transpose()` permutes arbitrary ordering of all axes. `swapaxes()` swaps exactly two specified axes.
26. Non-contiguous strides (e.g. after transpose) set `C_CONTIGUOUS` flag to `False`. Calling `reshape()` on non-contiguous arrays may force a memory copy.
