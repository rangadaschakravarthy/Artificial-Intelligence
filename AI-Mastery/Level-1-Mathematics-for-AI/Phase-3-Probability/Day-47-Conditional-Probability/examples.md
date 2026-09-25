# Worked Examples — Conditional Probability

## Example 1: Dice Rolling with Condition
**Problem**: A fair 6-sided die is rolled. Given that the roll is even, what is the probability that it is a 6?
**Solution**:
1. $\Omega = \{1, 2, 3, 4, 5, 6\}$.
2. Condition event $B = 	ext{Even} = \{2, 4, 6\} \implies P(B) = rac{3}{6}$.
3. Target event $A = \{6\}$. $A \cap B = \{6\} \implies P(A \cap B) = rac{1}{6}$.
4. $P(A|B) = rac{P(A \cap B)}{P(B)} = rac{1/6}{3/6} = rac{1}{3} pprox 0.3333$.

## Example 2: Contingency Table (User Churn)
**Problem**: In a SaaS company dataset of 1000 users:
- 200 users submitted a support ticket ($B$).
- 100 users churned ($A$).
- 80 users submitted a ticket AND churned ($A \cap B$).
Find the probability a user churns given they submitted a support ticket.
**Solution**:
1. $P(B) = rac{200}{1000} = 0.20$.
2. $P(A \cap B) = rac{80}{1000} = 0.08$.
3. $P(	ext{Churn} \mid 	ext{Ticket}) = rac{0.08}{0.20} = 0.40 = 40\%$.

## Example 3: Card Selection
**Problem**: Draw 1 card from a 52-card deck. Given the card is a Red card, what is the probability it is a King?
**Solution**:
1. $P(	ext{Red}) = rac{26}{52} = 0.5$.
2. $P(	ext{King AND Red}) = rac{2}{52}$ (King of Hearts, King of Diamonds).
3. $P(	ext{King} \mid 	ext{Red}) = rac{2/52}{26/52} = rac{2}{26} = rac{1}{13} pprox 0.0769$.

## Example 4: ML Classifier Precision & Recall
**Problem**: An AI model evaluated on 500 samples gives: $TP=100, FP=20, FN=30, TN=350$. Calculate Precision $P(Y=1 | \hat{Y}=1)$ and False Alarm Rate $P(\hat{Y}=1 | Y=0)$.
**Solution**:
1. Precision $= rac{TP}{TP + FP} = rac{100}{100 + 20} = rac{100}{120} = 0.8333$.
2. False Positive Rate (FPR) $= rac{FP}{FP + TN} = rac{20}{20 + 350} = rac{20}{370} pprox 0.0541$.

## Example 5: Multi-Step Conditional Tree
**Problem**: Box 1 has 3 Red, 2 Blue balls. Box 2 has 1 Red, 4 Blue balls. Pick a box at random ($P(	ext{Box 1}) = 0.5$) and draw a ball. Given ball is Red, find probability it came from Box 1.
**Solution**:
1. $P(R | 	ext{Box 1}) = 3/5 = 0.60$. $P(R | 	ext{Box 2}) = 1/5 = 0.20$.
2. Total $P(R) = P(R | 	ext{Box 1})P(	ext{Box 1}) + P(R | 	ext{Box 2})P(	ext{Box 2}) = (0.60)(0.5) + (0.20)(0.5) = 0.30 + 0.10 = 0.40$.
3. $P(	ext{Box 1} | R) = rac{P(R \cap 	ext{Box 1})}{P(R)} = rac{0.30}{0.40} = 0.75$.
