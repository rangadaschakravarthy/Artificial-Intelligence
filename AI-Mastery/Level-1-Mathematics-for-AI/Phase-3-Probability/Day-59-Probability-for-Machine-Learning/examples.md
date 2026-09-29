# Worked Examples — Probability for Machine Learning

## Example 1: MLE for Exponential Distribution
**Problem**: Given sample dataset $x_1, \dots, x_N$ from Exponential distribution $f(x) = \lambda e^{-\lambda x}$. Derive MLE estimate $\hat{\lambda}_{MLE}$.
**Solution**:
1. Likelihood $L(\lambda) = \prod_{i=1}^N \lambda e^{-\lambda x_i} = \lambda^N \exp\left(-\lambda \sum_{i=1}^N x_i
ight)$.
2. Log-Likelihood: $\ln L(\lambda) = N \ln(\lambda) - \lambda \sum_{i=1}^N x_i$.
3. Derivative: $\frac{d}{d\lambda} \ln L = \frac{N}{\lambda} - \sum_{i=1}^N x_i = 0$.
4. $\hat{\lambda}_{MLE} = \frac{N}{\sum_{i=1}^N x_i} = \frac{1}{ar{X}}$ (Inverse sample mean!).

## Example 2: Deriving BCE Loss for 1 Sample
**Problem**: True label $y = 1$, predicted probability $\hat{y} = 0.85$. Calculate Binary Cross-Entropy loss.
**Solution**:
1. BCE $= -[y \ln(\hat{y}) + (1-y) \ln(1-\hat{y})]$.
2. For $y=1$: BCE $= -\ln(0.85) pprox 0.1625$.

## Example 3: MAP Estimation with Beta Prior (Bernoulli)
**Problem**: Flip coin $N=10$ times, get $k=7$ Heads. Assume Beta prior $P(p) \propto p^{lpha-1} (1-p)^{eta-1}$ with $lpha=2, eta=2$ (smooth prior). Compute $\hat{p}_{MAP}$.
**Solution**:
1. Posterior $P(p | k) \propto p^{k + lpha - 1} (1-p)^{N - k + eta - 1} = p^{7+2-1} (1-p)^{3+2-1} = p^8 (1-p)^4$.
2. Mode of Beta distribution $	ext{Beta}(a, b)$ is $\frac{a-1}{a+b-2}$.
3. Here $a = 9, b = 5 \implies \hat{p}_{MAP} = \frac{9-1}{9+5-2} = \frac{8}{12} = \frac{2}{3} pprox 0.6667$.
4. (Compare with MLE $\hat{p}_{MLE} = 7/10 = 0.70$; prior pulled estimate slightly toward 0.5!).

## Example 4: Categorical Cross-Entropy (3 Classes)
**Problem**: Target class $y = [0, 1, 0]^T$. Predicted Softmax $q = [0.15, 0.75, 0.10]^T$. Compute Cross-Entropy loss.
**Solution**:
1. $L = -\sum_{i=1}^3 y_i \ln q_i = -\ln q_2 = -\ln(0.75) pprox 0.2877$.

## Example 5: Discriminative vs Generative Parameter Count
**Problem**: Dataset has $d=10$ binary features and binary target $Y$. Compare parameter count for Discriminative Logistic Regression vs Generative Naive Bayes.
**Solution**:
1. Logistic Regression: 10 weight parameters $w_i$ + 1 bias $b = 11$ parameters.
2. Naive Bayes: $2 	imes 10 = 20$ feature likelihoods + 1 prior $P(Y=1) = 21$ parameters.
