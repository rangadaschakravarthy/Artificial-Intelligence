# Day 96 Practice Questions: Array Operations

## Level 1 — Basic
1. What type of multiplication does operator `*` perform between two NumPy matrices?
2. What operator performs formal matrix multiplication in Python 3.5+ / NumPy?
3. True or False: In-place operator `a += b` creates a new array object.
4. What is the output of `np.array([10, 20]) // 3`?
5. What does `a == b` return for two 1D arrays of length 3?

## Level 2 — Coding
6. Given `a = np.array([1, 2, 3])`, compute its element-wise cube ($a^3$).
7. Perform element-wise modulo 2 (`% 2`) on `np.arange(10)`.
8. Given two matrices `A` and `B` of shape `(2, 2)`, compute their Hadamard product.
9. Use `np.multiply(a, b, out=a)` to perform in-place multiplication.
10. Check if all elements in `np.array([1, 2, 3])` are greater than 0 using `np.all()`.

## Level 3 — Data Analysis
11. Predict output: `np.array([True, False]) & np.array([True, True])`.
12. Predict output: `np.array([1, 2]) + np.array([10])` (Broadcasting scalar).
13. Explain why `a = a + b` allocates new memory while `a += b` modifies `a` in-place.
14. Predict output: `a = np.array([1, 2, 3]); print(a ** 0)`.
15. Predict output: `a = np.array([10, 20]); print(a > 15)`.

## Level 4 — Debugging
16. Fix error: `ValueError: operands could not be broadcast together with shapes (3,) (4,)`.
17. Fix bug where developer used `A * B` expecting matrix product, causing incorrect ML predictions.
18. Fix issue where integer division `a / b` produced floats when integers were expected (`a // b`).

## Level 5 — AI/ML Application
19. Implement Mean Absolute Error (MAE) loss formula: $	ext{MAE} = \frac{1}{N} \sum |y_{	ext{pred}} - y_{	ext{true}}|$.
20. Implement Sigmoid activation preprocessing formula: $\frac{1}{1 + e^{-x}}$.
21. Connect element-wise array operations to bias addition $X W + b$ in neural network layers.

## Level 6 — Interview Questions
22. What is a ufunc (Universal Function) in NumPy and how does it achieve high performance?
23. Explain how memory footprint differs between out-of-place operations vs using the `out` parameter.
24. How does NumPy handle division by zero in floating point arrays vs integer arrays?
25. Demonstrate how `np.any()` and `np.all()` reduce boolean array operations.
26. How do SIMD hardware instructions execute element-wise array math in CPU vector registers?
