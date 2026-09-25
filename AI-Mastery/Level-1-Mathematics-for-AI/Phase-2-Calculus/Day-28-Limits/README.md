# Day 28 — Limits

## Learning Objectives
- Understand Limits as the foundation of calculus and continuous analysis
- Evaluate limits algebraically: $\lim_{x \to a} f(x) = L$
- Master One-Sided Limits, Infinite Limits, and L'Hôpital's Rule for indeterminate forms ($0/0$)
- Connect limits to numerical stability and vanishing/exploding gradients in AI

## Prerequisites
Day 26 — Introduction to Calculus, Day 27 — Functions

## Topics Covered
- Limit definition and notation $\lim_{x \to a} f(x) = L$
- Left-hand $\lim_{x \to a^-}$ and Right-hand $\lim_{x \to a^+}$ limits
- Indeterminate Forms ($0/0, \infty/\infty$)
- L'Hôpital's Rule: $\lim \frac{f(x)}{g(x)} = \lim \frac{f'(x)}{g'(x)}$
- Continuity condition: $\lim_{x \to a} f(x) = f(a)$
- Numerical limits in Softmax and Loss computation

## Why This Matters for AI
Limits define derivatives and integrals. In AI engineering, limits explain numerical underflow/overflow (e.g. $\log(0) \to -\infty$) and justify tricks like Log-Sum-Exp for stable Softmax.

## Study Order
1. Read theory.md
2. Study examples.md
3. Run code.py
4. Complete practice.md
5. Verify with solution.md

## Practical Work
Evaluate limits numerically in Python and apply L'Hôpital's rule.

## Interview Preparation
Explain L'Hôpital's Rule and how to handle $0/0$ indeterminate forms in AI loss functions.

## Completion Checklist
- [ ] I can evaluate basic limits algebraically
- [ ] I know when to use L'Hôpital's Rule
- [ ] I understand continuity conditions
- [ ] I can prevent log(0) underflow in Python using epsilon

## Estimated Difficulty
Intermediate
