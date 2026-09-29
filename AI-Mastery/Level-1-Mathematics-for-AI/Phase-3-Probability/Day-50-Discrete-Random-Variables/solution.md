# Solutions — Discrete Random Variables

## Level 1
1. 1) $p(x) \ge 0$ for all $x$, 2) $\sum_{x} p(x) = 1$.
2. $F(\infty) = 1.0$.
3. $F(x) = P(X \le x) = \sum_{k \le x} p(k)$.
4. $p(5) = 1.0$.
5. False. CDF of a discrete RV is a step function with jump discontinuities at support points.

## Level 2
6. $\sum p(x) = c(1^2 + 2^2 + 3^2) = c(1 + 4 + 9) = 14 c = 1 \implies c = \frac{1}{14}$.
7. $P(X \ge 2) = p(2) + p(3) = \frac{4}{14} + \frac{9}{14} = \frac{13}{14} pprox 0.9286$.
8. $p(2) = F(2) - F(1) = 0.7 - 0.3 = 0.40$.
9. $p(3) = F(3) - F(2) = 1.0 - 0.7 = 0.30$.
10. $P(1 < X \le 2) = F(2) - F(1) = 0.7 - 0.3 = 0.40$.

## Level 3
11. $E[X] = 0(1-p) + 1(p) = p$.
12. $E[X^2] = 0^2(1-p) + 1^2(p) = p$. $	ext{Var}(X) = E[X^2] - (E[X])^2 = p - p^2 = p(1-p)$.
13. PMF: $p(x) = \frac{1}{n}$ for $x \in \{1, \dots, n\}$. CDF: $F(x) = \frac{\lfloor x 
floor}{n}$ for $1 \le x \le n$.
14. $P(X > x) = 1 - P(X \le x) = 1 - F(x)$.
15. Let $Y = X - c$. Symmetry implies $p(c + y) = p(c - y)$. Thus $E[Y] = \sum y p(c+y) = 0 \implies E[X - c] = 0 \implies E[X] = c$.

## Level 4
16. $F(1)=0.15, F(2)=0.60, F(3)=0.85, F(4)=1.00$.
17. Expected Loss $= 10(0.15) + 0(0.45) + 5(0.25) + 20(0.15) = 1.5 + 0 + 1.25 + 3.0 = 5.75$.
18. Expected Reward $= 10(0.5) + (-5)(0.3) + 2(0.2) = 5.0 - 1.5 + 0.4 = 3.90$.
19. $H(p, q) = -[1 \cdot \ln(0.8) + 0 \cdot \ln(0.2)] = -\ln(0.8) pprox 0.2231$.
20. MSE assumes continuous metric distance errors. Discrete class categories (e.g. Cat=0, Dog=1, Car=2) have no metric distance (Car is not "twice" Dog). Cross-entropy penalizes probability divergence directly.

## Level 5
21. $\sum_{k=0}^{\infty} P(X > k) = \sum_{k=0}^{\infty} \sum_{j=k+1}^{\infty} p(j)$. Swapping summation order yields $\sum_{j=1}^{\infty} p(j) \sum_{k=0}^{j-1} 1 = \sum_{j=1}^{\infty} j \cdot p(j) = E[X]$.
22. PMF $p(x) = P(X=x) \le 1$ gives exact probabilities for discrete points. PDF $f(x)$ gives probability density for continuous variables where $P(X=x)=0$ and $f(x)$ can exceed 1.
23. Draw uniform random number $U \sim 	ext{Uniform}(0, 1)$. Find outcome $x_k$ such that $F(x_{k-1}) < U \le F(x_k)$. Outcome $x_k$ is the sampled value.
