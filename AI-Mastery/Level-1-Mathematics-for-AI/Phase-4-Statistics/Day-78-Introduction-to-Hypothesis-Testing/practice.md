# Practice Problems — Introduction to Hypothesis Testing

## Level 1: Basic Concept Checks
1. List the 5 steps of the Hypothesis Testing Framework.
2. What does the Null Hypothesis $H_0$ represent?
3. What does the Alternative Hypothesis $H_a$ represent?
4. What is the standard significance level $lpha$?
5. When should you use a 1-tailed test instead of a 2-tailed test?

## Level 2: Direct Calculations
6. Formulate $H_0$ and $H_a$ for testing if average model training time has decreased below 10 hours.
7. For $lpha = 0.01$ in a 2-tailed Z-test, find $Z_{crit}$.
8. For $lpha = 0.05$ in a 1-tailed Left Z-test ($H_a: \mu < \mu_0$), find $Z_{crit}$.
9. Calculated $Z = -1.80$. Critical value for 1-tailed Left test at $lpha = 0.05$ is $Z_{crit} = -1.645$. Make decision.
10. Calculated $Z = +1.50$. Critical value for 2-tailed test at $lpha = 0.05$ is $Z_{crit} = \pm 1.96$. Make decision.

## Level 3: Conceptual & Multi-Step Problems
11. Explain why failing to reject $H_0$ is NOT equivalent to "proving $H_0$ is true" (Absence of evidence is not evidence of absence).
12. Why is the Null Hypothesis always formulated with an equality constraint ($=, \le, \ge$)?
13. Show why choosing a 1-tailed test AFTER looking at sample data is a violation of statistical integrity (p-hacking).
14. Explain how criminal trials mirror hypothesis testing ($H_0$: Defendant is Innocent; $H_a$: Defendant is Guilty).
15. Explain how setting $lpha = 0.01$ instead of $lpha = 0.05$ changes the burden of proof required to reject $H_0$.

## Level 4: AI & ML Applications
16. In A/B testing a new recommendation algorithm, write $H_0$ and $H_a$ for click-through rate $CTR$.
17. Write Python code using `scipy.stats` to find 1-tailed and 2-tailed $Z$ critical values for any input $lpha$.
18. In AI safety testing, write $H_0$ and $H_a$ for verifying an autonomous vehicle collision rate is below human baseline.
19. Explain how cross-validation error differences across folds form the dataset for a paired t-test between two AI algorithms.
20. In automated ML benchmarking pipelines, why must significance level $lpha$ be declared before running experiments?

## Level 5: Interview Questions
21. Why can we never "accept" the Null Hypothesis?
22. How does the choice between 1-tailed and 2-tailed tests affect the statistical power to detect an effect in a specific direction?
23. Write Python code using SciPy to implement the 5-step hypothesis testing framework on sample metric data.
