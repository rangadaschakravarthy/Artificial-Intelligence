# Day 40 — Calculus for Neural Networks

## Learning Objectives
- Master multivariate calculus across multi-layer neural network architectures
- Formulate layer-by-layer forward and backward pass derivative equations
- Derive error delta vectors $\mathbf{\delta}^{(l)} = \frac{\partial L}{\partial \mathbf{z}^{(l)}}$
- Analyze activation function derivatives (ReLU, LeakyReLU, Sigmoid, Tanh)

## Prerequisites
Day 32 — Chain Rule, Day 36 — Loss Functions, Day 39 — Gradient Descent in ML

## Topics Covered
- Multi-layer Neural Network mathematical model
- Forward Pass equations: $\mathbf{z}^{(l)} = \mathbf{W}^{(l)} \mathbf{a}^{(l-1)} + \mathbf{b}^{(l)}, \mathbf{a}^{(l)} = \sigma(\mathbf{z}^{(l)})$
- Layer Error Vector $\mathbf{\delta}^{(l)} = \frac{\partial L}{\partial \mathbf{z}^{(l)}}$
- Backward Error Recurrence: $\mathbf{\delta}^{(l)} = (\mathbf{W}^{(l+1)T} \mathbf{\delta}^{(l+1)}) \odot \sigma'(\mathbf{z}^{(l)})$
- Weight & Bias Gradients: $\frac{\partial L}{\partial \mathbf{W}^{(l)}} = \mathbf{\delta}^{(l)} (\mathbf{a}^{(l-1)})^T, \frac{\partial L}{\partial \mathbf{b}^{(l)}} = \mathbf{\delta}^{(l)}$

## Why This Matters for AI
This day provides the rigorous mathematical calculus blueprint for neural network training. Every deep learning framework implements these exact vector derivative recurrences.

## Study Order
1. Read theory.md
2. Study examples.md
3. Run code.py
4. Complete practice.md
5. Verify with solution.md

## Practical Work
Derive and code a 2-layer Neural Network forward and backward pass manually in Python.

## Interview Preparation
Derive the layer error delta recurrence formula $\mathbf{\delta}^{(l)} = (\mathbf{W}^{(l+1)T} \mathbf{\delta}^{(l+1)}) \odot \sigma'(\mathbf{z}^{(l)})$.

## Completion Checklist
- [ ] I can state forward pass matrix equations
- [ ] I can define layer error delta vector $\mathbf{\delta}^{(l)}$
- [ ] I know backward error recurrence formula
- [ ] I can code 2-layer neural network calculus in Python

## Estimated Difficulty
Advanced
