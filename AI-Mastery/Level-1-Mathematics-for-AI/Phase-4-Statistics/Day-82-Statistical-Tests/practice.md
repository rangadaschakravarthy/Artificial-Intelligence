# Practice Problems — Statistical Tests

## Level 1: Basic Concept Checks
1. When should you use a Paired t-test instead of an Independent 2-Sample t-test?
2. What statistical test checks independence between two categorical features?
3. What is Welch's t-test, and when should it be used?
4. What test compares 1 continuous sample mean against a target benchmark $\mu_0$?
5. State the degrees of freedom for a Paired t-test with $N$ pairs.

## Level 2: Direct Calculations
6. Sample $n=25, ar{x}=108, s=10$. Test $H_0: \mu = 100$. Compute $t$-statistic.
7. Two independent samples: $ar{x}_1=80, s_1=5, n_1=10$; $ar{x}_2=85, s_2=5, n_2=10$. Compute $t$-statistic.
8. Paired differences: $ar{d} = 4.0, s_d = 2.0, n = 16$. Compute $t$-statistic.
9. Chi-Square table: $O = [30, 20]$, $E = [25, 25]$. Compute $\chi^2$.
10. Compute $p$-value for $t=2.50, df=24$ (2-tailed) in SciPy.

## Level 3: Conceptual & Multi-Step Problems
11. Explain why pairing sample measurements (e.g. evaluating two algorithms on identical cross-validation folds) reduces variance and boosts statistical power.
12. Show how Welch's t-test modifies standard error and degrees of freedom to handle unequal sample variances.
13. Explain Yates' Continuity Correction for $2 	imes 2$ Chi-Square contingency tables.
14. Show that a 2-sample $Z$-test for proportions is mathematically equivalent to a $1 	imes 2$ Chi-Square test with $df = 1$.
15. Explain how ANOVA (Analysis of Variance) generalizes the 2-sample t-test to $K > 2$ group means.

## Level 4: AI & ML Applications
16. Write Python function `select_and_run_test(data1, data2, data_type, is_paired)` that selects and executes the appropriate statistical test.
17. Write Python code to evaluate 5 model architectures on 10 cross-validation folds using 1-Way ANOVA (`scipy.stats.f_oneway`).
18. In feature selection, explain how Chi-Square feature scoring (`SelectKBest(chi2)`) filters uninformative categorical features.
19. Write Python code to run 5x2-fold Cross-Validated Paired t-test (Dietterich's test) for comparing two classifiers.
20. In NLP sentiment analysis, test if sentiment rating (1-5) differs significantly across 3 user subscription tiers.

## Level 5: Interview Questions
21. Prove that for $df = 1$, the square of a Student's $t$ variable equals an $F$ variable ($t^2 = F_{1, df}$).
22. Why is running multiple pairwise t-tests across 4 models without ANOVA or Bonferroni correction invalid?
23. Write a self-contained Python class `StatisticalTestSuite` that automates Normality testing, Test selection, $p$-value calculation, and Effect Size reporting.
