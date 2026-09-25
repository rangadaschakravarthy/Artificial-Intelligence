# Day 81 — Type I and Type II Errors

## Learning Objectives
- Master Type I Error $lpha$ (False Positive) and Type II Error $eta$ (False Negative).
- Master Statistical Power $(1 - eta)$ and factors influencing power.
- Understand the trade-off between $lpha$ and $eta$.
- Compute power and required sample size in Python using `statsmodels`.

## Prerequisites
- Days 78–80 Hypothesis testing and $p$-values.

## Topics Covered
1. Confusion Matrix of Hypothesis Testing
2. Type I Error $lpha$ (False Positive / False Alarm Rate)
3. Type II Error $eta$ (False Negative / Miss Rate)
4. Statistical Power ($1 - eta$)
5. Power Analysis for A/B Testing Sample Size Calculation

## Why This Matters for AI
In medical AI, autonomous driving, and A/B testing, balancing Type I errors (false alarms) against Type II errors (missed critical events) governs system threshold tuning.

## Study Order
1. Read `theory.md`.
2. Review 5 examples in `examples.md`.
3. Complete `practice.md`.
4. Validate with `solution.md`.
5. Run `code.py`.

## Checklist
- [ ] Understand $lpha = P(	ext{Reject } H_0 \mid H_0 	ext{ True})$
- [ ] Understand $eta = P(	ext{Fail to Reject } H_0 \mid H_0 	ext{ False})$
- [ ] Understand Power $= 1 - eta$ (Target $\ge 0.80$)
- [ ] Perform Power Analysis in Python

## Estimated Difficulty
- **Difficulty**: 3/10
- **Duration**: 2.0 Hours
