# Day 30 — Derivative Rules

## Learning Objectives
- Master core rules of differentiation: Constant Multiple, Sum/Difference, Product, and Quotient Rules
- Calculate derivatives of combined algebraic and transcendental functions
- Apply derivative rules to common ML error functions
- Prepare for multi-variable calculus and chain rule

## Prerequisites
Day 29 — Derivatives

## Topics Covered
- Constant Multiple Rule: $\frac{d}{dx}[c f(x)] = c f'(x)$
- Sum and Difference Rule: $\frac{d}{dx}[f(x) \pm g(x)] = f'(x) \pm g'(x)$
- Product Rule: $\frac{d}{dx}[f(x) g(x)] = f'(x) g(x) + f(x) g'(x)$
- Quotient Rule: $\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2}$
- Derivative of Sigmoid activation function $\sigma'(x) = \sigma(x)(1 - \sigma(x))$

## Why This Matters for AI
Derivative rules allow us to differentiate complex ML formulas algebraically. For example, deriving the Sigmoid activation derivative $\sigma'(x) = \sigma(x)(1 - \sigma(x))$ is a classic ML interview question.

## Study Order
1. Read theory.md
2. Study examples.md
3. Run code.py
4. Complete practice.md
5. Verify with solution.md

## Practical Work
Derive Sigmoid derivative algebraically and verify numerically in Python.

## Interview Preparation
Derive the derivative of Sigmoid function $\sigma(x) = \frac{1}{1 + e^{-x}}$ step-by-step.

## Completion Checklist
- [ ] I know Constant Multiple, Sum, Product, and Quotient rules
- [ ] I can derive the derivative of Sigmoid function
- [ ] I can compute derivatives of combined expressions
- [ ] I can verify derivative rules using Python SymPy

## Estimated Difficulty
Intermediate
