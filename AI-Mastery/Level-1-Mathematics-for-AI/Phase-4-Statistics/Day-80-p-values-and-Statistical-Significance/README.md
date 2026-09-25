# Day 80 — p-values and Statistical Significance

## Learning Objectives
- Master definition of $p$-value: $P(	ext{Data as or more extreme} \mid H_0 	ext{ is true})$.
- Understand significance level $lpha$ and decision rule ($p \le lpha \implies 	ext{Reject } H_0$).
- Avoid common $p$-value misconceptions.
- Compute $p$-values in Python across $Z, t, \chi^2$ statistics.

## Prerequisites
- Days 78–79 Hypothesis testing framework and hypotheses.

## Topics Covered
1. What is a $p$-value? (Formal Definition & Intuition)
2. Comparing $p$-value to Significance Level $lpha$
3. $p$-value Misconceptions ($p$-value is NOT $P(H_0 	ext{ is true})$!)
4. Practical Significance vs Statistical Significance (Effect Size)
5. $p$-value Calculation in Python

## Why This Matters for AI
$p$-values quantify whether an observed accuracy increase or loss reduction in an A/B test could have occurred by pure random chance.

## Study Order
1. Read `theory.md`.
2. Review 5 examples in `examples.md`.
3. Complete `practice.md`.
4. Validate with `solution.md`.
5. Run `code.py`.

## Checklist
- [ ] Memorize formal definition of $p$-value
- [ ] Apply decision rule: $p \le lpha \implies$ Reject $H_0$
- [ ] Identify $p$-value misconceptions
- [ ] Compute $p$-values in Python using SciPy

## Estimated Difficulty
- **Difficulty**: 3/10
- **Duration**: 2.0 Hours
