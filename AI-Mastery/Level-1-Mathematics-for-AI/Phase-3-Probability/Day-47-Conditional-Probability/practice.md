# Practice Problems — Conditional Probability

## Level 1: Basic Concept Checks
1. Write the mathematical definition formula for $P(A|B)$.
2. What restriction must apply to $P(B)$ in $P(A|B)$?
3. What is $P(A|B)$ if $A$ and $B$ are mutually exclusive?
4. What is $P(A|B)$ if $B \subseteq A$?
5. If $P(A \cap B) = 0.12$ and $P(B) = 0.40$, compute $P(A|B)$.

## Level 2: Direct Calculations
6. Roll a fair die. Given roll is $> 2$, find probability roll is even.
7. Cards: Given drawn card is Black, find probability it is an Ace.
8. If $P(A) = 0.5$, $P(B) = 0.6$, $P(A \cup B) = 0.8$, find $P(A|B)$.
9. In Q8, find $P(B|A)$.
10. A bag has 4 red and 6 blue chips. Draw 2 chips without replacement. Find probability 2nd chip is red given 1st was red.

## Level 3: Conceptual & Multi-Step Problems
11. Show that $P(A \cap B \cap C) = P(A) P(B|A) P(C | A \cap B)$ (Chain Rule of Probability).
12. If $P(A|B) > P(A)$, what does this say about the relationship between $A$ and $B$?
13. In a cohort, $60\%$ pass Math, $50\%$ pass Physics, and $30\%$ pass both. Find probability a student passes Physics given they passed Math.
14. In Q13, find probability a student passes Math given they failed Physics.
15. Prove that $P(A^c | B) = 1 - P(A|B)$.

## Level 4: AI & ML Applications
16. Given confusion matrix: $TP=150, FP=50, FN=25, TN=775$. Calculate Precision $P(Y=1|\hat{Y}=1)$.
17. Calculate Recall $P(\hat{Y}=1|Y=1)$ for the confusion matrix in Q16.
18. Compute Specificity $P(\hat{Y}=0|Y=0)$ for the confusion matrix in Q16.
19. A self-driving vision system detects pedestrians with Recall 0.98. If 100 pedestrians cross, how many are expected to be detected?
20. Explain why high accuracy can be misleading when conditional probabilities $P(Y=1)$ (class prevalence) are heavily imbalanced (e.g. 0.001).

## Level 5: Interview Questions
21. What is the Transposition Fallacy (Prosecutor's Fallacy)? Give an AI context example.
22. Derive the Chain Rule of Probability for $n$ variables $P(X_1, X_2, \dots, X_n)$.
23. How does conditional probability form the foundation of Auto-regressive Language Models like GPT ($P(w_t \mid w_1, w_2, \dots, w_{t-1})$)?
