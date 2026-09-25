# Practice Problems — Statistics AI Mini-Project

## Level 1: Basic Concept Checks
1. What test checks for variance homogeneity across groups?
2. What test is selected when data violates the Normality assumption?
3. What test is selected when data is Normal but has unequal group variances?
4. What is the formula for Cohen's $d$ effect size?
5. What is the standard threshold for statistical significance ($lpha$)?

## Level 2: Direct Calculations
6. Group A: $ar{x}_A = 50, s_A = 10, n_A = 30$. Group B: $ar{x}_B = 55, s_B = 10, n_B = 30$. Compute pooled $s_{pooled}$ and Cohen's $d$.
7. Baseline conversion $= 0.10$, Treatment conversion $= 0.12$. Compute relative lift percentage.
8. If $p$-value $= 0.004$ at $lpha = 0.05$, state the deployment decision.
9. If $p$-value $= 0.120$ at $lpha = 0.05$, state the deployment decision.
10. Compute $95\%$ CI for difference $ar{x}_B - ar{x}_A = 5.0$ with $SE_{	ext{diff}} = 1.5$ ($Z = 1.96$).

## Level 3: Conceptual & Multi-Step Problems
11. Explain why automated test selection prevents applying invalid parametric tests to skewed or heteroscedastic data.
12. Show how Levene's test $H_0: \sigma_1^2 = \sigma_2^2$ protects against inflated Type I error rates in Student's t-test.
13. Explain why pairing effect size (Cohen's $d$) with $p$-value is mandatory for executive decision-making.
14. Explain how sample size determination prevents underpowered A/B testing in production systems.
15. Explain how data drift monitoring via 2-sample KS tests triggers automated model retraining.

## Level 4: AI & ML Applications
16. Implement automated Shapiro-Wilk normality check function in Python.
17. Implement automated Levene's variance equality check function in Python.
18. Implement Cohen's $d$ calculation function in Python.
19. Implement complete automated A/B test evaluator class in Python.
20. Execute full `code.py` mini-project script and verify all module outputs.

## Level 5: Interview Questions
21. Walk through the complete architectural design of an automated A/B testing statistical engine.
22. How do you handle multi-armed bandit allocation (e.g. Thompson Sampling) compared to fixed-sample A/B testing?
23. Run the complete `code.py` script and present the final executive report for LEVEL 1 Mathematics for AI.
