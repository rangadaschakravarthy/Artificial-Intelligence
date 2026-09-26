# Day 88 Practice Questions: Array Dimensions

## Level 1 — Basic
1. What does `ndim` return for a 2D matrix?
2. In a 2D array, which axis corresponds to rows?
3. What is the effect of `np.squeeze()` on an array?
4. True or False: `v[:, np.newaxis]` converts a 1D vector into a 2D row vector.
5. What is the shape of `np.array([[[1]]])`?

## Level 2 — Coding
6. Given 1D array `a = np.arange(5)`, convert it to shape `(1, 5)` using `np.newaxis`.
7. Given 1D array `a = np.arange(5)`, convert it to shape `(5, 1)` using `np.expand_dims`.
8. Given 3D array of shape `(1, 10, 1)`, squeeze all length-1 dimensions.
9. Compute row-wise sums for 2D matrix `m = np.arange(12).reshape(3, 4)`.
10. Compute column-wise max for 2D matrix `m = np.arange(12).reshape(3, 4)`.

## Level 3 — Data Analysis
11. Predict output shape of `arr.sum(axis=1)` for `arr` of shape `(50, 10)`.
12. Predict output shape of `arr.mean(axis=(0, 2))` for `arr` of shape `(4, 5, 6)`.
13. Explain why `np.dot(a, b)` fails when `a` has shape `(5,)` and `b` has shape `(1, 5)`.
14. How many axes are collapsed when performing `a.std(axis=(1, 2))` on a 4D tensor?
15. Predict shape of `x[np.newaxis, :, np.newaxis]` where `x` has shape `(10,)`.

## Level 4 — Debugging
16. Fix error: `ValueError: Expected 2D array, got 1D array instead` when passing feature vector to model.
17. Fix bug: `arr.mean(axis=2)` throws `AxisError: axis 2 is out of bounds for array of dimension 2`.
18. Fix issue where `squeeze()` accidentally removed batch dimension when batch size happened to be 1 (`shape (1, 10)` -> `(10,)`).

## Level 5 — AI/ML Application
19. Why must single test predictions `x` be promoted from `(D,)` to `(1, D)` before inference?
20. Explain axis reduction in calculating Cross-Entropy loss over batch of size $N$ and $K$ classes: `shape (N, K)`.
21. Connect `axis=0` reduction to sample-wise gradient averaging in SGD.

## Level 6 — Interview Questions
22. Explain how `np.newaxis` modifies stride metadata without allocating new RAM memory.
23. What is the distinction between reduction axes and keepdims parameter (`keepdims=True`)?
24. How does axis ordering differ between PyTorch `(B, C, H, W)` and TensorFlow `(B, H, W, C)`?
25. Demonstrate how to insert an axis at an arbitrary position using `np.expand_dims`.
26. How do multi-axis reductions perform under the hood in C loops?
