# Day 31 — Partial Derivatives

## Learning Objectives
- Master multi-variable functions $f(x, y, z)$ and partial differentiation
- Calculate partial derivatives $\frac{\partial f}{\partial x}$ treating other variables as constants
- Understand Clairaut's Theorem on equality of mixed partial derivatives $\frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x}$
- Apply partial derivatives to loss functions with multiple weight parameters

## Prerequisites
Day 29 — Derivatives, Day 30 — Derivative Rules

## Topics Covered
- Multi-variable functions $f(x_1, x_2, \dots, x_n)$
- Partial Derivative definition and curly delta notation $\frac{\partial f}{\partial x_i}$
- Treating non-target variables as constants during differentiation
- Second-order partial derivatives $\frac{\partial^2 f}{\partial x^2}, \frac{\partial^2 f}{\partial x \partial y}$
- Clairaut's Theorem (Schwarz's Theorem) on mixed partials

## Why This Matters for AI
Real AI loss functions depend on millions of weight parameters $L(w_1, w_2, \dots, w_m)$. Partial derivatives compute the individual slope of loss with respect to each single weight.

## Study Order
1. Read theory.md
2. Study examples.md
3. Run code.py
4. Complete practice.md
5. Verify with solution.md

## Practical Work
Compute partial derivatives algebraically and evaluate numerical partial derivatives using Python.

## Interview Preparation
Explain partial derivative definition and Clairaut's Theorem.

## Completion Checklist
- [ ] I can calculate partial derivatives $\frac{\partial f}{\partial x}$ and $\frac{\partial f}{\partial y}$
- [ ] I know how to treat non-target variables as constants
- [ ] I understand mixed partial derivatives
- [ ] I can code partial derivatives in Python

## Estimated Difficulty
Intermediate
