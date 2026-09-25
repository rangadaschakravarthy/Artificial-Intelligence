# Day 66 Solutions: Measures of Dispersion

## Level 1: Basic Concepts
1. Range = max - min.
2. IQR = Q3 - Q1.
3. Middle 50% of the distribution.
4. Lower = Q1 - 1.5*IQR; Upper = Q3 + 1.5*IQR.
5. Outliers only affect extreme ends; IQR ignores top and bottom 25% of data.

## Level 2: Calculation
6. Range = 24 - 2 = 22. Q1=5, Q3=20 => IQR = 15.
7. Q1=10, Q3=17, IQR=7. Upper = 17 + 10.5 = 27.5. Value 85 is an outlier.
8. Scaled = (25 - 20) / 10 = 0.5.
9. Mean = 5. Deviations = |-3|, |-1|, |1|, |3| = [3, 1, 1, 3]. MAD = 8/4 = 2.0.
10. Q1 = 25, Q2 = 45, Q3 = 65.

## Level 3: Conceptual
11. Adding constant c shifts Q1 -> Q1+c and Q3 -> Q3+c. Difference (Q3+c) - (Q1+c) = Q3 - Q1 = IQR.
12. Multiplying by c scales quartiles by c: c Q3 - c Q1 = c (Q3 - Q1).
13. To visually isolate extreme anomalies beyond 1.5*IQR as individual points.
14. SD assumes normality and is sensitive to outliers; IQR is non-parametric and robust.
15. Variance squares deviations (hugely impacted); MAD takes absolute value (moderately impacted).

## Level 4: AI Applications
16. Keeps feature values bounded cleanly without letting extreme outliers produce huge inputs to activations.
17. Zero variance implies zero information content (constant column), which causes singular covariance matrices.
18. Provides instant 5-number summary (Min, Q1, Median, Q3, Max) and visual outlier identification.
19. Prevents leak of extreme outlier noise across folds.
20. Measures tail dispersion and down-side risk bounds.

## Level 5: Interview Solutions
21. For a normal distribution, Q1 ≈ -0.675σ and Q3 ≈ +0.675σ, so IQR ≈ 1.35σ. Bounds Q3 + 1.5*IQR = 0.675σ + 2.025σ = 2.7σ (~99.3% coverage), flagging points beyond 2.7σ as outliers.
22. See `code.py`.
23. MinMax scales to [0,1] (sensitive to min/max outliers); Standard scales to mean=0, std=1 (sensitive to outliers); Robust scales by median/IQR (robust to outliers).
