# Day 93 Practice Questions: Slicing

## Level 1 — Basic
1. What is the default `start` value in a slice `arr[:stop]`?
2. How do you slice an array to reverse its element order?
3. True or False: Slicing an array creates an independent memory copy.
4. What syntax extracts all rows of a 2D matrix?
5. What does `matrix[::2, ::2]` extract?

## Level 2 — Coding
6. Given 1D array `a = np.arange(10)`, extract elements at indices `3, 4, 5`.
7. Given 2D matrix `m = np.arange(16).reshape(4, 4)`, extract the 2x2 bottom-right sub-matrix.
8. Extract the last column of a 2D matrix as a 2D column vector of shape `(N, 1)`.
9. Reverse the row order of a 2D matrix without changing column order.
10. Given 3D tensor of shape `(10, 32, 32)`, extract the first 5 samples along axis 0.

## Level 3 — Data Analysis
11. Predict output shape of `m[1:3, 2:4]` for `m` of shape `(5, 5)`.
12. Predict output of `np.array([1, 2, 3, 4, 5])[1:-1]`.
13. Explain why modifying `sub = m[:2, :2]; sub[0, 0] = 0` changes `m[0, 0]`.
14. Predict shape of `matrix[:, -1]`.
15. Predict shape of `matrix[:, -1:]`.

## Level 4 — Debugging
16. Fix bug where developer intended to copy sliced data but accidentally mutated original array.
17. Fix shape mismatch bug when assigning a 1D slice into a 2D column subset.
18. Fix error: `IndexError: slice index out of bounds` (Wait, does slicing raise IndexError for out-of-bound indices?).

## Level 5 — AI/ML Application
19. How do you split a dataset array of shape `(1000, 10)` into 80% train and 20% test slices?
20. In time series processing, how to extract a sliding window of length 10 ending at index $t$?
21. Connect 2D slicing to spatial ROI extraction in computer vision pipelines.

## Level 6 — Interview Questions
22. How does NumPy compute new stride values when step size is $> 1$ (e.g. `arr[::2]`)?
23. Explain why slicing out-of-bounds indices (e.g. `arr[0:100]` for size 10) does NOT raise an `IndexError`.
24. How do negative steps (e.g. `arr[5:1:-1]`) affect `start` and `stop` index interpretations?
25. Demonstrate how to create a 2D view with reversed rows and normal columns.
26. Compare performance between sliced view iteration vs list comprehension copying.
