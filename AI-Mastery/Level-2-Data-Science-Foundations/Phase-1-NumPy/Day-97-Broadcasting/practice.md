# Day 97 Practice Questions: Broadcasting

## Level 1 — Basic
1. What are the two rules for NumPy shape broadcasting compatibility?
2. Can an array of shape `(4, 3)` be broadcast with a scalar?
3. What is the output shape of adding array `(5, 1)` and array `(1, 4)`?
4. True or False: Broadcasting physically duplicates array data in memory.
5. In what direction (left-to-right or right-to-left) does NumPy compare shape dimensions?

## Level 2 — Coding
6. Given matrix `M` of shape `(3, 4)`, subtract 1D vector `v` of shape `(4,)` row-wise.
7. Given matrix `M` of shape `(3, 4)`, subtract 1D vector `v` of shape `(3,)` column-wise using `newaxis`.
8. Check if shapes `(10, 5, 1)` and `(5, 4)` are broadcast compatible.
9. Create a multiplication table grid of size 5x5 using broadcasting `a[:, None] * b[None, :]`.
10. Given 3D tensor of shape `(2, 4, 3)` and 1D vector of shape `(3,)`, compute their element-wise sum.

## Level 3 — Data Analysis
11. Predict output shape of `np.ones((4, 1, 5)) + np.ones((3, 5))`.
12. Why does `np.ones((4, 3)) + np.ones((4,))` raise a `ValueError`?
13. How do you modify `np.ones((4,))` so it broadcasts cleanly with `np.ones((4, 3))`?
14. Predict output shape of `np.zeros((10, 1)) * np.zeros((1, 20))`.
15. Predict output: `a = np.array([[1], [2]]); b = np.array([10, 20]); print(a + b)`.

## Level 4 — Debugging
16. Fix error: `ValueError: operands could not be broadcast together with shapes (4,3) (4,)`.
17. Fix bug where row normalization divided by column sums along wrong axis.
18. Fix issue where developer used explicit `np.tile()` loop instead of zero-copy broadcasting.

## Level 5 — AI/ML Application
19. How do you subtract per-channel mean `(3,)` from image batch tensor `(32, 28, 28, 3)`?
20. In Softmax activation, how to subtract batch row maximums `max(axis=1, keepdims=True)` to prevent exponent overflow?
21. Connect broadcasting to pair-wise distance matrix calculation $D_{ij} = \|x_i - y_j\|^2$.

## Level 6 — Interview Questions
22. How does NumPy perform stride manipulations to achieve zero-copy memory broadcasting?
23. Contrast `np.broadcast_to()` vs `np.tile()`.
24. Explain why broadcasting right-to-left dimension padding convention matches C-contiguous storage.
25. Demonstrate how `np.ogrid` and `np.mgrid` utilize broadcasting for grid generation.
26. What are the performance and memory implications of broadcasting very high-dimensional arrays?
