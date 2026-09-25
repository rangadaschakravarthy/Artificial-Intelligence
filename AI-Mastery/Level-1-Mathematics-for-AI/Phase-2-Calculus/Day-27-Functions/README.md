# Day 27 — Functions

## Learning Objectives
- Master mathematical function definitions, domain, range, and mappings
- Distinguish between Linear Functions and Non-linear Functions
- Understand Composite Functions $f(g(x))$ used in deep neural networks
- Identify key AI functions: Polynomial, Exponential, Logarithmic, Sigmoid, ReLU, Softmax

## Prerequisites
Day 26 — Introduction to Calculus

## Topics Covered
- Function definition $f: X \rightarrow Y$
- Domain (valid inputs) and Range (possible outputs)
- Linear vs Non-linear Functions
- Composite Functions $(f \circ g)(x) = f(g(x))$
- Common AI Functions: Exponential $e^x$, Logarithm $\ln(x)$, Sigmoid $\sigma(x)$, ReLU

## Why This Matters for AI
Neural networks are universal function approximators. A deep network is a huge composite function $f(x) = f_L(f_{L-1}(\dots f_1(x)))$ mapping raw inputs to predictions.

## Study Order
1. Read theory.md
2. Study examples.md
3. Run code.py
4. Complete practice.md
5. Verify with solution.md

## Practical Work
Plot linear, exponential, logarithmic, Sigmoid, and ReLU functions using NumPy and Matplotlib.

## Interview Preparation
Explain why non-linear activation functions are necessary in deep neural networks.

## Completion Checklist
- [ ] I can define domain and range of a function
- [ ] I know the difference between linear and non-linear functions
- [ ] I can compute composite functions $f(g(x))$
- [ ] I can plot Sigmoid and ReLU in Python

## Estimated Difficulty
Beginner
