# Theory — Statistics AI Mini-Project Architecture

## 1. Project Overview
This capstone mini-project implements a production-grade **Automated A/B Testing & Statistical Hypothesis Engine** in Python. The engine takes experimental data from control (Variant A) and treatment (Variant B) cohorts, runs diagnostic tests, automatically selects the optimal statistical test, computes $p$-values and effect sizes, and outputs an executive statistical report.

## 2. Decision Logic Pipeline
```
                              Input Data (Group A vs Group B)
                                             |
                              Check Normality (Shapiro-Wilk)
                                             |
                       +---------------------+---------------------+
                       |                                           |
                 Both Normal                                  At least 1 Non-Normal
                       |                                           |
            Check Variance Homogeneity                      Run Non-Parametric
                 (Levene's Test)                           Mann-Whitney U Test
                       |
         +-------------+-------------+
         |                           |
  Equal Variances             Unequal Variances
         |                           |
  Run Student's t-Test        Run Welch's t-Test
```

## 3. Output Metrics
- Statistical $p$-value and Rejection Decision ($p \le lpha$).
- Absolute Lift and Relative Lift ($\%$).
- Cohen's $d$ Effect Size.
- $95\%$ Confidence Interval for Difference in Means.

## 4. Summary
This mini-project completes LEVEL 1 Mathematics for AI by implementing a production statistical decision system.
