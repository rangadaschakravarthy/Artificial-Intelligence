# Solutions — Joint Probability Distributions

## Level 1
1. $\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x, y) dx dy = 1.0$.
2. $f(x, y) = rac{\partial^2}{\partial x \partial y} F(x, y)$.
3. $f(x, y) = f_X(x) f_Y(y)$.
4. $3 	imes 3$.
5. True.

## Level 2
6. $P(X=Y) = p(0,0) + p(1,1) = 0.1 + 0.4 = 0.50$.
7. $P(X > Y) = p(1,0) = 0.30$.
8. $\int_0^1 \int_0^1 c (x + 2y) dx dy = c \int_0^1 \left( rac{1}{2} + 2y ight) dy = c \left( rac{1}{2} + 1 ight) = 1.5 c = 1 \implies c = rac{2}{3}$.
9. $\int_0^{0.5} \int_0^{0.5} 4 x y dx dy = 4 \left[ rac{x^2}{2} ight]_0^{0.5} \left[ rac{y^2}{2} ight]_0^{0.5} = 4 (0.125) (0.125) = 0.0625$.
10. $|oldsymbol{\Sigma}|^{1/2} = 3 \implies rac{1}{2\pi (3)} = rac{1}{6\pi} pprox 0.0531$.

## Level 3
11. Entire domain is $x+y \le 1$, so integral over domain equals total probability $= 1.0$.
12. $E[XY] = \int_0^1 \int_0^1 x y (x + y) dx dy = \int_0^1 \int_0^1 (x^2 y + x y^2) dx dy = \int_0^1 \left( rac{1}{3} y + rac{1}{2} y^2 ight) dy = rac{1}{6} + rac{1}{6} = rac{1}{3} pprox 0.3333$.
13. $F(x,y) = \int_{-\infty}^x \int_{-\infty}^y f_X(u) f_Y(v) dv du = \left( \int_{-\infty}^x f_X(u) du ight) \left( \int_{-\infty}^y f_Y(v) dv ight) = F_X(x) F_Y(y)$.
14. Standard 2D rectangular set inclusion-exclusion decomposition of probability measure over $F(x,y)$.
15. $\int_0^{\infty} c e^{-x} dx \int_0^{\infty} e^{-2y} dy = c (1) (0.5) = 0.5 c = 1 \implies c = 2$.

## Level 4
16. 784-dimensional joint probability distribution space.
17. $3 	ext{ clusters} 	imes 2 	ext{ dimensions} = 6$ mean parameters.
18. $|oldsymbol{\Sigma}| = (2)(2) - (1)(1) = 4 - 1 = 3$.
19. $oldsymbol{\Sigma}^{-1} = rac{1}{3} egin{bmatrix} 2 & -1 \ -1 & 2 \end{bmatrix} = egin{bmatrix} 2/3 & -1/3 \ -1/3 & 2/3 \end{bmatrix}$.
20. If $N < d$, sample covariance matrix $\mathbf{S}$ is rank-deficient (singular), making $|oldsymbol{\Sigma}| = 0$ and $oldsymbol{\Sigma}^{-1}$ undefined.

## Level 5
21. $E[g(X, Y)] = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} g(x, y) f(x, y) dx dy$.
22. VAE uses Marginalization $p(\mathbf{x}) = \int p(\mathbf{x}|\mathbf{z}) p(\mathbf{z}) d\mathbf{z}$ and optimizes Evidence Lower Bound (ELBO) via encoder $q_\phi(\mathbf{z}|\mathbf{x})$ and decoder $p_	heta(\mathbf{x}|\mathbf{z})$.
23. `from scipy.stats import multivariate_normal; density = multivariate_normal(mean=[0,0], cov=[[1,0],[0,1]]).pdf([1, 2])`.
