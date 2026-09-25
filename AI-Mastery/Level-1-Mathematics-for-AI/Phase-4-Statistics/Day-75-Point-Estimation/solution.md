# Day 75 Solutions: Point Estimation

## Level 1: Basic Concepts
1. Statistic calculated from sample to provide a single-value estimate of population parameter.
2. E[θ_hat] - θ.
3. Minimum variance among unbiased estimators.
4. θ_hat converges in probability to true θ as n -> infty.
5. MSE = Bias^2 + Variance.

## Level 2: Calculation
6. MSE = (-0.5)^2 + 0.25 = 0.25 + 0.25 = 0.50.
7. x_bar = 80 / 5 = 16.0.
8. Bias = 0.95 θ - θ = -0.05 θ.
9. MSE(T1) = 0 + 9 = 9; MSE(T2) = 1^2 + 4 = 5. T2 is better.
10. p_hat = 45 / 150 = 0.30 (30%).

## Level 3: Conceptual
11. MSE = E[(θ_hat - θ)^2] = E[((θ_hat - E[θ_hat]) + (E[θ_hat] - θ))^2]. Expanding cross term vanishes since E[θ_hat - E[θ_hat]] = 0.
12. P(|x_bar - μ| >= ε) <= Var(x_bar)/ε^2 = σ^2 / (n ε^2) -> 0 as n -> infty. Consistent!
13. Sets a theoretical lower limit on the variance of any unbiased estimator: Var(θ_hat) >= 1 / I(θ).
14. If reducing variance by a large amount costs only a small increase in bias, overall MSE decreases.
15. MVUE is unbiased with minimum variance; MLE may be biased for small samples but is asymptotically efficient.

## Level 4: AI Applications
16. Increases weight estimation bias slightly while significantly reducing weight variance.
17. E[S_n^2] = ((n-1)/n) σ^2 < σ^2, under-estimating variance when n is small.
18. k=n (LOOCV) has low bias but high variance; k=5 has higher bias but lower variance.
19. Gradient descent seeks point estimates of network weights w that minimize empirical risk.
20. High variance means model fits sample noise instead of population trend.

## Level 5: Interview Solutions
21. MSE = E[(θ_hat - θ)^2] = E[((θ_hat - m) + (m - θ))^2] where m = E[θ_hat].
    = E[(θ_hat - m)^2] + 2(m - θ) E[θ_hat - m] + (m - θ)^2
    = Var(θ_hat) + 0 + Bias(θ_hat)^2.
22. See `code.py`.
23. I(θ) = E[( d/dθ log f(X; θ) )^2], measuring amount of information data carries about θ.
