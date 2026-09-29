# Theory — Probability for Machine Learning

## 1. Simple Definition
Machine Learning is fundamentally applied probability: algorithms fit parameters $	heta$ to data $\mathcal{D}$ to predict target conditional probabilities $P(Y | X; 	heta)$ or estimate joint data distributions $P(X, Y; 	heta)$.

## 2. Intuition
When a model makes a prediction, it chooses parameters $	heta$ that make the observed training data as likely as possible (Maximum Likelihood Estimation).

## 3. Mathematical Foundations
- **Maximum Likelihood Estimation (MLE)**:
  

$$
\hat{	heta}_{MLE} = rg\max_{	heta} P(\mathcal{D} \mid 	heta) = rg\max_{	heta} \sum_{i=1}^N \ln P(y_i \mid x_i; 	heta)
$$

- **Maximum A Posteriori (MAP)**:
  $$\hat{	heta}_{MAP} = rg\max_{	heta} P(	heta \mid \mathcal{D}) = rg\max_{	heta} \left[ \sum_{i=1}^N \ln P(y_i \mid x_i; 	heta) + \ln P(	heta) 
ight]$$

## 4. Deriving Loss Functions
1. **Bernoulli Likelihood $\implies$ Binary Cross-Entropy (BCE)**:
   

$$
P(y \mid x) = \hat{y}^y (1 - \hat{y})^{1-y}
$$

   $$-\ln P(y \mid x) = -\left[ y \ln \hat{y} + (1-y) \ln(1 - \hat{y}) 
ight]$$
2. **Gaussian Likelihood $\implies$ Mean Squared Error (MSE)**:
   $$P(y \mid x) = \frac{1}{\sqrt{2\pi \sigma^2}} \exp\left( -\frac{(y - f(x))^2}{2\sigma^2} 
ight)$$
   

$$
-\ln P(y \mid x) = 	ext{const} + \frac{1}{2\sigma^2} (y - f(x))^2 \propto 	ext{MSE}
$$

## 5. Notation
- $\mathcal{D} = \{(x_i, y_i)\}_{i=1}^N$: Training dataset.
- $\hat{	heta}_{MLE}$: MLE parameter estimate.
- $\hat{	heta}_{MAP}$: MAP parameter estimate.

## 6. Step-by-Step MLE Derivation (Coin Flip)
Flips: $N$ total, $k$ Heads. Likelihood $L(p) = p^k (1-p)^{N-k}$.
1. Log-Likelihood: $\ln L(p) = k \ln(p) + (N-k) \ln(1-p)$.
2. Derivative w.r.t $p$: $\frac{d}{dp} \ln L(p) = \frac{k}{p} - \frac{N-k}{1-p} = 0$.
3. Clear denominators: $k(1-p) - (N-k)p = 0 \implies k - kp - Np + kp = 0 \implies k = Np$.
4. $\hat{p}_{MLE} = \frac{k}{N}$ (Empirical proportion of Heads!).

## 7. Discriminative vs Generative Models
- **Discriminative Models**: Learn $P(Y|X)$ directly (Logistic Regression, Neural Networks, SVMs).
- **Generative Models**: Learn joint $P(X, Y) = P(X|Y) P(Y)$ and use Bayes' Theorem (Naive Bayes, GMMs, VAEs, GANs).

## 8. Common Mistakes
- Thinking raw confidence scores from neural networks are calibrated probabilities (modern deep networks are often overconfident!).
- Forgetting that weight regularization ($L_2$ Ridge, $L_1$ Lasso) is mathematically identical to MAP priors (Gaussian prior $\implies L_2$, Laplacian prior $\implies L_1$).

## 9. AI Connection
$L_2$ Regularization $\lambda \|\mathbf{w}\|^2_2$ is mathematically derived from MAP estimation assuming a Gaussian prior $\mathbf{w} \sim \mathcal{N}(0, 	au^2 \mathbf{I})$.

## 10. Algorithm Connection
- **Logistic Regression**: Minimizes BCE loss via SGD.
- **Ridge Regression**: Minimizes MSE + $L_2$ penalty (MAP estimate).

## 11. Practical Interpretation
Interpreting loss functions as negative log-likelihoods allows principled extension to custom loss metrics (e.g. Huber loss, Focal loss).

## 12. Interview Insight
**Q**: Prove that $L_2$ regularization corresponds to a Gaussian prior on parameters $\mathbf{w}$.
**A**: $\hat{\mathbf{w}}_{MAP} = rg\max [ \ln P(\mathcal{D}|\mathbf{w}) + \ln P(\mathbf{w}) ]$. For Gaussian prior $P(\mathbf{w}) \propto \exp(-\frac{\|\mathbf{w}\|^2}{2	au^2})$, $\ln P(\mathbf{w}) = -\frac{1}{2	au^2} \|\mathbf{w}\|^2 + 	ext{const}$. Adding this to negative log-likelihood yields $	ext{Loss} + \lambda \|\mathbf{w}\|^2$.

## 13. Summary
Machine learning training is Maximum Likelihood / MAP optimization; BCE and MSE losses are Negative Log-Likelihoods.
