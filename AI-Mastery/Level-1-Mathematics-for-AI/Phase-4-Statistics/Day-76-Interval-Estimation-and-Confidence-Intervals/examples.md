# Day 76 Worked Examples: Interval Estimation & Confidence Intervals

## Example 1: Very Easy — 95% Z-Interval Calculation
x_bar = 20, SE = 2, 95% confidence (Z = 1.96).
ME = 1.96 * 2 = 3.92. CI = [16.08, 23.92].

## Example 2: Beginner — Proportion CI for Model Accuracy
Model correctly classifies 450 out of 500 images. p_hat = 0.90.
SE = sqrt(0.90 * 0.10 / 500) = sqrt(0.00018) = 0.0134.
95% CI = 0.90 ± 1.96(0.0134) = 0.90 ± 0.0263 = [87.37%, 92.63%].

## Example 3: Intermediate — Sample Size Calculation for Target Width
Want 95% CI margin of error ME <= 1.0 for σ = 10.
1.0 = 1.96 * (10 / sqrt(n)) => sqrt(n) = 19.6 => n = 384.16 -> Need n = 385 samples.

## Example 4: AI Focus — Difference of Means in A/B Testing
Control CTR: p_A = 0.05 (n_A = 10,000). Treatment CTR: p_B = 0.06 (n_B = 10,000).
Difference diff = 0.01. SE_diff = sqrt(0.05*0.95/10k + 0.06*0.94/10k) = 0.0032.
95% CI on uplift = 0.01 ± 1.96(0.0032) = [0.0037, 0.0163].
Since interval is entirely > 0, Treatment B is statistically significantly superior!

## Example 5: Real-World AI — UCB Multi-Armed Bandit Strategy
Arm action value estimate Q(a) + c * sqrt(log(t) / N(a)). The second term is a confidence interval width term encouraging exploration of uncertain actions!
