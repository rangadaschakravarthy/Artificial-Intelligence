# Day 90 Practice Questions: Array Data Types

## Level 1 — Basic
1. What property returns the data type of an array?
2. How many bytes does a `float32` element consume?
3. What happens to decimal values when casting `float` to `int` using `.astype()`?
4. What is the valid range of values for a `uint8` data type?
5. True or False: Converting `float64` to `float32` cuts array memory size in half.

## Level 2 — Coding
6. Create an array `[1.7, 2.3, 3.9]` and cast it to `int64`.
7. Create a boolean mask array from `np.array([1, 0, 5, 0])` using `.astype(bool)`.
8. Check the byte size (`itemsize`) of `int8`, `int32`, and `float64`.
9. Construct a 2D matrix of zeros of shape `(100, 100)` with data type `int16`.
10. Demonstrate integer overflow by adding 1 to `np.array([127], dtype=np.int8)`.

## Level 3 — Data Analysis
11. Predict the resulting `dtype` of `np.array([1, 2]) + np.array([1.5, 2.5])`.
12. Calculate total MB memory required for dataset of shape `(1_000_000, 50)` stored as `float64`.
13. Calculate total MB memory for same dataset stored as `float32`.
14. Predict output: `a = np.array([1, 2, 3]); a[0] = 4.99; print(a[0])`.
15. Why does `np.nan` require floating point `dtype`?

## Level 4 — Debugging
16. Fix bug where image pixels `0..255` overflow when subtracting mean value 128 in `uint8`.
17. Fix precision loss error when storing large timestamps as `float32`.
18. Fix issue where string numerical array `np.array(['1.0', '2.0'])` fails during mathematical addition.

## Level 5 — AI/ML Application
19. Why do modern LLMs use `bfloat16` and `int8` quantization during model inference?
20. How does mixed precision training maintain numerical stability while accelerating computations?
21. Connect `dtype` choice to GPU VRAM bottlenecks in deep learning.

## Level 6 — Interview Questions
22. Explain the difference between `float32` (IEEE 754 single precision) and `bfloat16`.
23. What is the difference between safe casting and unsafe casting in NumPy?
24. Explain how NaN and Inf values are represented in IEEE 754 floating point standard.
25. How do structured data types (`np.dtype([('name', 'S10'), ('age', 'i4')])`) work in NumPy?
26. How does downcasting optimize memory performance in large-scale data analysis?
