# Day 72 — Student's t-Distribution and Chi-Square Distribution

## Learning Objectives
- Master Student's t-distribution math, degrees of freedom ($df$), and tail behavior.
- Master Chi-Square distribution $\chi^2_k$ math and degrees of freedom.
- Understand when to use $t$-distribution vs Standard Normal $Z$.
- Evaluate $t$ and $\chi^2$ critical values and probabilities in Python.

## Prerequisites
- Days 69–70 Normal distribution and statistical distributions.

## Topics Covered
1. Student's $t$-Distribution PDF and Degrees of Freedom ($df = N - 1$)
2. $t$-Distribution vs Standard Normal $Z$ Distribution
3. Chi-Square Distribution $\chi^2_k$ Properties
4. Degrees of Freedom Concept in Statistical Models
5. Python Evaluation (`scipy.stats.t`, `scipy.stats.chi2`)

## Why This Matters for AI
Small sample model benchmarking ($N < 30$), feature selection variance testing, and contingency table categorical testing rely on $t$ and $\chi^2$ distributions.

## Study Order
1. Read `theory.md`.
2. Review 5 examples in `examples.md`.
3. Complete `practice.md`.
4. Validate with `solution.md`.
5. Run `code.py`.

## Checklist
- [ ] Understand $df = N - 1$
- [ ] Compute $t$-score $t = \frac{ar{x} - \mu}{s / \sqrt{N}}$
- [ ] Evaluate $\chi^2$ test statistic $\sum \frac{(O - E)^2}{E}$
- [ ] Compute $t$ and $\chi^2$ probabilities in SciPy

## Estimated Difficulty
- **Difficulty**: 4/10
- **Duration**: 2.5 Hours
