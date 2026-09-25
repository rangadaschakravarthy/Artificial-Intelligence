# Day 76 Theory: Interval Estimation & Confidence Intervals

### 1. Simple Definition
A Confidence Interval (CI) provides a range of plausible values for an unknown population parameter, accompanied by a confidence level (e.g. 95%) quantifying estimation certainty.

### 2. Intuition
Instead of guessing a single point estimate ("the mean height is 170 cm"), a confidence interval gives a safe range ("we are 95% confident the true mean height is between 167 cm and 173 cm").

### 3. Mathematical Definition
A (1 - α) Confidence Interval for parameter θ is an interval [L, U] computed from sample data such that:
P(L <= θ <= U) = 1 - α.

Common confidence levels:
- 90% (α = 0.10, Z_{α/2} = 1.645)
- 95% (α = 0.05, Z_{α/2} = 1.960)
- 99% (α = 0.01, Z_{α/2} = 2.576)

### 4. Mathematical Notation
CI = Point Estimate ± Margin of Error (ME)
ME = Critical Value * Standard Error

### 5. Formula
Z-Interval (Known σ or large n):
CI = x_bar ± Z_{α/2} * (σ / sqrt(n))

t-Interval (Unknown σ, small n < 30):
CI = x_bar ± t_{α/2, df} * (s / sqrt(n))

Proportion Interval:
CI = p_hat ± Z_{α/2} * sqrt( p_hat (1 - p_hat) / n )

### 6. Symbol Explanation
- Z_{α/2}: Critical value from standard normal distribution
- t_{α/2, df}: Critical value from Student-t distribution with df = n - 1 degrees of freedom
- Margin of Error (ME): Half-width of the confidence interval

### 7. Step-by-Step Calculation
Sample x_bar = 100, s = 15, n = 36. Compute 95% CI.
Step 1: n = 36 >= 30 => Use Z-interval. Z_{0.025} = 1.96.
Step 2: Compute SE = 15 / sqrt(36) = 15 / 6 = 2.5.
Step 3: Margin of Error ME = 1.96 * 2.5 = 4.9.
Step 4: CI = 100 ± 4.9 = [95.1, 104.9].
Interpretation: We are 95% confident that the true population mean μ lies between 95.1 and 104.9.

### 8. Second Concrete Example
Small sample n = 10, x_bar = 50, s = 6. 95% t-interval (df = 9).
t_{0.025, 9} = 2.262.
SE = 6 / sqrt(10) = 1.897.
ME = 2.262 * 1.897 = 4.29.
CI = 50 ± 4.29 = [45.71, 54.29]. (Wider than Z-interval due to small sample size!).

### 9. Common Mistakes
- Misinterpreting 95% CI as "there is a 95% probability that the true parameter lies in this specific calculated interval" (the true parameter is fixed; 95% means 95% of constructed intervals across repeated sampling will cover the true parameter!).
- Using Z-critical values instead of t-critical values when n < 30 and population std σ is unknown.

### 10. AI Connection
Reporting model test accuracy as 88% ± 2.1% (95% CI) provides rigorous proof of performance stability in production deployment.

### 11. Algorithm Connection
- A/B Testing: Confidence intervals on difference between treatment and control means (μ_A - μ_B).
- Upper Confidence Bound (UCB) algorithm in Multi-Armed Bandits trades off exploration vs exploitation.

### 12. Practical Interpretation
A narrower confidence interval indicates higher precision (achieved by increasing sample size n or decreasing noise σ).

### 13. Interview Insight
Question: How does increasing the confidence level from 95% to 99% affect the width of the confidence interval?
Answer: Increasing confidence level increases the critical value (Z_0.025 = 1.96 -> Z_0.005 = 2.576), making the margin of error larger and the interval wider!

### 14. Summary
Confidence Intervals report point estimates with error bounds; Z and t critical values scale the margin of error.
