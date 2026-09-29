# Solutions — Statistics AI Mini-Project

## Level 1
1. Levene's Test (`scipy.stats.levene`).
2. Mann-Whitney U Test (`scipy.stats.mannwhitneyu`).
3. Welch's 2-Sample t-Test (`scipy.stats.ttest_ind(equal_var=False)`).
4. $d = \frac{ar{x}_B - ar{x}_A}{s_{	ext{pooled}}}$.
5. $lpha = 0.05$.

## Level 2
6. $s_{	ext{pooled}} = 10.0$. $d = \frac{55 - 50}{10} = 0.50$ (Medium effect size).
7. Relative Lift $= \frac{0.12 - 0.10}{0.10} = \frac{0.02}{0.10} = +20.0\%$.
8. Reject $H_0$; Statistically Significant Lift Approved for Deployment.
9. Fail to Reject $H_0$; Not Statistically Significant.
10. $ME = 1.96 	imes 1.5 = 2.94$. $CI = 5.0 \pm 2.94 = [2.06, 7.94]$.

## Level 3
11. Running Student's t-test on skewed or heteroscedastic data distorts critical tail boundaries, leading to inaccurate $p$-values. Diagnostic pre-testing selects robust alternative tests.
12. When variances differ ($s_1^2 
\neq s_2^2$), Student's t-test understates standard error, leading to inflated false positive rates ($p < 0.05$ when $H_0$ is true). Levene's test routes unequal variances to Welch's t-test.
13. $p$-values measure statistical certainty ($P(	ext{Data}|H_0)$), not magnitude. Large samples produce tiny $p$-values for trivial $+0.001\%$ lifts. Cohen's $d$ quantifies whether the lift is large enough to matter economically.
14. Underpowered tests ($n$ too small) have low probability ($< 80\%$) of detecting true performance lifts, causing teams to mistakenly reject good model improvements.
15. Production feature monitoring runs 2-sample KS tests between baseline training distributions and live inference streams. When $p < 0.01$, data drift is flagged and automated retraining pipelines trigger.

## Level 4
16–20. Fully implemented and demonstrated in `code.py`.

## Level 5
21. Architecture pipeline walks from data ingestion $\to$ Shapiro-Wilk normality check $\to$ Levene variance check $\to$ Test selection (Student vs Welch vs Mann-Whitney) $\to$ Effect size engine $\to$ Executive markdown report generation.
22. Fixed-sample A/B testing allocates fixed $50/50$ traffic until $n$ is reached. Multi-armed bandits dynamically shift traffic toward winning variants in real time, minimizing opportunity cost during evaluation.
23. Executing `code.py` produces a complete, production-grade statistical evaluation report, validating 100% completion of LEVEL 1 — MATHEMATICS FOR ARTIFICIAL INTELLIGENCE.
