# Solutions — Random Variables

## Level 1
1. Measurable function mapping sample space outcomes $\Omega$ to real numbers $\mathbb{R}$.
2. Uppercase $X$ is the function/random variable; lowercase $x$ is a specific numerical realized value.
3. Discrete.
4. Continuous.
5. $S_X = \{1, 2, 3, 4, 5, 6\}$.

## Level 2
6. $\Omega = \{HH, HT, TH, TT\}$. $X=1$ for $\{HT, TH\}$. $P(X=1) = rac{2}{4} = 0.50$.
7. Favorable pairs for sum 4: $(1,3), (2,2), (3,1) \implies 3$ pairs. $P(X=4) = rac{3}{36} = rac{1}{12} pprox 0.0833$.
8. Favorable pairs for sum $\ge 10$: $(4,6), (5,5), (5,6), (6,4), (6,5), (6,6) \implies 6$ pairs. $P(X \ge 10) = rac{6}{36} = rac{1}{6} pprox 0.1667$.
9. $Y(1) = 3, Y(2) = 5, Y(3) = 7 \implies S_Y = \{3, 5, 7\}$.
10. Evens are $\{2, 4\} \implies P = rac{2}{5} = 0.40$.

## Level 3
11. $E[I_A] = 1 \cdot P(I_A = 1) + 0 \cdot P(I_A = 0) = 1 \cdot P(A) + 0 \cdot P(A^c) = P(A)$.
12. $S_X = \{1, 2, 3, 4, \dots\}$. Countably infinite.
13. Total probability sum $= 1 \implies k(1 + 2 + 3 + 4) = 10 k = 1 \implies k = 0.10$.
14. $P(X > 2) = P(X=3) + P(X=4) = 0.10(3) + 0.10(4) = 0.30 + 0.40 = 0.70$.
15. Probability is area under density curve. For an exact point, width is zero $\int_x^x f(t)dt = 0$.

## Level 4
16. Discrete RV with support $S_N = \{0, 1, 2, 3, \dots\}$.
17. Fixed parameters: weights $w$, bias $b$. Random variables: input $X$, noise $\epsilon$, target $Y$.
18. Discrete RV $Y \in \{1, 2, 3, 4, 5\}$.
19. $\mathbf{Y} \in \{[1,0,0]^T, [0,1,0]^T, [0,0,1]^T\}$.
20. Due to environment transition dynamics uncertainty and policy action sampling.

## Level 5
21. A random variable is a single function mapping outcomes to numbers. A stochastic process is an indexed collection of random variables $\{X_t\}_{t \in T}$ over time or space.
22. Measurability ensures that preimage sets $\{\omega \mid X(\omega) \le x\}$ belong to event $\sigma$-algebra $\mathcal{F}$ so probabilities can be assigned consistently.
23. Generative models draw random normal vectors $\mathbf{z} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$ and pass them through a neural network transformation $g_	heta(\mathbf{z})$ to generate synthetic images/data.
