# Day 47 — Conditional Probability

## Learning Objectives
- Define and compute conditional probability $P(A|B)$.
- Understand how new information updates sample spaces and event probabilities.
- Master joint, marginal, and conditional probabilities using contingency tables.
- Compute conditional probabilities in classification confusion matrices.

## Prerequisites
- Days 44–46 Probability foundations and rules.

## Topics Covered
1. Definition of Conditional Probability $P(A|B)$
2. Reduced Sample Space Intuition
3. Formula $P(A|B) = \frac{P(A \cap B)}{P(B)}$
4. Contingency Tables and Confusion Matrices
5. Precision, Recall, and False Positive Rates as Conditional Probabilities

## Why This Matters for AI
Machine learning inference is fundamentally conditional probability: finding $P(	ext{Target} = y \mid 	ext{Features} = X)$. Classifier metrics like Precision ($P(y=1 | \hat{y}=1)$) and Recall ($P(\hat{y}=1 | y=1)$) are direct applications.

## Study Order
1. Read `theory.md`.
2. Study worked examples in `examples.md`.
3. Complete `practice.md`.
4. Validate with `solution.md`.
5. Run `code.py`.

## Checklist
- [ ] Understand conditioning as restricting the sample space to $B$
- [ ] Calculate $P(A|B) = \frac{P(A \cap B)}{P(B)}$
- [ ] Express Precision and Recall as conditional probabilities
- [ ] Build confusion matrix code in Python

## Estimated Difficulty
- **Difficulty**: 3/10
- **Duration**: 2.0 Hours
