# Practice Problems — Student's t-Distribution and Chi-Square Distribution

## Level 1: Basic Concept Checks
1. When should you use Student's t-distribution instead of Standard Normal $Z$?
2. What is the degrees of freedom ($df$) for a 1-sample t-test with sample size $N$?
3. Describe the shape of a Chi-Square distribution $\chi^2_k$.
4. What happens to the shape of Student's t-distribution as degrees of freedom $df \to \infty$?
5. Write the formula for Chi-Square test statistic $\chi^2$.

## Level 2: Direct Calculations
6. Given $N=25, ar{x}=105, s=10, \mu_0=100$. Compute $t$-statistic.
7. State $df$ for the t-test in Q6.
8. Find critical value $t_{crit}$ for 2-tailed test with $df=24$ at $lpha=0.05$ using SciPy.
9. Observed counts: $O = [30, 20]$, Expected: $E = [25, 25]$. Compute $\chi^2$.
10. State $df$ for the Chi-Square test in Q9.

## Level 3: Conceptual & Multi-Step Problems
11. Explain why the $t$-distribution has wider, heavier tails than the Normal distribution for small $N$.
12. Show that mean and variance of $\chi^2_k$ distribution are $E[X] = k$ and $	ext{Var}(X) = 2k$.
13. Show that $df$ for a contingency table with $r$ rows and $c$ columns is $(r-1)(c-1)$.
14. Explain why Chi-Square values can never be negative ($\chi^2 \ge 0$).
15. Differentiate 1-sample t-test, 2-sample independent t-test, and paired t-test.

## Level 4: AI & ML Applications
16. Write Python code using `scipy.stats.ttest_1samp` to test if model execution time mean differs from 50 ms.
17. Write Python code using `scipy.stats.ttest_ind` to compare accuracy scores of Model A vs Model B across 10 cross-validation folds.
18. Write Python code using `scipy.stats.chi2_contingency` to test independence between feature "User Device" and label "Conversion".
19. Compute $95\%$ confidence interval for mean latency using Student's t-distribution in Python (`stats.t.interval`).
20. In cross-validation evaluation ($K=10$), why is a paired t-test appropriate for comparing two model architectures evaluated on identical data folds?

## Level 5: Interview Questions
21. Prove that $t$-statistic $t = \frac{Z}{\sqrt{U / 
u}}$ where $Z \sim \mathcal{N}(0,1)$ and $U \sim \chi^2_
u$ independent follows Student's t-distribution.
22. Why does Welch's t-test replace Student's t-test when two sample groups have unequal variances (Heteroscedasticity)?
23. Write Python code using SciPy to perform 1-sample t-test, 2-sample t-test, and Chi-Square test on synthetic data.
