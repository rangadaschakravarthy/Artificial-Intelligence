# Day 35 — Optimization

## Learning Objectives
- Master Mathematical Optimization principles for machine learning
- Identify Critical Points where gradient vector $\nabla f(\mathbf{x}) = \mathbf{0}$
- Construct the Hessian Matrix $\mathbf{H} \in \mathbb{R}^{n \times n}$ of second-order partial derivatives
- Classify critical points (Local Minima, Local Maxima, Saddle Points) using Hessian Eigenvalues
- Understand Convex vs Non-Convex optimization landscapes in Deep Learning

## Prerequisites
Day 33 — Gradients, Day 34 — Jacobians

## Topics Covered
- Unconstrained Optimization problem $\min_{\mathbf{x}} f(\mathbf{x})$
- First-Order Necessary Condition: $\nabla f(\mathbf{x}^*) = \mathbf{0}$
- Hessian Matrix definition $H_{i,j} = \frac{\partial^2 f}{\partial x_i \partial x_j}$
- Second-Order Conditions (Hessian Positive Definite $\mathbf{H} \succ 0 \implies$ Minimum)
- Saddle Points in High-Dimensional Loss Landscapes

## Why This Matters for AI
Training AI models IS optimization. Understanding loss surface geometry (saddle points, local minima, Hessian curvature) allows us to design better optimizers and learning rate schedules.

## Study Order
1. Read theory.md
2. Study examples.md
3. Run code.py
4. Complete practice.md
5. Verify with solution.md

## Practical Work
Find critical points algebraically and classify them using Hessian eigenvalues in Python.

## Interview Preparation
Explain how Hessian matrix eigenvalues classify local minima, local maxima, and saddle points.

## Completion Checklist
- [ ] I can find critical points where $\nabla f = \mathbf{0}$
- [ ] I can construct the Hessian matrix $H_{i,j} = \frac{\partial^2 f}{\partial x_i \partial x_j}$
- [ ] I can classify critical points using Hessian eigenvalues
- [ ] I understand saddle points in high-D spaces

## Estimated Difficulty
Advanced
