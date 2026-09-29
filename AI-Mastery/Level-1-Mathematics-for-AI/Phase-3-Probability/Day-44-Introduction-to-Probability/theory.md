# Theory — Introduction to Probability

## 1. Simple Definition
Probability is a number between $0$ and $1$ that measures how likely an event is to happen. A probability of $0$ means the event is impossible, while a probability of $1$ means the event is absolutely certain.

## 2. Intuition
Imagine flipping a fair coin 1,000 times. You cannot predict the exact outcome of flip #427, but over 1,000 flips, approximately 500 will be Heads. Probability allows AI models to make rational predictions even when individual data points are noisy or unpredictable.

## 3. Mathematical Definition
Given a sample space $\Omega$ containing all possible outcomes, an event $A$ is a subset of $\Omega$ ($A \subseteq \Omega$). Probability is a function $P: \mathcal{F} \to [0, 1]$ mapping events to real numbers adhering to Kolmogorov Axioms.

## 4. Notation
- $\Omega$: Sample Space (set of all outcomes)
- $A$: An Event ($A \subseteq \Omega$)
- $P(A)$: Probability of event $A$ occurring

## 5. Formula
Mathematical definition under equal likelihood:

$$
P(A) = \frac{|A|}{|\Omega|} = \frac{	ext{Number of favorable outcomes}}{	ext{Total number of possible outcomes}}
$$

Kolmogorov Axioms:
1. **Non-negativity**: $P(A) \ge 0$ for all $A$.
2. **Unitarity**: $P(\Omega) = 1$.
3. **Countable Additivity**: For disjoint events $A_1, A_2, \dots$:
$$P\left(igcup_{i=1}^{\infty} A_i
ight) = \sum_{i=1}^{\infty} P(A_i)$$

## 6. Symbol Explanation
- $|A|$: Cardinality (count of elements) in set $A$.
- $|\Omega|$: Total count of outcomes in sample space.
- $igcup$: Union of sets.

## 7. Step-by-Step Calculation
Consider rolling a fair 6-sided die. Find probability of rolling an even number.
- $\Omega = \{1, 2, 3, 4, 5, 6\} \implies |\Omega| = 6$.
- Event $A = 	ext{Even number} = \{2, 4, 6\} \implies |A| = 3$.
- $P(A) = \frac{3}{6} = 0.5$.

## 8. Second Example (Real-World AI)
In an image classification model predicting Cat vs Dog:
- Neural network outputs logits $[2.1, 0.5]$.
- Softmax converts logits to probabilities: $P(	ext{Cat}) = \frac{e^{2.1}}{e^{2.1} + e^{0.5}} pprox 0.832$.
- $P(	ext{Dog}) = 1 - 0.832 = 0.168$.

## 9. Common Mistakes
- Thinking $P(A) > 1$ or $P(A) < 0$.
- Confusing individual trial outcomes with long-run frequency.
- Assuming all outcomes are equally likely when they are not.

## 10. AI Connection
Classifier predictions (e.g., logistic regression, softmax layer in deep learning) output values in $[0, 1]$ representing $P(Y=1|X)$.

## 11. Algorithm Connection
- **Logistic Regression**: Sigmoid function $\sigma(z) = \frac{1}{1 + e^{-z}}$ forces output to be a probability.
- **Classification Thresholding**: Decision boundary where prediction is class 1 if $P(Y=1|X) \ge 0.5$.

## 12. Practical Interpretation
A model reporting $P(	ext{Fraud}=1) = 0.95$ indicates a $95\%$ confidence that the transaction is fraudulent, allowing automated flagging.

## 13. Interview Insight
**Q**: What are Kolmogorov's Axioms?
**A**: 1) $P(A) \ge 0$, 2) $P(\Omega) = 1$, 3) For mutually exclusive events, probability of union is the sum of probabilities.

## 14. Summary
Probability quantifies uncertainty. AI uses probability to turn raw inputs into decision-making scores between 0 and 1.
