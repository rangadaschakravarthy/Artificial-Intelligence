# Day 88 Solutions: Array Dimensions

## Level 1 — Basic
1. `2`
2. `axis=0` (vertical movement down rows).
3. Removes all single-dimensional (length-1) entries from array shape.
4. False (It converts it into a 2D **column** vector of shape `(N, 1)`).
5. `(1, 1, 1)`

## Level 2 — Coding
6. `a_row = a[np.newaxis, :]`
7. `a_col = np.expand_dims(a, axis=1)`
8. `squeezed = np.squeeze(arr)` -> Shape `(10,)`.
9. `row_sums = m.sum(axis=1)`
10. `col_maxes = m.max(axis=0)`

## Level 3 — Data Analysis
11. `(50,)`
12. `(5,)` (Axes 0 and 2 are collapsed, leaving dimension 1 of size 5).
13. `a` is 1D `(5,)`, `b` is 2D `(1, 5)`. Inner matrix dimensions don't match ($5 
\neq 1$).
14. 2 axes (axis 1 and axis 2).
15. `(1, 10, 1)`

## Level 4 — Debugging
16. Promote 1D vector to 2D: `x_2d = x.reshape(1, -1)` or `x[np.newaxis, :]`.
17. A 2D array only has valid axes `0` and `1`. Change `axis=2` to valid axis or check array `ndim`.
18. Use explicit axis specification: `np.squeeze(arr, axis=2)` or slice `arr[0]` to retain intended rank.

## Level 5 — AI/ML Application
19. ML estimators expect input shape `(n_samples, n_features)`. A 1D vector has 0 sample dimension.
20. Sum/mean across class probabilities (`axis=1`) computes per-sample loss; mean across batch (`axis=0`) computes total batch loss.
21. Accumulating loss gradients across samples collapses batch axis `0`, leaving feature parameter gradient vector matching weight shapes.

## Level 6 — Interview Solutions
22. `np.newaxis` sets stride value of the new dimension to `0` and shape to `1`, creating zero-copy pointer view.
23. Standard reduction collapses target axes (`shape (3,4) -> (4,)`). `keepdims=True` retains collapsed axes as length-1 dimensions (`shape (3,4) -> (1,4)`).
24. PyTorch uses channels-first (`NCHW`); TensorFlow defaults to channels-last (`NHWC`).
25. `np.expand_dims(arr, axis=pos)` inserts a new dimension at index `pos`.
26. NumPy C-loops iterate over contiguous memory strides, accumulating sum/mean values into output memory buffer accumulator registers.
