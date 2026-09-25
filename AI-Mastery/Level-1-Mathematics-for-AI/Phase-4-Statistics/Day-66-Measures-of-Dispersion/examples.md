# Day 66 Worked Examples: Measures of Dispersion

## Example 1: Very Easy — Range and IQR
Data: [3, 7, 8, 12, 14, 18, 21].
Range = 21 - 3 = 18. Q1 = 7, Q3 = 18 => IQR = 11.

## Example 2: Beginner — Outlier Detection with 1.5*IQR Rule
Data: [10, 12, 14, 15, 16, 18, 95].
Q1 = 12, Q3 = 18, IQR = 6.
Upper Bound = 18 + 1.5(6) = 27. Value 95 > 27 is an outlier!

## Example 3: Intermediate — Robust Feature Scaling
Feature x = [10, 20, 30, 40, 1000]. Median = 30, Q1 = 20, Q3 = 40, IQR = 20.
Robust Scaled value for x=30: (30 - 30) / 20 = 0.0.
Robust Scaled value for x=40: (40 - 30) / 20 = 0.5.

## Example 4: AI Focus — Variance Threshold Feature Selection
Feature matrix with columns [Age, Constant_Flag, Income].
Variance of Constant_Flag = 0. Variance Thresholding drops Constant_Flag automatically.

## Example 5: Real-World AI — Anomaly Detection in Credit Cards
Transactions IQR calculated per user profile; transactions exceeding Q3 + 3*IQR flagged as high-risk fraud alerts.
