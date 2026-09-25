# Practice Problems — Conditional Independence

## Level 1: Basic Concept Checks
1. Write the mathematical definition of $X \perp \!\!\! \perp Y \mid Z$.
2. State the Naive Bayes assumption for $d$ features $X_1, \dots, X_d$ given target $Y$.
3. True or False: If $X$ and $Y$ are conditionally independent given $Z$, they are guaranteed to be marginally independent.
4. What is a "Collider" structure in a Bayesian network graph?
5. How does conditioning on a Collider affect the independence of its parent variables?

## Level 2: Direct Calculations
6. Given $P(X=1|Z=1) = 0.3$, $P(Y=1|Z=1) = 0.7$. If $X \perp \!\!\! \perp Y \mid Z$, compute $P(X=1, Y=1 | Z=1)$.
7. Given $P(X=1|Z=0) = 0.1$, $P(Y=1|Z=0) = 0.2$. Compute $P(X=1, Y=0 | Z=0)$ under conditional independence.
8. In Naive Bayes with $P(	ext{Spam})=0.3$, $P(X_1=1|	ext{Spam})=0.9$, $P(X_2=1|	ext{Spam})=0.8$. Compute joint likelihood $P(X_1=1, X_2=1, 	ext{Spam})$.
9. In a Markov Chain $X_1 ightarrow X_2 ightarrow X_3$, simplify $P(X_3 | X_2, X_1)$.
10. For 10 binary features, how many conditional probability parameters does Naive Bayes store per class?

## Level 3: Conceptual & Multi-Step Problems
11. Prove that $X \perp \!\!\! \perp Y \mid Z \iff P(X | Y, Z) = P(X | Z)$.
12. Give a real-world example of two variables that are marginally independent but conditionally dependent given a third variable.
13. Give a real-world example of two variables that are marginally dependent but conditionally independent given a third variable.
14. Explain the concept of "Explaining Away" in Bayesian networks with a 3-variable example.
15. Show that $P(X, Y, Z) = P(Z) P(X|Z) P(Y|Z)$ for a Common Cause graph $X \leftarrow Z ightarrow Y$.

## Level 4: AI & ML Applications
16. In Naive Bayes, write the full expression for $P(Y=1 | X_1, \dots, X_d)$ using Bayes' Theorem and conditional independence.
17. Explain why Naive Bayes is called "Naive".
18. In Gaussian Naive Bayes, continuous feature distributions $P(X_i | Y=y) \sim \mathcal{N}(\mu_{y,i}, \sigma_{y,i}^2)$ are modeled. How many parameters are fit per feature per class?
19. In NLP text classification (Bag of Words), why does the Naive Bayes assumption break for phrases like "not bad"?
20. In Hidden Markov Models (HMM), state the two conditional independence assumptions.

## Level 5: Interview Questions
21. Define d-separation rules for: 1) Chain, 2) Common Cause, 3) Collider.
22. Why does Naive Bayes often produce over-confident (pushed to 0 or 1) posterior probabilities when features are correlated?
23. Write Python code to calculate Naive Bayes log-posterior scores for a 3-feature test sample.
