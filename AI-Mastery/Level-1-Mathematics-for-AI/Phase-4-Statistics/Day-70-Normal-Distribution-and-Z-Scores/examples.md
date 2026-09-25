# Worked Examples — Normal Distribution and Z-Scores

## Example 1: Z-Score Calculation
**Problem**: Feature $X \sim \mathcal{N}(50, 10^2)$. Compute $Z$-score for $x = 65$.
**Solution**:
1. $Z = rac{x - \mu}{\sigma} = rac{65 - 50}{10} = rac{15}{10} = +1.5$.
2. $x = 65$ lies 1.5 standard deviations above the mean.

## Example 2: Probability from Z-Score Table
**Problem**: Find $P(X \le 65)$ using $Z = +1.5$ from Example 1.
**Solution**:
1. Look up Standard Normal CDF $\Phi(1.5)$.
2. $\Phi(1.5) pprox 0.9332$.
3. $P(X \le 65) = 93.32\%$.

## Example 3: Empirical Rule Interval
**Problem**: $X \sim \mathcal{N}(100, 15^2)$ (IQ scores). What range contains $95.45\%$ of population IQs?
**Solution**:
1. $\mu \pm 2\sigma = 100 \pm 2(15) = 100 \pm 30$.
2. Range is $[70, 130]$.

## Example 4: Z-Score Outlier Detection
**Problem**: Server memory usage feature has $\mu = 40$ GB, $\sigma = 5$ GB. A reading shows $58$ GB. Is it an outlier ($|Z| > 3.0$)?
**Solution**:
1. $Z = rac{58 - 40}{5} = rac{18}{5} = 3.6$.
2. Since $|3.6| > 3.0$, reading $58$ GB IS an outlier.

## Example 5: Custom StandardScaler Implementation
**Problem**: Standardize array `[10, 20, 30, 40, 50]` in NumPy.
**Solution**:
```python
import numpy as np

x = np.array([10, 20, 30, 40, 50])
z = (x - np.mean(x)) / np.std(x)
# z has mean 0.0 and std 1.0
```
