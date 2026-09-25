# Solutions — Introduction to Hypothesis Testing

## Level 1
1. 1) State $H_0, H_a$, 2) Set $lpha$, 3) Compute Test Statistic, 4) Determine $p$-value or Critical Region, 5) Make Decision.
2. $H_0$ represents the baseline status quo assumption of no effect, no difference, or no improvement.
3. $H_a$ represents the research claim being tested (presence of an effect, difference, or improvement).
4. $lpha = 0.05$ ($5\%$ probability threshold).
5. When prior domain knowledge specifies interest exclusively in a single direction of change (e.g. testing for latency *reduction* only).

## Level 2
6. $H_0: \mu \ge 10$ hours; $H_a: \mu < 10$ hours (1-tailed Left).
7. $lpha/2 = 0.005 \implies Z_{crit} = \pm 2.576$.
8. $Z_{crit} = -1.645$.
9. Since $-1.80 < -1.645$, test statistic falls in rejection region. Decision: Reject $H_0$.
10. Since $1.50 < 1.96$, test statistic is not in rejection region. Decision: Fail to reject $H_0$.

## Level 3
11. Failing to reject $H_0$ means sample size $n$ was insufficient to detect a difference at level $lpha$, not that the true effect size is strictly zero.
12. Because evaluating the sampling distribution under $H_0$ requires specifying an exact numerical point parameter value (e.g. $\mu = \mu_0$) to calculate standard error and $Z$-scores.
13. Selecting a 1-tailed direction after observing sample data effectively doubles the effective $lpha$ level (from $0.025$ to $0.05$ in that tail), artificially inflating false positive rates.
14. Presumption of innocence $= H_0$. Jury must find evidence "beyond a reasonable doubt" ($lpha$) to convict ($H_a$). Verdict "Not Guilty" means insufficient evidence to convict, not proven innocence.
15. Decreasing $lpha$ from $0.05$ to $0.01$ moves critical boundaries further out into the tails ($1.96 	o 2.58$), requiring much stronger empirical evidence to reject $H_0$.

## Level 4
16. $H_0: CTR_{B} - CTR_{A} \le 0$; $H_a: CTR_{B} - CTR_{A} > 0$.
17. `z_2tail = stats.norm.ppf(1 - alpha/2); z_1tail = stats.norm.ppf(1 - alpha)`
18. $H_0: 	ext{Rate}_{AI} \ge 	ext{Rate}_{Human}$; $H_a: 	ext{Rate}_{AI} < 	ext{Rate}_{Human}$.
19. Metric differences $d_i = 	ext{Score}_{B,i} - 	ext{Score}_{A,i}$ across folds $i=1..K$ form a 1-sample input array tested against $\mu_d = 0$.
20. Pre-declaring $lpha$ prevents cherry-picking thresholds after inspecting test results to manufacture desired outcomes.

## Level 5
21. Statistical tests evaluate conditional probability $P(	ext{Data} | H_0)$. Failing to reject $H_0$ means data is consistent with $H_0$, but infinitely many other candidate values are also consistent with the data. We only reject or fail to reject.
22. 1-tailed tests place the entire rejection area $lpha$ into a single tail, moving $Z_{crit}$ closer to center ($1.645$ vs $1.96$), increasing power to detect effects in that specific direction.
23. Complete 5-step Python script implemented in `code.py`.
