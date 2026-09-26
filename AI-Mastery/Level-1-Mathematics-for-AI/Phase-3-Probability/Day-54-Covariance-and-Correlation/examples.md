# Worked Examples — Covariance and Correlation

## Example 1: Covariance Formula $E[XY] - E[X]E[Y]$
**Problem**: $E[X] = 3, E[Y] = 5, E[XY] = 18$. Calculate $	ext{Cov}(X, Y)$.
**Solution**:
1. $	ext{Cov}(X, Y) = E[XY] - E[X]E[Y] = 18 - (3 	imes 5) = 18 - 15 = 3$.

## Example 2: Pearson Correlation Calculation
**Problem**: From Example 1, if $	ext{Var}(X) = 4$ and $	ext{Var}(Y) = 9$, compute $
ho_{X,Y}$.
**Solution**:
1. $\sigma_X = \sqrt{4} = 2$.
2. $\sigma_Y = \sqrt{9} = 3$.
3. $
ho_{X,Y} = rac{	ext{Cov}(X, Y)}{\sigma_X \sigma_Y} = rac{3}{2 	imes 3} = rac{3}{6} = 0.50$.

## Example 3: Zero Correlation with Non-Linear Dependence
**Problem**: Let $X \in \{-1, 0, 1\}$ with equal probabilities $1/3$, and let $Y = X^2$. Calculate $	ext{Cov}(X, Y)$.
**Solution**:
1. $E[X] = rac{-1 + 0 + 1}{3} = 0$.
2. $Y \in \{1, 0, 1\} \implies E[Y] = rac{1 + 0 + 1}{3} = rac{2}{3}$.
3. $XY = X \cdot X^2 = X^3 \in \{-1, 0, 1\} \implies E[XY] = rac{-1 + 0 + 1}{3} = 0$.
4. $	ext{Cov}(X, Y) = E[XY] - E[X]E[Y] = 0 - 0 \left(rac{2}{3}
ight) = 0$.
5. $	ext{Cov}(X, Y) = 0$ even though $Y$ is completely determined by $X$ ($Y = X^2$).

## Example 4: Linear Scaling Effect on Covariance vs Correlation
**Problem**: Let $U = 2X$ and $V = 3Y$. How do $	ext{Cov}(U, V)$ and $
ho_{U,V}$ compare to $	ext{Cov}(X, Y)$ and $
ho_{X,Y}$?
**Solution**:
1. $	ext{Cov}(U, V) = 	ext{Cov}(2X, 3Y) = 2 	imes 3 	imes 	ext{Cov}(X, Y) = 6 	ext{Cov}(X, Y)$ (scaled by 6!).
2. $
ho_{U,V} = rac{6 	ext{Cov}(X, Y)}{(2 \sigma_X)(3 \sigma_Y)} = rac{6 	ext{Cov}(X, Y)}{6 \sigma_X \sigma_Y} = 
ho_{X,Y}$ (Correlation is scale invariant!).

## Example 5: 2x2 Covariance Matrix Construction
**Problem**: Given $	ext{Var}(X_1) = 16$, $	ext{Var}(X_2) = 25$, and $	ext{Cov}(X_1, X_2) = -10$. Construct covariance matrix $oldsymbol{\Sigma}$.
**Solution**:

$$
oldsymbol{\Sigma} = egin{bmatrix} 	ext{Var}(X_1) & 	ext{Cov}(X_1, X_2) \ 	ext{Cov}(X_2, X_1) & 	ext{Var}(X_2) \end{bmatrix} = egin{bmatrix} 16 & -10 \ -10 & 25 \end{bmatrix}
$$

