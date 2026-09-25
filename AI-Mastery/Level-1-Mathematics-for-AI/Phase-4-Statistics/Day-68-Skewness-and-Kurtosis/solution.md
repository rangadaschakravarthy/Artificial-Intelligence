# Day 68 Solutions: Skewness and Kurtosis

## Level 1: Basic Concepts
1. Asymmetry of distribution around mean.
2. Tail thickness and peakiness relative to normal distribution.
3. Skewness = 0, Kurtosis = 3 (Excess Kurtosis = 0).
4. Distribution with heavy tails and high peak (Excess Kurtosis > 0).
5. Distribution with light tails and flat peak (Excess Kurtosis < 0).

## Level 2: Calculation
6. Pearson Skewness = 3 * (45 - 40) / 5 = 15 / 5 = +3.0 (Positive skew).
7. Mean < Median => Negative (Left) Skew.
8. Excess Kurtosis = 5.2 - 3.0 = +2.2.
9. log1p(x) = [log(1), log(10), log(100), log(1000)] = [0, 2.30, 4.61, 6.91].
10. Negative dev -10 cubed = -1000 dominates sum => Negative skewness sign.

## Level 3: Conceptual
11. Standardized moment divides by σ^3. Scaling X by a multiplies numerator by a^3 and denominator by (aσ)^3 = a^3 σ^3, cancelling a completely!
12. Log function compresses large values exponentially more than small values, pulling right tail inward.
13. High kurtosis places much higher probability mass in outer tails than the 0.27% predicted by Gaussian 3-sigma rule.
14. Pearson 1st uses Mode: (Mean - Mode)/σ; Pearson 2nd uses Median: 3(Mean - Median)/σ.
15. Box-Cox formula x^λ involves logarithm log(x) when λ=0 and fractional powers, undefined for x <= 0.

## Level 4: AI Applications
16. Prevents extreme target values from generating massive loss gradients that distort weight updates.
17. Yeo-Johnson extends Box-Cox by adding smooth piecewise functions for negative inputs.
18. Right-skewed features have high leverage points that disproportionately pull linear regression decision boundaries.
19. Causes rare but massive gradient spikes during backpropagation.
20. High kurtosis signals presence of heavy-tailed non-Gaussian outlier signals.

## Level 5: Interview Solutions
21. No. Z-score z = (x - μ)/σ is linear. It changes location (mean=0) and scale (std=1), but 3rd and 4th moments remain unchanged.
22. See `code.py`.
23. 3rd moment E[(X-μ)^3 / σ^3] measures asymmetric direction (odd power preserves sign); 4th moment E[(X-μ)^4 / σ^4] measures symmetric tail mass (even power makes all deviations positive).
