# Day 100 Practice Questions: Mathematical Functions

## Level 1 — Basic
1. What function computes the natural logarithm (base $e$) of an array?
2. What function computes $e^x$ for each array element?
3. What is the difference between `np.floor()` and `np.ceil()`?
4. True or False: `np.sqrt(-1)` returns an error in real-valued NumPy arrays.
5. What function calculates absolute values of negative numbers?

## Level 2 — Coding
6. Calculate `sin(x)` and `cos(x)` for angles `x = np.array([0, np.pi/4, np.pi/2])`.
7. Apply `np.log1p()` to array `[0, 1e-10, 0.5, 1.0]`.
8. Round values `[1.456, 2.789, 3.141]` to 2 decimal places using `np.round()`.
9. Compute sign of elements in `np.array([-10, 0, 25])` using `np.sign()`.
10. Calculate hypotenuse $\sqrt{a^2 + b^2}$ for $a=3, b=4$ using `np.hypot()`.

## Level 3 — Data Analysis
11. Predict output of `np.sqrt(np.array([4, 9, 16]))`.
12. Why does `np.log(0)` output `-inf` with a `RuntimeWarning`?
13. Predict output: `np.trunc(np.array([-2.9, 2.9]))`.
14. Predict output: `np.floor(np.array([-1.5, 1.5]))`.
15. Predict output: `np.ceil(np.array([-1.5, 1.5]))`.

## Level 4 — Debugging
16. Fix NaN bug when computing `np.log(df['income'])` where some income values are 0.
17. Fix overflow error when computing `np.exp(1000.0)`.
18. Fix issue where `np.round()` rounded `2.5` to `2.0` instead of `3.0` (Explain round-to-even behavior).

## Level 5 — AI/ML Application
19. Implement Sigmoid activation function $S(x) = rac{1}{1 + e^{-x}}$ using `np.exp()`.
20. Implement Binary Cross-Entropy Loss function $	ext{BCE} = - 	ext{mean}(y \ln(p) + (1-y) \ln(1-p))$.
21. Connect log transformations to normalizing right-skewed feature distributions before training linear models.

## Level 6 — Interview Questions
22. Explain how floating-point cancellation occurs in `np.log(1 + x)` when $x \ll 1$.
23. What is IEEE 754 "round-half-to-even" rounding strategy used in `np.round()`?
24. Explain the Log-Sum-Exp trick for preventing exponent overflow in Softmax computations.
25. How do Intel SVML (Short Vector Math Library) routines optimize transcendental functions (`exp`, `log`, `sin`)?
26. Demonstrate how `np.clip()` prevents extreme values before mathematical ufunc evaluation.
