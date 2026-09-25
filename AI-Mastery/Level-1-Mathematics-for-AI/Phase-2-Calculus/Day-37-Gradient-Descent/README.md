# Day 37 — Gradient Descent

## Learning Objectives
- Master the Gradient Descent Optimization algorithm update rule $\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \nabla L(\mathbf{w}_t)$
- Distinguish between Batch Gradient Descent, Stochastic Gradient Descent (SGD), and Mini-Batch Gradient Descent
- Analyze trade-offs between computational speed, memory requirements, and gradient variance
- Implement gradient descent parameter updating loops from scratch in Python

## Prerequisites
Day 33 — Gradients, Day 36 — Loss Functions

## Topics Covered
- Gradient Descent Core Principle (Iterative steepest descent)
- Update Rule: $\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \nabla L(\mathbf{w}_t)$
- Batch Gradient Descent (Uses 100% of dataset per step)
- Stochastic Gradient Descent (SGD - Uses 1 sample per step)
- Mini-Batch Gradient Descent (Uses batch of $B=32..256$ samples per step)
- Gradient Variance and Epochs vs Iterations

## Why This Matters for AI
Gradient Descent is the foundational optimization algorithm used to train virtually all machine learning models and deep neural networks in existence.

## Study Order
1. Read theory.md
2. Study examples.md
3. Run code.py
4. Complete practice.md
5. Verify with solution.md

## Practical Work
Implement Batch, Stochastic, and Mini-Batch Gradient Descent in Python on synthetic regression data.

## Interview Preparation
Compare Batch GD vs SGD vs Mini-Batch GD in terms of memory, speed, and gradient variance.

## Completion Checklist
- [ ] I can state the Gradient Descent update rule
- [ ] I can differentiate Batch GD, SGD, and Mini-Batch GD
- [ ] I know what Epochs and Iterations mean
- [ ] I can code Mini-Batch SGD in Python

## Estimated Difficulty
Intermediate
