# Solutions — Marginal Probability

## Level 1
1. $p_Y(y) = \sum_x p_{X,Y}(x, y)$.
2. $f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x, y) dy$.
3. $1.0$.
4. The result equals $1.0$ (total probability).
5. True.

## Level 2
6. $p_X(0) = p(0,0) + p(0,1) = 0.15 + 0.35 = 0.50$.
7. $p_Y(1) = p(0,1) + p(1,1) = 0.35 + 0.30 = 0.65$.
8. $f_X(x) = \int_0^1 (x + y) dy = \left[ x y + \frac{y^2}{2} 
ight]_0^1 = x + 0.5$ for $0 \le x \le 1$.
9. $f_X(x) = \int_x^1 2 dy = 2(1 - x)$ for $0 \le x \le 1$.
10. $	ext{Var}(Y) = 25 \implies \sigma_Y = \sqrt{25} = 5.0$.

## Level 3
11. $f_Y(y) = \int_0^y 2 dx = 2 y$ for $0 \le y \le 1$.
12. $E[X] = \int_0^1 x(x + 0.5) dx = \int_0^1 (x^2 + 0.5 x) dx = \left[ \frac{x^3}{3} + \frac{x^2}{4} 
ight]_0^1 = \frac{1}{3} + \frac{1}{4} = \frac{7}{12} pprox 0.5833$.
13. Proof: $E[X]_{	ext{joint}} = \int\int x f(x,y) dy dx = \int x \left( \int f(x,y) dy 
ight) dx = \int x f_X(x) dx = E[X]_{	ext{marginal}}$.
14. $f_X(x) = \int f_X(x) f_Y(y) dy = f_X(x) \int f_Y(y) dy = f_X(x) (1) = f_X(x)$.
15. For fixed $x$, $y$ goes from $0$ to $x$. $f_X(x) = \int_0^x 3 x dy = 3 x [y]_0^x = 3 x^2$ for $0 \le x \le 1$.

## Level 4
16. Joint: $p(x, z) = p(x|z)p(z)$. Marginal: $p(x) = \sum_k p(x, z=k)$.
17. Intractable because high-dimensional latent space $z \in \mathbb{R}^d$ requires integrating non-linear deep neural network decoder outputs $p_	heta(x|z)$ over all possible $z$, which has no closed-form analytical solution.
18. By Law of Large Numbers, empirical average of likelihoods evaluated at $S$ sampled points $z^{(s)}$ converges to true integral $\int p(x|z)p(z)dz$ as $S \to \infty$.
19. $p_X(x) = \sum_y \sum_z p(x, y, z)$.
20. $P(s' | s, a) = \sum_{r \in S_R} P(s', r | s, a)$.

## Level 5
21. Partition block covariance matrix $oldsymbol{\Sigma} = egin{bmatrix} oldsymbol{\Sigma}_{11} & oldsymbol{\Sigma}_{12} \ oldsymbol{\Sigma}_{21} & oldsymbol{\Sigma}_{22} \end{bmatrix}$. Fourier transform / Characteristic function $\phi_{\mathbf{X}}(\mathbf{t}) = \exp(i \mathbf{t}^T oldsymbol{\mu} - \frac{1}{2} \mathbf{t}^T oldsymbol{\Sigma} \mathbf{t})$. Setting component subvectors $\mathbf{t}_2 = 0$ yields characteristic function of $\mathbf{X}_1$ matching $\mathcal{N}(oldsymbol{\mu}_1, oldsymbol{\Sigma}_{11})$.
22. Marginalization accounts for ALL possible values of nuisance variable weighted by their probability (averaging out). Conditioning at zero isolates a single slicing hyperplane at $Y=0$, throwing away all other data.
23. `marginal_X = np.sum(joint_pmf, axis=1); marginal_Y = np.sum(joint_pmf, axis=0)`.
