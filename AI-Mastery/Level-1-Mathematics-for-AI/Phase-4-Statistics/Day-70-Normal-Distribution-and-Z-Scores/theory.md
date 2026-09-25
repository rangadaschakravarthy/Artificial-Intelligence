# Theory — Normal Distribution and Z-Scores

## 1. Simple Definition
The **Normal Distribution** is a symmetric, bell-shaped continuous probability distribution defined by mean $\mu$ and variance $\sigma^2$. The **$Z$-score** standardizes any normal variable into distances from the mean in units of standard deviation ($Z \sim \mathcal{N}(0, 1)$).

## 2. Intuition
A raw test score of 85 means little without context. If $\mu = 70$ and $\sigma = 5$, a score of 85 gives $Z = rac{85 - 70}{5} = +3.0$. You scored 3 standard deviations above average (top $0.13\%$ of participants!).

## 3. Mathematical Definitions
- **Gaussian PDF**:
  $$f(x) = rac{1}{\sigma \sqrt{2\pi}} \exp\left( -rac{(x - \mu)^2}{2\sigma^2} ight)$$
- **Standard Normal Transformation**:
  $$Z = rac{X - \mu}{\sigma} \implies Z \sim \mathcal{N}(0, 1)$$
- **Standard Normal PDF**:
  $$\phi(z) = rac{1}{\sqrt{2\pi}} e^{-rac{z^2}{2}}$$

## 4. 68-95-99.7 Empirical Rule
- $\mu \pm 1\sigma$: $\Phi(1) - \Phi(-1) pprox 68.27\%$ of data.
- $\mu \pm 2\sigma$: $\Phi(2) - \Phi(-2) pprox 95.45\%$ of data.
- $\mu \pm 3\sigma$: $\Phi(3) - \Phi(-3) pprox 99.73\%$ of data.

## 5. $Z$-Score Outlier Rule
In a Gaussian feature, points with $|Z| > 3.0$ (further than 3 standard deviations from mean) represent extreme tail values ($< 0.27\%$ probability) and are flagged as outliers.

## 6. AI Connection
Machine learning features scaled via `StandardScaler` ($Z = rac{X - \mu}{\sigma}$) ensure all feature dimensions have $E[Z]=0$ and $	ext{Var}(Z)=1$, optimizing neural network loss surfaces.

## 7. Summary
$Z$-score transforms raw metrics into scale-free standard deviations, powering standardization, outlier detection, and Gaussian probability lookups.
