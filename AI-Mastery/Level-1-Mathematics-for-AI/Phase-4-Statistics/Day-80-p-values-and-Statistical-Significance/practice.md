# Practice Problems — p-values and Statistical Significance

## Level 1: Basic Concept Checks
1. Define $p$-value in formal statistical terms.
2. State the decision rule comparing $p$-value to significance level $lpha$.
3. True or False: A $p$-value of $0.04$ means there is a $4\%$ probability that the Null Hypothesis is true.
4. What is the relationship between sample size $n$ and $p$-value for a fixed non-zero effect size?
5. Differentiate Statistical Significance from Practical Significance.

## Level 2: Direct Calculations
6. Given $Z = +1.96$ in a 2-tailed Z-test, compute $p$-value given $\Phi(1.96) = 0.9750$.
7. Given $Z = -2.33$ in a 1-tailed Left Z-test, compute $p$-value given $\Phi(-2.33) = 0.0100$.
8. Calculated $t = +2.50$ for $df = 20$. Compute 2-tailed $p$-value using SciPy.
9. If $p$-value $= 0.024$ and $lpha = 0.05$, state the decision.
10. If $p$-value $= 0.082$ and $lpha = 0.05$, state the decision.

## Level 3: Conceptual & Multi-Step Problems
11. Explain why doubling single-tail probability is required to calculate 2-tailed $p$-values.
12. Show how $p$-hacking (repeatedly testing hypotheses or stopping data collection when $p < 0.05$) inflates false positive rates.
13. State Cohen's $d$ guidelines for Small ($0.2$), Medium ($0.5$), and Large ($0.8$) effect sizes.
14. Explain why the American Statistical Association (ASA) issued a statement warning against over-reliance on $p < 0.05$ thresholds.
15. Explain how Bonferroni Correction $lpha_{new} = lpha / m$ controls Family-Wise Error Rate across $m$ multiple tests.

## Level 4: AI & ML Applications
16. Write Python code using SciPy to compute 2-tailed $p$-value for test statistic $t = 2.45$ with $df = 30$.
17. Write Python code implementing Bonferroni Correction on an array of 20 raw $p$-values.
18. Write Python code implementing Benjamini-Hochberg False Discovery Rate (FDR) control in Python.
19. In A/B testing, why does checking $p$-values daily during test execution increase false positive rates (Peeking Problem)?
20. Calculate Cohen's $d$ in Python for two accuracy fold arrays `scores_A` and `scores_B`.

## Level 5: Interview Questions
21. Why does $P(	ext{Data} | H_0) 
\neq P(H_0 | 	ext{Data})$? Explain using Bayes' Theorem.
22. How do Sequential Analysis methods (e.g. mSPRT) solve the A/B testing Peeking Problem?
23. Write Python code using SciPy to perform 2-sample t-test, compute $p$-value, compute Cohen's $d$ effect size, and print full report.
