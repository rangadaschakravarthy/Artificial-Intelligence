# Practice Problems — Bernoulli and Binomial Statistical Foundations

## Level 1: Basic Concept Checks
1. State the formula for sample proportion $\hat{p}$.
2. State the formula for Standard Error of proportion $SE(\hat{p})$.
3. What two conditions must be satisfied for Normal approximation to Binomial?
4. What is the continuity correction used for?
5. Why does standard error $SE(\hat{p})$ decrease as sample size $n$ increases?

## Level 2: Direct Calculations
6. In a dataset of $n=1000$ emails, 250 are spam. Compute $\hat{p}$ and $SE(\hat{p})$.
7. For $n=100, p=0.4$, compute mean $\mu$ and standard deviation $\sigma$ of Binomial count $X$.
8. Compute $95\%$ confidence interval margin of error for $\hat{p}=0.50$ with $n=400$.
9. If $\hat{p}=0.10$ and $n=900$, compute $SE(\hat{p})$.
10. Check if Normal approximation is valid for $n=200, p=0.08$.

## Level 3: Conceptual & Multi-Step Problems
11. Derive $E[\hat{p}] = p$ showing that sample proportion is an unbiased estimator of population proportion $p$.
12. Derive $	ext{Var}(\hat{p}) = rac{p(1-p)}{n}$ using linearity of variance on independent Bernoulli indicator variables.
13. Show that $p(1-p)$ achieves its maximum value at $p = 0.50$, proving that standard error is highest at $p=0.50$.
14. Explain why Wilson Score interval or Clopper-Pearson exact interval is preferred over Normal approximation interval when $p$ is close to 0 or 1.
15. Determine the sample size $n$ required to estimate a proportion with margin of error $E = 0.03$ at $95\%$ confidence (worst-case $p=0.5$).

## Level 4: AI & ML Applications
16. Write Python code using `statsmodels` to compute Wilson score confidence interval for $X=12$ successes in $n=100$ trials ($p=0.12$).
17. Write Python code to simulate 10,000 Binomial draws $X \sim 	ext{Bin}(100, 0.5)$ and plot overlay with Normal PDF $\mathcal{N}(50, 25)$.
18. In A/B testing, click-through rates are $\hat{p}_A = 0.10 (n_A=1000)$ and $\hat{p}_B = 0.13 (n_B=1000)$. Compute pooled $SE$.
19. Compute $Z$-score for testing $H_0: p_A = p_B$ using metrics in Q18.
20. Explain how sample size estimation prevents underpowered A/B tests in production AI deployments.

## Level 5: Interview Questions
21. Prove De Moivre–Laplace Theorem showing that Binomial PMF converges to Normal PDF as $n 	o \infty$ using Stirling's approximation.
22. Derive the required sample size formula $n = rac{Z_{lpha/2}^2 p (1-p)}{E^2}$ for proportion estimation.
23. Write Python code using `statsmodels` to perform a 2-sample $Z$-test for proportions on A/B test conversion data.
