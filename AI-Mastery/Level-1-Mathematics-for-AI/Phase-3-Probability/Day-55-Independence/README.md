# Day 55 — Independence

## Learning Objectives
- Formalize independence of random variables $P(X, Y) = P(X) P(Y)$.
- Understand equivalent definitions ($P(Y|X) = P(Y)$, $	ext{Cov}(X,Y) = 0$).
- Master properties of independent random variables ($E[XY] = E[X]E[Y]$, $	ext{Var}(X+Y) = 	ext{Var}(X)+	ext{Var}(Y)$).
- Test feature independence in machine learning datasets.

## Prerequisites
- Days 44–54 Probability rules, conditional probability, covariance.

## Topics Covered
1. Definition of Independent Random Variables
2. Factorization of Joint PMF/PDF $f(x, y) = f_X(x) f_Y(y)$
3. Independence vs Uncorrelatedness
4. Multiplication Rule for Expectations of Independent RVs
5. Independent and Identically Distributed (i.i.d.) Assumption in Machine Learning

## Why This Matters for AI
The i.i.d. assumption (Independent and Identically Distributed data) is the foundational assumption of statistical machine learning theory. Naive Bayes classifiers rely on feature independence given the class.

## Study Order
1. Read `theory.md`.
2. Review 5 examples in `examples.md`.
3. Complete `practice.md`.
4. Validate with `solution.md`.
5. Run `code.py`.

## Checklist
- [ ] Verify $P(X \in A, Y \in B) = P(X \in A) P(Y \in B)$
- [ ] Differentiate independence from zero correlation
- [ ] Apply $E[XY] = E[X]E[Y]$ for independent RVs
- [ ] Code independence test (Chi-Square) in Python

## Estimated Difficulty
- **Difficulty**: 3/10
- **Duration**: 2.0 Hours
