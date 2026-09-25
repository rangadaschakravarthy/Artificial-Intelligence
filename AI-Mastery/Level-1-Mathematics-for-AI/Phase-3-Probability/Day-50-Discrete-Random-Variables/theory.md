# Theory — Discrete Random Variables

## 1. Simple Definition
A discrete random variable takes distinct, separate values. Its **Probability Mass Function (PMF)** gives the exact probability for each specific value. Its **Cumulative Distribution Function (CDF)** gives the probability of being less than or equal to a value.

## 2. Intuition
Think of PMF as slices of a pie: each slice represents the exact probability of one integer outcome (e.g. rolling 1, 2, or 3). The CDF is the cumulative sum of slices as you move from left to right across outcomes.

## 3. Mathematical Definition
Let $X$ be a discrete random variable with support $S_X = \{x_1, x_2, \dots\}$.
- **PMF**: $p_X(x) = P(X = x)$
- **CDF**: $F_X(x) = P(X \le x) = \sum_{x_i \le x} p_X(x_i)$

## 4. PMF Conditions
1. Non-negativity: $p_X(x) \ge 0$ for all $x$.
2. Normalization: $\sum_{x \in S_X} p_X(x) = 1$.

## 5. Formula
$$	ext{PMF: } p(x) = P(X = x)$$
$$	ext{CDF: } F(x) = P(X \le x) = \sum_{k \le x} p(k)$$
$$	ext{Interval Probability: } P(a < X \le b) = F(b) - F(a)$$

## 6. Symbol Explanation
- $p(x)$: Probability mass function.
- $F(x)$: Cumulative distribution function (step function).
- $\sum$: Discrete sum.

## 7. Step-by-Step Calculation
Coin flip 2 times, $X = 	ext{Heads count}$.
- $S_X = \{0, 1, 2\}$.
- PMF: $p(0) = 0.25$, $p(1) = 0.50$, $p(2) = 0.25$.
- Check sum: $0.25 + 0.50 + 0.25 = 1.0$.
- CDF:
  - $F(0) = P(X \le 0) = 0.25$
  - $F(1) = P(X \le 1) = 0.25 + 0.50 = 0.75$
  - $F(2) = P(X \le 2) = 1.00$

## 8. Second Example (Classification Model Outputs)
A classifier outputs discrete prediction class $C \in \{1, 2, 3\}$.
- PMF: $p(1) = 0.70, p(2) = 0.20, p(3) = 0.10$.
- $P(C \le 2) = F(2) = 0.70 + 0.20 = 0.90$.

## 9. Common Mistakes
- Confusing PMF value $p(x)$ with CDF value $F(x)$.
- Forgetting that CDF $F(x)$ for discrete RVs is a step function (discontinuous at support points).

## 10. AI Connection
Softmax output layer in multi-class classification defines a discrete PMF over classes $1, \dots, K$.

## 11. Algorithm Connection
- **Categorical Cross-Entropy Loss**: $L = -\sum_i y_i \log p(i)$, where $y_i$ is ground truth PMF and $p(i)$ is model PMF.

## 12. Practical Interpretation
In multi-class prediction, top-k accuracy evaluates $P(X \in 	ext{Top-k})$.

## 13. Interview Insight
**Q**: How do you reconstruct the PMF $p(x)$ from the discrete CDF $F(x)$?
**A**: By computing step jumps: $p(x_i) = F(x_i) - F(x_{i-1})$.

## 14. Summary
PMFs assign exact probabilities to discrete outcomes; CDFs accumulate them. Multi-class AI classifiers output discrete PMFs.
