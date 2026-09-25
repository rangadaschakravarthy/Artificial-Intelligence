# Day 77 Practice Questions: Maximum Likelihood Estimation (MLE)

## Level 1: Basic Concepts
1. What is Maximum Likelihood Estimation?
2. Why do we work with Log-Likelihood instead of Likelihood?
3. What is the difference between Probability and Likelihood?
4. What is Negative Log-Likelihood (NLL)?
5. What ML loss function corresponds to MLE under Gaussian noise assumption?

## Level 2: Calculation
6. Derive MLE for Bernoulli success probability p given k successes in n trials.
7. Derive MLE for Exponential rate parameter λ given sample sum x_i = 50 and n = 10.
8. Compute log-likelihood for Bernoulli data [1, 1, 0, 1] given p = 0.75.
9. Show that d/dλ [ n ln λ - λ sum x_i ] = 0 yields λ_hat = 1 / x_bar.
10. Derive MLE for Uniform distribution U(0, θ) given sample [2, 5, 8, 3, 9].

## Level 3: Conceptual & Proofs
11. Prove that maximizing Gaussian Log-Likelihood is equivalent to minimizing MSE loss.
12. Prove that maximizing Bernoulli Log-Likelihood is equivalent to minimizing Binary Cross-Entropy.
13. Explain asymptotic properties of MLE: Consistency, Asymptotic Normality, Asymptotic Efficiency.
14. Show why MLE estimator for Gaussian variance σ^2 is biased: σ^2_MLE = (1/n) sum (x_i - x_bar)^2.
15. Contrast MLE vs MAP (Maximum A Posteriori) estimation.

## Level 4: AI Applications
16. How does MLE connect probability distribution assumptions to neural network loss functions?
17. Why is Cross-Entropy preferred over MSE for classification tasks?
18. How is MLE used in training Gaussian Mixture Models (GMMs) via EM algorithm?
19. How does adding L2 regularization to MLE correspond to MAP estimation with Gaussian prior?
20. Why does MLE suffer from overfitting in small sample datasets?

## Level 5: Interview Questions
21. "Derive MLE for Gaussian parameters μ and σ^2 simultaneously."
22. "Write Python code optimizing Negative Log-Likelihood of a custom distribution using `scipy.optimize.minimize`."
23. "Explain why MAP = MLE + Log-Prior."
