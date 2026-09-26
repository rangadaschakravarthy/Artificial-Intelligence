# Day 107 Solutions: Series

## Level 1 — Basic
1. A Series has explicit custom index labels attached to values; a NumPy array uses 0-based positional integer indices.
2. Pass `name='MyName'` parameter: `pd.Series(data, name='MyName')`.
3. `.to_numpy()` (or `.values`).
4. `.value_counts()`
5. True.

## Level 2 — Coding
6. `s = pd.Series([100, 200, 300], index=['Jan', 'Feb', 'Mar'])`
7. `s.quantile(0.90)` -> `89.1`
8. `s.value_counts()` -> `'A': 3, 'B': 2, 'C': 1`.
9. `s.astype(int)`
10. `s[s > 15]` -> `'b': 20, 'c': 30`.

## Level 3 — Data Analysis
11. `'a': NaN`, `'b': 12.0`, `'c': NaN`.
12. By default, `dropna=True` ignores NaNs. `dropna=False` includes a count of missing `NaN` values in the frequency output.
13. `2`
14. `20.0`
15. For numerical Series, `.describe()` computes count, mean, std, min, quartiles, max. For string/object Series, it computes count, unique, top (most frequent), and freq.

## Level 4 — Debugging
16. Label `'d'` does not exist in the index. Use `s.get('d', default=np.nan)` or check index labels.
17. Reindex Series to match before operating (`s1.reindex(s2.index)`), or fill missing values using `s1.add(s2, fill_value=0)`.
18. Pass parameter `dropna=False`: `s.value_counts(dropna=False)`.

## Level 5 — AI/ML Application
19. `y.value_counts(normalize=True)`. If minority class proportion is $< 10\%-20\%$, severe imbalance exists.
20. `valid_income = df['Income'][df['Income'] >= 0]`
21. When ensembling prediction Series $\hat{y}_1, \hat{y}_2$, index alignment ensures predictions for sample $i$ match correctly even if prediction Series were shuffled.

## Level 6 — Interview Solutions
22. If duplicate labels exist, Pandas computes Cartesian outer product for duplicate label keys during alignment operations.
23. `.loc[]` searches for matching **label** `10`. `.iloc[]` searches strictly for **positional** integer index `10` (0-based position).
24. `.map()` accepts a dictionary or function to map Series values. `.apply()` applies complex custom Python functions or ufuncs to Series values.
25. `df = pd.concat([s1, s2], axis=1)` combines Series as columns; `axis=0` stacks them vertically.
26. Pandas uses C-level hash tables (`Index` lookup) to align matching index labels between Series in $O(N)$ expected time.
