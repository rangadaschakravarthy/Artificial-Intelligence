# Theory — Probability Distributions

## 1. Simple Definition
A probability distribution is a mathematical model that describes how probabilities are distributed over the possible values of a random variable.

## 2. Intuition
Think of distributions as pre-built mathematical shapes:
- **Bernoulli**: Single coin flip (Yes/No).
- **Binomial**: Count of Heads in $n$ flips.
- **Poisson**: Number of emails arriving per hour.
- **Uniform**: Flat probability across a range (equal likelihood).
- **Gaussian (Normal)**: Bell curve around an average value.

## 3. Mathematical Formulas Summary

| Distribution | Type | PMF / PDF | Mean $E[X]$ | Variance $	ext{Var}(X)$ |
| :--- | :--- | :--- | :--- | :--- |
| **Bernoulli$(p)$** | Discrete | $p^x (1-p)^{1-x}, x \in \{0,1\}$ | $p$ | $p(1-p)$ |
| **Binomial$(n, p)$** | Discrete | $inom{n}{x} p^x (1-p)^{n-x}$ | $n p$ | $n p (1-p)$ |
| **Poisson$(\lambda)$** | Discrete | $rac{\lambda^x e^{-\lambda}}{x!}, x \in \mathbb{N}_0$ | $\lambda$ | $\lambda$ |
| **Uniform$(a, b)$** | Continuous | $rac{1}{b-a}, x \in [a,b]$ | $rac{a+b}{2}$ | $rac{(b-a)^2}{12}$ |
| **Normal$(\mu, \sigma^2)$** | Continuous | $rac{1}{\sigma \sqrt{2\pi}} e^{-rac{(x-\mu)^2}{2\sigma^2}}$ | $\mu$ | $\sigma^2$ |

## 4. Notation
- $X \sim 	ext{Bern}(p)$
- $X \sim 	ext{Bin}(n, p)$
- $X \sim 	ext{Poisson}(\lambda)$
- $X \sim \mathcal{N}(\mu, \sigma^2)$

## 5. Step-by-Step Example (Binomial)
Flip 10 fair coins ($n=10, p=0.5$). Find probability of getting exactly 6 Heads:
$$P(X = 6) = inom{10}{6} (0.5)^6 (0.5)^4 = 210 	imes 0.015625 	imes 0.0625 = 210 	imes 0.0009765625 pprox 0.2051 = 20.51\%$$

## 6. Second Example (Poisson Web Traffic)
A website gets an average of $\lambda = 3$ API calls per second. Find $P(X = 0)$ calls in a second:
$$P(X = 0) = rac{3^0 e^{-3}}{0!} = e^{-3} pprox 0.0498 = 4.98\%$$

## 7. Common Mistakes
- Confusing standard deviation $\sigma$ with variance $\sigma^2$ in SciPy (`scale=sigma`, not `sigma**2`).
- Using Binomial when trials are dependent (Binomial requires independent trials).

## 8. AI Connection
- Binary Cross-Entropy assumes target $Y \sim 	ext{Bern}(p)$.
- Gaussian initialization (He/Xavier) prevents exploding/vanishing gradients.

## 9. Algorithm Connection
- **Kullback-Leibler (KL) Divergence**: Measures relative entropy between target distribution $P$ and model distribution $Q$.

## 10. Practical Interpretation
Matching model loss functions to data distributions is mandatory (e.g. Poisson Regression for count targets).

## 11. Interview Insight
**Q**: Why is the Gaussian distribution so prevalent in nature and AI?
**A**: Because of the Central Limit Theorem (sum of independent random variables converges to Gaussian distribution).

## 12. Summary
Standard probability distributions provide foundational templates for modeling AI data, parameters, and loss functions.
