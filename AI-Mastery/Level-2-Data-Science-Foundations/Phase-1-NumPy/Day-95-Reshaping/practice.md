# Day 95 Practice Questions: Reshaping

## Level 1 — Basic
1. Does `arr.reshape()` modify the array in-place or return a new object?
2. What function flattens a 2D matrix to 1D while returning a zero-copy view?
3. What property shortcut computes the transpose of a 2D matrix `m`?
4. True or False: `v.T` converts 1D array of shape `(5,)` to `(5, 1)`.
5. What function swaps two specific axes of a tensor?

## Level 2 — Coding
6. Reshape `np.arange(12)` into a 3D tensor of shape `(2, 2, 3)`.
7. Flatten a 3D tensor of shape `(2, 3, 4)` into a 1D vector using `ravel()`.
8. Transpose a matrix `m` of shape `(4, 5)` to shape `(5, 4)`.
9. Convert 1D vector `v = np.arange(4)` into a 2D column vector using `reshape()`.
10. Given tensor of shape `(10, 3, 32, 32)`, permute axes to shape `(10, 32, 32, 3)`.

## Level 3 — Data Analysis
11. Predict output shape of `m.T` for `m` of shape `(10, 1)`.
12. Why does `arr.reshape(5, 5)` fail when `arr.size = 20`?
13. Explain why `np.shares_memory(m, m.flatten())` returns `False`.
14. Predict shape of `np.zeros((2, 3, 4)).swapaxes(1, 2)`.
15. Predict output: `a = np.array([[1, 2], [3, 4]]); print(a.ravel())`.

## Level 4 — Debugging
16. Fix error: `AttributeError: 'tuple' object has no attribute 'reshape'`.
17. Fix non-contiguous reshape error: `ValueError: cannot reshape array of size 6 into shape (2,3) without copying`.
18. Fix bug where transposing 1D vector `v = np.array([1,2,3]); v = v.T` fails to create a column vector.

## Level 5 — AI/ML Application
19. How do you flatten spatial activation feature maps of shape `(Batch, Channels, H, W)` into `(Batch, Channels * H * W)`?
20. Why do PyTorch and TensorFlow require specific axis ordering `(NCHW vs NHWC)`?
21. Connect tensor reshaping to batch processing in deep learning models.

## Level 6 — Interview Questions
22. Explain memory layout changes during C-order (`order='C'`) vs F-order (`order='F'`) reshaping.
23. Why does transposing a 2D matrix make it non-contiguous in memory?
24. What does `np.ascontiguousarray()` do under the hood?
25. Demonstrate how `swapaxes()` can be implemented using `transpose()`.
26. How does memory stride recalculation allow zero-copy tensor axis transposition?
