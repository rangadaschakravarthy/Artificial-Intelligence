# Theory — Rules of Probability

## 1. Simple Definition
Probability rules are mathematical laws that allow us to calculate the likelihood of combined events (such as event A OR event B, event A AND event B, or NOT event A).

## 2. Intuition
- **Complement Rule**: If there's a $5\%$ chance of rain, there is a $95\%$ chance of NO rain.
- **Addition Rule (OR)**: Chance of selecting a user who is either a student OR a subscriber.
- **Multiplication Rule (AND)**: Chance that user is a student AND opens an email.

## 3. Mathematical Definition
- **Complement**: $P(A^c) = 1 - P(A)$
- **Addition Rule (General)**: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
- **Addition Rule (Mutually Exclusive)**: $P(A \cup B) = P(A) + P(B)$
- **Multiplication Rule (General)**: $P(A \cap B) = P(A) \cdot P(B|A)$
- **Multiplication Rule (Independent)**: $P(A \cap B) = P(A) \cdot P(B)$

## 4. Notation
- $P(A^c)$: Probability of complement of $A$.
- $P(A \cup B)$ or $P(A 	ext{ or } B)$: Union probability.
- $P(A \cap B)$ or $P(A, B)$ or $P(A 	ext{ and } B)$: Joint probability.
- $P(B|A)$: Conditional probability of $B$ given $A$.

## 5. Formula Summary
$$	ext{Complement: } P(A^c) = 1 - P(A)$$
$$	ext{Addition: } P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
$$	ext{Multiplication: } P(A \cap B) = P(B|A)P(A)$$

## 6. Symbol Explanation
- $\cup$: Union (OR).
- $\cap$: Intersection (AND).
- $|$: Given (Conditioning).

## 7. Step-by-Step Calculation
Given $P(A) = 0.6$, $P(B) = 0.5$, $P(A \cap B) = 0.3$.
- Find $P(A \cup B)$:
  $$P(A \cup B) = 0.6 + 0.5 - 0.3 = 0.8$$
- Find $P(A^c)$:
  $$P(A^c) = 1 - 0.6 = 0.4$$

## 8. Second Example (Ensemble AI Models)
Suppose 3 independent classifiers each have error rate $p = 0.10$. What is the probability that AT LEAST ONE classifier makes an error?
- $P(	ext{No classifier errs}) = (1 - 0.10)^3 = 0.9^3 = 0.729$.
- $P(	ext{At least 1 errs}) = 1 - 0.729 = 0.271 = 27.1\%$.

## 9. Common Mistakes
- Adding probabilities without subtracting $P(A \cap B)$ for non-disjoint events (double counting).
- Multiplying probabilities assuming independence when events are dependent.

## 10. AI Connection
Ensemble learning (Random Forests, Gradient Boosting) leverages independent model predictions to drastically drop joint error probabilities.

## 11. Algorithm Connection
- **Bagging & Random Forests**: Reduces variance by combining outputs of trees trained on bootstrapped data samples.

## 12. Practical Interpretation
Complements simplify "at least one" calculations in reliability engineering and system safety.

## 13. Interview Insight
**Q**: Why do we subtract $P(A \cap B)$ in the Addition Rule?
**A**: Because the elements in $A \cap B$ are counted twice: once inside $P(A)$ and once inside $P(B)$.

## 14. Summary
Probability rules (Complement, Addition, Multiplication) structure complex event combinations into solvable formulas.
