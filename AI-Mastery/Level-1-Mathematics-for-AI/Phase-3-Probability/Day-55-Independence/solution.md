# Solutions — Independence

## Level 1
1. $f_{X,Y}(x,y) = f_X(x) f_Y(y)$ for all $x,y$.
2. $P(X|Y) = P(X)$.
3. $	ext{Cov}(X, Y) = 0$.
4. Independent and Identically Distributed.
5. False (only true if Jointly Gaussian).

## Level 2
6. $E[XY] = E[X] E[Y] = 2 	imes 7 = 14$.
7. $	ext{Var}(X - Y) = 1^2 	ext{Var}(X) + (-1)^2 	ext{Var}(Y) = 5 + 8 = 13$.
8. $P(X=1, Y=1) = P(X=1) P(Y=1) = 0.4 	imes 0.5 = 0.20$.
9. No. $f(x, y) = c(x+y)$ cannot be factorized into $g(x) h(y)$ due to the addition $+$.
10. $E[X + 2Y - Z] = E[X] + 2 E[Y] - E[Z] = 3 + 2(3) - 3 = 6$.

## Level 3
11. $E[XY] = \int\int x y f(x,y) dx dy = \int\int x y f_X(x) f_Y(y) dx dy = \left( \int x f_X(x) dx ight) \left( \int y f_Y(y) dy ight) = E[X] E[Y]$.
12. $	ext{Var}(X+Y) = 	ext{Var}(X) + 	ext{Var}(Y) + 2 	ext{Cov}(X,Y)$. Since $X \perp \!\!\! \perp Y \implies 	ext{Cov}(X,Y) = 0$, $	ext{Var}(X+Y) = 	ext{Var}(X) + 	ext{Var}(Y)$.
13. Since $f_{X,Y}(x,y) = f_X(x) f_Y(y)$, for any measurable functions $g, h$, $E[g(X) h(Y)] = \int\int g(x) h(y) f_X(x) f_Y(y) dx dy = E[g(X)] E[h(Y)]$, confirming independence.
14. $P(I_A=1, I_B=1) = P(A \cap B)$. If $A \perp B$, $P(A \cap B) = P(A)P(B) = P(I_A=1)P(I_B=1)$.
15. Multivariate Gaussian PDF contains exponent term $-rac{1}{2} (\mathbf{x}-oldsymbol{\mu})^T oldsymbol{\Sigma}^{-1} (\mathbf{x}-oldsymbol{\mu})$. When $	ext{Cov}(X,Y)=0$, $oldsymbol{\Sigma}$ is diagonal, so $oldsymbol{\Sigma}^{-1}$ is diagonal, splitting the exponent into $e^{-Q_1(x)} e^{-Q_2(y)} = f_X(x) f_Y(y)$.

## Level 4
16. $P(X_1, X_2 | Y) = P(X_1 | Y) P(X_2 | Y)$.
17. Time series data points are temporally autocorrelated ($X_t$ depends on $X_{t-1}$), violating sample independence.
18. Shuffling randomizes mini-batch samples, breaking sequential correlations and ensuring mini-batches represent independent samples from the underlying data distribution.
19. $\ln L = -rac{N}{2} \ln(2\pi \sigma^2) - rac{1}{2\sigma^2} \sum_{i=1}^N (x_i - \mu)^2$.
20. Sampling random mini-batches from a replay buffer decorrelates sequential RL transition tuples $(s_t, a_t, r_t, s_{t+1})$, stabilizing neural network gradient updates.

## Level 5
21. $	ext{Cov}(X,Y) = E[XY] - E[X]E[Y]$. If independent, $E[XY] = E[X]E[Y] \implies 	ext{Cov}(X,Y) = E[X]E[Y] - E[X]E[Y] = 0$.
22. Non-Gaussian distributions can have non-linear dependencies (e.g. $Y=X^2$) that yield $	ext{Cov}(X,Y)=0$ despite strong dependence. For Jointly Gaussian variables, all higher-order dependencies are fully defined by the linear covariance matrix $oldsymbol{\Sigma}$, so $	ext{Cov}(X,Y)=0$ completely eliminates all dependence.
23. `from scipy.stats import chi2_contingency; res = chi2_contingency(pd.crosstab(df['cat1'], df['cat2'])); p_val = res.pvalue`.
