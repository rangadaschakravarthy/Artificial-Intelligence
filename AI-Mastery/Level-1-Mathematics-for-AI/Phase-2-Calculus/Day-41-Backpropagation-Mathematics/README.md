# Day 41 — Backpropagation Mathematics

## Learning Objectives
- Master the complete mathematical proof and formal derivation of the Backpropagation Algorithm
- Formulate the 4 Fundamental Equations of Backpropagation for $L$-layer neural networks
- Perform step-by-step hand calculations of forward and backward passes for a 2-layer network
- Analyze computational efficiency: $O(N)$ reverse pass vs $O(N^2)$ forward-mode passes

## Prerequisites
Day 32 — Chain Rule, Day 40 — Calculus for Neural Networks

## Topics Covered
- Formal Backpropagation Theorem for $L$-layer feedforward networks
- Equation 1: Output Layer Error Delta $\mathbf{\delta}^{(L)} = \nabla_{\mathbf{a}} L \odot \sigma'(\mathbf{z}^{(L)})$
- Equation 2: Hidden Layer Error Recurrence $\mathbf{\delta}^{(l)} = ((\mathbf{W}^{(l+1)})^T \mathbf{\delta}^{(l+1)}) \odot \sigma'(\mathbf{z}^{(l)})$
- Equation 3: Bias Gradient $\frac{\partial L}{\partial \mathbf{b}^{(l)}} = \mathbf{\delta}^{(l)}$
- Equation 4: Weight Matrix Gradient $\frac{\partial L}{\partial \mathbf{W}^{(l)}} = \mathbf{\delta}^{(l)} (\mathbf{a}^{(l-1)})^T$
- Step-by-step hand calculation proof

## Why This Matters for AI
Backpropagation is the core algorithm that enabled the deep learning revolution. Understanding its exact mathematical derivation is a cornerstone requirement for AI researchers and engineers.

## Study Order
1. Read theory.md
2. Study examples.md
3. Run code.py
4. Complete practice.md
5. Verify with solution.md

## Practical Work
Hand-solve a 2-layer network backpropagation pass and verify numbers against Python code.

## Interview Preparation
Write down the 4 fundamental equations of Backpropagation and prove Equation 2 on the whiteboard.

## Completion Checklist
- [ ] I can state all 4 fundamental equations of Backpropagation
- [ ] I can prove hidden layer delta recurrence $\mathbf{\delta}^{(l)}$
- [ ] I can perform a hand calculation of backprop
- [ ] I can code backprop from scratch in Python

## Estimated Difficulty
Advanced
