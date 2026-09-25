# Practice Problems — Expectation and Variance

## Level 1: Basic Concept Checks
1. State the formula for $	ext{Var}(X)$ in terms of $E[X]$ and $E[X^2]$.
2. If $c$ is a constant, what is $E[c]$ and $	ext{Var}(c)$?
3. State Linearity of Expectation for $E[X + Y]$.
4. True or False: $	ext{Var}(X + Y) = 	ext{Var}(X) + 	ext{Var}(Y)$ holds for ALL random variables.
5. What is the relation between standard deviation $\sigma$ and variance $	ext{Var}(X)$?

## Level 2: Direct Calculations
6. Given $P(X=0)=0.3, P(X=1)=0.5, P(X=2)=0.2$. Compute $E[X]$.
7. For Q6, compute $E[X^2]$ and $	ext{Var}(X)$.
8. If $E[X] = 10$ and $	ext{Var}(X) = 4$, find $E[3X + 5]$ and $	ext{Var}(3X + 5)$.
9. Independent $X, Y$ have $	ext{Var}(X) = 3, 	ext{Var}(Y) = 4$. Compute $	ext{Var}(2X - 3Y)$.
10. If $E[X] = 4$ and $E[X^2] = 25$, find $	ext{Var}(X)$.

## Level 3: Conceptual & Multi-Step Problems
11. Prove that $	ext{Var}(X) = E[X^2] - (E[X])^2$.
12. Prove that $	ext{Var}(aX + b) = a^2 	ext{Var}(X)$.
13. If $X_1, \dots, X_n$ are i.i.d. with mean $\mu$ and variance $\sigma^2$, find the mean and variance of sample mean $ar{X} = rac{1}{n} \sum_{i=1}^n X_i$.
14. Explain why $	ext{Var}(ar{X}) = rac{\sigma^2}{n}$ implies that larger sample sizes reduce estimation variance.
15. Prove that $E[(X - c)^2]$ is minimized when $c = E[X]$.

## Level 4: AI & ML Applications
16. Input feature $X$ has mean $\mu = 50$ and $\sigma = 10$. Express standardized feature $Z = rac{X - 50}{10}$ and state its mean and variance.
17. In Batch Normalization, feature $x_i$ is normalized to $\hat{x}_i = rac{x_i - \mu_B}{\sqrt{\sigma_B^2 + \epsilon}}$, then scaled $y_i = \gamma \hat{x}_i + eta$. State $E[y_i]$ and $	ext{Var}(y_i)$.
18. An ensemble averages predictions of $M$ independent models, each with variance $\sigma^2$. Compute variance of ensemble average $ar{f}(x) = rac{1}{M} \sum_{m=1}^M f_m(x)$.
19. Relate Q18 to variance reduction in Random Forests (Bagging).
20. In reinforcement learning, cumulative return $G_t = \sum_{k=0}^{\infty} \gamma^k R_{t+k+1}$. Use Linearity of Expectation to write expected return $V(s) = E[G_t | S_t = s]$.

## Level 5: Interview Questions
21. Prove Linearity of Expectation $E[X + Y] = E[X] + E[Y]$ for continuous joint random variables.
22. State Jensen's Inequality for a convex function $g(x)$ and write the relationship between $g(E[X])$ and $E[g(X)]$.
23. Write Python code using NumPy to generate 100,000 samples and empirically prove $	ext{Var}(3X + 4) = 9 	ext{Var}(X)$.
