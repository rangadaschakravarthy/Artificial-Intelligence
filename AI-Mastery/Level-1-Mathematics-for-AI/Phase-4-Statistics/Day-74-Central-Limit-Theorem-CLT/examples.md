# Day 74 Worked Examples: Central Limit Theorem (CLT)

## Example 1: Very Easy — Sample Size Threshold
Is sample size n = 40 large enough for CLT? Yes (rule of thumb n >= 30).

## Example 2: Beginner — Binomial Approximation via CLT
Flips n = 100, p = 0.5. μ = 50, σ = sqrt(100 * 0.5 * 0.5) = 5.
P(Sum >= 60) -> Z = (60 - 50)/5 = +2.0. Prob ≈ 2.28%.

## Example 3: Intermediate — Exponential Population CLT
Exponential data with λ = 0.2 (μ = 5, σ = 5). Sample n = 100.
SE = 5 / 10 = 0.5.
By CLT, X_bar ~ N(5, 0.5^2). P(4.5 <= X_bar <= 5.5) = P(-1 <= Z <= +1) ≈ 68.26%.

## Example 4: AI Focus — SGD Gradient Noise Normality
Mini-batch size b = 64. Average gradient g_bar across 64 samples converges to Gaussian N(∇L, Σ/64), stabilizing Adam optimizer updates.

## Example 5: Real-World AI — Web Traffic Latency Sums
Server requests latency: Exponentially skewed. Averaged across 500 concurrent users, mean latency distribution is perfectly Gaussian.
