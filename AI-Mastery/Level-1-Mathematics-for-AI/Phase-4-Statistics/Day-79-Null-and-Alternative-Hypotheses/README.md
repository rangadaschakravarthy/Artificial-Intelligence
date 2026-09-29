# Day 79 — Null and Alternative Hypotheses

## Learning Objectives
- Formulate precise mathematical Null ($H_0$) and Alternative ($H_a$) hypotheses across different AI scenarios.
- Master Equality vs Inequality constraints ($=, 
\neq, \le, \ge, <, >$).
- Understand Directional vs Non-Directional Hypotheses.
- Write hypothesis generators in Python.

## Prerequisites
- Day 78 Introduction to Hypothesis Testing.

## Topics Covered
1. Deep Dive into Null Hypothesis $H_0$
2. Deep Dive into Alternative Hypothesis $H_a$
3. Mathematical Rules for Operator Placement ($=, \le, \ge$ ALWAYS in $H_0$)
4. A/B Testing Hypotheses Formulations
5. Model Comparison Hypotheses Formulations

## Why This Matters for AI
Correctly translating business and technical goals (e.g., "Is Model B accuracy higher than Model A?") into mathematical $H_0$ and $H_a$ statements is the starting requirement for all A/B testing and AI validation.

## Study Order
1. Read `theory.md`.
2. Review 5 examples in `examples.md`.
3. Complete `practice.md`.
4. Validate with `solution.md`.
5. Run `code.py`.

## Checklist
- [ ] Ensure $=$ is in $H_0$
- [ ] Match research question to $H_a$
- [ ] Differentiate 2-tailed ($H_a: 
\neq$) vs 1-tailed ($H_a: >, <$)
- [ ] Code hypothesis setup in Python

## Estimated Difficulty
- **Difficulty**: 2/10
- **Duration**: 1.5 Hours
