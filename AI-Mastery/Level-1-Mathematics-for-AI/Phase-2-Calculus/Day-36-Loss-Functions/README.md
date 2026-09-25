# Day 36 — Loss Functions

## Learning Objectives
- Master the mathematical formulations of core AI Loss Functions (Cost Functions / Objective Functions)
- Understand Mean Squared Error (MSE) for regression and Cross-Entropy for classification
- Derive gradient formulas $\frac{\partial L}{\partial \hat{y}}$ for MSE, BCE, and Categorical Cross-Entropy
- Compare L1 Loss (MAE), L2 Loss (MSE), and Huber Loss robustness against outliers

## Prerequisites
Day 27 — Functions, Day 29 — Derivatives

## Topics Covered
- Loss Function $L(\mathbf{y}, \hat{\mathbf{y}})$ vs Cost Function $J(\mathbf{w})$
- Mean Squared Error (MSE / L2 Loss): $\text{MSE} = \frac{1}{N} \sum (y_i - \hat{y}_i)^2$
- Mean Absolute Error (MAE / L1 Loss): $\text{MAE} = \frac{1}{N} \sum |y_i - \hat{y}_i|$
- Binary Cross-Entropy (BCE / Log Loss): $L_{BCE} = -[y \ln(\hat{y}) + (1-y) \ln(1-\hat{y})]$
- Categorical Cross-Entropy (CCE): $L_{CCE} = -\sum_{c=1}^C y_c \ln(\hat{y}_c)$
- Huber Loss (Smooth L1 Loss)

## Why This Matters for AI
The loss function quantifies how 'wrong' the AI model's predictions are. Calculus takes the derivative of this loss function with respect to weights to guide model learning.

## Study Order
1. Read theory.md
2. Study examples.md
3. Run code.py
4. Complete practice.md
5. Verify with solution.md

## Practical Work
Implement MSE, BCE, CCE, and Huber loss functions and their derivatives in Python.

## Interview Preparation
Explain why MSE is used for regression while Cross-Entropy is used for classification.

## Completion Checklist
- [ ] I can state formulas for MSE, MAE, BCE, and CCE
- [ ] I can derive gradients of MSE and BCE loss functions
- [ ] I know when to use Huber Loss instead of MSE
- [ ] I can code loss functions in Python

## Estimated Difficulty
Intermediate
