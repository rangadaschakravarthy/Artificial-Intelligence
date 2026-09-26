# Day 94 Solutions: Boolean and Fancy Indexing

## Level 1 — Basic
1. `bool_` (`True` or `False`).
2. `&`
3. `~`
4. False (Boolean indexing returns a memory copy).
5. `m[[0, 2, 4], :]` (or `m[[0, 2, 4]]`).

## Level 2 — Coding
6. `a[a > 10]`
7. `a[a % 2 != 0] = -1`
8. `a[(a % 2 == 0) & (a > 4)]` -> `[6, 8]`.
9. `m[[0, 1, 2], [0, 1, 2]]`
10. `idx = np.where(a > 30)[0]` -> `array([1, 3])`.

## Level 3 — Data Analysis
11. `1` (Because `b` is a copy; editing `b` does not mutate `a`).
12. Python `and` evaluates truthiness of the whole array object as a single boolean, raising ambiguity error. Use element-wise `&`.
13. `[30, 10, 20]`
14. `(2,)` (Pairs elements `(0,0)` and `(1,1)` into a 1D vector of length 2).
15. `[5, 10, 0]`

## Level 4 — Debugging
16. Replace Python logical keywords `and`/`or`/`not` with NumPy element-wise operators `&`/`|`/`~`.
17. Wrap conditions in parentheses: `(arr > 5) & (arr < 10)`.
18. Ensure boolean mask length matches the target dimension length of the array being filtered.

## Level 5 — AI/ML Application
19. `clean_X = X[~np.isnan(X[:, 0])]`
20. `X_class0 = X[y == 0]; X_class1 = X[y == 1]`
21. Randomly sample $B$ row indices `batch_idx = np.random.choice(N, B, replace=False)`, then extract `X_batch = X[batch_idx]`.

## Level 6 — Interview Solutions
22. Python does not allow overloading `and`/`or` keywords. NumPy overloads bitwise `&`/`|`/`~` to perform element-wise vectorized logical evaluations.
23. Slicing adjusts stride metadata over existing buffer ($O(1)$ zero-copy view). Fancy indexing allocates new RAM buffer and copies values ($O(N)$ memory copy).
24. `arr[mask]` filters array length down to matching elements. `np.where(cond, x, y)` preserves array shape, taking element from `x` if `True` and `y` if `False`.
25. `m[[r1, r2], [c1, c2]]` pairs coordinates `(r1, c1)` and `(r2, c2)`. To get a rectangular sub-matrix grid, use `m[[r1, r2]][:, [c1, c2]]` or `np.ix_`.
26. CPU SIMD vector registers evaluate conditions across 8-16 elements simultaneously, generating a bitmask register to gather matching RAM elements.
