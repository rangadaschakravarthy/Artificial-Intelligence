# Solutions — Student's t-Distribution and Chi-Square Distribution

## Level 1
1. When population standard deviation $\sigma$ is unknown and estimated using sample standard deviation $s$, especially for small samples ($N < 30$).
2. $df = N - 1$.
3. Right-skewed continuous distribution starting at $0$ extending to $+\infty$, becoming more symmetric as $k$ increases.
4. It converges to the Standard Normal distribution $\mathcal{N}(0, 1)$.
5. \chi^2 = \sum_{i=1}^k \frac{(O_i - E_i)^2}{E_i}.

## Level 2
6. $SE = \frac{10}{\sqrt{25}} = \frac{10}{5} = 2.0$. $t = \frac{105 - 100}{2.0} = \frac{5}{2.0} = +2.50$.
7. $df = 25 - 1 = 24$.
8. `stats.t.ppf(0.975, df=24)` $pprox 2.0639$.
9. \chi^2 = \frac{(30-25)^2}{25} + \frac{(20-25)^2}{25} = \frac{25}{25} + \frac{25}{25} = 1.0 + 1.0 = 2.0.
10. $df = 2 - 1 = 1$.

## Level 3
11. Estimating unknown population variance $\sigma$ with sample standard deviation $s$ introduces an additional source of random variability into the denominator $s/\sqrt{N}$, inflating tail probability density.
12. Since $X = \sum_{i=1}^k Z_i^2$, $E[X] = \sum E[Z_i^2] = \sum 1 = k$. Independent terms $\implies 	ext{Var}(X) = \sum 	ext{Var}(Z_i^2) = \sum (E[Z_i^4] - (E[Z_i^2])^2) = \sum (3 - 1) = 2k$.
13. Row totals fixed $\implies (r-1)$ free row probabilities; column totals fixed $\implies (c-1)$ free column probabilities. Total free parameters $= (r-1)(c-1)$.
14. Because $\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}$ is a sum of squared real terms divided by positive expected counts, making every term $\ge 0$.
15. 1-sample t-test compares sample mean to known constant $\mu_0$; 2-sample independent t-test compares means of two separate groups; Paired t-test compares mean differences of paired measurements on identical subjects.

## Level 4
16. `t_stat, p_val = stats.ttest_1samp(latencies, 50.0)`
17. `t_stat, p_val = stats.ttest_ind(scores_A, scores_B)`
18. `res = stats.chi2_contingency(pd.crosstab(df['device'], df['conversion'])); p_val = res.pvalue`
19. `ci = stats.t.interval(0.95, df=len(x)-1, loc=np.mean(x), scale=stats.sem(x))`
20. Cross-validation fold scores are paired because both models are trained/tested on identical data splits, controlling for fold variance.

## Level 5
21. Write joint density $f(z, u) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2} \frac{1}{2^{
u/2} \Gamma(
u/2)} u^{
u/2 - 1} e^{-u/2}$. Transform variables $T = Z / \sqrt{U/
u}, V = U$. Integrate out $V$ to obtain Student's t PDF.
22. Student's t-test assumes equal variances $\sigma_1^2 = \sigma_2^2$. Welch's t-test uses unpooled variances and calculates effective degrees of freedom via Welch–Satterthwaite equation, preserving valid Type I error rates under heteroscedasticity.
23. `stats.ttest_1samp(x, mu0); stats.ttest_ind(x1, x2); stats.chi2_contingency(table)`.
