# Day 68 Theory: Skewness and Kurtosis

### 1. Simple Definition
Skewness measures how lopsided or asymmetric a distribution is. Kurtosis measures how heavy or fat the distribution tails are compared to a Normal distribution.

### 2. Intuition
- Skewness = 0: Perfectly symmetric (bell curve).
- Positive Skew (>0): Tail stretches to the right (e.g. Income).
- Negative Skew (<0): Tail stretches to the left (e.g. Age at death).
- Excess Kurtosis > 0 (Leptokurtic): Heavy tails, prone to extreme outlier black swan events!

### 3. Mathematical Definition
- 3rd Standardized Moment (Skewness):
γ_1 = E[ ((X - μ) / σ)^3 ]

- 4th Standardized Moment (Kurtosis):
β_2 = E[ ((X - μ) / σ)^4 ]
Excess Kurtosis = β_2 - 3.

### 4. Mathematical Notation
- Normal Distribution: Skewness = 0, Kurtosis = 3 (Excess Kurtosis = 0).
- Leptokurtic: Excess > 0 (heavy tails).
- Platykurtic: Excess < 0 (thin tails).

### 5. Formula
Sample Skewness:
g_1 = (1/n) sum ((x_i - x_bar)/s)^3

Sample Excess Kurtosis:
g_2 = (1/n) sum ((x_i - x_bar)/s)^4 - 3

Box-Cox Power Transformation:
y(λ) = (x^λ - 1)/λ if λ != 0 else log(x)

### 6. Symbol Explanation
- γ_1: Skewness parameter
- β_2: Kurtosis parameter
- λ (lambda): Box-Cox transformation parameter normalizing skewed data

### 7. Step-by-Step Calculation
Distribution with right tail [1, 2, 2, 3, 10]:
Mean = 3.6, Median = 2.0. Mean > Median => Positive Skewness!
Cubed standardized deviations sum to positive value => Positive skewness confirmed.

### 8. Second Concrete Example
Financial Asset Returns:
Normal curve expects 3-sigma event 0.27% of time.
Leptokurtic financial returns (Excess Kurtosis = 5.0) experience extreme crash events far more frequently!

### 9. Common Mistakes
- Assuming Z-score standardization removes skewness (Z-scoring is linear; it leaves skewness completely unchanged!).
- Confusing high Kurtosis with high Variance (Kurtosis measures tail probability, not standard width).

### 10. AI Connection
Linear Regression and Gaussian Naive Bayes assume normally distributed features/residuals. Log or Box-Cox transformations remove skewness to fix model performance.

### 11. Algorithm Connection
- Log Transform (np.log1p) fixes positive right-skew in loss targets (e.g. house prices).
- Yeo-Johnson Transformation normalizes features containing positive and negative values.

### 12. Practical Interpretation
- Skewness: Directs choice of log/power transforms.
- Kurtosis: Flags risk of extreme out-of-distribution outliers.

### 13. Interview Insight
Question: Why doesn't StandardScaler make skewed feature distributions Normal?
Answer: StandardScaler is a linear transformation: z = (x - μ)/σ. Linear shifts and scaling do not alter the shape, asymmetry, or 3rd moment (skewness) of a distribution. Non-linear transforms like Log or PowerTransformer are required!

### 14. Summary
Skewness quantifies asymmetry; Kurtosis quantifies extreme tail risk. Power transformations normalize skewed features for ML models.
