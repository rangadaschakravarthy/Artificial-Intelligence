# Practice Problems — Probability for Machine Learning

## Level 1: Basic Concept Checks
1. Define Maximum Likelihood Estimation (MLE).
2. What is the fundamental difference between MLE and MAP?
3. Which loss function is derived from Bernoulli log-likelihood?
4. Which loss function is derived from Gaussian log-likelihood?
5. State the main structural difference between Generative and Discriminative models.

## Level 2: Direct Calculations
6. Given 5 coin flips: $H, H, H, T, H$. Compute $\hat{p}_{MLE}$.
7. For predicted probability $\hat{y} = 0.90$ when true label $y = 0$, compute BCE loss.
8. For true class 3 in a 4-class problem with predicted Softmax $q = [0.05, 0.05, 0.80, 0.10]$, compute Categorical Cross-Entropy.
9. Given sample dataset $\{2, 4, 6\}$ drawn from $\mathcal{N}(\mu, 1)$, compute $\hat{\mu}_{MLE}$.
10. In Q9, compute total sample log-likelihood at $\mu = 4$.

## Level 3: Conceptual & Multi-Step Problems
11. Derive the MLE estimate $\hat{\mu}_{MLE}$ for a Normal distribution $\mathcal{N}(\mu, \sigma^2)$ with known $\sigma^2$.
12. Derive the MLE estimate $\hat{\sigma}^2_{MLE}$ for a Normal distribution with known $\mu$.
13. Show that $L_1$ regularization (Lasso) corresponds to MAP estimation under a Laplacian prior $P(w) \propto \exp(-\gamma |w|)$.
14. Show that maximizing Likelihood $L(	heta)$ is equivalent to maximizing Log-Likelihood $\ln L(	heta)$ because $\ln$ is a strictly monotonically increasing function.
15. Explain how expected calibration error (ECE) measures whether a model's predicted confidence $0.80$ matches true accuracy $80\%$.

## Level 4: AI & ML Applications
16. In Logistic Regression, sigmoid $\sigma(z) = rac{1}{1 + e^{-z}}$. Compute derivative $rac{d\sigma}{dz}$ in terms of $\sigma(z)$.
17. Show that gradient of BCE loss $L = -[y \ln \hat{y} + (1-y) \ln(1-\hat{y})]$ w.r.t logit $z$ simplifies to $(\hat{y} - y)$.
18. Explain why Softmax + Cross-Entropy loss avoids vanishing gradients during neural network training compared to MSE + Sigmoid.
19. Classify the following models as Generative or Discriminative: 1) Logistic Regression, 2) Naive Bayes, 3) Linear Discriminant Analysis (LDA), 4) Support Vector Machine (SVM).
20. In temperature scaling for neural network calibration $q_i = rac{e^{z_i / T}}{\sum e^{z_j / T}}$, what happens when $T > 1$?

## Level 5: Interview Questions
21. Prove that minimizing Cross-Entropy $H(p, q) = -\sum p(x) \log q(x)$ is mathematically equivalent to minimizing KL Divergence $D_{KL}(p \parallel q)$.
22. Derive MAP estimate for Bernoulli parameter $p$ with Beta$(lpha, eta)$ prior, showing $\hat{p}_{MAP} = rac{k + lpha - 1}{N + lpha + eta - 2}$.
23. Write Python code using `scipy.optimize` to find MLE parameters for a custom distribution.
