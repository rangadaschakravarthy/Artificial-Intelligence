# Day 68 Practice Questions: Skewness and Kurtosis

## Level 1: Basic Concepts
1. What does Skewness measure?
2. What does Kurtosis measure?
3. What are the Skewness and Kurtosis of a standard Normal distribution?
4. Define Leptokurtic distribution.
5. Define Platykurtic distribution.

## Level 2: Calculation
6. Given Mean = 45, Median = 40, Std = 5, compute Pearson's median skewness coefficient: 3*(Mean - Median)/Std.
7. Identify skewness direction if Mean = 20, Median = 30.
8. If Kurtosis = 5.2, compute Excess Kurtosis.
9. Apply log1p transform to x = [0, 9, 99, 999].
10. Calculate 3rd standardized moment sign for [-10, -1, 0, 1, 2].

## Level 3: Conceptual & Proofs
11. Prove that linear transformation Y = a X + b (with a > 0) preserves skewness: γ_1(Y) = γ_1(X).
12. Why does log transformation reduce positive right skewness?
13. Discuss why heavy tails (high kurtosis) invalidate 3-sigma confidence rules.
14. Differentiate Pearson's first vs second skewness coefficients.
15. Explain why Box-Cox power transform requires strictly positive inputs.

## Level 4: AI Applications
16. Why does Log transformation help Neural Networks train faster on skewed targets?
17. How to normalize features containing zero or negative values using Yeo-Johnson?
18. Why do linear models perform poorly on right-skewed predictor features?
19. How does high kurtosis in loss gradients lead to unstable learning rate behavior?
20. In anomaly detection, how is kurtosis used to detect non-Gaussian noise?

## Level 5: Interview Questions
21. "Does StandardScaler normalize a non-Gaussian distribution? Explain mathematically."
22. "Write Python code using Scipy to compute skewness, excess kurtosis, and apply Box-Cox transformation."
23. "Explain the mathematical difference between 3rd and 4th standardized moments."
