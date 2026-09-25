# Practice Problems — Covariance and Correlation

## Level 1: Basic Concept Checks
1. Write the formula for $	ext{Cov}(X, Y)$ in terms of expectations.
2. What are the minimum and maximum possible values of Pearson correlation $ho$?
3. What does $	ext{Cov}(X, X)$ equal?
4. If $X$ and $Y$ are independent, what is $	ext{Cov}(X, Y)$?
5. State the property that makes correlation preferred over covariance for comparing relationships across different datasets.

## Level 2: Direct Calculations
6. Given $E[X] = 4, E[Y] = 2, E[XY] = 11$. Calculate $	ext{Cov}(X, Y)$.
7. If $	ext{Cov}(X, Y) = -6$, $	ext{Var}(X) = 9$, $	ext{Var}(Y) = 16$. Calculate $ho_{X,Y}$.
8. If $Y = -3X + 5$, compute $ho_{X,Y}$.
9. Compute $	ext{Cov}(X, 5X + 2)$ if $	ext{Var}(X) = 4$.
10. Construct the $2 	imes 2$ correlation matrix for variables with $ho_{X_1, X_2} = 0.8$.

## Level 3: Conceptual & Multi-Step Problems
11. Prove that $	ext{Cov}(aX + b, cY + d) = a c 	ext{Cov}(X, Y)$.
12. Prove Cauchy-Schwarz inequality for covariance: $|	ext{Cov}(X, Y)| \le \sigma_X \sigma_Y$, showing why $-1 \le ho \le 1$.
13. If $	ext{Var}(X + Y) = 	ext{Var}(X) + 	ext{Var}(Y)$, show that $X$ and $Y$ are uncorrelated.
14. Show that covariance is a bilinear operator: $	ext{Cov}(X + Y, Z) = 	ext{Cov}(X, Z) + 	ext{Cov}(Y, Z)$.
15. If $oldsymbol{\Sigma}$ is a valid covariance matrix, explain why all diagonal entries must be non-negative.

## Level 4: AI & ML Applications
16. In linear regression, collinearity occurs when $ho_{X_i, X_j} pprox 1.0$. Explain why this causes matrix $(X^T X)$ to be ill-conditioned.
17. In PCA, the total variance of a dataset with covariance matrix $oldsymbol{\Sigma}$ equals $	ext{Tr}(oldsymbol{\Sigma})$. Compute total variance for $oldsymbol{\Sigma} = egin{bmatrix} 4 & 2 \ 2 & 9 \end{bmatrix}$.
18. Compute Mahalanobis distance formula $d_M(\mathbf{x}, oldsymbol{\mu}) = \sqrt{(\mathbf{x} - oldsymbol{\mu})^T oldsymbol{\Sigma}^{-1} (\mathbf{x} - oldsymbol{\mu})}$ for $\mathbf{x} = [2, 0]^T$, $oldsymbol{\mu} = [0, 0]^T$, $oldsymbol{\Sigma} = egin{bmatrix} 1 & 0 \ 0 & 4 \end{bmatrix}$.
19. Explain how Feature Selection uses high correlation with target $Y$ and low mutual correlation among features $X_i$ to select optimal feature subsets.
20. In Gaussian Mixture Models, what is the difference between Spherical, Diagonal, and Full covariance matrices?

## Level 5: Interview Questions
21. Prove that if $Y = a X + b$ with $a > 0$, then $ho_{X,Y} = 1$.
22. Give an explicit mathematical example of two random variables that have correlation $ho = 0$ but are NOT independent.
23. Write Python code using NumPy to compute the sample covariance matrix of a $1000 	imes 3$ feature matrix.
