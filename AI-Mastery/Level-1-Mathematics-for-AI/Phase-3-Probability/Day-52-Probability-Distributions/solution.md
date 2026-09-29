# Solutions — Probability Distributions

## Level 1
1. Mean $E[X] = p$, Variance $	ext{Var}(X) = p(1-p)$.
2. Binomial distribution $	ext{Bin}(n, p)$.
3. Mean $E[X] = \lambda$, Variance $	ext{Var}(X) = \lambda$.
4. Mean $\mu$ and Variance $\sigma^2$ (or Standard Deviation $\sigma$).
5. Uniform distribution $	ext{Uniform}(a, b)$.

## Level 2
6. $E[X] = n p = 10(0.3) = 3.0$. $	ext{Var}(X) = n p (1-p) = 10(0.3)(0.7) = 2.1$.
7. $P(X=3) = inom{5}{3} (0.5)^3 (0.5)^2 = 10 	imes (0.5)^5 = \frac{10}{32} = 0.3125$.
8. $P(X=1) = \frac{4^1 e^{-4}}{1!} = 4 e^{-4} pprox 4(0.0183156) = 0.0733$.
9. $P(2 \le X \le 7) = \frac{7 - 2}{10 - 0} = \frac{5}{10} = 0.50$.
10. $\sigma = \sqrt{25} = 5.0$. $z = \frac{x - \mu}{\sigma} = \frac{110 - 100}{5} = +2.0$.

## Level 3
11. $\lim_{n \to \infty} inom{n}{x} \left(\frac{\lambda}{n}
ight)^x \left(1 - \frac{\lambda}{n}
ight)^{n-x} = \frac{\lambda^x}{x!} \lim_{n \to \infty} \frac{n!}{(n-x)! n^x} \left(1 - \frac{\lambda}{n}
ight)^n \left(1 - \frac{\lambda}{n}
ight)^{-x} = \frac{\lambda^x e^{-\lambda}}{x!}$.
12. $E[X] = \sum_{x=0}^{\infty} x \frac{\lambda^x e^{-\lambda}}{x!} = \lambda e^{-\lambda} \sum_{x=1}^{\infty} \frac{\lambda^{x-1}}{(x-1)!} = \lambda e^{-\lambda} e^{\lambda} = \lambda$.
13. Sum of $n$ independent Bernoulli trials $	ext{Bern}(p)$ counts total successes, which matches the definition of $	ext{Bin}(n, p)$.
14. $E[X^4] = \int_{-\infty}^{\infty} x^4 \frac{1}{\sqrt{2\pi}} e^{-x^2/2} dx$. Integrating by parts gives $3 E[X^2] = 3(1) = 3$.
15. $Z \sim \mathcal{N}(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$.

## Level 4
16. Variance $\sigma^2 = \frac{2}{512} = \frac{1}{256} \implies \sigma = \sqrt{\frac{1}{256}} = \frac{1}{16} = 0.0625$.
17. For Poisson$(\lambda=200)$, $	ext{Var}(X) = 200 \implies \sigma = \sqrt{200} pprox 14.14$ words.
18. Log-Likelihood $= \log P(Y=y|X) = \log p_y$.
19. Mean vector $oldsymbol{\mu}_t = \sqrt{1-eta_t} x_{t-1}$.
20. Maximizing log-likelihood under $\mathcal{N}(y; f(x), \sigma^2)$ maximizes $-\frac{1}{2\sigma^2} \sum (y_i - f(x_i))^2$, which is mathematically identical to minimizing MSE $\sum (y_i - f(x_i))^2$.

## Level 5
21. Let $X = \sum_{i=1}^n I_i$ where $I_i \sim 	ext{Bern}(p)$. $E[X] = \sum E[I_i] = n p$. Since trials are independent, $	ext{Var}(X) = \sum 	ext{Var}(I_i) = n p(1-p)$.
22. Solving calculus of variations problem $\max_{f} -\int f(x)\ln f(x)dx$ subject to $\int f=1, \int x f = \mu, \int (x-\mu)^2 f = \sigma^2$ yields unique optimal density $f(x) = \mathcal{N}(\mu, \sigma^2)$.
23. `samples = np.random.normal(0, 1, size=10000); print(np.mean(samples), np.var(samples))`.
