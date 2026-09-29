# Theory — Probability with Python

## 1. Overview
Python provides two primary ecosystems for probability:
1. `numpy.random`: High-performance vector sampling.
2. `scipy.stats`: Comprehensive statistical distributions with exact analytical methods (`pdf`, `cdf`, `ppf`, `fit`, `rvs`).

## 2. Key SciPy Methods
For any statistical distribution object `dist = stats.norm(loc=mu, scale=sigma)`:
- `dist.rvs(size)`: Generate Random Variates (Samples).
- `dist.pdf(x)`: Probability Density Function value.
- `dist.pmf(k)`: Probability Mass Function value (discrete).
- `dist.cdf(x)`: Cumulative Distribution Function $P(X \le x)$.
- `dist.ppf(q)`: Percent Point Function (Inverse CDF / Quantile) $F^{-1}(q)$.
- `dist.interval(alpha)`: Confidence Interval for coverage $lpha$.

## 3. Monte Carlo Method
Monte Carlo simulation approximates expected values $E[g(X)]$ by drawing $S$ independent random samples and computing average:

$$
E[g(X)] pprox \frac{1}{S} \sum_{s=1}^S g(x^{(s)}), \quad x^{(s)} \sim P(X)
$$

By Law of Large Numbers, error decreases at rate $O\left(\frac{1}{\sqrt{S}}
ight)$.

## 4. Fitting Distributions
To find parameters $\hat{	heta}$ that best model empirical dataset `data`:
```python
mu_fit, std_fit = stats.norm.fit(data)
```

## 5. Common Mistakes
- Using legacy `np.random.rand()` instead of recommended modern Generator `rng = np.random.default_rng()`.
- Passing variance $\sigma^2$ instead of standard deviation $\sigma$ to `scipy.stats.norm(scale=sigma)`.

## 6. AI Connection
Monte Carlo sampling powers Reinforcement Learning (MCTS in AlphaGo), Bayesian Neural Networks, and Diffusion Model image generation steps.

## 7. Summary
`scipy.stats` and `numpy.random` provide complete tools for sampling, evaluating density, finding quantiles, and fitting probability models.
