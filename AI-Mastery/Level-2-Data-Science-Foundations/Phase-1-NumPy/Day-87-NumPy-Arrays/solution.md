# Day 87 Solutions: NumPy Arrays

## Level 1 — Basic
1. Scalar.
2. `.ndim`
3. `a.copy()`
4. `True` if `a` and `b` share underlying memory buffers, `False` otherwise.
5. 3 dimensions: `(Height, Width, Channels)`.

## Level 2 — Coding
6. `arr = np.arange(24).reshape(2, 3, 4)`
7. `np.shares_memory(a, a[::2])` -> Returns `True`.
8. 
```python
arr = np.zeros((4, 2), dtype=np.float64)
print(arr.strides) # (16, 8)
```
9. `print(arr.flags.c_contiguous)`
10. `s = np.array(3.14159); print(s.ndim)` -> `0`

## Level 3 — Data Analysis
11. `(10, 1000, 2)` or `(10, 2, 1000)`.
12. Row and column strides swap. E.g., `(40, 4)` bytes becomes `(4, 40)` bytes.
13. `int32` is 4 bytes. Row stride = 20 columns $	imes 4$ bytes = 80 bytes.
14. Slicing creates a view metadata wrapper pointing to existing memory buffer without copying data bytes.
15. `10` (since `b = a[:]` creates a view).

## Level 4 — Debugging
16. Inconsistent row lengths (`[1, 2]` vs `[3, 4, 5]`) forces fallback to generic `dtype=object`. Ensure rectangular sub-lists.
17. Call `.copy()` on sliced array: `slice_copy = df_array[row_mask].copy()`.
18. Use `np.ascontiguousarray(arr)` to re-align memory contiguously before passing to external C-functions.

## Level 5 — AI/ML Application
19. `(Batch, Channels, Height, Width)` e.g. `(32, 3, 224, 224)` for 32 color images of size 224x224.
20. Slicing mini-batches creates zero-copy pointer views, preventing RAM copying bottlenecks during pipeline batch iteration.
21. Transpose simply swaps stride values in metadata in $O(1)$ time instead of shuffling physical bytes in RAM ($O(N)$).

## Level 6 — Interview Solutions
22. $	ext{Address} = 	ext{Base} + \sum (	ext{index}_i 	imes 	ext{stride}_i)$.
23. Standardized compatibility with C programming language conventions where row elements sit next to each other in memory.
24. `may_share_memory` checks overlapping memory bounds quickly; `shares_memory` performs exact memory pointer intersection analysis.
25. `np.ascontiguousarray(arr)`.
26. Contiguous memory alignment maximizes CPU L1/L2 cache locality during row-column dot-product dot operations.
