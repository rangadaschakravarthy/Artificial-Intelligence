# Practice Problems — Bayes' Theorem

## Level 1: Basic Concept Checks
1. Write Bayes' Theorem formula for events $A$ and $B$.
2. Name the four component terms in Bayes' Theorem.
3. What is the Law of Total Probability used for in Bayes' Theorem?
4. Define Likelihood in probability terminology.
5. What happens to the Posterior if the Evidence $P(E) = 1$?

## Level 2: Direct Calculations
6. Given $P(A) = 0.3$, $P(B|A) = 0.8$, $P(B) = 0.4$, calculate $P(A|B)$.
7. Given $P(H) = 0.5$, $P(E|H) = 0.9$, $P(E|H^c) = 0.1$, compute $P(H|E)$.
8. $P(	ext{Spam}) = 0.20$. $P(	ext{Word}|	ext{Spam}) = 0.50$. $P(	ext{Word}|	ext{Ham}) = 0.05$. Find $P(	ext{Spam}|	ext{Word})$.
9. A test for condition $X$ has sensitivity 0.90 and specificity 0.90. If prevalence is 0.10, compute $P(X|+)$.
10. In Q9, compute $P(X^c|-)$ (Negative Predictive Value).

## Level 3: Conceptual & Multi-Step Problems
11. Prove Bayes' Theorem starting from the definition of conditional probability.
12. Explain the Base Rate Fallacy with a numerical counter-example.
13. Three factories $F_1, F_2, F_3$ produce $50\%, 30\%, 20\%$ of chips with defect rates $1\%, 2\%, 5\%$. Find $P(F_3 | 	ext{Defect})$.
14. Show how Bayes' Theorem can be expressed in Odds form: $	ext{Posterior Odds} = 	ext{Prior Odds} 	imes 	ext{Likelihood Ratio}$.
15. If Prior $P(H) = 0.01$ and Likelihood Ratio $\frac{P(E|H)}{P(E|H^c)} = 100$, compute Posterior $P(H|E)$.

## Level 4: AI & ML Applications
16. A credit card fraud model has prior $P(	ext{Fraud}) = 0.002$. High amount feature has $P(	ext{High}|	ext{Fraud}) = 0.80$, $P(	ext{High}|	ext{Legit}) = 0.05$. Calculate $P(	ext{Fraud}|	ext{High})$.
17. In Naive Bayes classification with two features $X_1, X_2$ independent given $Y$, write the formula for $P(Y=1|X_1, X_2)$.
18. A self-driving car LiDAR sees object shape: $P(	ext{Pedestrian}) = 0.05$. $P(	ext{Shape}|	ext{Pedestrian}) = 0.90$, $P(	ext{Shape}|	ext{Pole}) = 0.10$. Find $P(	ext{Pedestrian}|	ext{Shape})$.
19. Explain Maximum Likelihood Estimation (MLE) vs Maximum A Posteriori (MAP) estimation.
20. In MAP estimation, what happens when we assume a uniform (flat) Prior distribution?

## Level 5: Interview Questions
21. Derive the Naive Bayes decision rule from Bayes' Theorem.
22. Why is the denominator $P(E)$ often ignored in MAP classification algorithms?
23. How does Bayesian updating naturally allow continuous online learning as new data arrives?
