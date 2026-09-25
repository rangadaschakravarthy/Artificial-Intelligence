# Day 38 — Learning Rate

## Learning Objectives
- Master the Learning Rate hyperparameter $\alpha$ (or $\eta$) in optimization
- Analyze failure modes: Under-shooting (learning rate too small) vs Over-shooting / Divergence (learning rate too large)
- Understand Learning Rate Schedules (Step Decay, Exponential Decay, Cosine Annealing, Warmup)
- Connect learning rate selection to loss surface curvature and condition number

## Prerequisites
Day 37 — Gradient Descent

## Topics Covered
- Learning Rate definition $\eta$
- Small Learning Rate: Slow convergence, getting stuck in local minima
- Large Learning Rate: Overshooting minimum, loss divergence to $\infty$
- Optimal Learning Rate $\eta^* \approx 1 / \lambda_{max}(\mathbf{H})$
- Learning Rate Schedules: Step Decay, Cosine Annealing, Warmup
- Adaptive Learning Rate algorithms overview (AdaGrad, RMSprop, Adam)

## Why This Matters for AI
Learning rate is universally acknowledged as the single most critical hyperparameter in deep learning. Setting it correctly determines whether a model converges to state-of-the-art performance or diverges completely.

## Study Order
1. Read theory.md
2. Study examples.md
3. Run code.py
4. Complete practice.md
5. Verify with solution.md

## Practical Work
Simulate under-shooting, over-shooting, and Cosine Annealing learning rate schedules in Python.

## Interview Preparation
Explain what happens when learning rate is too large vs too small, and why Learning Rate Warmup is used in Transformers.

## Completion Checklist
- [ ] I understand learning rate impact on optimization
- [ ] I know symptoms of too large vs too small learning rate
- [ ] I can explain Cosine Annealing and Learning Rate Warmup
- [ ] I can implement learning rate decay in Python

## Estimated Difficulty
Intermediate
