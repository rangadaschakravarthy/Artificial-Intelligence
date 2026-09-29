# Solutions — Statistical Distributions in Statistics

## Level 1
1. Parametric tests assume specific distribution family (e.g. Normal); non-parametric tests make no distribution shape assumptions.
2. Shapiro-Wilk test (or D'Agostino-Pearson / Kolmogorov-Smirnov test).
3. Chi-Square distribution with $k$ degrees of freedom ($\chi^2_k$).
4. Student's t-distribution.
5. F-Distribution ($F = \frac{S_1^2 / \sigma_1^2}{S_2^2 / \sigma_2^2}$).

## Level 2
6. `stats.shapiro(data)`
7. Since $Z \sim \mathcal{N}(0,1)$, $E[Z]=0, 	ext{Var}(Z)=1 \implies E[Z^2] = 	ext{Var}(Z) + (E[Z])^2 = 1 + 0 = 1.0$.
8. $E[X] = k$, $	ext{Var}(X) = 2k$.
9. `transformed, _ = stats.boxcox(data)`
10. Bernoulli distribution $	ext{Bern}(p)$.

## Level 3
11. Because sample variance $s^2$ is an estimate of unknown $\sigma^2$, introducing additional uncertainty in the denominator $\frac{ar{X}-\mu}{s/\sqrt{N}}$, which widens distribution tails.
12. As $N \to \infty$, sample standard deviation $s$ converges almost surely to true $\sigma$ by Law of Large Numbers, causing denominator $s/\sqrt{N} \to \sigma/\sqrt{N}$ and transforming $t$-statistic into standard normal $Z$.
13. Rank-sum tests replace raw values with ordinal ranks ($1, 2, \dots, N$). An extreme outlier value $1,000,000$ receives rank $N$, exactly 1 position above rank $N-1$, capping its numerical influence.
14. MGF of $\chi^2_k$ is $(1 - 2t)^{-k/2}$. Product of MGFs for independent $X, Y$ is $(1-2t)^{-k_1/2} (1-2t)^{-k_2/2} = (1-2t)^{-(k_1+k_2)/2}$, which is the MGF of $\chi^2_{k_1+k_2}$.
15. KS test computes $D = \sup_x |F_N(x) - F_0(x)|$. Larger $D$ indicates empirical data deviates significantly from theoretical distribution model $F_0$.

## Level 4
16. `for col in df.select_dtypes(np.number): print(col, stats.shapiro(df[col]).pvalue)`
17. `import statsmodels.api as sm; sm.qqplot(data, line='s')`
18. Gaussian residuals guarantee that parameter estimators $\hat{eta}$ follow Exact Normal distributions, allowing valid hypothesis testing ($t$-tests for coefficients) and confidence intervals.
19. `ks_stat, p_val = stats.ks_2samp(train_col, test_col); if p_val < 0.05: print("Data drift detected!")`
20. Switch to Mann-Whitney U test when sample size is small ($N < 30$) and metric distribution displays severe skewness or extreme outliers.

## Level 5
21. 1) $Z \sim \mathcal{N}(0, 1)$. 2) $Z_1^2 + \dots + Z_k^2 \sim \chi^2_k$. 3) $t = \frac{Z}{\sqrt{U / k}}$ where $U \sim \chi^2_k \implies t$-distribution. 4) $F = \frac{U_1 / k_1}{U_2 / k_2}$ where $U_1 \sim \chi^2_{k_1}, U_2 \sim \chi^2_{k_2} \implies F$-distribution.
22. Small-sample t-test critical values rely on the exact ratio of normal numerator to chi-square denominator. Non-normality distorts tail probabilities, inflating Type I error rates.
23. `print(stats.shapiro(data)); print(stats.kstest(data, 'norm')); print(stats.anderson(data, 'norm'))`.
