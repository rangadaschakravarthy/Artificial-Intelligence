# Day 92 Solutions: Indexing

## Level 1 — Basic
1. `0`
2. `-1`
3. `m[2, 3]` (0-based indexing means 3rd row, 4th column).
4. False (`m[0, 1]` is faster).
5. `IndexError`.

## Level 2 — Coding
6. `m[1, 1]`
7. `m[2, 2] = -1`
8. `val = tensor[0, 2, 3]`
9. `print(a[[0, -1]])`
10. `val = data[-1, 0]`

## Level 3 — Data Analysis
11. Row indices: `0` to `4` (or `-5` to `-1`). Column indices: `0` to `4` (or `-5` to `-1`).
12. `m[1, 2]` performs single C pointer lookup. `m[1][2]` creates intermediate 1D slice array object for row 1, then indexes index 2.
13. `10`
14. `1.0`
15. `0.0`

## Level 4 — Debugging
16. Array of size 3 has valid indices `0, 1, 2`. Change index `3` to valid index within `0..2`.
17. Replace chained indexing `arr[0][1]` with tuple indexing `arr[0, 1] = 99`.
18. Replace semicolon `;` with comma `,`: `matrix[1, 2]`.

## Level 5 — AI/ML Application
19. `y_i = data[i, -1]` accesses sample $i$ at the final target column index.
20. `Q_val = Q_table[state_idx, action_idx]` retrieves scalar expected reward value for state-action pair.
21. Image pixels are indexed as `img[y, x, c]` where $y$ is row (height), $x$ is column (width), and $c$ is color channel.

## Level 6 — Interview Solutions
22. Pointer $	ext{offset} = 	ext{base\_ptr} + i 	imes 	ext{stride}_0 + j 	imes 	ext{stride}_1$.
23. Scalar integer indexing extracts a single value, producing a scalar object. Slicing preserves dimension bounds, returning a view over memory buffer.
24. Python/NumPy performs runtime boundary checks against shape dimensions, throwing `IndexError` to prevent memory segment faults.
25. Passing a tuple of ints `idx = (1, 2)` inside brackets `arr[idx]` evaluates identically to `arr[1, 2]`.
26. Row indexing (`C-contiguous`) accesses contiguous sequential bytes in RAM, maximizing L1 CPU cache lines. Column indexing jumps strides of size $N$, causing cache misses.
