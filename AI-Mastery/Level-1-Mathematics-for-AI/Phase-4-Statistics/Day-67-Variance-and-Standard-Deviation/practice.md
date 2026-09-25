# Day 67 Practice Questions: Variance and Standard Deviation

## Level 1: Basic Concepts
1. What is Variance?
2. What is Standard Deviation?
3. What is Bessel's correction?
4. Why do we square deviations instead of taking simple sum of deviations?
5. What are the mean and standard deviation of standardized z-scores?

## Level 2: Calculation
6. Calculate sample variance and std for [4, 8, 12].
7. Compute population variance for [4, 8, 12].
8. If Var(X) = 16, compute Var(5 X - 3).
9. Calculate Z-score for x = 110 given μ = 100, σ = 15.
10. Given sum (x_i - x_bar)^2 = 180 and n = 11, find s^2 and s.

## Level 3: Conceptual & Proofs
11. Prove that E[s^2] = σ^2 when dividing by n-1 (Bessel's proof outline).
12. Prove Var(a X + b) = a^2 Var(X).
13. Show that Var(X) = E[X^2] - (E[X])^2.
14. Explain why standard deviation is in the same physical units as the mean.
15. Why does adding constant c to all data points leave variance unchanged?

## Level 4: AI Applications
16. How does Standardizing features prevent gradient descent oscillation?
17. Why add epsilon ε in Batch Normalization denominator?
18. How is sample variance used in active learning for uncertainty sampling?
19. Why do distance metrics fail when feature variances differ by orders of magnitude?
20. Explain weight initialization scaling (He / Xavier) using weight variance.

## Level 5: Interview Questions
21. "Derive Var(X) = E[X^2] - (E[X])^2 from definition of variance."
22. "Write Python function computing both population and sample standard deviation."
23. "Explain how Xavier initialization sets layer weight variance Var(W) = 2 / (fan_in + fan_out)."
