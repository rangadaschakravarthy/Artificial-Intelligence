# Solutions — Type I and Type II Errors

## Level 1
1. Rejecting Null Hypothesis $H_0$ when $H_0$ is actually true (False Positive).
2. Failing to reject Null Hypothesis $H_0$ when $H_0$ is actually false (False Negative).
3. $	ext{Power} = 1 - eta$.
4. $80\%$ power ($1 - eta = 0.80$).
5. Increasing $n$ shrinks standard error, increasing distribution separation and reducing $eta$ (increasing power).

## Level 2
6. $	ext{Power} = 1 - 0.10 = 0.90 = 90\%$.
7. $eta = 1 - 0.92 = 0.08 = 8\%$.
8. $P(	ext{Type I Error}) = lpha = 0.05 = 5\%$.
9. $1 - lpha = 1 - 0.05 = 0.95 = 95\%$.
10. `TTestIndPower().solve_power(effect_size=0.3, nobs1=100, alpha=0.05)` $pprox 0.561$ ($56.1\%$ power).

## Level 3
11. For a fixed sample size $n$, decreasing $lpha$ moves critical boundaries outward, making $H_0$ harder to reject. This expands the non-rejection region, increasing probability $eta$ of missing a true effect.
12. Missing a pedestrian (Type II error) results in a fatal crash; false braking (Type I error) causes temporary inconvenience. Safety engineering prioritizes minimizing fatal false negatives.
13. Larger effect size $d = (\mu_a - \mu_0)/\sigma$ pushes alternative mean $\mu_a$ further to the right. The area under the alternative curve behind the critical boundary $Z_{lpha/2}$ shrinks, reducing $eta$ and boosting power $1-eta$.
14. An underpowered test lacks sample size to achieve $p \le 0.05$ even when a real $+2\%$ lift exists. The team sees $p = 0.25$, fails to reject $H_0$, and discards a valid algorithm improvement.
15. FWER $= 1 - (1-lpha)^m$. For $m=10$ independent tests at $lpha=0.05$, FWER $= 1 - (0.95)^{10} pprox 0.40$, giving $40\%$ chance of at least one false positive.

## Level 4
16. `analysis = TTestIndPower(); analysis.plot_power(dep_var='n', nobs=np.arange(10, 500), effect_size=[0.2, 0.5, 0.8])`
17. `n = TTestIndPower().solve_power(effect_size=0.2, alpha=0.05, power=0.80)` $pprox 393.4 \implies n = 394$ per group.
18. Type I Error $lpha = FPR = rac{FP}{FP + TN}$; Type II Error $eta = FNR = rac{FN}{TP + FN}$.
19. Power $1 - eta = 	ext{Recall (Sensitivity)} = rac{TP}{TP + FN}$; Specificity $= 1 - lpha = rac{TN}{TN + FP}$.
20. Lower decision threshold $	au$ from $0.50$ down to $	au = rac{5}{5 + 500} = rac{5}{505} pprox 0.01$, drastically reducing costly false negatives.

## Level 5
21. Critical boundary $x_{crit} = \mu_0 + Z_{lpha/2} rac{\sigma}{\sqrt{n/2}}$. For alternative distribution, $x_{crit} = \mu_a - Z_eta rac{\sigma}{\sqrt{n/2}}$. Equating boundaries: $\mu_a - \mu_0 = (Z_{lpha/2} + Z_eta) rac{\sigma \sqrt{2}}{\sqrt{n}}$. Divide by $\sigma$ to get $d = rac{(Z_{lpha/2} + Z_eta) \sqrt{2}}{\sqrt{n}} \implies n = rac{2 (Z_{lpha/2} + Z_eta)^2}{d^2}$.
22. Post-hoc power computed using sample effect size is a deterministic transform of $p$-value adding no new information. Pre-experiment power planning determines sample size $n$ required before data collection.
23. Complete power analysis pipeline script implemented in `code.py`.
