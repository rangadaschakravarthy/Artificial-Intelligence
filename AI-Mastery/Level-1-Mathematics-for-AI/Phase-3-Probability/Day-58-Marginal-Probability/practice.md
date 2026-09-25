# Practice Problems — Marginal Probability

## Level 1: Basic Concept Checks
1. Write the formula for discrete marginal PMF $p_Y(y)$.
2. Write the formula for continuous marginal PDF $f_X(x)$.
3. If $f(x, y)$ is a joint PDF, what is $\int_{-\infty}^{\infty} f_X(x) dx$?
4. What happens when you marginalize out all variables from a joint distribution?
5. True or False: Marginalizing $Y$ from $f(x,y)$ removes $y$ entirely from the resulting expression.

## Level 2: Direct Calculations
6. Discrete joint PMF: $p(0,0)=0.15, p(0,1)=0.35, p(1,0)=0.20, p(1,1)=0.30$. Compute marginal $p_X(0)$.
7. In Q6, compute marginal $p_Y(1)$.
8. Joint PDF $f(x,y) = x + y$ on $[0,1] 	imes [0,1]$. Derive marginal $f_X(x)$.
9. Joint PDF $f(x,y) = 2$ on $0 \le x \le y \le 1$. Derive marginal $f_X(x)$.
10. For Bivariate Gaussian $\mathcal{N}\left( egin{bmatrix} 0 \ 0 \end{bmatrix}, egin{bmatrix} 16 & 5 \ 5 & 25 \end{bmatrix} ight)$, state standard deviation $\sigma_Y$.

## Level 3: Conceptual & Multi-Step Problems
11. Derive marginal $f_Y(y)$ for joint PDF $f(x,y) = 2$ on $0 \le x \le y \le 1$.
12. For $f_X(x) = x + 0.5$ on $[0, 1]$, compute marginal mean $E[X]$.
13. Prove that $E[X]$ computed from joint $f(x,y)$ equals $E[X]$ computed from marginal $f_X(x)$.
14. If $X \perp \!\!\! \perp Y$, show that continuous marginalization of $f(x,y) = f_X(x)f_Y(y)$ yields $f_X(x)$.
15. If $f(x,y) = 3 x$ on $0 \le y \le x \le 1$, derive marginal $f_X(x)$.

## Level 4: AI & ML Applications
16. In Bayesian Mixture Models $p(x) = \sum_{k=1}^K p(x | z=k) p(z=k)$, identify the joint distribution and the marginal distribution.
17. In VAE latent spaces, observed image data marginal likelihood is $p(x) = \int p(x|z) p(z) dz$. Why is this integral intractable for complex neural networks $p(x|z)$?
18. Explain how Monte Carlo integration approximates marginal $p(x) pprox rac{1}{S} \sum_{s=1}^S p(x | z^{(s)})$ by sampling $z^{(s)} \sim p(z)$.
19. Given 3D joint PMF $p(x, y, z)$, write the formula to marginalize out both $Y$ and $Z$ to find $p_X(x)$.
20. In reinforcement learning, state transition dynamics $P(s' | s, a) = \sum_r P(s', r | s, a)$ marginalizes out reward $r$. Write the sum.

## Level 5: Interview Questions
21. Prove that for any Joint Gaussian distribution $\mathbf{X} \sim \mathcal{N}(oldsymbol{\mu}, oldsymbol{\Sigma})$, any subset marginal distribution is also Gaussian.
22. Explain why summing out nuisance variables (Marginalization) differs from setting nuisance variables to zero (Conditioning at zero).
23. Write Python code using NumPy to marginalize a $2D$ joint probability array along axis 1 and axis 0.
