# Day 67 Worked Examples: Variance and Standard Deviation

## Example 1: Very Easy — Sample Variance Calculation
Sample: [10, 20]. Mean = 15.
Deviations: [-5, 5]. Squared: [25, 25]. Sum = 50.
Sample Variance s^2 = 50 / (2 - 1) = 50. s = sqrt(50) ≈ 7.07.

## Example 2: Beginner — Population vs Sample Variance
Data: [2, 4, 6].
Population Variance σ^2 = 8 / 3 = 2.67.
Sample Variance s^2 = 8 / 2 = 4.00.

## Example 3: Intermediate — Z-Score Normalization
Exam scores: Mean = 70, s = 10. Student score x = 85.
Z-score = (85 - 70) / 10 = +1.5 (1.5 standard deviations above mean).

## Example 4: AI Focus — Batch Normalization Layer
Batch features: μ_B = 0.5, σ_B^2 = 0.04 (σ_B = 0.2), ε = 1e-5.
Input x = 0.9. Normalized x_hat = (0.9 - 0.5) / 0.2 = 2.0.

## Example 5: Real-World AI — Model Overfitting Check
Train Loss Variance across 5 folds = 0.001 (stable). Test Loss Variance = 0.15 (high model instability!).
