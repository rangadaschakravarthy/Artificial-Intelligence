# Solutions — Statistical Tests

## Level 1
1. When observations in the two groups are naturally paired or matched (e.g. pre/post measurements on identical subjects, or two models tested on identical CV folds).
2. Chi-Square Test of Independence (`chi2_contingency`).
3. A 2-sample t-test that does not assume equal sample variances (unpooled variances), using Welch–Satterthwaite degrees of freedom.
4. One-Sample t-Test (`ttest_1samp`).
5. $df = N - 1$ (where $N$ is the number of pairs).

## Level 2
6. $SE = 10 / \sqrt{25} = 2.0$. $t = (108 - 100) / 2.0 = +4.00$.
7. $SE_{pool} = \sqrt{rac{25}{10} + rac{25}{10}} = \sqrt{5.0} pprox 2.236$. $t = (85 - 80) / 2.236 = +2.236$.
8. $SE = 2.0 / \sqrt{16} = 0.5$. $t = 4.0 / 0.5 = +8.00$.
9. $\chi^2 = rac{(30-25)^2}{25} + rac{(20-25)^2}{25} = 1.0 + 1.0 = 2.0$.
10. `2 * (1 - stats.t.cdf(2.50, df=24))` $pprox 0.0194$.

## Level 3
11. Subtracting paired scores $d_i = x_{B,i} - x_{A,i}$ eliminates subject-to-subject / fold-to-fold baseline variance, leaving only net treatment difference variance $	ext{Var}(d)$, which drastically shrinks standard error and boosts power.
12. Unpooled $SE = \sqrt{rac{s_1^2}{n_1} + rac{s_2^2}{n_2}}$. Welch–Satterthwaite $df = rac{(v_1 + v_2)^2}{rac{v_1^2}{n_1-1} + rac{v_2^2}{n_2-1}}$ where $v_i = s_i^2/n_i$, adjusting critical values for variance imbalance.
13. Subtracts $0.5$ from absolute difference $|O - E|$ before squaring: $\chi^2_{Yates} = \sum rac{(|O - E| - 0.5)^2}{E}$, preventing overestimation of significance in small $2 	imes 2$ tables.
14. The square of the normal proportion test statistic $Z^2$ equals the Chi-Square statistic $\chi^2$ with $df = 1$.
15. ANOVA compares between-group variance to within-group variance via F-ratio $F = rac{MS_{between}}{MS_{within}}$. If $K=2$, $F = t^2$, matching 2-sample t-test exactly.

## Level 4
16. Code implemented in `code.py`.
17. `f_stat, p_val = stats.f_oneway(m1_scores, m2_scores, m3_scores, m4_scores, m5_scores)`
18. `SelectKBest(chi2, k=10)` computes $\chi^2$ statistic between each non-negative categorical feature and target label $Y$, selecting features with highest dependencies ($p < 0.05$).
19. Dietterich's 5x2-fold cv paired t-test evaluates $t = rac{p_1^{(1)}}{\sqrt{rac{1}{5}\sum s_i^2}}$, controlling for fold overlap correlation.
20. 1-Way ANOVA (`f_oneway`) if normality holds, or Kruskal-Wallis non-parametric test (`kruskal`) if ordinal/skewed.

## Level 5
21. $t = rac{Z}{\sqrt{U/1}}$. Squaring yields $t^2 = rac{Z^2 / 1}{U / 1}$. Since $Z^2 \sim \chi^2_1$ and $U \sim \chi^2_{df}$, ratio of two independent chi-square variables divided by their $df$ matches definition of $F_{1, df}$.
22. Running $inom{4}{2} = 6$ pairwise t-tests at $lpha=0.05$ inflates Family-Wise Error Rate to $1 - (0.95)^6 pprox 26.5\%$. ANOVA tests overall group equality first at $lpha=0.05$.
23. Complete unified statistical suite class implemented in `code.py`.
