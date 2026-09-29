# Theory — Continuous Random Variables

## 1. Simple Definition
A continuous random variable takes values in a continuous range (an interval of real numbers). Because there are infinitely many points, the probability of hitting any exact single number is zero ($P(X = x) = 0$). Instead, we use a **Probability Density Function (PDF)** to find probabilities over intervals.

## 2. Intuition
Imagine height in centimeters. What is the probability someone is EXACTLY 175.49281... cm tall? Zero. But what is the probability someone is BETWEEN 175 cm and 176 cm tall? That is a positive probability, equal to the area under the density curve between 175 and 176.

## 3. Mathematical Definition
Let $X$ be a continuous random variable with PDF $f_X(x): \mathbb{R} \to [0, \infty)$.
- **Probability over Interval**: $P(a \le X \le b) = \int_a^b f_X(x) dx$
- **CDF**: $F_X(x) = P(X \le x) = \int_{-\infty}^x f_X(t) dt$

## 4. Fundamental Relationship (Calculus)

$$
f(x) = \frac{d}{dx} F(x) = F'(x)
$$

## 5. PDF Conditions
1. Non-negativity: $f(x) \ge 0$ for all $x$.
2. Normalization: $\int_{-\infty}^{\infty} f(x) dx = 1$.

## 6. Symbol Explanation
- $f(x)$: Probability Density Function (height of curve).
- $F(x)$: Cumulative Distribution Function (accumulated area).
- $\int$: Definite integral (area under density curve).

## 7. Step-by-Step Calculation
Uniform distribution on $[0, 2]$. $f(x) = 0.5$ for $x \in [0, 2]$.
Find $P(0.5 \le X \le 1.5)$:

$$
P(0.5 \le X \le 1.5) = \int_{0.5}^{1.5} 0.5 dx = [0.5 x]_{0.5}^{1.5} = 0.5(1.5 - 0.5) = 0.5(1.0) = 0.50
$$

## 8. Second Example (Gaussian PDF in Machine Learning)
Standard Normal distribution $\mathcal{N}(0, 1)$:

$$
f(x) = \frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}}
$$

- $P(-1 \le X \le 1) = \int_{-1}^1 \frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}} dx pprox 0.6827$ ($68.27\%$ empirical rule).

## 9. Common Mistakes
- Thinking PDF height $f(x)$ cannot exceed 1 (PDF is density, not probability; $f(x)$ can be $> 1$ as long as integral equals 1).
- Confusing $f(x)$ (PDF) with $F(x)$ (CDF).

## 10. AI Connection
Gaussian distributions $\mathcal{N}(\mu, \sigma^2)$ are used everywhere in AI: weight initialization, VAE latent space representations, and Gaussian Processes.

## 11. Algorithm Connection
- **Variational Autoencoders (VAEs)**: Use KL Divergence between continuous latent PDF $q_\phi(z|x)$ and prior standard normal PDF $p(z) = \mathcal{N}(0, I)$.

## 12. Practical Interpretation
Regression models predict continuous conditional expectations $E[Y|X]$ and output predictive variance $\sigma^2$.

## 13. Interview Insight
**Q**: Why is $P(X = x) = 0$ for continuous random variables?
**A**: Because an exact point has zero width. Definite integral $\int_x^x f(t)dt = 0$.

## 14. Summary
Continuous RVs use PDFs $f(x)$ to define interval probabilities via integration $\int_a^b f(x) dx$.
