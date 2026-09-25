# Day 66 Theory: Measures of Dispersion

### 1. Simple Definition
Measures of dispersion quantify the spread, variability, or scatter of data points around their central value.

### 2. Intuition
Two models may both have an average prediction error of 0 (mean), but Model A ranges from [-1, +1] while Model B ranges from [-100, +100]. Dispersion tells you how risky or unpredictable a distribution is!

### 3. Mathematical Definition
- Range = x_max - x_min
- IQR = Q3 - Q1 (Middle 50% spread)
- Mean Absolute Deviation (MAD) = (1/n) sum |x_i - x_bar|

### 4. Mathematical Notation
- Q1: 25th percentile
- Q3: 75th percentile
- IQR: Interquartile Range

### 5. Formula
IQR = Q3 - Q1
Outlier bounds:
Lower Bound = Q1 - 1.5 * IQR
Upper Bound = Q3 + 1.5 * IQR

### 6. Symbol Explanation
- Q1, Q3: First and third quartiles
- 1.5 * IQR: Standard Tukey outlier multiplier

### 7. Step-by-Step Calculation
Data: [1, 2, 5, 6, 7, 9, 12, 15, 20, 100] (n=10)
Sorted: [1, 2, 5, 6, 7, 9, 12, 15, 20, 100]
- Q1 (25th percentile) = 5
- Q3 (75th percentile) = 15
- IQR = 15 - 5 = 10
- Outlier Lower = 5 - 1.5(10) = -10
- Outlier Upper = 15 + 1.5(10) = 30
Value 100 > 30 => Detected as an outlier!

### 8. Second Concrete Example
Feature Variance Thresholding:
Feature A: [1.0, 1.0, 1.0, 1.0] (Var = 0.0) -> Zero information, remove!
Feature B: [1.0, 5.0, 9.0, 12.0] (Var > 0.0) -> Useful feature, keep!

### 9. Common Mistakes
- Relying solely on Range, which is extremely sensitive to single extreme values.
- Forgetting to scale features before comparing dispersion across variables with different units.

### 10. AI Connection
- Outlier Removal: IQR bounds filter noisy training samples.
- Low-Variance Feature Selection: Dropping features with dispersion near zero.

### 11. Algorithm Connection
- RobustScaler uses Median and IQR scaling: x_scaled = (x - Median) / IQR.
- Isolation Forests and SVMs use dispersion metrics for anomaly detection.

### 12. Practical Interpretation
- Range: Quick min-max span.
- IQR: Robust measure of spread (unaffected by extreme outliers).

### 13. Interview Insight
Question: Why is RobustScaler (using IQR) better than StandardScaler for datasets with extreme outliers?
Answer: StandardScaler uses Mean and Standard Deviation, both corrupted by outliers. RobustScaler uses Median and IQR, ensuring outliers do not distort scaling centers or scaling factors.

### 14. Summary
Dispersion measures measure data uncertainty; IQR provides robust outlier detection for ML pipelines.
