# Solutions — Null and Alternative Hypotheses

## Level 1
1. Null Hypothesis $H_0$.
2. Alternative Hypothesis $H_a$.
3. $H_0: \mu_1 = \mu_2$; $H_a: \mu_1 
\neq \mu_2$.
4. One-Tailed Right (Upper Tail) test.
5. Two-Tailed test.

## Level 2
6. $H_0: \mu \le 50$; $H_a: \mu > 50$.
7. $H_0: \mu = 70$; $H_a: \mu 
\neq 70$.
8. $H_0: \mu \ge 500$; $H_a: \mu < 500$.
9. $H_0: 
ho = 0$; $H_a: 
ho 
\neq 0$.
10. $H_0: \sigma_1^2 = \sigma_2^2$; $H_a: \sigma_1^2 
\neq \sigma_2^2$.

## Level 3
11. $H_0$ must specify an exact boundary point (equality) so that sampling distributions and standard errors can be computed under $H_0$.
12. Superiority tests if new model is strictly better ($> 0$); Non-Inferiority tests if new model is not worse by more than acceptable margin $\delta$ ($> -\delta$).
13. Statistical methodology assumes $H_0$ by default; $H_0$ is only rejected when sample evidence against it is overwhelming ($p \le lpha$).
14. By requiring strong empirical proof before rejecting $H_0$, teams avoid shipping complex, expensive models that offer no real performance gain over simple baselines.
15. Testing 100 features independently at $lpha = 0.05$ yields expected $100 	imes 0.05 = 5$ false positive feature selections purely by chance (Family-Wise Error Rate).

## Level 4
16. `def create_ab_test_hypotheses(metric, a, b): return f"H0: {metric}_{b} - {metric}_{a} <= 0", f"Ha: {metric}_{b} - {metric}_{a} > 0"`
17. $H_0: eta_j = 0$ (Feature $j$ has zero effect on $Y$); $H_a: eta_j 
\neq 0$.
18. $H_0$: Feature 1 and Feature 2 are independent; $H_a$: Feature 1 and Feature 2 are dependent.
19. $H_0$: Train and Test data come from the same distribution; $H_a$: Train and Test distributions differ (Data Drift).
20. $H_0$: Data follows a Normal distribution; $H_a$: Data does not follow a Normal distribution.

## Level 5
21. Specifying an exact equality point (e.g. $\mu = \mu_0$) pins down the null distribution parameters, enabling standard error calculation and $p$-value integration.
22. TOST sets $H_0: |\mu_A - \mu_B| \ge \Delta$ (models are different) vs $H_a: -\Delta < \mu_A - \mu_B < \Delta$ (models are equivalent within margin $\Delta$), requiring statistical proof of equivalence.
23. Formatted code generator implemented in `code.py`.
