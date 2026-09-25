# Day 33 — Gradients

## Learning Objectives
- Master the Gradient Vector $\nabla f = \left[\frac{\partial f}{\partial x_1}, \dots, \frac{\partial f}{\partial x_n}\right]^T$
- Understand geometric property: $\nabla f$ points in the direction of STEEPEST ASCENT
- Understand negative gradient $-\nabla f$ points in the direction of STEEPEST DESCENT
- Compute gradients of multi-variable loss surfaces and vector functions

## Prerequisites
Day 31 — Partial Derivatives, Day 32 — Chain Rule

## Topics Covered
- Gradient Vector definition $\nabla f$ (nabla operator)
- Gradient vector geometry (orthogonal to level sets / contour lines)
- Steepest Ascent direction $(\nabla f)$ and Steepest Descent direction $(-\nabla f)$
- Directional Derivative $D_{\mathbf{u}} f = \nabla f \cdot \mathbf{u}$
- Gradient computation of Mean Squared Error and Cross-Entropy loss

## Why This Matters for AI
The Gradient Vector is the single most important vector in AI optimization. Every gradient-based training algorithm (SGD, Adam, RMSprop) moves model parameters in the direction of the negative gradient vector $-\nabla L(\mathbf{w})$ to minimize loss.

## Study Order
1. Read theory.md
2. Study examples.md
3. Run code.py
4. Complete practice.md
5. Verify with solution.md

## Practical Work
Compute gradient vectors algebraically and visualize 2D loss contour gradient vectors in Python.

## Interview Preparation
Explain why $\nabla f$ points in steepest ascent direction and why gradient is perpendicular to contour lines.

## Completion Checklist
- [ ] I can compute gradient vector $\nabla f(\mathbf{x})$
- [ ] I know $\nabla f$ is steepest ascent and $-\nabla f$ is steepest descent
- [ ] I understand orthogonality to contour level sets
- [ ] I can compute gradient vectors in Python

## Estimated Difficulty
Intermediate
