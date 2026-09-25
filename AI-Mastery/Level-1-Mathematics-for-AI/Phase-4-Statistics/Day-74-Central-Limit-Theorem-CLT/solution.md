# Day 74 Solutions: Central Limit Theorem (CLT)

## Level 1: Basic Concepts
1. Distribution of sample means of i.i.d. variables converges to Normal N(μ, σ^2/n) as n -> infty.
2. i.i.d. observations, finite mean, finite variance.
3. No! It claims the sample means distribution becomes Normal.
4. n >= 30.
5. CLT fails (converges to Stable / Cauchy distributions instead).

## Level 2: Calculation
6. Mean = 10, SE = 10 / sqrt(100) = 1.0.
7. Z = (12 - 10) / 1.0 = +2.0.
8. Sum mean = n p = 80; Sum std = sqrt(n p (1-p)) = sqrt(64) = 8.
9. Mean = 4, SE = sqrt(4 / 64) = 2 / 8 = 0.25. X_bar ~ N(4, 0.25^2).
10. SE = 12 / 6 = 2.0. Z = (52 - 50)/2 = +1.0. P(Z > 1) = 1 - 0.8413 = 15.87%.

## Level 3: Conceptual
11. Express characteristic function φ(t) of Z_n; Taylor expand log φ(t) around 0; limit as n -> infty yields e^(-t^2/2) (Gaussian characteristic function).
12. Cauchy distribution has undefined mean and infinite variance.
13. Berry-Esseen bound proves maximum absolute difference between empirical CDF and Gaussian CDF is bounded by O(1/sqrt(n)).
14. LLN states X_bar converges in probability to a constant μ; CLT describes the distribution shape of fluctuations around μ.
15. Adding/subtracting 0.5 to discrete values when approximating discrete Binomial with continuous Gaussian.

## Level 4: AI Applications
16. Errors represent sum of many unobserved independent random factors; by CLT, their sum is Gaussian.
17. Iterative addition of small independent noise steps accumulates into a Gaussian marginal distribution.
18. Mini-batch gradient is sample mean of b individual gradients; larger b enforces CLT convergence.
19. Difference in sample conversion rates between A and B is asymptotically Gaussian by CLT.
20. Summing predictions of independent weak learners produces Gaussian aggregate error.

## Level 5: Interview Solutions
21. LLN guarantees convergence to a point (X_bar -> μ); CLT describes the Gaussian shape of variation around that point.
22. See `code.py`.
23. Additive combination of independent factors -> Normal; Multiplicative combination -> Log-Normal (since sum of logs is Normal by CLT).
