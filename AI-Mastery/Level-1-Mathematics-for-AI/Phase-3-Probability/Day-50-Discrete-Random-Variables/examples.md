# Worked Examples — Discrete Random Variables

## Example 1: PMF Verification
**Problem**: Is $p(x) = rac{x}{10}$ for $x \in \{1, 2, 3, 4\}$ a valid PMF?
**Solution**:
1. Non-negativity check: $p(1)=0.1, p(2)=0.2, p(3)=0.3, p(4)=0.4$. All $\ge 0$.
2. Sum check: $\sum p(x) = 0.1 + 0.2 + 0.3 + 0.4 = 1.0$.
3. Yes, it is a valid PMF.

## Example 2: CDF Construction
**Problem**: For the valid PMF in Example 1, compute $F(x)$ for all integer values $x \in \{1, 2, 3, 4\}$.
**Solution**:
1. $F(1) = p(1) = 0.1$.
2. $F(2) = p(1) + p(2) = 0.1 + 0.2 = 0.3$.
3. $F(3) = 0.3 + 0.3 = 0.6$.
4. $F(4) = 0.6 + 0.4 = 1.0$.

## Example 3: Interval Probability from CDF
**Problem**: Given CDF values $F(1) = 0.2, F(2) = 0.5, F(3) = 0.8, F(4) = 1.0$. Compute $P(1 < X \le 3)$.
**Solution**:
1. $P(1 < X \le 3) = F(3) - F(1) = 0.8 - 0.2 = 0.60$.

## Example 4: AI Softmax PMF Evaluation
**Problem**: A neural network predicts 3 classes with Softmax output probabilities $[0.60, 0.30, 0.10]$. Find $P(X \ge 2)$.
**Solution**:
1. $P(X \ge 2) = p(2) + p(3) = 0.30 + 0.10 = 0.40$.

## Example 5: Expectation of Discrete RV
**Problem**: Compute expected value $E[X]$ for $X \in \{1, 2, 3, 4\}$ with PMF $p(x) = rac{x}{10}$.
**Solution**:
1. $E[X] = \sum x \cdot p(x) = 1(0.1) + 2(0.2) + 3(0.3) + 4(0.4) = 0.1 + 0.4 + 0.9 + 1.6 = 3.0$.
