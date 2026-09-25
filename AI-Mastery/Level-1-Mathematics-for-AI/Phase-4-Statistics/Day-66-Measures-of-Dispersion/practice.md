# Day 66 Practice Questions: Measures of Dispersion

## Level 1: Basic Concepts
1. What is Range?
2. What is Interquartile Range (IQR)?
3. What percentage of data lies within the IQR?
4. Write the formula for upper and lower outlier bounds using IQR.
5. Why is IQR more robust than Range?

## Level 2: Calculation
6. Calculate Range and IQR for [2, 5, 8, 12, 16, 20, 24].
7. Identify outliers in [1, 10, 12, 13, 15, 17, 85].
8. Compute Robust Scaled value for x=25 given Median=20, IQR=10.
9. Find MAD (Mean Absolute Deviation) of [2, 4, 6, 8].
10. Calculate Q1, Q2 (Median), Q3 for [10, 20, 30, 40, 50, 60, 70, 80].

## Level 3: Conceptual & Proofs
11. Prove that IQR is invariant to constant shifts: IQR(X + c) = IQR(X).
12. Show that IQR(c * X) = |c| * IQR(X).
13. Why does boxplot draw whiskers to 1.5 * IQR instead of min/max when outliers exist?
14. Compare Standard Deviation vs IQR as dispersion metrics.
15. Explain how extreme outliers affect Mean Absolute Deviation vs Variance.

## Level 4: AI Applications
16. How does RobustScaler prevent gradient explosion in deep learning?
17. Why drop zero-variance features prior to model training?
18. How are boxplots used during Exploratory Data Analysis (EDA)?
19. How does IQR filtering improve cross-validation stability?
20. In financial risk modeling (VaR), why is quartile dispersion crucial?

## Level 5: Interview Questions
21. "Explain the 1.5 * IQR rule for outlier detection and its theoretical justification for Normal distributions."
22. "Write a Python function to automatically detect and trim outliers using IQR."
23. "Compare MinMax, Standard, and Robust Scaling methods."
