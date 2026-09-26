# Day 98 Solutions: Vectorization

## Level 1 — Basic
1. Replaces Python interpreter dynamic type checking with C-compiled inner loops operating on contiguous memory.
2. SIMD (Single Instruction Multiple Data) registers.
3. False (`np.vectorize` is a convenience wrapper that still executes Python loops internally).
4. `np.where(condition, x, y)`
5. `np.select(condlist, choicelist)`

## Level 2 — Coding
6. 
```python
import math, time, numpy as np
N = 1000000
arr = np.linspace(0, 10, N)
# Loop
t0 = time.time(); res1 = [math.sin(x) for x in arr]; t_loop = time.time() - t0
# Vectorized
t0 = time.time(); res2 = np.sin(arr); t_vec = time.time() - t0
print(f"Speedup: {t_loop / t_vec:.1f}x")
```
7. `np.maximum(0, arr)` (or `np.where(arr > 0, arr, 0)`).
8. `np.where(arr > 50, 'High', 'Low')` -> `array(['Low', 'High', 'Low', 'High'])`.
9. `v_poly = np.vectorize(poly); res = v_poly(arr)`
10. `row_dots = np.sum(A * B, axis=1)`

## Level 3 — Data Analysis
11. `np.sum` calls C-compiled vector sum; Python `sum()` converts each array element to a Python `int`/`float` object first, incurring heavy boxing/unboxing overhead.
12. Dynamic appending continually triggers array memory reallocation and copying ($O(N)$ dynamic resize cost).
13. `array([10, 20])`
14. `array([0, 2, 0])`
15. Vectorized SIMD streams contiguous RAM bytes into CPU L1 cache lines. Nested loop indexing triggers Python object lookup for every single cell iteration.

## Level 4 — Debugging
16. Replace nested loops `for i... for j... sum += m[i, j]` with `total = m.sum()`.
17. Pass third `y` argument to `np.where(cond, x, y)` or use boolean masking `arr[arr > 0]`.
18. Replace `np.vectorize` with native NumPy ufuncs (`np.sin`, `np.exp`, arithmetic operators) to leverage true C-compilation.

## Level 5 — AI/ML Application
19. `def sigmoid(x): return 1.0 / (1.0 + np.exp(-x))`
20. `cos_sim = (A @ B.T) / (np.linalg.norm(A, axis=1, keepdims=True) * np.linalg.norm(B, axis=1, keepdims=True).T)`
21. Deep learning frameworks compile computational graphs into CUDA kernel / SIMD vector instructions operating directly on tensor memory buffers.

## Level 6 — Interview Solutions
22. SIMD registers (e.g. 256-bit AVX-2) load eight 32-bit floats into a single CPU register and execute arithmetic instruction `VADDPS` in 1 clock cycle.
23. Every Python loop iteration checks element type, looks up dunder method `__add__`, manages reference counts, and checks for signals/GIL locks.
24. SIMD is data-level parallelism executing 1 instruction on multiple data elements in 1 core. Multi-threading is task-level parallelism running separate instruction threads across multiple CPU cores.
25. `np.piecewise(x, [x < 0, x >= 0], [lambda x: -x, lambda x: x])` (Implements absolute value function).
26. Contiguous vectorized memory accesses hit L1/L2 CPU cache lines with >95% hit rate. Scattered pointer indexing causes CPU cache misses, stalling execution while waiting for RAM.
