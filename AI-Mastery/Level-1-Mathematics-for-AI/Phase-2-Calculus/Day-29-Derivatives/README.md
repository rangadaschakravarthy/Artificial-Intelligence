# Day 29 — Derivatives

## Learning Objectives
- Master the formal definition of the Derivative $f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$
- Understand derivatives geometrically as tangent line slopes and rate of change
- Compute derivatives of basic functions ($x^n, e^x, \ln(x), \sin(x)$)
- Connect derivatives to loss function sensitivity in machine learning

## Prerequisites
Day 26 — Introduction to Calculus, Day 28 — Limits

## Topics Covered
- Formal Definition of Derivative $f'(x)$
- Leibniz notation $\frac{df}{dx}$ and Lagrange notation $f'(x)$
- Differentiability condition
- Derivatives of Basic Functions ($x^n, e^x, \ln(x)$)
- Numerical Differentiation (Forward, Backward, Central Difference)

## Why This Matters for AI
Derivatives quantify model sensitivity. The derivative $\frac{\partial L}{\partial w}$ tells us precisely how much the loss $L$ changes per unit change in weight $w$.

## Study Order
1. Read theory.md
2. Study examples.md
3. Run code.py
4. Complete practice.md
5. Verify with solution.md

## Practical Work
Implement central difference numerical differentiation in Python.

## Interview Preparation
Explain derivative definition and why central difference is more accurate than forward difference.

## Completion Checklist
- [ ] I can state the formal limit definition of derivative
- [ ] I can compute basic derivatives ($x^n, e^x, \ln(x)$)
- [ ] I understand central difference numerical differentiation
- [ ] I can code numerical derivatives in Python

## Estimated Difficulty
Intermediate
