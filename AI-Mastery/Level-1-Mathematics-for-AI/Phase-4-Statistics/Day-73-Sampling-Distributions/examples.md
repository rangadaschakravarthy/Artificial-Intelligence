# Day 73 Worked Examples: Sampling Distributions

## Example 1: Very Easy — Standard Error Calculation
Population σ = 20, Sample n = 100.
SE = 20 / sqrt(100) = 20 / 10 = 2.0.

## Example 2: Beginner — Comparing Sample Sizes
n1 = 16 => SE1 = σ / 4.
n2 = 64 => SE2 = σ / 8.
Quadrupling sample size halves the standard error.

## Example 3: Intermediate — Probability Bounds on Sample Mean
Population μ = 50, σ = 10, n = 25. SE = 10 / 5 = 2.0.
Find P(46 <= X_bar <= 54).
Z_lower = (46 - 50)/2 = -2.0. Z_upper = (54 - 50)/2 = +2.0.
Probability = 0.9544 (95.44%).

## Example 4: AI Focus — Bootstrap Resampling for Loss Uncertainty
Dataset size 1,000. Sample 100 bootstrap datasets with replacement.
Train 100 models -> 100 test losses form sampling distribution of test accuracy.

## Example 5: Real-World AI — AB Testing Sample Size Design
To reduce sample proportion standard error below 0.01 for p=0.5:
0.01 = sqrt(0.25 / n) => 0.0001 = 0.25 / n => n = 2,500 users needed.
