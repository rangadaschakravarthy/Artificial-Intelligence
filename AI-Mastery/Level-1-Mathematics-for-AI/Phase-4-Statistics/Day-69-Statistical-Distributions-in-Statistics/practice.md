# Practice Problems — Statistical Distributions in Statistics

## Level 1: Basic Concept Checks
1. What is the fundamental difference between parametric and non-parametric statistical tests?
2. Which test checks if sample data is Normally distributed?
3. State the distribution of the sum of $k$ squared independent standard normal variables.
4. Name the distribution used for small-sample ($N < 30$) mean inference when population variance is unknown.
5. Which distribution models ratio of two independent sample variances in ANOVA?

## Level 2: Direct Calculations
6. Run Shapiro-Wilk test on sample array in Python and report $p$-value.
7. Given $Z \sim \mathcal{N}(0, 1)$, what is $E[Z^2]$?
8. If $X \sim \chi^2_k$, what is $E[X]$ and $	ext{Var}(X)$ in terms of degrees of freedom $k$?
9. Convert raw feature data to normal scores using SciPy `stats.boxcox`.
10. Identify distribution for binary outcome $Y \in \{0, 1\}$.

## Level 3: Conceptual & Multi-Step Problems
11. Explain why Student's t-distribution has heavier tails than the Standard Normal distribution for small $df$.
12. Show that as degrees of freedom $df 	o \infty$, Student's t-distribution converges to the Standard Normal distribution.
13. Explain why non-parametric rank-sum tests (Mann-Whitney U) are less sensitive to extreme outliers than t-tests.
14. Show that if $X \sim \chi^2_{k_1}$ and $Y \sim \chi^2_{k_2}$ are independent, then $X + Y \sim \chi^2_{k_1 + k_2}$.
15. Explain how goodness-of-fit Kolmogorov-Smirnov test uses maximum empirical distribution distance $D$.

## Level 4: AI & ML Applications
16. Write Python code using SciPy to perform Shapiro-Wilk normality test on all numerical columns of a Pandas DataFrame.
17. Write Python code to plot Q-Q plot (Quantile-Quantile plot) to visually inspect normality.
18. In linear regression assumptions, why must error residuals $e_i = y_i - \hat{y}_i$ be Normally distributed $\mathcal{N}(0, \sigma^2)$?
19. Write Python code to perform 2-sample Kolmogorov-Smirnov test comparing train vs test feature distributions (detecting Data Drift).
20. In A/B testing continuous metrics, when should you switch from a 2-sample t-test to a Mann-Whitney U test?

## Level 5: Interview Questions
21. Derive the connection between Normal, Chi-Square, Student's t, and F distributions.
22. Why does violating the Normality assumption in small samples ($N < 15$) invalidate t-test $p$-values?
23. Write Python code using SciPy to run Shapiro-Wilk, Kolmogorov-Smirnov, and Anderson-Darling normality tests on a dataset.
