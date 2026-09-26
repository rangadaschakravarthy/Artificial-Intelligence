# Day 91 Practice Questions: Array Creation

## Level 1 — Basic
1. What function creates an array filled entirely with zeros?
2. Which function generates $N$ evenly spaced numbers over a specified interval?
3. What is the default data type of `np.zeros((2, 2))`?
4. True or False: `np.arange(0, 5)` includes number `5`.
5. How do you create a 4x4 Identity matrix?

## Level 2 — Coding
6. Create an array of 50 evenly spaced numbers between -5.0 and +5.0.
7. Create a 2D matrix of shape `(3, 3)` filled with value `-1.0`.
8. Create an array of even integers from 10 to 30 (inclusive).
9. Extract diagonal values from matrix `m = np.arange(9).reshape(3, 3)` using `np.diag()`.
10. Given matrix `x`, create an array of ones with the exact same shape and dtype using `_like`.

## Level 3 — Data Analysis
11. Compare output of `np.arange(0, 1, 0.2)` vs `np.linspace(0, 1, 5)`.
12. Why is `np.empty((100, 100))` faster to execute than `np.zeros((100, 100))`?
13. What is the shape of `np.eye(5, 3)`?
14. Predict output: `np.diag([1, 2, 3])`.
15. Predict output: `np.arange(10, 0, -2)`.

## Level 4 — Debugging
16. Fix bug: `np.zeros(2, 3)` throws `TypeError: Field data-type forbidden` (Why does passing two ints fail?).
17. Fix precision bug: `np.arange(0.0, 0.3, 0.1)` generates 4 elements `[0.0, 0.1, 0.2, 0.30000000000000004]` instead of intended 3.
18. Fix error when calling `np.ones_like([1, 2, 3])` on a standard Python list.

## Level 5 — AI/ML Application
19. How is `np.eye(D)` used to add L2 regularization ($\lambda I$) to covariance matrices $X^T X$?
20. Why do neural network bias terms initialize to `np.zeros(out_features)`?
21. Connect `np.meshgrid` (built on linspace) to decision boundary visualization maps.

## Level 6 — Interview Questions
22. Explain how `np.empty()` interacts with operating system memory pages and `calloc` vs `malloc`.
23. What is the difference between `np.eye()` and `np.identity()`?
24. How can `np.diag()` be used both to create a diagonal matrix and to extract a diagonal vector?
25. Explain floating point accumulator drift in `np.arange` with decimal steps.
26. When should you pre-allocate output arrays instead of dynamically appending elements?
