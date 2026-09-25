# Practice Problems — Naive Bayes Algorithm Mathematics

## Level 1: Basic Concept Checks
1. State the main decision rule formula for Naive Bayes in log-space.
2. Why is Laplace smoothing necessary in Multinomial Naive Bayes?
3. What distribution does Gaussian Naive Bayes assume for continuous features?
4. What happens when floating point underflow occurs during probability multiplication?
5. Which Naive Bayes variant is suitable for binary presence/absence word features?

## Level 2: Direct Calculations
6. In a dataset with 60 Spam and 40 Ham emails, calculate prior probabilities $P(	ext{Spam})$ and $P(	ext{Ham})$.
7. Word count in Spam $N_{	ext{Spam}} = 200$. Word "deal" appears 10 times. Vocabulary $D = 500$. Compute Laplace smoothed probability $P(	ext{"deal"}|	ext{Spam})$ with $lpha=1$.
8. Compute log-likelihood $\ln P(	ext{"deal"}|	ext{Spam})$ using Q7.
9. For $X \sim \mathcal{N}(10, 4)$ (so $\mu=10, \sigma^2=4$), compute log-likelihood $\ln f(12)$.
10. Given log posterior scores $S_{	ext{Spam}} = -5.0$ and $S_{	ext{Ham}} = -7.0$, calculate normalized $P(	ext{Spam}|X)$.

## Level 3: Conceptual & Multi-Step Problems
11. Show that the decision boundary of Gaussian Naive Bayes with equal variances $\sigma_{0,i}^2 = \sigma_{1,i}^2 = \sigma^2$ is a linear hyperplane.
12. Show that Gaussian Naive Bayes with unequal class variances yields a quadratic decision boundary.
13. Derive the formula for Lidstone smoothing (add-$lpha$ smoothing where $lpha > 0$).
14. Show how Log-Sum-Exp identity $\ln(e^a + e^b) = m + \ln(e^{a-m} + e^{b-m})$ where $m = \max(a,b)$ prevents numerical underflow.
15. Explain why Naive Bayes is computationally efficient during both training ($O(N d)$) and inference ($O(d K)$).

## Level 4: AI & ML Applications
16. Implement Gaussian Naive Bayes fit equations for sample means $\mu_{c,i}$ and sample variances $\sigma_{c,i}^2$ given class data subsets.
17. Explain how Out-Of-Vocabulary (OOV) words are handled during Naive Bayes testing.
18. In text classification, why is TF-IDF scaling sometimes combined with Multinomial Naive Bayes?
19. Compute memory requirement of storing a Gaussian Naive Bayes model for $K=10$ classes and $d=1000$ features.
20. Why does Naive Bayes perform well on spam filtering even when words like "viagra" and "cheap" are correlated?

## Level 5: Interview Questions
21. Prove that Multinomial Naive Bayes defines a linear classifier in log-space.
22. How does Naive Bayes handle missing feature values during inference?
23. Write Python NumPy code from scratch to implement Gaussian Naive Bayes `fit(X, y)` and `predict(X)`.
