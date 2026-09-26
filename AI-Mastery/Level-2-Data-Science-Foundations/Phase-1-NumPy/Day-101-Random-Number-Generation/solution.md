# Day 101 Solutions: Random Number Generation

## Level 1 — Basic
1. `rng = np.random.default_rng(42)`
2. `rng.random()` (or `rng.uniform(0.0, 1.0)`).
3. `replace=False`
4. Normal (Gaussian) distribution with mean $\mu = 10$ and standard deviation $\sigma = 2$.
5. True (Deterministic pseudo-random sequence).

## Level 2 — Coding
6. `rng.uniform(-1.0, 1.0, size=(3, 3))`
7. `rng.integers(low=1, high=101, size=5)`
8. `rng.shuffle(arr)`
9. `poisson_samples = rng.poisson(lam=4.0, size=1000)`
10. `idx = rng.choice(10, size=3, replace=False); sample_rows = X[idx]`

## Level 3 — Data Analysis
11. Guarantees exact experiment reproducibility so other researchers can verify results and get identical outputs.
12. `(5, 3)`
13. `p=[0.8, 0.2]` assigns 80% probability to choice 0 and 20% probability to choice 1.
14. `True` (Both generators initialized with identical seed `0`).
15. `rng.shuffle(arr)` mutates `arr` in-place and returns `None`. `rng.permutation(arr)` leaves `arr` unchanged and returns a new shuffled array copy.

## Level 4 — Debugging
16. Use generator instance: `rng = np.random.default_rng(); arr = rng.random(5)`.
17. Instantiate `rng = np.random.default_rng(seed)` once **outside** the loop instead of re-instantiating inside the loop.
18. Normalize probabilities so they sum to 1.0: `p = p / np.sum(p)`.

## Level 5 — AI/ML Application
19. 
```python
bound = np.sqrt(6.0 / (fan_in + fan_out))
W = rng.uniform(low=-bound, high=bound, size=(fan_in, fan_out))
```
20. 
```python
indices = rng.permutation(1000)
train_idx, test_idx = indices[:800], indices[800:]
```
21. Monte Carlo methods simulate thousands of random episode state-action paths to estimate action-value expectations.

## Level 6 — Interview Solutions
22. PCG64 has higher statistical quality (passes TestU01 BigCrush), smaller state footprint (128-bit vs 2.5KB), and faster generation speed than MT19937.
23. PRNGs use deterministic algorithms seeded by a initial number. TRNGs sample physical environmental entropy (e.g. thermal noise, radioactive decay).
24. Box-Muller uses 2 independent uniform variables $U_1, U_2 \sim 	ext{Uniform}(0,1)$ to construct standard normal variables $Z = \sqrt{-2 \ln U_1} \cos(2\pi U_2)$.
25. `rng.multinomial(n=10, pvals=[0.2, 0.5, 0.3])` simulates 10 trials across 3 outcome categories.
26. Each worker thread instantiates its own `default_rng()` with a distinct seed, eliminating GIL/mutex lock contention on a shared global random state.
