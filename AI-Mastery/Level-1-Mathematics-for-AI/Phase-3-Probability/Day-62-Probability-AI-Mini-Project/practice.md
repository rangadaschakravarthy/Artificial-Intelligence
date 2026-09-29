# Practice Problems — Probability AI Mini-Project

## Level 1: Basic Concept Checks
1. Why is Laplace smoothing essential for text classification?
2. Why are log-probabilities used instead of raw probabilities during text classification?
3. What is the role of prior probabilities in credit risk assessment?
4. What matrix metric evaluates binary classifier performance across all threshold values?
5. Define Precision and Recall in terms of Spam classification outcomes.

## Level 2: Direct Calculations
6. Given 100 Spam emails with 2,000 total words and vocabulary size $D=1,000$. Word "click" appears 40 times. Compute Laplace smoothed $P(	ext{"click"}|	ext{Spam})$.
7. For Q6, compute log-likelihood $\ln P(	ext{"click"}|	ext{Spam})$.
8. Base risk $P(D) = 0.05$. Observed event with likelihood ratio 10. Compute posterior default probability.
9. If model predicts $[0.9, 0.8, 0.1, 0.2]$ for true labels $[1, 1, 0, 0]$, compute binary cross-entropy loss.
10. Compute accuracy for predictions $[1, 1, 0, 1]$ against ground truth $[1, 1, 0, 0]$.

## Level 3: Conceptual & Multi-Step Problems
11. Explain how text preprocessing (lowercasing, punctuation removal) affects vocabulary size $D$ and Laplace smoothing denominators.
12. Show that Laplace smoothed probability $\frac{N_{c,i} + 1}{N_c + D}$ sums to 1 across all $D$ words in vocabulary.
13. Prove that updating posterior probability sequentially with independent evidence yields the exact same result as updating with all evidence simultaneously.
14. Explain why high Precision is prioritized over High Recall in email spam filtering (avoiding moving legitimate emails to spam).
15. Explain why high Recall is prioritized over High Precision in medical disease diagnosis.

## Level 4: AI & ML Applications
16. Implement Bag-of-Words text vectorization in Python.
17. Implement Multinomial Naive Bayes fit and predict in Python.
18. Implement Bayesian credit risk updating function in Python.
19. Compute confusion matrix metrics ($TP, FP, FN, TN$) in Python.
20. Explain how the mini-project pipeline scales to real-world industrial text classifiers.

## Level 5: Interview Questions
21. Walk through the complete mathematical derivation of Multinomial Naive Bayes from Bayes' Theorem to final log-score code.
22. How would you handle out-of-vocabulary (OOV) tokens encountered during production inference?
23. Run the complete `code.py` mini-project script and report training and test accuracy metrics.
