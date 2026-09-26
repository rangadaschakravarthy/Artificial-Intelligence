# Day 99 Solutions: Aggregation and Statistics

## Level 1 — Basic
1. `np.median()`
2. The index location of the maximum value.
3. `ddof=0` divides by $N$ (population variance); `ddof=1` divides by $N-1$ (sample variance).
4. `np.ptp()` (peak-to-peak).
5. False (It returns `nan`).

## Level 2 — Coding
6. `col_means = m.mean(axis=0)` -> `array([4.5, 5.5, 6.5])`
7. `sample_std = np.std(np.array([10, 20, 30, 40]), ddof=1)` -> `12.9099`
8. `np.argmin(np.array([45, 12, 88, 3, 29]))` -> `3`
9. `np.cumsum([1, 2, 3, 4])` -> `array([1, 3, 6, 10])`
10. `np.nanmedian(np.array([5, np.nan, 15, 25]))` -> `15.0`

## Level 3 — Data Analysis
11. `(100,)` (Returns 100 predicted class indices for the 100 samples).
12. Standard floating point math propagates `NaN` across additions; $x + 	ext{NaN} = 	ext{NaN}$.
13. `np.argsort()` returns indices in ascending order (smallest to largest). Reversing `[::-1]` flips order to descending (largest to smallest).
14. `1` (Flattened array `[1, 5, 3, 2]` has max value 5 at index 1).
15. `array([1, 0])` (Max along col 0 is 3 at row 1; max along col 1 is 5 at row 0).

## Level 4 — Debugging
16. Set `ddof=1` parameter: `np.var(arr, ddof=1)`.
17. Replace standard functions with NaN-robust equivalents (`np.nanmean`, `np.nanstd`, `np.nanmedian`).
18. Use `keepdims=True` in aggregation: `row_means = arr.mean(axis=1, keepdims=True); arr - row_means`.

## Level 5 — AI/ML Application
19. `y_pred = np.argmax(logits, axis=1)`
20. `worst_sample_idx = np.argmax(reconstruction_losses)`
21. Extract top-K prediction indices for each sample: `top_k = np.argsort(logits, axis=1)[:, :-K-1:-1]`.

## Level 6 — Interview Solutions
22. For odd length $N$, median is exact middle element at index $N//2$ after sorting. For even length $N$, median is the average of the two middle elements at indices $N//2 - 1$ and $N//2$.
23. `np.min` scans elements in a single $O(N)$ pass. Full sorting `np.sort` takes $O(N \log N)$ time.
24. C-reduction loops update `min_val` and `min_idx` register only when strictly smaller elements are encountered (`<`), preserving the first occurrence index.
25. `np.mean(tensor, axis=(1, 2))` collapses both axes 1 and 2 simultaneously, retaining remaining dimensions.
26. CPU SIMD registers use parallel reduction trees (e.g., adding vector register lanes into partial accumulator registers) to process 8-16 element additions per cycle.
