# Practice Problems — Joint Probability Distributions

## Level 1: Basic Concept Checks
1. State the normalization condition for a 2D continuous joint PDF $f(x, y)$.
2. How do you recover joint PDF $f(x, y)$ from joint CDF $F(x, y)$?
3. If $X$ and $Y$ are independent, express joint PDF $f(x, y)$ in terms of marginals.
4. What is the dimension of the covariance matrix for a 3-dimensional random vector?
5. True or False: For a joint discrete PMF table, the sum of all cell entries must equal 1.

## Level 2: Direct Calculations
6. Given joint PMF $p(0,0)=0.1, p(0,1)=0.2, p(1,0)=0.3, p(1,1)=0.4$. Compute $P(X = Y)$.
7. For the PMF in Q6, compute $P(X > Y)$.
8. Find constant $c$ for joint PDF $f(x, y) = c (x + 2y)$ on $0 \le x \le 1, 0 \le y \le 1$.
9. For PDF $f(x, y) = 4 x y$ on $[0, 1] 	imes [0, 1]$, compute $P(X \le 0.5, Y \le 0.5)$.
10. For Bivariate Gaussian with $|oldsymbol{\Sigma}| = 9$, compute normalization constant $\frac{1}{2\pi |oldsymbol{\Sigma}|^{1/2}}$.

## Level 3: Conceptual & Multi-Step Problems
11. Compute $P(X + Y \le 1)$ for joint PDF $f(x, y) = 2$ on $x \ge 0, y \ge 0, x+y \le 1$.
12. For joint PDF $f(x, y) = x + y$ on $[0, 1] 	imes [0, 1]$, compute $E[XY]$.
13. Show that for independent continuous RVs $X, Y$, joint CDF factorizes: $F(x, y) = F_X(x) F_Y(y)$.
14. Show that $P(a < X \le b, c < Y \le d) = F(b, d) - F(a, d) - F(b, c) + F(a, c)$.
15. If $f(x, y) = c e^{-(x+2y)}$ for $x \ge 0, y \ge 0$, find constant $c$.

## Level 4: AI & ML Applications
16. In image generation, an image is a random vector $\mathbf{x} \in \mathbb{R}^{784}$ (MNIST 28x28). What is the dimensionality of its joint distribution?
17. In GMM clustering with $K=3$ components in 2D space, how many total scalar parameters are in the mean vectors $oldsymbol{\mu}_k$?
18. Compute determinant $|oldsymbol{\Sigma}|$ for $oldsymbol{\Sigma} = egin{bmatrix} 2 & 1 \ 1 & 2 \end{bmatrix}$.
19. Compute inverse matrix $oldsymbol{\Sigma}^{-1}$ for covariance matrix in Q18.
20. Explain why Maximum Likelihood Estimation of high-dimensional joint Gaussian parameters $oldsymbol{\Sigma}$ requires $N > d$ sample data points.

## Level 5: Interview Questions
21. Derive the double integral expression for $E[g(X, Y)]$ under joint PDF $f(x, y)$.
22. How does a Variational Autoencoder (VAE) approximate intractable joint data density $p(\mathbf{x})$ using latent variables $\mathbf{z}$?
23. Write Python code using `scipy.stats.multivariate_normal` to evaluate joint PDF density at point $[1, 2]^T$.
