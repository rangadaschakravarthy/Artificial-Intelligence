# Day 90 Solutions: Array Data Types

## Level 1 — Basic
1. `.dtype`
2. 4 bytes (32 bits / 8 bits per byte).
3. Decimal values are truncated (rounded towards zero).
4. $0$ to $255$ ($2^8 - 1$).
5. True ($8$ bytes per element becomes $4$ bytes per element).

## Level 2 — Coding
6. `np.array([1.7, 2.3, 3.9]).astype(np.int64)` -> `[1, 2, 3]`.
7. `np.array([1, 0, 5, 0]).astype(bool)` -> `[True, False, True, False]`.
8. 
```python
print(np.dtype(np.int8).itemsize)   # 1
print(np.dtype(np.int32).itemsize)  # 4
print(np.dtype(np.float64).itemsize)# 8
```
9. `arr = np.zeros((100, 100), dtype=np.int16)`
10. `np.array([127], dtype=np.int8) + 1` -> `[-128]` (Overflow wrapper).

## Level 3 — Data Analysis
11. `float64` (Upcasted to match floating point array).
12. $1,000,000 	imes 50 	imes 8 	ext{ bytes} = 400,000,000 	ext{ bytes} pprox 400 	ext{ MB}$.
13. $1,000,000 	imes 50 	imes 4 	ext{ bytes} = 200,000,000 	ext{ bytes} pprox 200 	ext{ MB}$.
14. `4` (Silent truncation to match existing integer array dtype).
15. `NaN` (Not a Number) is defined in IEEE 754 floating point specification; integer dtypes cannot store NaN.

## Level 4 — Debugging
16. Cast image array to signed float before subtracting: `img.astype(np.float32) - 128.0`.
17. Large integer timestamps exceed 24-bit mantissa precision of `float32`. Use `int64` or `datetime64`.
18. Convert string elements to numbers first: `arr.astype(float) + 5.0`.

## Level 5 — AI/ML Application
19. Quantization reduces memory bandwidth demands by 2x-4x and enables specialized integer Tensor Core acceleration.
20. Maintains dynamic range by computing forward/backward passes in `float16` while holding master weight updates in `float32`.
21. GPU VRAM is strictly bounded (e.g., 24GB). Smaller dtypes allow larger batch sizes $B$ and larger model parameter counts $P$.

## Level 6 — Interview Solutions
22. `float32` has 8 exponent bits and 23 mantissa bits. `bfloat16` retains 8 exponent bits (same dynamic range as float32) but reduces mantissa to 7 bits.
23. Safe casting only allows implicit conversions that preserve values without data loss. Unsafe casting forces conversion even if truncation or overflow occurs.
24. Reserved bit patterns in IEEE 754: Inf has exponent filled with 1s and mantissa 0s; NaN has exponent filled with 1s and non-zero mantissa.
25. Structured dtypes define custom compound memory records combining different types in contiguous C-structs.
26. Downcasting reduces total memory footprint, enabling datasets to fit entirely within L3 CPU cache / system RAM for zero-disk-paging analysis.
