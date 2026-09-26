# Day 91 Solutions: Array Creation

## Level 1 — Basic
1. `np.zeros()`
2. `np.linspace()`
3. `float64`
4. False (`np.arange` is half-open interval `[start, stop)`).
5. `np.eye(4)` (or `np.identity(4)`).

## Level 2 — Coding
6. `np.linspace(-5.0, 5.0, 50)`
7. `np.full((3, 3), -1.0)`
8. `np.arange(10, 31, 2)`
9. `np.diag(m)` -> `array([0, 4, 8])`
10. `np.ones_like(x)`

## Level 3 — Data Analysis
11. `arange`: `[0. , 0.2, 0.4, 0.6, 0.8]` (5 elements). `linspace`: `[0.  , 0.25, 0.5 , 0.75, 1.  ]` (5 elements including 1.0).
12. `np.empty()` calls `malloc` without populating memory bytes with zero values, saving memory write cycles.
13. `(5, 3)` (Rectangular matrix with 1s on main diagonal and 0s elsewhere).
14. 3x3 diagonal matrix with 1, 2, 3 along diagonal.
15. `array([10,  8,  6,  4,  2])`

## Level 4 — Debugging
16. Dimensions must be passed as a single tuple argument: `np.zeros((2, 3))`.
17. Replace floating-point `arange` with `np.linspace(0.0, 0.2, 3)` or `np.round()`.
18. `_like` functions expect an array-like object. Convert list to array or pass `np.ones(len(py_list))`.

## Level 5 — AI/ML Application
19. Regularized inverse $(X^T X + \lambda I)^{-1}$ adds $\lambda 	imes 	ext{np.eye}(D)$ to guarantee positive definiteness.
20. Zero initialization for biases ensures unbiased initial neuron activation centered around weight initialization distributions.
21. `np.meshgrid` evaluates continuous 2D coordinate pairs $(X, Y)$ generated via `linspace` across decision classification boundaries.

## Level 6 — Interview Solutions
22. `np.zeros` uses C `calloc` (clears memory bytes to zero). `np.empty` uses `malloc` (allocates raw buffer instantly without zeroing bytes).
23. `np.identity(n)` only creates square $n 	imes n$ matrices. `np.eye(N, M, k)` supports rectangular shapes and diagonal offset parameter `k`.
24. If input is 1D vector, `np.diag` constructs 2D diagonal matrix. If input is 2D matrix, `np.diag` extracts 1D diagonal vector.
25. Repeatedly adding floating-point step $\Delta$ accumulates IEEE 754 binary rounding errors over long sequence steps.
26. Pre-allocation allocates fixed memory buffer once ($O(1)$), avoiding repeated memory reallocation and copying overhead of dynamic appends ($O(N^2)$).
