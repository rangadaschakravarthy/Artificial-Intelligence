# Theory — Bayes' Theorem

## 1. Simple Definition
Bayes' Theorem is a formula that calculates the updated probability of a hypothesis after observing new evidence. It converts "probability of evidence given hypothesis" into "probability of hypothesis given evidence."

## 2. Intuition
Suppose a rare disease affects $0.1\%$ of people ($P(	ext{Disease}) = 0.001$). A test is $99\%$ accurate. If you test positive, what is the chance you actually have the disease? Counterintuitively, it is around $9\%$, because the prior rate of disease is so extremely low. Bayes' Theorem mathematically balances initial belief (Prior) against new signal (Likelihood).

## 3. Mathematical Definition
Given hypothesis $H$ and evidence $E$:
$$P(H|E) = rac{P(E|H) \cdot P(H)}{P(E)}$$

Using Law of Total Probability for denominator:
$$P(H|E) = rac{P(E|H) P(H)}{P(E|H) P(H) + P(E|H^c) P(H^c)}$$

## 4. Notation
- $P(H|E)$: **Posterior Probability** (Probability of Hypothesis given Evidence).
- $P(E|H)$: **Likelihood** (Probability of observing Evidence if Hypothesis is true).
- $P(H)$: **Prior Probability** (Initial probability of Hypothesis before evidence).
- $P(E)$: **Marginal Likelihood / Evidence** (Total probability of observing Evidence under all hypotheses).

## 5. Formula
$$	ext{Posterior} = rac{	ext{Likelihood} 	imes 	ext{Prior}}{	ext{Evidence}}$$
$$P(A_i | B) = rac{P(B | A_i) P(A_i)}{\sum_{j=1}^k P(B | A_j) P(A_j)}$$

## 6. Symbol Explanation
- $H$: Hypothesis event.
- $E$: Evidence event.
- $\sum$: Summation across all exhaustive hypotheses.

## 7. Step-by-Step Calculation
Medical Diagnosis Problem:
- Prior $P(D) = 0.01$, $P(D^c) = 0.99$.
- Sensitivity (Likelihood) $P(+|D) = 0.95$.
- False Positive Rate $P(+|D^c) = 0.05$.

Calculate $P(D|+)$:
1. Calculate Evidence $P(+)$:
   $$P(+) = P(+|D)P(D) + P(+|D^c)P(D^c) = (0.95)(0.01) + (0.05)(0.99) = 0.0095 + 0.0495 = 0.0590$$
2. Calculate Posterior $P(D|+)$:
   $$P(D|+) = rac{(0.95)(0.01)}{0.0590} = rac{0.0095}{0.0590} pprox 0.1610 = 16.10\%$$

## 8. Second Example (Spam Filtering)
Word "VIAGRA" appears in an email ($E$).
- Prior $P(	ext{Spam}) = 0.30$.
- $P(	ext{"VIAGRA"} | 	ext{Spam}) = 0.20$.
- $P(	ext{"VIAGRA"} | 	ext{Ham}) = 0.001$.
- Posterior $P(	ext{Spam} | 	ext{"VIAGRA"}) = rac{(0.20)(0.30)}{(0.20)(0.30) + (0.001)(0.70)} = rac{0.06}{0.06 + 0.0007} = rac{0.06}{0.0607} pprox 0.9885 = 98.85\%$.

## 9. Common Mistakes
- Base Rate Fallacy: Ignoring the prior probability $P(H)$.
- Swapping Likelihood $P(E|H)$ for Posterior $P(H|E)$.

## 10. AI Connection
Formulates Bayesian Inference, Naive Bayes Classifiers, Maximum A Posteriori (MAP) estimation, and hyperparameter optimization (Bayesian Optimization).

## 11. Algorithm Connection
- **Naive Bayes Classifier**: $\hat{y} = rg\max_y P(Y=y) \prod_{i=1}^d P(X_i | Y=y)$.
- **MAP Estimation**: $\hat{	heta}_{MAP} = rg\max_	heta [P(X|	heta) P(	heta)]$.

## 12. Practical Interpretation
Posterior probabilities serve as decision scores: if $P(	ext{Fraud}|X) > 0.50$, block transaction.

## 13. Interview Insight
**Q**: What is the Base Rate Fallacy?
**A**: Ignoring the prior probability $P(H)$ when computing $P(H|E)$, leading to severe overestimation of posterior probability for rare events.

## 14. Summary
Bayes' Theorem dynamically combines prior knowledge with observed evidence to compute optimal posterior probabilities in AI.
