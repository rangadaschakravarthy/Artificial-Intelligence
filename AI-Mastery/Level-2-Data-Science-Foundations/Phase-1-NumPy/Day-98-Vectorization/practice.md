# Day 98 Practice Questions: Vectorization

## Level 1 — Basic
1. What is the main reason vectorized NumPy code runs faster than Python loops?
2. What hardware CPU feature does vectorization leverage?
3. True or False: `np.vectorize()` converts Python code to native C ufuncs.
4. What NumPy function allows vectorized element selection based on a condition `(cond, x, y)`?
5. What function evaluates piecewise multiple conditional choices in a vectorized manner?

## Level 2 — Coding
6. Benchmark the time taken to compute `sin(x)` for 1,000,000 elements using `math.sin` loop vs `np.sin`.
7. Replace loop `[max(0, x) for x in arr]` with a vectorized NumPy expression.
8. Use `np.where()` to flag elements in `arr = np.array([10, 55, 30, 80])` as `'High'` if $> 50$ else `'Low'`.
9. Vectorize scalar function `def poly(x): return 3*x**2 + 2*x + 1` using `np.vectorize`.
10. Compute element-wise dot product of corresponding rows between two matrices `(N, D)` without loops using `np.sum(A * B, axis=1)`.

## Level 3 — Data Analysis
11. Why is `np.sum(arr)` significantly faster than Python built-in `sum(arr)` on NumPy arrays?
12. Explain the performance pitfall of calling `list.append()` inside an array iteration loop.
13. Predict output: `np.where(np.array([True, False]), 10, 20)`.
14. Predict output: `a = np.array([-1, 2, -3]); print(np.maximum(0, a))`.
15. Compare RAM bandwidth consumption between 1D vectorization vs nested loop indexing.

## Level 4 — Debugging
16. Fix performance bug where developer wrote explicit nested `for` loops to compute 2D matrix sum.
17. Fix bug: `np.where(arr > 0, arr)` fails due to missing third `y` argument.
18. Fix issue where `np.vectorize` failed to speed up a slow Python data processing function.

## Level 5 — AI/ML Application
19. Implement vectorized Sigmoid activation function $S(x) = rac{1}{1 + e^{-x}}$ over 2D input matrix.
20. Implement vectorized Cosine Similarity between two feature matrices $A$ and $B$: $rac{A \cdot B^T}{\|A\| \|B\|}$.
21. Connect SIMD vector instructions to parallel tensor computations in machine learning frameworks.

## Level 6 — Interview Questions
22. Explain how SIMD registers (AVX-2 / AVX-512) process multiple floating point values in parallel.
23. Why does Python loop execution incur high dynamic dispatch and garbage collection overhead?
24. Explain the difference between data-level parallelism (SIMD) and thread-level parallelism (Multi-threading).
25. Demonstrate how `np.piecewise()` evaluates vectorized piecewise continuous mathematical functions.
26. How do cache hits vs cache misses impact vectorized computation throughput?
