# Practice Problems — Discrete Random Variables

## Level 1: Basic Concept Checks
1. State the two requirements for a valid PMF $p(x)$.
2. What is the value of $F(\infty)$ for any valid CDF?
3. How is CDF $F(x)$ related to PMF $p(x)$?
4. If $X$ can only take value 5, what is $p(5)$?
5. True or False: For a discrete RV, $F(x)$ is continuous everywhere.

## Level 2: Direct Calculations
6. Given PMF $p(x) = c x^2$ for $x \in \{1, 2, 3\}$. Find constant $c$.
7. Using $c$ from Q6, find $P(X \ge 2)$.
8. Given CDF: $F(1)=0.3, F(2)=0.7, F(3)=1.0$. Find PMF $p(2)$.
9. Find $P(X = 3)$ using the CDF from Q8.
10. Find $P(1 < X \le 2)$ using CDF from Q8.

## Level 3: Conceptual & Multi-Step Problems
11. Compute $E[X]$ for $X \in \{0, 1\}$ with $p(1) = p, p(0) = 1-p$ (Bernoulli RV).
12. Compute $	ext{Var}(X) = E[X^2] - (E[X])^2$ for the Bernoulli RV in Q11.
13. If $X$ is uniform on $\{1, 2, \dots, n\}$, write its PMF $p(x)$ and CDF $F(x)$.
14. Show that $P(X > x) = 1 - F(x)$.
15. If PMF is symmetric around $c$, prove $E[X] = c$.

## Level 4: AI & ML Applications
16. A multi-class model outputs class probabilities $p = [0.15, 0.45, 0.25, 0.15]$. Compute cumulative distribution values $F(k)$ for classes $k \in \{1, 2, 3, 4\}$.
17. Compute expected loss if predicted probabilities for class predictions carry losses $[10, 0, 5, 20]$ for classes $1, 2, 3, 4$ using Q16 probabilities.
18. In reinforcement learning, an agent chooses discrete actions $a \in \{1, 2, 3\}$ according to policy PMF $\pi(a) = [0.5, 0.3, 0.2]$. Compute expected reward if rewards are $[+10, -5, +2]$.
19. Cross-entropy loss formula is $H(p, q) = -\sum p(x) \log q(x)$. Compute $H$ when true $p=[1, 0]$ and predicted $q=[0.8, 0.2]$.
20. Explain why discrete target distributions require classification loss functions (Cross-Entropy) rather than regression loss functions (MSE).

## Level 5: Interview Questions
21. Prove that for discrete $X \ge 0$ taking integer values, $E[X] = \sum_{k=0}^{\infty} P(X > k)$.
22. What is the difference between a PMF and a Probability Density Function (PDF)?
23. How does sampling from a discrete PMF using inverse transform sampling work with the CDF $F(x)$?
