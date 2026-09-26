# Day 86 Solutions: NumPy Introduction

## Level 1 — Basic
1. Numerical Python.
2. `ndarray` (N-dimensional array).
3. `import numpy as np`.
4. False (Python lists store array of pointers to scattered heap objects).
5. All elements are upcasted to `float64`: `array([1. , 2.5, 3. ])`.

## Level 2 — Coding
6. `arr = np.arange(5, 16)`
7. `arr = np.arange(1.0, 10.0).reshape(3, 3)`
8. 
```python
arr = np.array([[10, 20], [30, 40]])
print(arr.ndim, arr.shape, arr.dtype, arr.nbytes)
# Output: 2 (2, 2) int64 32
```
9. `arr = np.array(['1.5', '2.5', '3.5'], dtype=float)`
10. `print(np.__version__)`

## Level 3 — Data Analysis
11. `scaled_x = x / 100.0` -> `[1.0, 2.0, 3.0]`.
12. $100 	imes 10 = 1,000$ total elements.
13. `float64` is 8 bytes. $1,000 	imes 8 = 8,000$ bytes (8 KB).
14. Booleans upcast to integers (`True` -> `1`), integers upcast to floats (`1` -> `1.0`), resulting in `float64`.
15. NumPy array uses $1000 	imes 8 = 8000$ bytes contiguous buffer. Python list uses ~28 bytes per int object + 8 bytes per pointer ≈ 36,000 bytes (~4.5x larger).

## Level 4 — Debugging
16. Must alias `import numpy as np` or call `numpy.array`.
17. `.shape` is a tuple property attribute, not a function method. Remove parentheses: `a.shape`.
18. String `'3'` upcasted entire array to string dtype (`<U21`). Convert to int first: `np.array([1, 2, '3'], dtype=int) + 5`.

## Level 5 — AI/ML Application
19. Shape `(500, 20)` where rows represent 500 sample patients and columns represent 20 feature variables.
20. GPUs execute SIMD parallel threads expecting identical memory stride per element; non-homogenous objects disrupt thread execution.
21. Pre-fetching contiguous bytes into L1/L2 CPU cache lines eliminates RAM fetch latency during nested matrix loops.

## Level 6 — Interview Solutions
22. Strides are tuples of bytes to step in each dimension when traversing RAM memory to locate `arr[i, j]`.
23. Upcasting automatically promotes lower-precision types to the highest-precision type present to maintain homogenous typing.
24. NumPy C-extensions release the GIL during heavy vector calculations, letting native C code run on raw C buffers.
25. C-contiguous stores rows consecutively in memory (row-major); Fortran-contiguous stores columns consecutively (column-major).
26. When storing heterogeneous object types, dynamically resizing lists, or working with sparse non-numerical structures.
