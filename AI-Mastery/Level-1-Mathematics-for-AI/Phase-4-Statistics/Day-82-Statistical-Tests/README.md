# Day 82 — Statistical Tests (Z-Test, t-Test, Chi-Square Test)

## Learning Objectives
- Master 1-Sample and 2-Sample $Z$-Tests.
- Master 1-Sample, 2-Sample Independent, and Paired $t$-Tests.
- Master Chi-Square Test of Independence and Goodness-of-Fit.
- Build a Unified Statistical Test Decision Engine in Python.

## Prerequisites
- Days 78–81 Hypothesis testing, $p$-values, errors.

## Topics Covered
1. Statistical Test Selection Tree
2. $Z$-Test Formulas (1-Sample, 2-Sample Proportions)
3. $t$-Test Formulas (1-Sample, 2-Sample Independent, Paired)
4. Chi-Square Test Formulas (Independence & Goodness-of-Fit)
5. Comprehensive Python Statistical Test Suite (`scipy.stats`)

## Why This Matters for AI
Statistical test selection is the core execution step for data science validation, A/B testing, cross-validation fold comparison, and feature independence filtering.

## Study Order
1. Read `theory.md`.
2. Review 5 examples in `examples.md`.
3. Complete `practice.md`.
4. Validate with `solution.md`.
5. Run `code.py`.

## Checklist
- [ ] Select test based on data type, sample size, and group independence
- [ ] Compute $t$-test using `stats.ttest_ind` and `stats.ttest_rel`
- [ ] Compute Chi-Square test using `stats.chi2_contingency`
- [ ] Code unified decision engine in Python

## Estimated Difficulty
- **Difficulty**: 4/10
- **Duration**: 2.5 Hours
