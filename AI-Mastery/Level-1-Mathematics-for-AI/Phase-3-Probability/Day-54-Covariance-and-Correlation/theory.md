# Theory — Covariance and Correlation

## 1. Simple Definition
- **Covariance**: Measures the directional joint variability of two random variables (whether they tend to increase together or move in opposite directions).
- **Correlation**: A standardized version of covariance bounded between $-1$ and $+1$ that measures the strength and direction of a linear relationship.

## 2. Intuition
- Positive Covariance/Correlation: As house size increases, price increases.
- Zero Covariance/Correlation: Shoe size vs IQ score (no linear relation).
- Negative Covariance/Correlation: Car age vs market resale price.

## 3. Mathematical Definitions
- **Covariance**:
  $$	ext{Cov}(X, Y) = E[(X - \mu_X)(Y - \mu_Y)] = E[XY] - E[X] E[Y]$$
- **Pearson Correlation**:
  $$ho_{X,Y} = rac{	ext{Cov}(X, Y)}{\sigma_X \sigma_Y}$$

## 4. Range and Interpretation
- $ho = +1$: Perfect positive linear relationship.
- $ho = 0$: No linear relationship (variables may still have non-linear dependence!).
- $ho = -1$: Perfect negative linear relationship.

## 5. Covariance Matrix $oldsymbol{\Sigma}$
For random vector $\mathbf{X} = [X_1, X_2, \dots, X_d]^T$:
$$oldsymbol{\Sigma} = egin{bmatrix} 	ext{Var}(X_1) & 	ext{Cov}(X_1, X_2) & \dots & 	ext{Cov}(X_1, X_d) \ 	ext{Cov}(X_2, X_1) & 	ext{Var}(X_2) & \dots & 	ext{Cov}(X_2, X_d) \ dots & dots & \ddots & dots \ 	ext{Cov}(X_d, X_1) & 	ext{Cov}(X_d, X_2) & \dots & 	ext{Var}(X_d) \end{bmatrix}$$

## 6. Symbol Explanation
- $	ext{Cov}(X, Y)$: Covariance.
- $ho_{X,Y}$: Pearson correlation coefficient.
- $oldsymbol{\Sigma}$: $d 	imes d$ symmetric positive semi-definite covariance matrix.

## 7. Step-by-Step Calculation
Discrete joint points $(X, Y)$: $(1, 2), (2, 4), (3, 6)$ each with probability $1/3$.
- $E[X] = rac{1+2+3}{3} = 2$.
- $E[Y] = rac{2+4+6}{3} = 4$.
- $E[XY] = rac{1(2) + 2(4) + 3(6)}{3} = rac{2 + 8 + 18}{3} = rac{28}{3} pprox 9.3333$.
- $	ext{Cov}(X, Y) = E[XY] - E[X]E[Y] = rac{28}{3} - (2)(4) = 9.3333 - 8 = 1.3333$.

## 8. Second Example (AI Feature Redundancy)
In a linear regression dataset:
- Feature $X_1$: Income in USD.
- Feature $X_2$: Income in Euros.
- $ho_{X_1, X_2} = 1.0$. Highly redundant features (multicollinearity) cause unstable weight matrix inversion $(X^T X)^{-1}$.

## 9. Common Mistakes
- Assuming $ho = 0$ means $X$ and $Y$ are independent (they can have non-linear dependence like $Y = X^2$ where $ho = 0$).
- Thinking covariance scale indicates strength (covariance units depend on raw feature scales; correlation must be used to compare strength).

## 10. AI Connection
Principal Component Analysis (PCA) computes eigenvectors of the sample covariance matrix $oldsymbol{\Sigma}$ to find orthogonal directions of maximum variance.

## 11. Algorithm Connection
- **Multivariate Normal Distribution**: $\mathcal{N}(oldsymbol{\mu}, oldsymbol{\Sigma})$. Covariance matrix $oldsymbol{\Sigma}$ dictates cluster shapes in Gaussian Mixture Models (GMMs).

## 12. Practical Interpretation
A correlation heatmap identifies redundant input features before training ML models, allowing feature pruning.

## 13. Interview Insight
**Q**: If $ho_{X,Y} = 0$, are $X$ and $Y$ independent?
**A**: Not necessarily! Independence implies zero correlation, but zero correlation only rules out *linear* association. For $Y = X^2$ with symmetric $X \sim 	ext{Unif}(-1, 1)$, $ho = 0$ despite perfect deterministic dependence.

## 14. Summary
Covariance quantifies joint movement; correlation standardizes it to $[-1, 1]$. Covariance matrices structure multivariate AI algorithms.
