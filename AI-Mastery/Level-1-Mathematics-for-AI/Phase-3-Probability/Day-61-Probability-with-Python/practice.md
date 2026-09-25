# Practice Problems — Probability with Python

## Level 1: Basic Concept Checks
1. What does SciPy method `ppf()` calculate?
2. Which NumPy function generates random floats in $[0.0, 1.0)$?
3. How do you fit continuous data to a Gaussian distribution in SciPy?
4. What is the convergence rate of Monte Carlo estimation error relative to sample count $S$?
5. How do you set random seed in modern NumPy?

## Level 2: Direct Calculations (Python Code)
6. Write Python code to find $P(X \le 2.5)$ for $X \sim \mathcal{N}(0, 1)$.
7. Write Python code to find 99th percentile of $X \sim 	ext{Exponential}(\lambda=0.1)$.
8. Write Python code to generate 5,000 samples from $	ext{Binomial}(n=20, p=0.4)$.
9. Compute sample mean and variance of samples from Q8.
10. Write Python code to calculate PMF $P(X=3)$ for $X \sim 	ext{Poisson}(\lambda=5)$.

## Level 3: Conceptual & Multi-Step Problems
11. Write a Python function to perform Bootstrap resampling on an array to compute 95% confidence interval of the mean.
12. Write a Monte Carlo simulation to estimate $P(X + Y > 5)$ where $X \sim 	ext{Unif}(0, 4)$ and $Y \sim 	ext{Unif}(0, 4)$ are independent.
13. Write Python code to compute KL Divergence $D_{KL}(P \parallel Q)$ between two discrete arrays $P$ and $Q$.
14. Use SciPy to fit a Gamma distribution `stats.gamma.fit(data)` to positive skew data.
15. Demonstrate the Central Limit Theorem in Python by plotting distribution of sample means for $N=30$ Exponential samples across 10,000 trials.

## Level 4: AI & ML Applications
16. Write Python code to perform Temperature Scaling on raw neural network logits array `logits = [2.0, 1.0, 0.1]` with $T=2.0$.
17. Write Python code to generate synthetic dataset $(X, y)$ for Linear Regression: $y = 3X + 2 + \epsilon$, $\epsilon \sim \mathcal{N}(0, 0.5^2)$.
18. Write Python code to compute Expected Calibration Error (ECE) for predicted probabilities and true binary labels.
19. Write Python code to sample latent vectors $\mathbf{z} \sim \mathcal{N}(\mathbf{0}, \mathbf{I}_{10})$ for a generative model batch of size 32.
20. Write Python code to estimate the probability that an ensemble of 5 models (accuracy 0.75 each) outputs majority correct prediction using Monte Carlo.

## Level 5: Interview Questions
21. Write a complete, self-contained Python script to estimate the integral $\int_0^1 e^{-x^2} dx$ using Monte Carlo integration.
22. Explain how Inverse Transform Sampling is implemented in Python using `scipy.stats` PPF function.
23. Write Python code demonstrating that empirical covariance matrix of 100,000 samples converges to theoretical covariance matrix $oldsymbol{\Sigma} = egin{bmatrix} 4 & 2 \ 2 & 9 \end{bmatrix}$.
