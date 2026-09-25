# Solutions — Expectation and Variance

## Level 1
1. $	ext{Var}(X) = E[X^2] - (E[X])^2$.
2. $E[c] = c$, $	ext{Var}(c) = 0$.
3. $E[X + Y] = E[X] + E[Y]$.
4. False. Requires $X$ and $Y$ to be uncorrelated (e.g. independent). If correlated, $	ext{Var}(X+Y) = 	ext{Var}(X) + 	ext{Var}(Y) + 2 	ext{Cov}(X, Y)$.
5. $\sigma = \sqrt{	ext{Var}(X)}$.

## Level 2
6. $E[X] = 0(0.3) + 1(0.5) + 2(0.2) = 0.5 + 0.4 = 0.90$.
7. $E[X^2] = 0^2(0.3) + 1^2(0.5) + 2^2(0.2) = 0.5 + 0.8 = 1.30$. $	ext{Var}(X) = 1.30 - (0.90)^2 = 1.30 - 0.81 = 0.49$.
8. $E[3X + 5] = 3(10) + 5 = 35$. $	ext{Var}(3X + 5) = 3^2 	ext{Var}(X) = 9(4) = 36$.
9. For independent $X, Y$: $	ext{Var}(2X - 3Y) = 2^2 	ext{Var}(X) + (-3)^2 	ext{Var}(Y) = 4(3) + 9(4) = 12 + 36 = 48$.
10. $	ext{Var}(X) = E[X^2] - (E[X])^2 = 25 - 4^2 = 25 - 16 = 9$.

## Level 3
11. $	ext{Var}(X) = E[(X - \mu)^2] = E[X^2 - 2\mu X + \mu^2] = E[X^2] - 2\mu E[X] + \mu^2 = E[X^2] - 2\mu^2 + \mu^2 = E[X^2] - \mu^2 = E[X^2] - (E[X])^2$.
12. $	ext{Var}(aX + b) = E[((aX + b) - E[aX + b])^2] = E[(aX + b - a\mu - b)^2] = E[(a(X - \mu))^2] = a^2 E[(X - \mu)^2] = a^2 	ext{Var}(X)$.
13. $E[ar{X}] = E\left[rac{1}{n}\sum X_iight] = rac{1}{n} \sum E[X_i] = rac{n \mu}{n} = \mu$. $	ext{Var}(ar{X}) = 	ext{Var}\left(rac{1}{n}\sum X_iight) = rac{1}{n^2} \sum 	ext{Var}(X_i) = rac{n \sigma^2}{n^2} = rac{\sigma^2}{n}$.
14. Because $	ext{Var}(ar{X}) = rac{\sigma^2}{n}$, as sample size $n 	o \infty$, variance of the sample mean drops to zero, guaranteeing higher precision (Law of Large Numbers).
15. Let $g(c) = E[(X - c)^2] = E[X^2 - 2cX + c^2] = E[X^2] - 2c E[X] + c^2$. Take derivative w.r.t $c$: $g'(c) = -2 E[X] + 2c = 0 \implies c = E[X]$. Second derivative $g''(c) = 2 > 0$ confirms minimum.

## Level 4
16. $Z = rac{X - 50}{10}$. $E[Z] = 0$, $	ext{Var}(Z) = 1$.
17. Normalized $\hat{x}_i$ has $E[\hat{x}_i] = 0, 	ext{Var}(\hat{x}_i) = 1$. Scaled $y_i = \gamma \hat{x}_i + eta$ has $E[y_i] = eta$, $	ext{Var}(y_i) = \gamma^2$.
18. $	ext{Var}(ar{f}(x)) = 	ext{Var}\left(rac{1}{M}\sum f_m(x)ight) = rac{1}{M^2} \sum 	ext{Var}(f_m(x)) = rac{M \sigma^2}{M^2} = rac{\sigma^2}{M}$.
19. Averaging $M$ independent decision trees reduces overall model prediction variance by a factor of $M$, stabilizing predictions without increasing bias.
20. $V(s) = E\left[ \sum_{k=0}^{\infty} \gamma^k R_{t+k+1} \mid S_t = s ight] = \sum_{k=0}^{\infty} \gamma^k E[R_{t+k+1} \mid S_t = s]$.

## Level 5
21. $E[X+Y] = \int\int (x+y) f(x,y) dx dy = \int\int x f(x,y) dx dy + \int\int y f(x,y) dx dy = \int x f_X(x) dx + \int y f_Y(y) dy = E[X] + E[Y]$.
22. Jensen's Inequality: For convex $g(x)$, $g(E[X]) \le E[g(X)]$. Crucial in deriving Variational Lower Bound (ELBO) in VAEs using convex function $-\ln(x)$.
23. `X = np.random.normal(5, 2, 100000); Y = 3*X + 4; print(np.var(Y), 9*np.var(X))` shows exact numerical agreement.
