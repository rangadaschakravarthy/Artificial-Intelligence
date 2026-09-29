# Day 101 Practice Questions: Random Number Generation

## Level 1 — Basic
1. How do you instantiate the modern NumPy random generator object with seed `42`?
2. What function generates random floating-point numbers in range $[0.0, 1.0)$?
3. What parameter in `rng.choice()` prevents selecting duplicate elements?
4. What distribution does `rng.normal(loc=10, scale=2)` sample from?
5. True or False: Setting a random seed produces identical pseudo-random numbers every time code runs.

## Level 2 — Coding
6. Generate a 3x3 matrix of random floats uniformly distributed between `-1.0` and `+1.0`.
7. Sample 5 random integers between `1` and `100` (inclusive).
8. Shuffle array `arr = np.arange(10)` in-place using `rng.shuffle()`.
9. Generate 1,000 samples from a Poisson distribution with $\lambda = 4.0$.
10. Randomly select 3 rows from a 2D matrix `X` of shape `(10, 4)` without replacement.

## Level 3 — Data Analysis
11. Why is setting a random seed essential when publishing scientific data science research?
12. Predict output shape of `rng.normal(size=(5, 3))`.
13. Explain why `rng.choice([0, 1], size=10, p=[0.8, 0.2])` generates ~80% zeros and ~20% ones.
14. Predict output: `rng = np.random.default_rng(0); a = rng.random(); rng = np.random.default_rng(0); b = rng.random(); print(a == b)`.
15. Compare `rng.shuffle(arr)` (in-place) vs `rng.permutation(arr)` (returns copy).

## Level 4 — Debugging
16. Fix error: `TypeError: 'module' object is not callable` when calling `np.random(5)` (Use `rng.random(5)`).
17. Fix bug where dynamic random seeds inside a loop produced identical values on every iteration.
18. Fix issue where random sampling failed because probabilities `p` in `choice` did not sum to `1.0`.

## Level 5 — AI/ML Application
19. Implement Xavier (Glorot) Uniform initialization: $W \sim 	ext{Uniform}\left(-\sqrt{\frac{6}{	ext{fan\_in} + 	ext{fan\_out}}}, +\sqrt{\frac{6}{	ext{fan\_in} + 	ext{fan\_out}}}
ight)$.
20. Implement a 80/20 train/test random indices split for a dataset of size $N=1000$.
21. Connect random sampling to Monte Carlo policy evaluation in Reinforcement Learning.

## Level 6 — Interview Questions
22. Explain how PCG64 (Permuted Congruential Generator) improves upon Mersenne Twister (MT19937).
23. What is the difference between pseudo-random number generators (PRNG) and true hardware random number generators (TRNG)?
24. How does the Box-Muller transform convert uniform random variables into standard Gaussian variables?
25. Demonstrate how `rng.multinomial()` models multi-class categorical event sampling.
26. How do thread-local Generator instances prevent lock contention in parallel multi-threaded ML code?
