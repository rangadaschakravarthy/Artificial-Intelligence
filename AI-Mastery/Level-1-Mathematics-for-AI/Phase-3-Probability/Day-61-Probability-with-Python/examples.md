# Worked Examples — Probability with Python

## Example 1: SciPy Quantile / PPF Calculation
**Problem**: Find 95th percentile value of $X \sim \mathcal{N}(100, 15^2)$.
**Solution**:
```python
from scipy import stats

dist = stats.norm(loc=100, scale=15)
val_95 = dist.ppf(0.95)
# val_95 approx 124.67
```

## Example 2: Monte Carlo Estimation of $\pi$
**Problem**: Estimate value of $\pi$ by sampling 100,000 points uniformly in square $[-1, 1] 	imes [-1, 1]$.
**Solution**:
```python
import numpy as np

N = 100000
x = np.random.uniform(-1, 1, N)
y = np.random.uniform(-1, 1, N)
inside_circle = (x**2 + y**2) <= 1.0
pi_estimate = 4.0 * np.mean(inside_circle)
# pi_estimate approx 3.1416
```

## Example 3: Fitting Normal Distribution
**Problem**: Fit empirical data samples to Normal distribution.
**Solution**:
```python
from scipy import stats
import numpy as np

data = np.random.normal(loc=5.0, scale=2.0, size=1000)
mu_hat, std_hat = stats.norm.fit(data)
# mu_hat approx 5.0, std_hat approx 2.0
```

## Example 4: Poisson Confidence Interval
**Problem**: Compute 90% central interval for $X \sim 	ext{Poisson}(\lambda = 20)$.
**Solution**:
```python
from scipy import stats

dist = stats.poisson(mu=20)
low, high = dist.interval(0.90)
# low=13.0, high=27.0
```

## Example 5: Sampling from Custom Discrete Distribution
**Problem**: Sample 1000 items from categories `['A', 'B', 'C']` with probabilities `[0.5, 0.3, 0.2]`.
**Solution**:
```python
import numpy as np

samples = np.random.choice(
    ['A', 'B', 'C'], size=1000, p=[0.5, 0.3, 0.2]
)
```
