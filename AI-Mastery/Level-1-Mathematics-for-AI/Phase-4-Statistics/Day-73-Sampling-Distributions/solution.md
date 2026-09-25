# Day 73 Solutions: Sampling Distributions

## Level 1: Basic Concepts
1. Distribution of a sample statistic over repeated sampling.
2. SD is variability of individual data points; SE is variability of sample statistic.
3. Decreases SE by factor of 1/sqrt(n).
4. Equal to population mean μ.
5. SE = σ / sqrt(n).

## Level 2: Calculation
6. SE = 12 / sqrt(36) = 12 / 6 = 2.0.
7. SE = sqrt(0.4 * 0.6 / 400) = sqrt(0.24 / 400) = sqrt(0.0006) = 0.0245.
8. 1.0 = 20 / sqrt(n) => sqrt(n) = 20 => n = 400.
9. SE = 50 / 10 = 5. Z_lower = (490-500)/5 = -2; Z_upper = (510-500)/5 = +2. Prob = 95.44%.
10. Var(X_bar) = 64 / 16 = 4.0.

## Level 3: Conceptual
11. E[X_bar] = E[(1/n) sum X_i] = (1/n) sum E[X_i] = (1/n) (n μ) = μ.
12. Var(X_bar) = Var((1/n) sum X_i) = (1/n^2) sum Var(X_i) = (1/n^2) (n σ^2) = σ^2 / n (since X_i are independent).
13. Sum of squared standard normal variables follows Chi-Square distribution with n-1 degrees of freedom.
14. Halving error requires 4x data; reducing error by 10x requires 100x data.
15. FPC multiplier sqrt((N-n)/(N-1)) adjusts SE when sampling without replacement from small finite N.

## Level 4: AI Applications
16. Averaging B independent models trained on bootstrap samples reduces model variance by factor of 1/B.
17. Assesses precision of Monte Carlo integral approximations.
18. Sample B bootstrap datasets, train model on each, construct 2.5% and 97.5% prediction quantiles.
19. Small CV test folds increase sample-to-sample variance of score estimates.
20. Small batch size n means high mini-batch gradient sampling error (SE = σ/sqrt(n)).

## Level 5: Interview Solutions
21. Var(X_bar) = Var((1/n) sum X_i) = (1/n^2) sum Var(X_i) = (1/n^2) (n σ^2) = σ^2 / n.
22. See `code.py`.
23. Samples with replacement from sample data as an empirical proxy for sampling from population.
