# Day 100 Solutions: Mathematical Functions

## Level 1 — Basic
1. `np.log()`
2. `np.exp()`
3. `np.floor()` rounds down towards $-\infty$; `np.ceil()` rounds up towards $+\infty$.
4. False (It returns `nan` with a `RuntimeWarning: invalid value encountered in sqrt`).
5. `np.abs()` (or `np.absolute()`).

## Level 2 — Coding
6. 
```python
x = np.array([0, np.pi/4, np.pi/2])
print("Sin:", np.sin(x))
print("Cos:", np.cos(x))
```
7. `np.log1p([0, 1e-10, 0.5, 1.0])` -> `array([0.0, 1e-10, 0.405, 0.693])`
8. `np.round([1.456, 2.789, 3.141], decimals=2)` -> `array([1.46, 2.79, 3.14])`
9. `np.sign([-10, 0, 25])` -> `array([-1, 0, 1])`
10. `np.hypot(3, 4)` -> `5.0`

## Level 3 — Data Analysis
11. `array([2., 3., 4.])`
12. $\ln(0)$ is mathematically $-\infty$. NumPy returns `-inf` and flags a runtime warning.
13. `array([-2.,  2.])` (Truncates decimal digits towards zero).
14. `array([-2.,  1.])` (Rounds down to nearest smaller integer).
15. `array([-1.,  2.])` (Rounds up to nearest larger integer).

## Level 4 — Debugging
16. Replace `np.log(x)` with `np.log1p(x)` or `np.log(x + 1e-15)` to avoid $\ln(0)$.
17. Subtract maximum value before exponentiation (Log-Sum-Exp trick) or clip values: `np.clip(x, -500, 500)`.
18. NumPy uses IEEE 754 round-to-even standard to prevent statistical bias. Halfway values (e.g. `2.5`) round to the nearest even integer (`2.0`).

## Level 5 — AI/ML Application
19. `def sigmoid(x): return 1.0 / (1.0 + np.exp(-x))`
20. `bce = -np.mean(y * np.log(p + 1e-15) + (1 - y) * np.log(1 - p + 1e-15))`
21. Right-skewed features have extreme right-tail outliers. Taking `log1p` compresses the dynamic range, transforming the feature into a symmetric Gaussian-like distribution suitable for linear models.

## Level 6 — Interview Solutions
22. Adding $1.0 + 10^{-15}$ drops lower precision bits of $10^{-15}$ because single/double precision floats have limited mantissa bits. `np.log1p` uses direct Taylor expansion $\ln(1+x) pprox x - rac{x^2}{2} + rac{x^3}{3}$.
23. Round-to-even (banker's rounding) rounds $X.5$ to the nearest even integer. Over large datasets, rounding up half the time and down half the time prevents systematic upward rounding bias.
24. $	ext{LSE}(z) = m + \ln \left( \sum e^{z_i - m} ight)$ where $m = \max(z)$. Shifting exponents by $-m$ ensures the maximum exponent is $e^0 = 1$, completely avoiding $+\infty$ overflow.
25. SVML vectorized libraries replace standard `libm` scalar function calls with 256-bit SIMD polynomial approximations that compute transcendental functions for 4-8 elements concurrently.
26. `np.clip(arr, min_val, max_val)` bounds values strictly before calling sensitive functions like `np.log` or `np.arcsin`.
