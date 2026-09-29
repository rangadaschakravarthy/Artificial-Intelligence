# Theory — Random Variables

## 1. Simple Definition
A random variable is a rule or mathematical function that assigns a numerical value to each possible outcome of a random process.

## 2. Intuition
When flipping a coin 3 times, the sample space consists of strings like $\{HHT, TTH, \dots\}$. Computers cannot perform matrix math on words. A random variable $X$ translates these outcomes into numbers, such as "number of Heads" ($X=2$ for $HHT$).

## 3. Mathematical Definition
A random variable $X$ is a measurable function $X: \Omega \to \mathbb{R}$ that maps elements $\omega \in \Omega$ from the sample space to real numbers on the real line.

## 4. Notation
- Uppercase $X, Y, Z$: The random variable itself (the rule / function).
- Lowercase $x, y, z$: A specific realized numerical value.
- $P(X = x)$: Probability that random variable $X$ takes the specific value $x$.

## 5. Types of Random Variables
- **Discrete**: Countable set of values (e.g., $X \in \{0, 1, 2, \dots\}$).
- **Continuous**: Uncountable continuum of values (e.g., $X \in [a, b] \subseteq \mathbb{R}$).

## 6. Symbol Explanation
- $X(\omega)$: Evaluation of random variable function at sample point $\omega$.
- $\mathbb{R}$: Set of real numbers.

## 7. Step-by-Step Example
Rolling two fair 6-sided dice. Let $X$ be the sum of the two dice.
- Sample point $\omega = (3, 4) \in \Omega$.
- $X((3, 4)) = 3 + 4 = 7$.
- Support of $X$: $S_X = \{2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12\}$.
- $P(X = 7) = \frac{6}{36} = \frac{1}{6}$.

## 8. Second Example (AI Target Variable)
In binary customer churn prediction:
- $\Omega$: Customer behaviors and records.
- $Y(\omega) = 1$ if customer churns within 30 days, $Y(\omega) = 0$ otherwise.
- $Y$ is a Bernoulli random variable.

## 9. Common Mistakes
- Confusing the random variable $X$ with a static unknown variable in high school algebra.
- Mixing up uppercase $X$ (the process) with lowercase $x$ (a specific observed number).

## 10. AI Connection
In ML feature engineering, input vectors $\mathbf{x} = [X_1, X_2, \dots, X_d]^T$ represent a vector of random variables.

## 11. Algorithm Connection
- **Linear Regression**: Models $Y = \mathbf{w}^T \mathbf{X} + \epsilon$, where $\epsilon \sim \mathcal{N}(0, \sigma^2)$ is a Gaussian random variable.

## 12. Practical Interpretation
Specifying whether a target $Y$ is discrete or continuous determines model selection: classification (discrete) vs regression (continuous).

## 13. Interview Insight
**Q**: What is a random variable formally in measure-theoretic probability?
**A**: A measurable function from a probability space $(\Omega, \mathcal{F}, P)$ to the real numbers $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$.

## 14. Summary
Random variables convert raw real-world random outcomes into numbers $\mathbb{R}$ that algorithms process.
