# Day 68 Worked Examples: Skewness and Kurtosis

## Example 1: Very Easy — Identifying Skewness
Data A: Mean = 50, Median = 50 => Symmetric (Skew ≈ 0).
Data B: Mean = 75, Median = 50 => Positive Right Skew.

## Example 2: Beginner — Log Transformation of Right-Skewed Data
Income data: [10k, 20k, 30k, 50k, 1M].
Log Transformed: [9.21, 9.90, 10.30, 10.81, 13.81].
Extreme 1M value compresses into a manageable scalar, reducing skewness!

## Example 3: Intermediate — Classifying Kurtosis
Normal Distribution: Kurtosis = 3.0 (Excess = 0.0, Mesokurtic).
Student-t Distribution (df=4): Kurtosis = 6.0 (Excess = +3.0, Leptokurtic).
Uniform Distribution: Kurtosis = 1.8 (Excess = -1.2, Platykurtic).

## Example 4: AI Focus — PowerTransformer Pipeline
Feature `House_Price` has skewness +3.5.
Applying `PowerTransformer(method='box-cox')` reduces skewness to -0.05, improving linear regression R^2 score.

## Example 5: Real-World AI — Risk Assessment in Self-Driving Cars
Sensor noise distribution with Excess Kurtosis = +10.0 signals high probability of sudden sensor spikes, requiring robust Kalman filtering.
