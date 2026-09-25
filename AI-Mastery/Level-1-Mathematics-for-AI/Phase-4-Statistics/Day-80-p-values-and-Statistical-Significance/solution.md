# Solutions — p-values and Statistical Significance

## Level 1
1. The probability of obtaining a test statistic as or more extreme than observed, assuming $H_0$ is true.
2. If $p \le lpha \implies$ Reject $H_0$; if $p > lpha \implies$ Fail to Reject $H_0$.
3. False! $p$-value is $P(	ext{Data} | H_0)$, not $P(H_0 | 	ext{Data})$.
4. As sample size $n$ increases, standard error shrinks ($SE 	o 0$), causing test statistics to grow and $p$-values to decrease toward 0.
5. Statistical significance measures whether an effect is unlikely due to chance ($p \le lpha$); Practical significance measures whether the effect size is large enough to matter in practice.

## Level 2
6. Upper tail $= 1 - 0.9750 = 0.0250$. 2-tailed $p = 2 	imes 0.0250 = 0.0500$.
7. Lower tail $p = 0.0100$.
8. `2 * (1 - stats.t.cdf(2.50, df=20))` $pprox 0.0213$.
9. Since $0.024 \le 0.05$, Reject $H_0$ (Statistically Significant).
10. Since $0.082 > 0.05$, Fail to Reject $H_0$ (Not Significant).

## Level 3
11. Two-tailed alternative $H_a: \mu 
eq \mu_0$ considers extreme deviation in either positive or negative direction, requiring summing area in both upper and lower tails.
12. Peeking and stopping when $p < 0.05$ exploits random fluctuations. Total false positive rate across $k$ peeks rises to $1 - (1-lpha)^k \gg 0.05$.
13. Small: $d = 0.2$; Medium: $d = 0.5$; Large: $d = 0.8$.
14. ASA warned that $p$-values do not measure truth of a hypothesis or magnitude of an effect, and bright-line rules ($p < 0.05$) lead to scientific misinterpretations.
15. Bonferroni divides significance threshold $lpha$ by number of tests $m$ ($lpha_{	ext{bonf}} = lpha/m$), keeping overall family-wise error rate $\le lpha$.

## Level 4
16. `p_val = 2 * (1 - stats.t.cdf(2.45, df=30))`
17. `p_adj = np.minimum(1.0, p_vals * len(p_vals))`
18. `from statsmodels.stats.multitest import multipletests; reject, p_adj, _, _ = multipletests(p_vals, method='fdr_bh')`
19. Peeking repeatedly tests hypotheses at multiple time steps without adjusting $lpha$, inflating cumulative Type I error rates up to $20-30\%$.
20. `d = (np.mean(b) - np.mean(a)) / np.sqrt((np.var(a, ddof=1) + np.var(b, ddof=1))/2)`

## Level 5
21. By Bayes' Theorem: $P(H_0 | 	ext{Data}) = rac{P(	ext{Data} | H_0) P(H_0)}{P(	ext{Data})}$. $P(H_0 | 	ext{Data})$ depends heavily on the prior $P(H_0)$ and total evidence $P(	ext{Data})$, which $p$-value ignores.
22. Mixture Sequential Probability Ratio Test (mSPRT) computes a running mixture likelihood ratio that maintains valid Type I error control continuously at every sample update, allowing safe real-time peeking.
23. Complete report script implemented in `code.py`.
