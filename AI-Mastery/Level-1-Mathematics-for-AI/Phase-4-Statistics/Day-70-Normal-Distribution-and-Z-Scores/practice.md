# Practice Problems — Normal Distribution and Z-Scores

## Level 1: Basic Concept Checks
1. State the formula for $Z$-score transformation.
2. What are the mean and variance of the Standard Normal distribution $\mathcal{N}(0, 1)$?
3. State the 68-95-99.7 Empirical Rule percentages.
4. What threshold of $|Z|$ is commonly used for Gaussian outlier detection?
5. Write standard normal PDF formula $\phi(z)$.

## Level 2: Direct Calculations
6. Given $X \sim \mathcal{N}(100, 16)$ (so $\mu=100, \sigma=4$). Compute $Z$-score for $x = 108$.
7. Using $Z = 2.0$, compute $P(Z > 2.0)$ given $\Phi(2.0) = 0.9772$.
8. Compute $P(-1.0 \le Z \le 1.0)$ given $\Phi(1.0) = 0.8413$ and $\Phi(-1.0) = 0.1587$.
9. If $Z = -2.5, \mu = 50, \sigma = 10$, recover raw value $x$.
10. Standardize feature array `[2, 4, 6]` manually.

## Level 3: Conceptual & Multi-Step Problems
11. Prove that $E[Z] = 0$ and $	ext{Var}(Z) = 1$ for $Z = \frac{X - \mu}{\sigma}$.
12. Show that inflection points of Gaussian PDF $f(x)$ occur exactly at $x = \mu - \sigma$ and $x = \mu + \sigma$.
13. Prove that $f(x)$ achieves its global maximum at $x = \mu$ with value $\frac{1}{\sigma \sqrt{2\pi}}$.
14. Explain why standardizing features is essential for gradient descent algorithms (logistic regression, neural networks).
15. Explain why standardizing features is essential for distance-based ML algorithms (k-NN, SVM, K-Means).

## Level 4: AI & ML Applications
16. Write Python code implementing `StandardScaler` (fit and transform methods) from scratch using NumPy.
17. Write Python code to filter out rows where any numerical feature has $|Z| > 3.0$.
18. In Gaussian Mixture Models, express the component probability density function $\mathcal{N}(\mathbf{x}; oldsymbol{\mu}_k, oldsymbol{\Sigma}_k)$.
19. Compute raw values $x$ corresponding to 90th percentile of $\mathcal{N}(50, 100)$ using SciPy `stats.norm.ppf(0.90)`.
20. In neural network weight initialization (He Normal), weights are drawn from $\mathcal{N}\left(0, \frac{2}{d_{in}}
ight)$. Compute $Z$-score threshold for $W = 0.10$ when $d_{in} = 512$.

## Level 5: Interview Questions
21. Prove that standard normal PDF $\phi(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2}$ integrates to 1 over $(-\infty, \infty)$ using polar coordinates.
22. Differentiate `StandardScaler` ($Z$-score normalization) vs `MinMaxScaler` ($[0, 1]$ normalization). When is each preferred?
23. Write Python code using NumPy and SciPy to perform $Z$-score standardization, detect $|Z| > 3$ outliers, and output cleaned data.
