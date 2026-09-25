# Practice Problems — Type I and Type II Errors

## Level 1: Basic Concept Checks
1. Define Type I Error ($lpha$).
2. Define Type II Error ($eta$).
3. State the formula for Statistical Power.
4. What is the standard target statistical power in experimental design?
5. How does increasing sample size $n$ affect Type II error $eta$?

## Level 2: Direct Calculations
6. If Type II error $eta = 0.10$, compute Statistical Power.
7. If Statistical Power $= 0.92$, compute Type II error $eta$.
8. In a test with $lpha = 0.05$ and $H_0$ is true, what is the probability of making a Type I error?
9. In Q8, what is the probability of correctly failing to reject $H_0$?
10. Use Python `TTestIndPower` to find power for $n=100, d=0.3, lpha=0.05$.

## Level 3: Conceptual & Multi-Step Problems
11. Explain the fundamental trade-off between Type I error $lpha$ and Type II error $eta$.
12. Why do autonomous vehicle safety systems minimize Type II errors (false negatives in pedestrian detection) even at the cost of higher Type I errors (false braking alarms)?
13. Show how increasing effect size $d$ shifts the alternative distribution further from the null distribution, reducing overlap area $eta$ and increasing power $1-eta$.
14. Explain how underpowered A/B tests ($n$ too small, power $< 50\%$) cause companies to mistakenly abandon effective AI model improvements.
15. Explain why testing multiple metrics simultaneously increases overall Type I error risk (Family-Wise Error Rate).

## Level 4: AI & ML Applications
16. Write Python code using `statsmodels.stats.power.TTestIndPower` to plot Power vs Sample Size curves for different effect sizes $d \in \{0.2, 0.5, 0.8\}$.
17. Write Python code to calculate minimum required sample size per group for an A/B test with expected lift $d = 0.2$, $lpha = 0.05$, power $= 0.80$.
18. Relate Type I and Type II errors in hypothesis testing to False Positive Rate ($FPR$) and False Negative Rate ($FNR$) in binary confusion matrices.
19. Compute Precision and Recall equivalents in hypothesis testing terminology.
20. In fraud detection models, if cost of false positive (blocking clean card) is $5 and cost of false negative (fraud loss) is $500, how should prediction probability threshold be set?

## Level 5: Interview Questions
21. Derive the mathematical relationship between sample size $n$, effect size $d$, $lpha$, and $eta$ for a 2-sample $Z$-test: $n = rac{2 (Z_{lpha/2} + Z_{eta})^2}{d^2}$.
22. How do you conduct a post-hoc power analysis, and why is pre-experiment power planning preferred?
23. Write Python code using `statsmodels` to run complete power analysis and sample size estimation pipeline for an AI experiment.
