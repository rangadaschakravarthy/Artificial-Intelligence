# Solutions — Statistics for Machine Learning

## Level 1
1. ANOVA $F$-test (`f_classif`).
2. Chi-Square test (`chi2`).
3. $lpha_{	ext{adj}} = rac{lpha}{m}$.
4. Absolute lift $= p_B - p_A$; Relative lift $= rac{p_B - p_A}{p_A}$.
5. 2-Sample Kolmogorov-Smirnov test (`ks_2samp`).

## Level 2
6. $lpha_{	ext{adj}} = rac{0.05}{100} = 0.0005$.
7. Absolute Lift $= 0.84 - 0.80 = +0.04 = +4.0\%$; Relative Lift $= rac{0.04}{0.80} = +0.05 = +5.0\%$.
8. `1 - stats.f.cdf(12.5, dfn=2, dfd=97)` $pprox 0.0000137$.
9. No. $p = 0.003 > 0.0005$ (Fails Bonferroni threshold).
10. $SE_{	ext{diff}} = \sqrt{SE_A^2 + SE_B^2} = \sqrt{0.02^2 + 0.03^2} = \sqrt{0.0004 + 0.0009} = \sqrt{0.0013} pprox 0.03606$.

## Level 3
11. Feature selection on the full dataset uses target labels $Y_{test}$ from the test set to pick features, leaking test target information into the model training pipeline. Feature selection MUST be fit ONLY on training set folds.
12. Bonferroni controls Family-Wise Error Rate by dividing $lpha$ by $m$ uniformly, which is extremely conservative. FDR controls the proportion of false positives among rejected hypotheses, dynamically scaling thresholds $p_{(k)} \le rac{k}{m} q^*$ and retaining higher power to discover true features.
13. Models learn decision boundaries $P(Y|X)$ based on training input region density $P_{train}(X)$. When $P(X)$ shifts in production to unobserved feature regions, model confidence and accuracy degrade.
14. Sample means $ar{x}_A, ar{x}_B$ fluctuate due to random sampling noise. Statistical tests compute $SE$ and $p$-values to verify if observed difference exceeds sampling variability at confidence level $1-lpha$.
15. $PSI = \sum (Actual\% - Expected\%) 	imes \ln\left(rac{Actual\%}{Expected\%}ight)$. $PSI < 0.1 \implies$ No shift; $PSI > 0.25 \implies$ Significant shift requiring recalibration.

## Level 4
16. `selector = SelectKBest(score_func=f_classif, k=5); X_new = selector.fit_transform(X, y)`
17. `adj_alpha = 0.05 / len(p_vals); sig_mask = p_vals < adj_alpha`
18. `from statsmodels.stats.multitest import multipletests; reject, _, _, _ = multipletests(p_vals, alpha=0.05, method='fdr_bh')`
19. `z_stat, p_val = proportions_ztest([conv_B, conv_A], [n_B, n_A])`
20. MLOps monitors daily production feature distributions via `ks_2samp`. If $p$-value $< 0.01$ for consecutive days, automated pipeline triggers Data Drift alert and executes retraining script.

## Level 5
21. $MS_{	ext{between}} = rac{\sum N_k (ar{x}_k - ar{x})^2}{K - 1}$; $MS_{	ext{within}} = rac{\sum (N_k - 1) s_k^2}{N - K}$. Ratio $F = rac{MS_{	ext{between}}}{MS_{	ext{within}}}$ compares variance of class means to variance inside classes. High $F$ indicates class clusters are well-separated relative to their internal spread.
22. Randomize at cluster level (e.g. city or organization level) rather than individual user level, preventing social graph contamination where Variant B users interact with Variant A controls.
23. Complete combined feature selection and A/B testing pipeline implemented in `code.py`.
