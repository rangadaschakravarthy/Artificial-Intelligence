# Solutions — Probability with Python

## Level 1
1. Percent Point Function (Inverse CDF / Quantiles).
2. `np.random.random()` or `rng.random()`.
3. `mu, std = scipy.stats.norm.fit(data)`.
4. $O(1/\sqrt{S})$.
5. `rng = np.random.default_rng(seed=42)`.

## Level 2
6. `from scipy import stats; print(stats.norm.cdf(2.5))`
7. `stats.expon(scale=10).ppf(0.99)`
8. `samples = np.random.binomial(n=20, p=0.4, size=5000)`
9. `print(np.mean(samples), np.var(samples))`
10. `stats.poisson(mu=5).pmf(3)`

## Level 3
11.
```python
def bootstrap_ci(data, n_boot=1000):
  means = [
      np.mean(np.random.choice(data, size=len(data), replace=True))
      for _ in range(n_boot)
  ]
  return np.percentile(means, [2.5, 97.5])
```
12.
```python
X = np.random.uniform(0, 4, 100000)
Y = np.random.uniform(0, 4, 100000)
print(np.mean((X + Y) > 5))
```
13. `def kl(P, Q): return np.sum(P * np.log(P / Q))`
14. `a_fit, loc_fit, scale_fit = stats.gamma.fit(data)`
15.
```python
means = [
    np.mean(np.random.exponential(scale=1.0, size=30)) for _ in range(10000)
]
```

## Level 4
16.
```python
logits = np.array([2.0, 1.0, 0.1])
T = 2.0
exp_scaled = np.exp(logits / T)
probs = exp_scaled / np.sum(exp_scaled)
```
17.
```python
X = np.random.uniform(-3, 3, 1000)
y = 3 * X + 2 + np.random.normal(0, 0.5, 1000)
```
18. Bin predictions into 10 intervals, compute `np.abs(bin_acc - bin_conf)` weighted by bin size.
19. `z = np.random.normal(0, 1, size=(32, 10))`
20.
```python
preds = np.random.binomial(1, 0.75, size=(100000, 5))
print(np.mean(np.sum(preds, axis=1) >= 3))
```

## Level 5
21.
```python
x = np.random.uniform(0, 1, 100000)
integral = np.mean(np.exp(-(x**2)))
```
22. Draw $U \sim 	ext{Unif}(0, 1)$ using `np.random.uniform(0, 1, N)`, then compute $X = 	ext{stats.norm.ppf}(U)$.
23.
```python
cov_target = np.array([[4.0, 2.0], [2.0, 9.0]])
L = np.linalg.cholesky(cov_target)
Z = np.random.normal(0, 1, size=(100000, 2))
X = Z @ L.T
print(np.cov(X, rowvar=False))
```
