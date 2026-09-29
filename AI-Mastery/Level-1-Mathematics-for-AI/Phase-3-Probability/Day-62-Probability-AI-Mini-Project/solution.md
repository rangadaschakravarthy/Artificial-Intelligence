# Solutions — Probability AI Mini-Project

## Level 1
1. Prevents zero-probabilities for unseen words from multiplying total document probability to zero.
2. Prevents floating point numerical underflow when multiplying hundreds of small float probabilities.
3. Incorporates baseline population default frequency before observing specific borrower risk events.
4. Area Under the ROC Curve (ROC-AUC).
5. Precision $= \frac{	ext{True Spam}}{	ext{Total Flagged Spam}}$; Recall $= \frac{	ext{True Spam}}{	ext{Total Actual Spam}}$.

## Level 2
6. $P = \frac{40 + 1}{2000 + 1000} = \frac{41}{3000} pprox 0.01367$.
7. $\ln(41/3000) = \ln(41) - \ln(3000) = 3.7135 - 8.0064 = -4.2929$.
8. Prior Odds $= 0.05/0.95 pprox 0.05263$. Posterior Odds $= 0.05263 	imes 10 = 0.5263$. Posterior $P = \frac{0.5263}{1.5263} pprox 0.3448 = 34.48\%$.
9. Loss $= -\frac{1}{4} [\ln(0.9) + \ln(0.8) + \ln(0.9) + \ln(0.8)] = -\frac{1}{4} [-0.1054 - 0.2231 - 0.1054 - 0.2231] = 0.1643$.
10. Correct: 3 out of 4 $\implies$ Accuracy $= 0.75 = 75\%$.

## Level 3
11. Preprocessing reduces noisy duplicate entries, shrinking vocabulary size $D$, reducing Laplace smoothing denominator inflation, and sharpening word likelihoods.
12. Sum $= \sum_{i=1}^D \frac{N_{c,i} + 1}{N_c + D} = \frac{\sum N_{c,i} + \sum 1}{N_c + D} = \frac{N_c + D}{N_c + D} = 1.0$.
13. $P(H|E_1, E_2) \propto P(H) P(E_1|H) P(E_2|H)$. Updating with $E_1$ gives prior for $E_2$ as $P(H|E_1) \propto P(H)P(E_1|H)$. Multiplying by $E_2$ likelihood gives $P(H)P(E_1|H)P(E_2|H)$, identical to simultaneous update.
14. False positives in spam filter put important user emails into Spam folder (high cost). Precision must be high ($>99\%$) to avoid misclassifying legitimate emails.
15. False negatives in medical AI leave life-threatening diseases undetected (fatal cost). Recall must be near $100\%$ to catch all potential cases.

## Level 4
16–20. Fully implemented and demonstrated in `code.py`.

## Level 5
21. Full theoretical step derivation matching Day 60 and Day 62 theory document.
22. OOV tokens are safely skipped during log-likelihood summation, leaving prior and observed vocabulary scores intact.
23. Executing `code.py` produces clean $100\%$ test accuracy on sample data and outputs detailed Bayesian risk scores.
