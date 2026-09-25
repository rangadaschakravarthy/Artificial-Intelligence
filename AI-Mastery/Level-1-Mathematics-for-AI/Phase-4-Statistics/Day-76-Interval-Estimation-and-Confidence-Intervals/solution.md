# Day 76 Solutions: Interval Estimation & Confidence Intervals

## Level 1: Basic Concepts
1. Range of plausible values for population parameter at specified confidence level.
2. ME = Critical Value * Standard Error (half-width of CI).
3. 90%: 1.645; 95%: 1.960; 99%: 2.576.
4. When population std σ is unknown AND sample size n < 30.
5. Shrinks CI width (increases precision).

## Level 2: Calculation
6. SE = 10 / 10 = 1. ME = 1.96(1) = 1.96. CI = [73.04, 76.96].
7. ME = 2.576(1) = 2.576. CI = [72.424, 77.576].
8. SE = 4 / 4 = 1. ME = 2.131(1) = 2.131. CI = [27.869, 32.131].
9. SE = sqrt(0.6*0.4/100) = sqrt(0.0024) = 0.04899. ME = 1.96(0.04899) = 0.096. CI = [0.504, 0.696].
10. 0.5 = 1.96 * 5 / sqrt(n) => sqrt(n) = 19.6 => n = 384.16 -> n = 385.

## Level 3: Conceptual
11. Over infinite repeated random samplings of size n, 95% of calculated CIs will contain the true parameter.
12. ME = Z * σ / sqrt(n) => sqrt(n) = Z * σ / ME => n = (Z * σ / ME)^2.
13. t-distribution has heavier tails to account for uncertainty in estimating σ using sample s.
14. Higher variance directly increases SE, making CI wider.
15. Guarantees sample size is large enough for Central Limit Theorem to approximate Binomial distribution as Gaussian.

## Level 4: AI Applications
16. Resample test set B times, compute metric on each, take 2.5th and 97.5th percentiles.
17. Action selection: a_t = argmax [ Q(a) + c * sqrt(ln(t) / N(a)) ]. Unvisited actions have large confidence terms.
18. Implies no statistically significant difference between treatment and control at chosen confidence level.
19. Exposes high variance in model evaluation metrics on small benchmark sets.
20. Out-of-distribution inputs have higher prediction variance σ^2.

## Level 5: Interview Solutions
21. Frequentist CI: True parameter is fixed; 95% of intervals contain it. Bayesian Credible Interval: Parameter is a random variable; 95% probability parameter lies within interval given prior and data.
22. See `code.py`.
23. If 95% CI for β_1 does not contain 0, feature x has a statistically significant non-zero linear relationship with y.
