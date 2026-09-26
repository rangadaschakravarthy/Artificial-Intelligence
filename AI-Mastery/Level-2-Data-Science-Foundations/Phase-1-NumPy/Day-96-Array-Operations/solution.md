# Day 96 Solutions: Array Operations

## Level 1 — Basic
1. Element-wise (Hadamard) multiplication.
2. `@` (or `np.matmul()` / `np.dot()`).
3. False (It modifies the existing array in-place without allocating new memory).
4. `array([3, 6])` (Integer floor division).
5. A boolean array of length 3 containing element-wise comparison results (`[True/False, ...]`).

## Level 2 — Coding
6. `a ** 3` -> `array([1, 8, 27])`
7. `np.arange(10) % 2` -> `array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1])`
8. `H = A * B`
9. `np.multiply(a, b, out=a)`
10. `np.all(arr > 0)` -> Returns `True`.

## Level 3 — Data Analysis
11. `array([ True, False])`
12. `array([11, 12])`
13. `a = a + b` evaluates RHS into a new temporary array object and rebinds name `a`. `a += b` calls in-place ufunc modifying `a`'s existing buffer.
14. `array([1, 1, 1])`
15. `array([False,  True])`

## Level 4 — Debugging
16. Ensure array shapes match or are compatible for broadcasting (e.g. reshape `(3,)` to `(3, 1)` or match lengths).
17. Replace `*` with `@` or `np.dot(A, B)`.
18. Replace single slash `/` (float division) with double slash `//` (floor integer division) or cast with `.astype(int)`.

## Level 5 — AI/ML Application
19. `mae_loss = np.mean(np.abs(y_pred - y_true))`
20. `sigmoid = 1.0 / (1.0 + np.exp(-x))`
21. Matrix product $X W$ produces shape $(N, Out)$. Element-wise broadcasting adds bias vector $b$ of shape $(Out,)$ across all $N$ sample rows.

## Level 6 — Interview Solutions
22. A ufunc is a C-implemented wrapper over element-wise functions that executes compiled inner C-loops without Python GIL overhead.
23. Out-of-place operations allocate new RAM buffers ($O(N)$ memory). Using `out` writes results into existing memory buffers ($O(1)$ memory allocation).
24. Floating point division by zero produces `np.inf` or `np.nan` with a `RuntimeWarning`. Integer division by zero raises a `ZeroDivisionError`.
25. `np.any()` returns `True` if at least 1 element is `True`. `np.all()` returns `True` only if every element is `True`.
26. SIMD (Single Instruction Multiple Data) registers load 4-8 elements into 128/256-bit registers (AVX-2/AVX-512) and execute arithmetic in a single clock cycle.
