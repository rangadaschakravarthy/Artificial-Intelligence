# Theory — Conditional Probability

## 1. Simple Definition
Conditional probability is the probability of an event $A$ occurring given that another event $B$ has already occurred. It is written as $P(A|B)$ (read as "probability of A given B").

## 2. Intuition
Imagine picking a random person from the global population. The probability they speak Japanese is small. However, if you are given the new information that the person lives in Tokyo (event $B$), the conditional probability that they speak Japanese (event $A$) becomes nearly $100\%$. Event $B$ shrinks the sample space from the whole world down to Tokyo.

## 3. Mathematical Definition
For any two events $A$ and $B$ in sample space $\Omega$ with $P(B) > 0$:
$$P(A|B) = rac{P(A \cap B)}{P(B)}$$

## 4. Notation
- $P(A|B)$: Probability of $A$ given $B$.
- $P(A \cap B)$: Probability of both $A$ and $B$ occurring.
- $P(B)$: Marginal probability of condition event $B$.

## 5. Formula
$$P(A|B) = rac{P(A \cap B)}{P(B)}, \quad P(B) > 0$$
$$	ext{Reordered: } P(A \cap B) = P(A|B)P(B) = P(B|A)P(A)$$

## 6. Symbol Explanation
- $|$: "given" or "conditioned upon".
- $\cap$: Joint occurrence of both events.

## 7. Step-by-Step Calculation
In a dataset of 100 images:
- 40 images are Cats ($A$).
- 30 images have Whiskers ($B$).
- 25 images are Cats AND have Whiskers ($A \cap B$).

Find $P(	ext{Cat} \mid 	ext{Whiskers}) = P(A|B)$:
$$P(A|B) = rac{P(A \cap B)}{P(B)} = rac{25/100}{30/100} = rac{25}{30} = rac{5}{6} pprox 0.8333$$

## 8. Second Example (Machine Learning Confusion Matrix)
Given binary confusion matrix values: $TP=80, FP=10, FN=20, TN=890$.
- **Precision**: $P(Y=1 \mid \hat{Y}=1) = rac{TP}{TP + FP} = rac{80}{80 + 10} = rac{80}{90} pprox 0.8889$.
- **Recall (Sensitivity)**: $P(\hat{Y}=1 \mid Y=1) = rac{TP}{TP + FN} = rac{80}{80 + 20} = rac{80}{100} = 0.80$.

## 9. Common Mistakes
- Confusing $P(A|B)$ with $P(B|A)$ (Transposition Fallacy).
- Dividing by $P(A)$ instead of conditioning event $P(B)$.

## 10. AI Connection
Every supervised learning classifier estimates $P(Y=y \mid X=x)$, the conditional probability distribution of labels given input features.

## 11. Algorithm Connection
- **Logistic Regression**: Directly models $P(Y=1|X) = \sigma(w^T x + b)$.
- **Decision Trees**: Splits nodes to maximize conditional purity.

## 12. Practical Interpretation
In medical AI, $P(	ext{Disease} \mid 	ext{Positive Test}) 
eq P(	ext{Positive Test} \mid 	ext{Disease})$. Confusing these lead to massive false alarm misinterpretations.

## 13. Interview Insight
**Q**: What is the relationship between $P(A|B)$ and $P(B|A)$?
**A**: They are linked by Bayes' Theorem: $P(A|B) = rac{P(B|A)P(A)}{P(B)}$.

## 14. Summary
Conditional probability updates event likelihoods under new evidence by restricting the sample space to the conditioning event.
