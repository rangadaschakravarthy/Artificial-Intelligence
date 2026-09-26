# Theory — Independence

## 1. Simple Definition
Two random variables $X$ and $Y$ are independent if knowing the value of one provides absolutely zero information about the value of the other.

## 2. Intuition
The outcome of a coin flip in Tokyo and the outcome of a coin flip in New York are independent. Knowing Tokyo landed on Heads does not alter the probability distribution of New York's coin flip.

## 3. Mathematical Definition
Random variables $X$ and $Y$ are independent (written $X \perp \!\!\! \perp Y$) if and only if for all subsets $A, B \subseteq \mathbb{R}$:

$$
P(X \in A, Y \in B) = P(X \in A) \cdot P(Y \in B)
$$

For PMF / PDF:

$$
f_{X,Y}(x, y) = f_X(x) \cdot f_Y(y) \quad orall x, y
$$

Conditional Probability Form:

$$
P(Y=y \mid X=x) = P(Y=y) \quad orall x, y
$$

## 4. Fundamental Theorems for Independent RVs
1. **Product Expectation**: $E[X Y] = E[X] E[Y]$
2. **Additive Variance**: $	ext{Var}(X + Y) = 	ext{Var}(X) + 	ext{Var}(Y)$
3. **Zero Covariance**: $	ext{Cov}(X, Y) = 0$

## 5. Notation
- $X \perp \!\!\! \perp Y$: $X$ is independent of $Y$.
- i.i.d.: Independent and Identically Distributed.

## 6. Step-by-Step Verification
Given joint PMF table $p(x, y)$:
- $p_X(0) = 0.4, p_X(1) = 0.6$.
- $p_Y(0) = 0.3, p_Y(1) = 0.7$.
Check if $p(1, 1) = 0.42$:
- $p_X(1) p_Y(1) = 0.6 	imes 0.7 = 0.42$.
If $p(x, y) = p_X(x) p_Y(y)$ for ALL 4 pairs, $X$ and $Y$ are independent.

## 7. Second Example (i.i.d. Data in ML)
Dataset samples $\mathcal{D} = \{(x_1, y_1), \dots, (x_N, y_N)\}$.
Under i.i.d. assumption, dataset joint likelihood factorizes:

$$
L(	heta) = P(\mathcal{D} \mid 	heta) = \prod_{i=1}^N P(x_i, y_i \mid 	heta)
$$

Log-likelihood turns products into sums:

$$
\ln L(	heta) = \sum_{i=1}^N \ln P(x_i, y_i \mid 	heta)
$$

This derivation is why loss functions sum across dataset rows!

## 8. Common Mistakes
- Assuming zero correlation implies independence (Independence $\implies$ Uncorrelated, but Uncorrelated $
eq\implies$ Independent).
- Assuming i.i.d. holds for time-series data (time-series points are sequentially dependent!).

## 9. AI Connection
- Loss function summation across batches requires i.i.d. sample independence.
- Naive Bayes Classifier assumes features are conditionally independent given class target.

## 10. Algorithm Connection
- **Empirical Risk Minimization (ERM)**: Minimizes $rac{1}{N} \sum_{i=1}^N \mathcal{L}(y_i, f(x_i))$, justified by i.i.d. sampling.

## 11. Practical Interpretation
Violating i.i.d. assumptions (e.g. data leakage, temporal autocorrelation) leads to overoptimistic test evaluation.

## 12. Interview Insight
**Q**: Does Independence imply Zero Covariance? Does Zero Covariance imply Independence?
**A**: Independence $\implies$ Zero Covariance ALWAYS. Zero Covariance does NOT imply Independence (unless variables are Jointly Gaussian!).

## 13. Summary
Independence factorizes joint distributions into products of marginals $f(x,y) = f_X(x)f_Y(y)$, enabling log-likelihood summation in machine learning.
