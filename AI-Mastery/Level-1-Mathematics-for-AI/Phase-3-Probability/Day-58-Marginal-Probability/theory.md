# Theory — Marginal Probability

## 1. Simple Definition
Marginal probability is the probability distribution of a single random variable obtained by summing or integrating out all other variables from a joint probability distribution.

## 2. Intuition
Imagine a table of customer data showing Age ($X$) and Income ($Y$). If you want to know the probability distribution of Age ALONE ($X$), regardless of income, you collapse the 2D table by summing across all income columns. The resulting totals in the margin of the table form the **marginal distribution**.

## 3. Mathematical Definition
- **Discrete Marginal PMF**:
  $$p_X(x) = \sum_{y \in S_Y} p_{X,Y}(x, y)$$
  $$p_Y(y) = \sum_{x \in S_X} p_{X,Y}(x, y)$$

- **Continuous Marginal PDF**:
  $$f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x, y) dy$$
  $$f_Y(y) = \int_{-\infty}^{\infty} f_{X,Y}(x, y) dx$$

## 4. Notation
- $p_X(x)$ or $f_X(x)$: Marginal PMF / PDF of $X$.
- $\sum_y$ or $\int dy$: Integrating out nuisance variable $Y$.

## 5. Step-by-Step Calculation
Discrete Joint PMF:
| $X \setminus Y$ | $Y=0$ | $Y=1$ | **Marginal $p_X(x)$** |
| :--- | :--- | :--- | :--- |
| **$X=0$** | $0.1$ | $0.3$ | $0.1 + 0.3 = \mathbf{0.4}$ |
| **$X=1$** | $0.2$ | $0.4$ | $0.2 + 0.4 = \mathbf{0.6}$ |
| **Marginal $p_Y(y)$** | **$0.3$** | **$0.7$** | **Sum = $1.0$** |

- Marginal $p_X(0) = 0.4, p_X(1) = 0.6$.
- Marginal $p_Y(0) = 0.3, p_Y(1) = 0.7$.

## 6. Second Example (Continuous Marginalization)
Given joint PDF $f(x, y) = 4 x y$ on $[0, 1] 	imes [0, 1]$.
Find marginal PDF $f_X(x)$:
$$f_X(x) = \int_0^1 4 x y dy = 4 x \left[ rac{y^2}{2} ight]_0^1 = 4 x \left( rac{1}{2} ight) = 2 x \quad 	ext{for } 0 \le x \le 1$$

## 7. Common Mistakes
- Integrating with respect to $x$ when trying to find marginal $f_X(x)$ (To find $f_X(x)$, integrate out $y$!).
- Forgetting to specify valid domain bounds for the resulting marginal distribution.

## 8. AI Connection
In Bayesian AI models with latent variables $\mathbf{z}$ and observed features $\mathbf{x}$, marginal probability $p(\mathbf{x}) = \int p(\mathbf{x}, \mathbf{z}) d\mathbf{z}$ is the evidence / marginal likelihood.

## 9. Algorithm Connection
- **Expectation-Maximization (EM) Algorithm**: Handles intractable marginal likelihoods when latent variables $\mathbf{z}$ cannot be integrated out analytically.

## 10. Practical Interpretation
Marginalization collapses multi-feature models to focus on predictions for specific individual features.

## 11. Interview Insight
**Q**: How does marginalization relate to the Law of Total Probability?
**A**: Continuous marginalization $f_X(x) = \int f(x, y) dy = \int f(x|y) f_Y(y) dy$ is the continuous generalization of the Law of Total Probability.

## 12. Summary
Marginalization integrates out unwanted variables $\int f(x,y)dy = f_X(x)$, reducing multi-dimensional joint distributions to single-variable distributions.
