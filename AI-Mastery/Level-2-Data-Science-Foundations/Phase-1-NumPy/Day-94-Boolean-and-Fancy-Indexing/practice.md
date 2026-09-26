# Day 94 Practice Questions: Boolean and Fancy Indexing

## Level 1 — Basic
1. What data type does a boolean mask contain?
2. Which operator represents element-wise AND in NumPy?
3. Which operator represents element-wise NOT in NumPy?
4. True or False: `arr[arr > 5]` returns a memory view of `arr`.
5. How do you select rows 0, 2, and 4 from a matrix `m` using fancy indexing?

## Level 2 — Coding
6. Given `a = np.array([1, 5, 10, 15, 20])`, extract all elements greater than 10.
7. Replace all odd numbers in `np.array([1, 2, 3, 4, 5, 6])` with `-1`.
8. Given `a = np.arange(10)`, filter values that are even AND greater than 4.
9. Extract elements at diagonal indices `(0,0)`, `(1,1)`, `(2,2)` from 3x3 matrix `m` using fancy indexing.
10. Use `np.where()` to get indices where `a = np.array([10, 50, 20, 80])` is greater than 30.

## Level 3 — Data Analysis
11. Predict output of `a = np.array([1, 2, 3]); b = a[a > 1]; b[0] = 99; print(a[0])`.
12. Why does `(arr > 5) and (arr < 10)` throw a `ValueError`?
13. Predict output: `a = np.array([10, 20, 30]); print(a[[2, 0, 1]])`.
14. Predict output shape of `m[[0, 1], [0, 1]]` for 3x3 matrix `m`.
15. Predict output: `a = np.array([5, 10, 15]); a[a > 10] = 0; print(a)`.

## Level 4 — Debugging
16. Fix error: `ValueError: truth value of an Array with more than one element is ambiguous`.
17. Fix operator precedence error: `arr > 5 & arr < 10`.
18. Fix shape error when applying a boolean mask of length 5 to an array of length 10.

## Level 5 — AI/ML Application
19. How do you filter out samples where feature column 0 is `NaN` (`np.isnan(X[:, 0])`)?
20. In classification, how to separate dataset rows into class 0 matrix `X_class0` and class 1 matrix `X_class1`?
21. Connect fancy indexing to mini-batch random sampling in SGD: `X_batch = X[batch_indices]`.

## Level 6 — Interview Questions
22. Explain why bitwise operators (`&`, `|`, `~`) are overloaded in NumPy for element-wise booleans.
23. Contrast memory allocation behavior between Slicing vs Fancy Indexing.
24. How does `np.where(condition, x, y)` differ from simple boolean array masking `arr[mask]`?
25. Explain pairwise coordinate matching vs grid cross-product matching in 2D fancy indexing.
26. How does boolean masking execute under the hood using C SIMD mask registers?
