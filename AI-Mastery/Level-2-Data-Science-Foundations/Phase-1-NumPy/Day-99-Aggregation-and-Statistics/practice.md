# Day 99 Practice Questions: Aggregation and Statistics

## Level 1 — Basic
1. What function computes the median of a NumPy array?
2. What does `np.argmax(arr)` return?
3. What is the difference between `ddof=0` and `ddof=1` in `np.var()`?
4. What function computes the peak-to-peak range (`max - min`) of an array?
5. True or False: `np.mean(np.array([1.0, np.nan]))` returns `1.0`.

## Level 2 — Coding
6. Calculate feature column means for 2D matrix `m = np.arange(12).reshape(4, 3)`.
7. Compute sample standard deviation (`ddof=1`) of `np.array([10, 20, 30, 40])`.
8. Find the index location of the minimum value in `np.array([45, 12, 88, 3, 29])`.
9. Compute cumulative sum of array `[1, 2, 3, 4]` using `np.cumsum()`.
10. Calculate NaN-robust median of `np.array([5, np.nan, 15, 25])`.

## Level 3 — Data Analysis
11. Predict output shape of `np.argmax(matrix, axis=1)` for `matrix` of shape `(100, 10)`.
12. Why does `np.mean(data)` return `nan` when `data` contains missing values?
13. Explain why `np.argsort(arr)[::-1]` sorts indices in descending order.
14. Predict output: `a = np.array([[1, 5], [3, 2]]); print(np.argmax(a))`.
15. Predict output: `a = np.array([[1, 5], [3, 2]]); print(np.argmax(a, axis=0))`.

## Level 4 — Debugging
16. Fix bug where sample variance calculation matched population variance instead of sample formula.
17. Fix error: `nan` output propagating across statistical aggregation pipelines.
18. Fix shape issue when subtracting row means without setting `keepdims=True`.

## Level 5 — AI/ML Application
19. How do you convert output class logits `(Batch, Classes)` into predicted class labels `(Batch,)`?
20. In anomaly detection, how to identify sample index with maximum reconstruction loss?
21. Connect `np.argsort()` to Top-K accuracy evaluation in multi-class classification.

## Level 6 — Interview Questions
22. Explain how `np.median` computes the center value for odd vs even length arrays.
23. What is the computational complexity of `np.min` ($O(N)$) vs sorting ($O(N \log N)$)?
24. Explain why `np.argmin` returns the first occurrence index when duplicate minimum values exist.
25. Demonstrate multi-axis reductions (e.g. `np.mean(tensor, axis=(1, 2))`).
26. How do SIMD hardware instructions accelerate reduction loops (`sum`, `mean`) in CPU registers?
