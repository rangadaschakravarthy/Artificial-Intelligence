# Theory — Expectation and Variance

## 1. Simple Definition
- **Expectation $E[X]$**: The long-run average value of a random variable across infinite repeated trials.
- **Variance $	ext{Var}(X)$**: A measure of how spread out the values of a random variable are around its mean.

## 2. Intuition
Imagine two AI models with $90\%$ average accuracy ($E[X] = 0.90$).
- Model A accuracy varies between $89\%$ and $91\%$ (Low Variance).
- Model B accuracy swings wildly between $60\%$ and $100\%$ (High Variance).
Variance tells you about reliability and stability.

## 3. Mathematical Definitions
- **Discrete Expectation**: $E[X] = \sum_{x} x \cdot p(x)$
- **Continuous Expectation**: $E[X] = \int_{-\infty}^{\infty} x \cdot f(x) dx$
- **Variance**: $	ext{Var}(X) = E[(X - \mu)^2] = E[X^2] - (E[X])^2$, where $\mu = E[X]$.
- **Standard Deviation**: $\sigma_X = \sqrt{	ext{Var}(X)}$

## 4. Fundamental Properties
- **Linearity of Expectation**:
  

$$
E[a X + b Y + c] = a E[X] + b E[Y] + c
$$

  *(Note: Holds ALWAYS, regardless of whether $X$ and $Y$ are independent!)*
- **Variance Rules**:
  

$$
ext{Var}(a X + b) = a^2 	ext{Var}(X)
$$

  

$$
ext{Var}(X + Y) = 	ext{Var}(X) + 	ext{Var}(Y) + 2 	ext{Cov}(X, Y)
$$

  *(If $X, Y$ are independent, $	ext{Cov}(X, Y) = 0 \implies 	ext{Var}(X + Y) = 	ext{Var}(X) + 	ext{Var}(Y)$)*

## 5. Notation
- $E[X]$ or $\mu$: Expectation / Mean.
- $	ext{Var}(X)$ or $\sigma^2$: Variance.
- $\sigma$: Standard Deviation.

## 6. Step-by-Step Calculation
Discrete RV $X$: $P(X=1)=0.2, P(X=2)=0.5, P(X=3)=0.3$.
1. $E[X] = 1(0.2) + 2(0.5) + 3(0.3) = 0.2 + 1.0 + 0.9 = 2.1$.
2. $E[X^2] = 1^2(0.2) + 2^2(0.5) + 3^2(0.3) = 1(0.2) + 4(0.5) + 9(0.3) = 0.2 + 2.0 + 2.7 = 4.9$.
3. $	ext{Var}(X) = E[X^2] - (E[X])^2 = 4.9 - (2.1)^2 = 4.9 - 4.41 = 0.49$.
4. $\sigma = \sqrt{0.49} = 0.70$.

## 7. Second Example (Feature Standardization in AI)
Standardizing feature $X$: $Z = \frac{X - \mu}{\sigma}$.
- $E[Z] = E\left[\frac{X - \mu}{\sigma}
ight] = \frac{E[X] - \mu}{\sigma} = \frac{\mu - \mu}{\sigma} = 0$.
- $	ext{Var}(Z) = 	ext{Var}\left(\frac{X - \mu}{\sigma}
ight) = \frac{1}{\sigma^2} 	ext{Var}(X - \mu) = \frac{\sigma^2}{\sigma^2} = 1$.
Standardized variable $Z$ has Mean 0 and Variance 1!

## 8. Common Mistakes
- Thinking $	ext{Var}(aX) = a 	ext{Var}(X)$ instead of $a^2 	ext{Var}(X)$.
- Thinking $	ext{Var}(X - Y) = 	ext{Var}(X) - 	ext{Var}(Y)$ (it is $	ext{Var}(X) + 	ext{Var}(Y)$ for independent variables!).

## 9. AI Connection
Bias-Variance Tradeoff: Total Expected Generalization Error $= 	ext{Bias}^2 + 	ext{Variance} + \sigma_{	ext{noise}}^2$.

## 10. Algorithm Connection
- **Batch Normalization**: Zero-centers and normalizes hidden activations using batch expectation and variance.

## 11. Practical Interpretation
Standardizing input features to $E[X]=0, 	ext{Var}(X)=1$ accelerates neural network gradient descent convergence.

## 12. Interview Insight
**Q**: Does Linearity of Expectation require independence between variables?
**A**: NO! $E[X + Y] = E[X] + E[Y]$ holds for ALL random variables, dependent or independent.

## 13. Summary
Expectation measures central tendency; variance measures dispersion. Linearity of expectation and variance scaling rules govern AI optimization and data normalization.
