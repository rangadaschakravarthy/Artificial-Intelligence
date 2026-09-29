# Practice Problems — Statistics for Machine Learning

## Level 1: Basic Concept Checks
1. Name the ANOVA score function used for continuous feature selection in classification (`f_classif`).
2. Which statistical test selects categorical features (`SelectKBest`)?
3. What is the formula for Bonferroni adjusted significance threshold $lpha_{	ext{adj}}$?
4. What is the difference between absolute lift and relative lift in A/B testing?
5. Which 2-sample test detects continuous Data Drift between training and production distributions?

## Level 2: Direct Calculations
6. 100 features are tested at $lpha = 0.05$. Compute Bonferroni threshold $lpha_{	ext{adj}}$.
7. Baseline accuracy $= 0.80$, Variant B accuracy $= 0.84$. Compute absolute and relative lift.
8. ANOVA $F$-score for Feature A is $F=12.5$ ($df_1=2, df_2=97$). Find $p$-value in SciPy.
9. Feature has $p$-value $0.003$. Does it survive Bonferroni adjustment from Q6?
10. Compute standard error of difference for $SE_A = 0.02, SE_B = 0.03$.

## Level 3: Conceptual & Multi-Step Problems
11. Explain why selecting features using target $Y$ on the ENTIRE dataset before train/test split causes severe data leakage.
12. Show why Benjamini-Hochberg False Discovery Rate (FDR) control has higher statistical power than Bonferroni correction.
13. Explain how Covariate Shift ($P_{train}(X) 
\neq P_{test}(X)$) causes ML model performance degradation.
14. Explain why A/B tests use 2-sample proportion Z-tests or Welch's t-tests rather than simple sample mean comparisons.
15. Explain how Population Stability Index (PSI) measures distribution shift in credit risk modeling.

## Level 4: AI & ML Applications
16. Write Python code using Scikit-Learn `SelectKBest` and `f_classif` to transform a feature matrix `X` to top $k=5$ features.
17. Write Python code to calculate Bonferroni-adjusted $p$-values and return boolean mask of significant features.
18. Write Python code implementing Benjamini-Hochberg FDR control on 50 feature $p$-values.
19. Write Python code to simulate A/B test evaluation for conversion metrics $n_A=5000, n_B=5000$ and report statistical significance.
20. In automated MLOps pipelines, how are KS-test $p$-values used to trigger automated model retraining alerts?

## Level 5: Interview Questions
21. Derive the ANOVA $F$-statistic formula $F = \frac{MS_{	ext{between}}}{MS_{	ext{within}}}$ and explain how it measures class separation.
22. How do you design an A/B test for a recommendation engine while preventing network spillover / contagion effects between users?
23. Write Python code using Scikit-Learn and SciPy to execute a full Statistical Feature Selection and A/B Test Lift Evaluation pipeline.
