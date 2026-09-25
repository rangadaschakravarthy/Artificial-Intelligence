# Day 67 Theory: Variance and Standard Deviation

### 1. Simple Definition
Variance measures the average squared deviation of data points from their mean. Standard Deviation is the square root of variance, returning dispersion to original data units.

### 2. Intuition
Variance measures "how far on average data points spread out". We square differences so negative and positive deviations don't cancel out!

### 3. Mathematical Definition
- Population Variance: σ^2 = (1/N) sum_{i=1}^N (x_i - μ)^2
- Sample Variance: s^2 = (1/(n-1)) sum_{i=1}^n (x_i - x_bar)^2
- Standard Deviation: s = sqrt(s^2)

### 4. Mathematical Notation
- σ^2: Population variance
- s^2: Sample variance (Bessel corrected with n-1)
- σ, s: Standard deviations

### 5. Formula
Computational Shortcut Formula:
s^2 = (1 / (n - 1)) [ sum x_i^2 - (1/n) (sum x_i)^2 ]

Z-Score Standardization:
z = (x - x_bar) / s

### 6. Symbol Explanation
- n - 1: Degrees of freedom (Bessel's correction compensating for using sample mean x_bar)
- z: Standardized score (mean = 0, std = 1)

### 7. Step-by-Step Calculation
Sample: [2, 4, 6] (n=3)
Step 1: x_bar = (2+4+6)/3 = 4
Step 2: Deviations (x_i - x_bar) = [-2, 0, 2]
Step 3: Squared deviations = [4, 0, 4]
Step 4: Sum squared deviations = 8
Step 5: Sample Variance s^2 = 8 / (3 - 1) = 8 / 2 = 4.0
Step 6: Sample Standard Deviation s = sqrt(4.0) = 2.0.

### 8. Second Concrete Example
Scaling Property:
Var(a X + b) = a^2 Var(X).
If data X has s^2 = 5, then Var(3 X + 10) = 3^2 * 5 = 45. (Constant b shift adds zero variance!).

### 9. Common Mistakes
- Dividing by n instead of n-1 when calculating sample variance (underestimating true population variance).
- Adding variance units directly to mean values without taking square root first (unit mismatch!).

### 10. AI Connection
StandardScaler converts features to z-scores z = (x - μ) / σ, crucial for Gradient Descent convergence and distance-based ML models.

### 11. Algorithm Connection
- Batch Normalization in Neural Networks: x_hat = (x - μ_batch) / sqrt(σ_batch^2 + ε).
- Gaussian Mixture Models (GMM): Covariance matrices σ^2 parameterize cluster spread.

### 12. Practical Interpretation
- Variance: Squared units (e.g. $^2).
- Standard Deviation: Original units (e.g. $).

### 13. Interview Insight
Question: Why do we divide by (n - 1) instead of n for sample variance?
Answer: Because sample mean x_bar is calculated from the same sample, it is closer to sample points than true population mean μ. Dividing by n under-estimates variance. Dividing by (n - 1) provides an unbiased estimator: E[s^2] = σ^2.

### 14. Summary
Variance is squared dispersion; Bessel's n-1 correction guarantees unbiased sample estimation.
