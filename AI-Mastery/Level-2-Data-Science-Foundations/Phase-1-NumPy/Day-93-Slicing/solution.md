# Day 93 Solutions: Slicing

## Level 1 — Basic
1. `0`
2. `arr[::-1]`
3. False (Slicing creates a zero-copy view).
4. `:` (e.g. `matrix[:, col_slice]`).
5. Extracts every 2nd row and every 2nd column (subsampled grid).

## Level 2 — Coding
6. `a[3:6]`
7. `m[2:, 2:]`
8. `m[:, -1:]` (or `m[:, [-1]]`).
9. `m[::-1, :]`
10. `tensor[:5, :, :]` (or `tensor[:5]`).

## Level 3 — Data Analysis
11. `(2, 2)` (Rows 1, 2 and Cols 2, 3).
12. `[2, 3, 4]`
13. Slicing returns a view sharing the same memory buffer; mutations propagate to base array.
14. 1D vector of shape `(N,)`.
15. 2D column matrix of shape `(N, 1)`.

## Level 4 — Debugging
16. Call `.copy()` explicitly: `sub = m[:2, :2].copy()`.
17. Reshape 1D slice or use 2D slicing: `matrix[:, 0:1] = new_col_2d`.
18. Slicing in Python/NumPy does **not** raise `IndexError` for out-of-bound indices; it gracefully truncates to available bounds. Check logic if unexpected empty array `[]` is returned.

## Level 5 — AI/ML Application
19. 
```python
train_X = data[:800, :-1]; train_y = data[:800, -1]
test_X = data[800:, :-1];  test_y = data[800:, -1]
```
20. `window = series[t-10:t]`
21. Image cropping $I[y_1:y_2, x_1:x_2]$ extracts spatial pixel patches for object detection bounding boxes.

## Level 6 — Interview Solutions
22. $	ext{New Stride}_i = 	ext{Original Stride}_i 	imes 	ext{step}$.
23. Python slicing design convention clips out-of-bound bounds to $[0, N]$ range instead of throwing exceptions.
24. For negative steps, default `start` becomes $N-1$, default `stop` becomes $-1$ (before index 0), and step moves backward.
25. `m[::-1, :]`
26. Sliced view construction runs in $O(1)$ constant time with zero memory allocation. List comprehension copying takes $O(N)$ time and allocates new memory.
