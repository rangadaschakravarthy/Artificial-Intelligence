# Day 63 Solutions: Introduction to Statistics

## Level 1: Basic Concepts
1. Summarizing and describing features of a specific dataset.
2. Drawing conclusions/predictions about a population from sample data.
3. N is population size; n is sample size.
4. μ (mu).
5. x_bar.

## Level 2: Calculation
6. Mean = 90 / 5 = 18.
7. Mean = 1.5 / 3 = 0.5.
8. x_bar = 450 / 15 = 30.
9. Error rate = 30 / 200 = 0.15 (15%).
10. Total sum = 30 + 120 = 150. Total n = 5. Total mean = 30.

## Level 3: Conceptual
11. Because its value depends on the specific random sample drawn from the population.
12. By the Law of Large Numbers, variance of sample mean Var(x_bar) = σ^2 / n, which approaches 0 as n -> infinity.
13. sum (x_i - x_bar) = sum x_i - n x_bar = n x_bar - n x_bar = 0.
14. Selection bias arises from non-random sampling; sampling error is natural random variation.
15. Statistical inference handles stochastic uncertainty rather than exact deterministic outputs.

## Level 4: AI Applications
16. Validation set is a sample drawn to estimate model generalization performance on unseen population data.
17. Ensures sample observations are independent and identically distributed, required for ERM (Empirical Risk Minimization).
18. Unexpected identical sample statistics between train and test splits signal data leakage.
19. Annotator feedback sample not representing the broader human user population.
20. To report whether model A is statistically significantly better than model B.

## Level 5: Interview Solutions
21. An estimator whose expected value equals the true population parameter: E[T(X)] = θ.
22. E[x_bar] = E[(1/n) sum x_i] = (1/n) sum E[x_i] = (1/n) (n μ) = μ. Unbiased!
23. By filtering out features whose association with target y is not statistically significant (p > 0.05).
