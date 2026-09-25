# Practice Problems — Probability Distributions

## Level 1: Basic Concept Checks
1. State the mean and variance of $X \sim 	ext{Bern}(p)$.
2. What distribution models the number of successes in $n$ independent trials?
3. State the mean and variance of $X \sim 	ext{Poisson}(\lambda)$.
4. Name the key parameter(s) of a Normal distribution $\mathcal{N}(\mu, \sigma^2)$.
5. Which distribution has a flat constant density on $[a, b]$?

## Level 2: Direct Calculations
6. Let $X \sim 	ext{Bin}(10, 0.3)$. Compute $E[X]$ and $	ext{Var}(X)$.
7. For $X \sim 	ext{Bin}(5, 0.5)$, compute $P(X = 3)$.
8. For $X \sim 	ext{Poisson}(4)$, compute $P(X = 1)$.
9. For $X \sim 	ext{Uniform}(0, 10)$, compute $P(2 \le X \le 7)$.
10. For $X \sim \mathcal{N}(100, 25)$, compute standard deviation $\sigma$ and $z$-score for $x = 110$.

## Level 3: Conceptual & Multi-Step Problems
11. Show that the Binomial distribution converges to Poisson distribution when $n 	o \infty$, $p 	o 0$ with $\lambda = n p$ constant.
12. Derive $E[X] = \lambda$ for $X \sim 	ext{Poisson}(\lambda)$.
13. If $X_1, \dots, X_n \stackrel{iid}{\sim} 	ext{Bern}(p)$, show that $Y = \sum X_i \sim 	ext{Bin}(n, p)$.
14. Compute $E[X^4]$ for standard normal $X \sim \mathcal{N}(0, 1)$ using integration by parts.
15. If $X \sim \mathcal{N}(\mu_1, \sigma_1^2)$ and $Y \sim \mathcal{N}(\mu_2, \sigma_2^2)$ are independent, state the distribution of $Z = X + Y$.

## Level 4: AI & ML Applications
16. In Kaiming (He) Normal Initialization, weights are drawn from $\mathcal{N}\left(0, rac{2}{d_{in}}ight)$. Find $\sigma$ for $d_{in} = 512$.
17. A text generator outputs tokens where word count per document follows Poisson Distribution with $\lambda = 200$. Compute standard deviation of document lengths.
18. Softmax probabilities define a Categorical distribution (generalized Bernoulli). Write its log-likelihood loss for target class $y$.
19. In diffusion models, forward noise adding process adds Gaussian noise $q(x_t | x_{t-1}) = \mathcal{N}(x_t; \sqrt{1-eta_t} x_{t-1}, eta_t I)$. State mean vector.
20. Explain why linear regression with Gaussian errors $\epsilon \sim \mathcal{N}(0, \sigma^2)$ leads to Mean Squared Error (MSE) loss under MLE.

## Level 5: Interview Questions
21. Derive the Mean and Variance of $X \sim 	ext{Bin}(n, p)$ using linearity of expectation on indicator variables.
22. Explain how the Gaussian distribution maximizes Differential Entropy among all distributions with fixed mean $\mu$ and variance $\sigma^2$.
23. Write Python code using SciPy to sample 10,000 points from $\mathcal{N}(0, 1)$ and verify mean and variance numerically.
