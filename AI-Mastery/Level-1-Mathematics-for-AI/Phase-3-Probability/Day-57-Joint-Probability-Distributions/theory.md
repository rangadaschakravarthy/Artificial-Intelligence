# Theory — Joint Probability Distributions

## 1. Simple Definition
A joint probability distribution describes the simultaneous probability behavior of two or more random variables.

## 2. Intuition
Instead of looking at house size ($X$) or house price ($Y$) individually, a joint distribution gives the probability density for every combined pair $(X, Y)$ on a 2D surface landscape.

## 3. Mathematical Definition
- **Discrete Joint PMF**: $p_{X,Y}(x, y) = P(X = x, Y = y)$
  $$\sum_x \sum_y p_{X,Y}(x, y) = 1, \quad p(x,y) \ge 0$$
- **Continuous Joint PDF**: $f_{X,Y}(x, y)$ such that:
  $$P((X,Y) \in R) = \iint_R f_{X,Y}(x, y) dx dy$$
  $$\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f_{X,Y}(x, y) dx dy = 1$$
- **Joint CDF**: $F_{X,Y}(x, y) = P(X \le x, Y \le y) = \int_{-\infty}^x \int_{-\infty}^y f(u, v) dv du$

## 4. Notation
- $f(x, y)$ or $p(x, y)$: Joint PDF / PMF.
- $F(x, y)$: Joint CDF.
- $\mathbf{X} = [X_1, \dots, X_d]^T$: $d$-dimensional random vector.

## 5. Step-by-Step Integration Example
Let $f(x, y) = 2$ for $x \ge 0, y \ge 0, x + y \le 1$.
1. Check normalization (Area of triangle $= 0.5$):
   $$\int_0^1 \int_0^{1-x} 2 dy dx = \int_0^1 2(1-x) dx = \left[ 2x - x^2 ight]_0^1 = 2 - 1 = 1.0$$
2. Compute $P(X \le 0.5, Y \le 0.5)$:
   $$\int_0^{0.5} \int_0^{0.5} 2 dy dx = 2 	imes 0.5 	imes 0.5 = 0.50$$

## 6. Second Example (Bivariate Gaussian Distribution)
Continuous 2D Gaussian PDF with mean vector $oldsymbol{\mu} = [\mu_1, \mu_2]^T$ and covariance matrix $oldsymbol{\Sigma}$:
$$f(\mathbf{x}) = rac{1}{2\pi |oldsymbol{\Sigma}|^{1/2}} \exp\left( -rac{1}{2} (\mathbf{x} - oldsymbol{\mu})^T oldsymbol{\Sigma}^{-1} (\mathbf{x} - oldsymbol{\mu}) ight)$$

## 7. Common Mistakes
- Integrating continuous limits incorrectly when integration region boundary depends on $x$ or $y$.
- Confusing joint probability $p(x,y)$ with conditional probability $p(x|y)$.

## 8. AI Connection
Generative models (GANs, VAEs, Normalizing Flows) estimate the joint data distribution $p(\mathbf{x})$ over high-dimensional input vectors (e.g. $256 	imes 256 	imes 3$ pixel images).

## 9. Algorithm Connection
- **Gaussian Mixture Models (GMMs)**: Models joint data distribution as a weighted sum of $K$ multivariate Gaussian PDFs: $p(\mathbf{x}) = \sum_{k=1}^K \pi_k \mathcal{N}(\mathbf{x}; oldsymbol{\mu}_k, oldsymbol{\Sigma}_k)$.

## 10. Practical Interpretation
High joint probability density $f(\mathbf{x})$ indicates typical, realistic data points; low density indicates outliers or anomalies.

## 11. Interview Insight
**Q**: How do you extract joint PDF from joint CDF $F(x, y)$?
**A**: By taking partial derivatives: $f(x, y) = rac{\partial^2}{\partial x \partial y} F(x, y)$.

## 12. Summary
Joint distributions $f(x,y)$ model multi-variable feature spaces, forming the foundation of multivariate AI algorithms.
