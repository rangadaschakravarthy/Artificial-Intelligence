# Solutions — Covariance and Correlation

## Level 1
1. $	ext{Cov}(X, Y) = E[XY] - E[X]E[Y]$.
2. Range is $[-1, 1]$.
3. $	ext{Cov}(X, X) = E[X^2] - (E[X])^2 = 	ext{Var}(X)$.
4. $	ext{Cov}(X, Y) = 0$.
5. Correlation is scale-invariant (unitless), whereas covariance depends on feature measurement units.

## Level 2
6. $	ext{Cov}(X, Y) = 11 - (4 	imes 2) = 11 - 8 = 3$.
7. $\sigma_X = 3, \sigma_Y = 4$. $
ho = \frac{-6}{3 	imes 4} = \frac{-6}{12} = -0.50$.
8. Since $Y$ is a strict negative linear function of $X$, $
ho_{X,Y} = -1.0$.
9. $	ext{Cov}(X, 5X + 2) = 5 	ext{Cov}(X, X) = 5 	ext{Var}(X) = 5(4) = 20$.
10. $\mathbf{R} = egin{bmatrix} 1.0 & 0.8 \ 0.8 & 1.0 \end{bmatrix}$.

## Level 3
11. $	ext{Cov}(aX + b, cY + d) = E[(aX + b - a\mu_X - b)(cY + d - c\mu_Y - d)] = E[a(X-\mu_X) c(Y-\mu_Y)] = a c E[(X-\mu_X)(Y-\mu_Y)] = a c 	ext{Cov}(X, Y)$.
12. Define random variable $Z = t(X - \mu_X) + (Y - \mu_Y)$. Since $E[Z^2] \ge 0$ for all real $t$: $t^2 \sigma_X^2 + 2 t 	ext{Cov}(X, Y) + \sigma_Y^2 \ge 0$. Discriminant must be $\le 0$: $4 	ext{Cov}(X, Y)^2 - 4 \sigma_X^2 \sigma_Y^2 \le 0 \implies |	ext{Cov}(X, Y)| \le \sigma_X \sigma_Y$. Dividing by $\sigma_X \sigma_Y$ yields $|
ho| \le 1$.
13. $	ext{Var}(X + Y) = 	ext{Var}(X) + 	ext{Var}(Y) + 2 	ext{Cov}(X, Y)$. If $	ext{Var}(X + Y) = 	ext{Var}(X) + 	ext{Var}(Y)$, then $2 	ext{Cov}(X, Y) = 0 \implies 	ext{Cov}(X, Y) = 0$.
14. $	ext{Cov}(X + Y, Z) = E[(X + Y - \mu_X - \mu_Y)(Z - \mu_Z)] = E[(X-\mu_X)(Z-\mu_Z)] + E[(Y-\mu_Y)(Z-\mu_Z)] = 	ext{Cov}(X, Z) + 	ext{Cov}(Y, Z)$.
15. Diagonal entry $\Sigma_{ii} = 	ext{Cov}(X_i, X_i) = 	ext{Var}(X_i)$. Since variance is non-negative ($E[(X_i-\mu_i)^2] \ge 0$), all diagonal entries must be $\ge 0$.

## Level 4
16. High correlation $
ho pprox 1$ makes columns of data matrix $X$ linearly dependent, causing matrix $X^T X$ to be near-singular ($\det(X^T X) pprox 0$), leading to exploding inverse values $(X^T X)^{-1}$ and unstable regression weights.
17. Total Variance $= 	ext{Tr}(oldsymbol{\Sigma}) = 4 + 9 = 13$.
18. $oldsymbol{\Sigma}^{-1} = egin{bmatrix} 1 & 0 \ 0 & 0.25 \end{bmatrix}$. $\mathbf{x} - oldsymbol{\mu} = [2, 0]^T$. $d_M^2 = [2, 0] egin{bmatrix} 1 & 0 \ 0 & 0.25 \end{bmatrix} egin{bmatrix} 2 \ 0 \end{bmatrix} = [2, 0] egin{bmatrix} 2 \ 0 \end{bmatrix} = 4$. $d_M = \sqrt{4} = 2.0$.
19. High target correlation ensures high predictive signal; low feature-feature correlation ensures selected features carry unique, non-redundant information.
20. Spherical: $oldsymbol{\Sigma} = \sigma^2 \mathbf{I}$ (isotropic circular components); Diagonal: $oldsymbol{\Sigma} = 	ext{diag}(\sigma_1^2, \dots)$ (axis-aligned elliptical components); Full: dense matrix $oldsymbol{\Sigma}$ (arbitrarily oriented elliptical components).

## Level 5
21. $	ext{Cov}(X, aX+b) = a 	ext{Var}(X)$. $\sigma_Y = \sqrt{a^2 	ext{Var}(X)} = a \sigma_X$ for $a > 0$. $
ho = \frac{a 	ext{Var}(X)}{\sigma_X (a \sigma_X)} = \frac{a \sigma_X^2}{a \sigma_X^2} = 1.0$.
22. Let $X \sim 	ext{Uniform}(-1, 1)$ and $Y = X^2$. As shown in Example 3, $E[X] = 0, E[XY] = E[X^3] = 0 \implies 	ext{Cov}(X, Y) = 0 \implies 
ho = 0$. However, $Y$ is completely determined by $X$, so they are dependent.
23. `X = np.random.randn(1000, 3); cov_matrix = np.cov(X, rowvar=False)`.
