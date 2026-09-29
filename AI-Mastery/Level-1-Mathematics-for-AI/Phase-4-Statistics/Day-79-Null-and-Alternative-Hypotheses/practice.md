# Practice Problems — Null and Alternative Hypotheses

## Level 1: Basic Concept Checks
1. Which hypothesis ($H_0$ or $H_a$) must contain the equality operator ($=$)?
2. Which hypothesis represents the research claim being tested?
3. State $H_0$ and $H_a$ for testing if two population means are equal.
4. What tail type corresponds to $H_a: \mu > 100$?
5. What tail type corresponds to $H_a: \mu 
\neq 100$?

## Level 2: Direct Calculations
6. Formulate $H_0$ and $H_a$ for testing if a new recommendation engine increases average basket size above $50.
7. Formulate $H_0$ and $H_a$ for testing if server CPU usage differs from $70\%$.
8. Formulate $H_0$ and $H_a$ for testing if a data compression algorithm reduces file size below 500 MB.
9. Formulate $H_0$ and $H_a$ for testing if feature correlation $
ho$ is non-zero.
10. Formulate $H_0$ and $H_a$ for testing if Model A and Model B have identical error variance ($\sigma_1^2 = \sigma_2^2$).

## Level 3: Conceptual & Multi-Step Problems
11. Explain why placing strict inequality ($>$) in $H_0$ is a mathematical error.
12. Differentiate Superiority testing ($H_a: \mu_B - \mu_A > 0$) vs Non-Inferiority testing ($H_a: \mu_B - \mu_A > -\delta$).
13. Explain why the burden of proof rests on the Alternative Hypothesis $H_a$.
14. How does setting $H_0: 	ext{Loss}_B = 	ext{Loss}_A$ protect AI teams against deploying unnecessary complex models?
15. Explain how multiple hypothesis testing across 100 features increases overall false discovery risk.

## Level 4: AI & ML Applications
16. Write Python function `create_ab_test_hypotheses(metric, variant_a, variant_b)` returning formal $H_0$ and $H_a$ strings.
17. In linear regression summary output (`statsmodels`), state the standard $H_0$ and $H_a$ for each coefficient $p$-value.
18. In Chi-Square test of independence between two categorical features, state $H_0$ and $H_a$.
19. In Kolmogorov-Smirnov data drift test, state $H_0$ and $H_a$.
20. In Shapiro-Wilk normality test, state $H_0$ and $H_a$.

## Level 5: Interview Questions
21. Why is the Null Hypothesis formulated as a single point or half-space boundary in parameter space?
22. How does the Equivalence Testing (TOST - Two One-Sided Tests) framework flip $H_0$ and $H_a$ to prove two models are functionally identical?
23. Write Python code demonstrating formal hypothesis string generation and validation for common AI experimentation scenarios.
