# Day 32 — Chain Rule

## Learning Objectives
- Master single-variable Chain Rule $\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$
- Master multi-variable Chain Rule for composite functions $z = f(u(t), v(t))$
- Understand computational tree diagrams for derivative propagation
- Connect Chain Rule directly to Backpropagation in Deep Learning

## Prerequisites
Day 30 — Derivative Rules, Day 31 — Partial Derivatives

## Topics Covered
- Single-Variable Chain Rule definition
- Multi-Variable Chain Rule: $\frac{dz}{dt} = \frac{\partial z}{\partial u}\frac{du}{dt} + \frac{\partial z}{\partial v}\frac{dv}{dt}$
- Chain Rule for composite activations: $\frac{d}{dx}[\sigma(w x + b)]$
- Computational graphs and intermediate variables
- Backpropagation gradient chain multiplication

## Why This Matters for AI
The Chain Rule is THE single most important mathematical rule in deep learning! Backpropagation is nothing more than repeated applications of the Chain Rule across computational graphs.

## Study Order
1. Read theory.md
2. Study examples.md
3. Run code.py
4. Complete practice.md
5. Verify with solution.md

## Practical Work
Apply Chain Rule step-by-step to compute composite neural layer derivatives manually and in Python.

## Interview Preparation
Explain single and multi-variable Chain Rule and why it enables backpropagation in neural networks.

## Completion Checklist
- [ ] I can state the Chain Rule formula
- [ ] I can differentiate composite functions $f(g(x))$
- [ ] I know multi-variable Chain Rule formula
- [ ] I understand Chain Rule role in Backpropagation

## Estimated Difficulty
Intermediate
