# Day 34 — Jacobians

## Learning Objectives
- Master the Jacobian Matrix $\mathbf{J} \in \mathbb{R}^{m \times n}$ for vector-valued functions $\mathbf{f}: \mathbb{R}^n \rightarrow \mathbb{R}^m$
- Construct Jacobian matrices of all first-order partial derivatives
- Understand Jacobian Determinant $|\det(\mathbf{J})|$ as local volume scaling factor
- Connect Jacobians to multi-output neural network layers and Normalizing Flow generative models

## Prerequisites
Day 31 — Partial Derivatives, Day 33 — Gradients

## Topics Covered
- Vector-valued functions $\mathbf{f}(\mathbf{x}) = [f_1(\mathbf{x}), \dots, f_m(\mathbf{x})]^T$
- Jacobian Matrix definition and index structure $J_{i,j} = \frac{\partial f_i}{\partial x_j}$
- Jacobian of linear transformation $\mathbf{f}(\mathbf{x}) = \mathbf{A}\mathbf{x}$ is $\mathbf{A}$
- Jacobian Determinant $|\det(\mathbf{J})|$ and change-of-variables
- Jacobians in Normalizing Flows and Multi-Output Neural Networks

## Why This Matters for AI
When a neural network layer transforms a vector of size $n$ to an output vector of size $m$, the Jacobian matrix $J_{m \times n}$ represents the complete first-order sensitivity matrix connecting all outputs to all inputs.

## Study Order
1. Read theory.md
2. Study examples.md
3. Run code.py
4. Complete practice.md
5. Verify with solution.md

## Practical Work
Compute Jacobian matrices analytically and numerically using PyTorch/NumPy.

## Interview Preparation
Explain what a Jacobian matrix is, its dimensions, and why Jacobian determinant is used in Normalizing Flows.

## Completion Checklist
- [ ] I can state the formula for a Jacobian matrix
- [ ] I can compute the Jacobian for 2D->2D vector functions
- [ ] I understand Jacobian determinant volume scaling
- [ ] I can compute Jacobians in Python

## Estimated Difficulty
Advanced
