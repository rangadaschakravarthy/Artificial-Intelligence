# Practice Problems — Continuous Random Variables

## Level 1: Basic Concept Checks
1. State the two validity conditions for a PDF $f(x)$.
2. What is $P(X = 3.5)$ for a continuous random variable $X$?
3. How do you get PDF $f(x)$ from CDF $F(x)$?
4. True or False: PDF $f(x)$ can take values greater than 1.
5. What is the value of $F(-\infty)$?

## Level 2: Direct Calculations
6. Let $f(x) = 3 x^2$ for $x \in [0, 1]$. Compute $P(X \le 0.5)$.
7. For PDF in Q6, compute $P(0.2 \le X \le 0.8)$.
8. Find constant $k$ so $f(x) = k (1 - x)$ for $x \in [0, 1]$ is a valid PDF.
9. Using $k$ from Q8, derive CDF $F(x)$ on $[0, 1]$.
10. Compute median $m$ (value where $F(m) = 0.5$) for uniform distribution on $[10, 20]$.

## Level 3: Conceptual & Multi-Step Problems
11. Compute expectation $E[X] = \int_{-\infty}^{\infty} x f(x) dx$ for $f(x) = 3 x^2$ on $[0, 1]$.
12. Compute variance $	ext{Var}(X) = \int_{-\infty}^{\infty} (x - \mu)^2 f(x) dx$ for Q11.
13. Show that for any continuous RV, $P(a < X < b) = P(a \le X \le b)$.
14. If $X \sim 	ext{Uniform}(a, b)$, write its PDF $f(x)$ and CDF $F(x)$.
15. If $Y = e^X$ where $X \sim 	ext{Uniform}(0, 1)$, derive the PDF of $Y$.

## Level 4: AI & ML Applications
16. Neural network weights are initialized with $W \sim \mathcal{N}(0, 0.01)$. Find standard deviation $\sigma$.
17. In Q16, calculate $P(-0.02 \le W \le 0.02)$ using standard normal $\Phi(z)$.
18. Gaussian noise $\epsilon \sim \mathcal{N}(0, \sigma^2)$ is added to image pixels. Explain how noise variance $\sigma^2$ affects image quality.
19. In VAE loss, KL divergence measures distance between latent PDF $q(z)$ and prior $p(z) = \mathcal{N}(0, I)$. Why are continuous integrals used?
20. In continuous Reinforcement Learning (robotics), actions are vectors $\mathbf{a} \sim \mathcal{N}(oldsymbol{\mu}(s), oldsymbol{\Sigma})$. How is policy evaluated?

## Level 5: Interview Questions
21. What is the difference between PDF $f(x)$ and PMF $p(x)$?
22. Derive the expectation $E[X]$ and variance $	ext{Var}(X)$ of $X \sim 	ext{Uniform}(a, b)$.
23. Explain how the Probability Integral Transform ($U = F_X(X) \sim 	ext{Uniform}(0, 1)$) allows sampling from arbitrary continuous distributions.
