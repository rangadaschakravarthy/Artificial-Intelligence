# Solutions — Naive Bayes Algorithm Mathematics

## Level 1
1. $\hat{y} = rg\max_c [ \ln P(Y=c) + \sum_{i=1}^d \ln P(X_i | Y=c) ]$.
2. To prevent zero-probabilities ($P=0$) from zeroing out entire products for unseen feature words.
3. Gaussian (Normal) distribution $\mathcal{N}(\mu_{c,i}, \sigma_{c,i}^2)$.
4. Multiplying many numbers $< 1$ exceeds double-precision float limits ($< 10^{-308}$), rounding down to exact $0.0$.
5. Bernoulli Naive Bayes.

## Level 2
6. $P(	ext{Spam}) = rac{60}{100} = 0.60, P(	ext{Ham}) = rac{40}{100} = 0.40$.
7. $P = rac{10 + 1}{200 + 1(500)} = rac{11}{700} pprox 0.01571$.
8. $\ln(11/700) = \ln(11) - \ln(700) = 2.3979 - 6.5511 = -4.1532$.
9. $\sigma=2$. $\ln f(12) = -\ln(\sqrt{2\pi \cdot 4}) - rac{(12-10)^2}{2(4)} = -\ln(5.0132) - 0.5 = -1.6121 - 0.5 = -2.1121$.
10. Offset $m = -5.0$. $e^{-5 - (-5)} = 1.0, e^{-7 - (-5)} = e^{-2} pprox 0.1353$. $P(	ext{Spam}|X) = rac{1.0}{1.0 + 0.1353} = rac{1}{1.1353} pprox 0.8808 = 88.08\%$.

## Level 3
11. $\ln P(X|Y=1) - \ln P(X|Y=0) = \sum \left[ -rac{(x_i - \mu_{1,i})^2}{2\sigma_i^2} + rac{(x_i - \mu_{0,i})^2}{2\sigma_i^2} ight] + 	ext{const} = \sum rac{\mu_{1,i} - \mu_{0,i}}{\sigma_i^2} x_i + 	ext{const} = 0$, which is a linear equation in $\mathbf{x}$ ($\mathbf{w}^T \mathbf{x} + b = 0$).
12. When $\sigma_{1,i}^2 
eq \sigma_{0,i}^2$, $x_i^2$ quadratic terms fail to cancel out in $\ln P(X|1) - \ln P(X|0)$, creating quadratic boundary terms $\sum a_i x_i^2 + \sum b_i x_i + c = 0$.
13. $\hat{P}(X_i | c) = rac{N_{c,i} + lpha}{N_c + lpha D}$ for any real $lpha > 0$.
14. Factor out $e^m$: $\ln(e^m (e^{a-m} + e^{b-m})) = \ln(e^m) + \ln(e^{a-m} + e^{b-m}) = m + \ln(e^{a-m} + e^{b-m})$. Since $a-m \le 0$ and $b-m \le 0$, exponents remain $\le 1$, completely avoiding overflow.
15. Training computes single-pass sums for means/counts ($O(Nd)$); inference evaluates $d$ feature log-likelihoods for $K$ classes ($O(dK)$).

## Level 4
16. For each class $c$: $\mu_{c,i} = rac{1}{N_c} \sum_{j \in C_c} X_{j,i}$; $\sigma_{c,i}^2 = rac{1}{N_c} \sum_{j \in C_c} (X_{j,i} - \mu_{c,i})^2$.
17. OOV words not in training vocabulary $D$ are simply ignored during log-likelihood summation ($\sum \ln P(x_i|y)$ skips unknown words).
18. TF-IDF downweights non-informative high-frequency words (e.g. "the", "is"), improving feature likelihood discrimination.
19. $2 	imes K 	imes d$ floats (mean and variance per feature per class) $= 2 	imes 10 	imes 1000 = 20,000$ float values (approx 160 KB).
20. Naive Bayes decision boundary depends on the ratio of joint log-likelihoods. Even if absolute probabilities are biased by feature correlation, the correct class ranking $rg\max$ remains preserved as long as correlated features point in the same direction.

## Level 5
21. $\ln [ P(Y=c) \prod P(X_i|c)^{x_i} ] = \ln P(Y=c) + \sum x_i \ln P(X_i|c) = w_0 + \mathbf{w}^T \mathbf{x}$, which is a linear model.
22. By marginalizing out missing feature $X_m$: $\int P(X_{	ext{obs}}, X_m | Y) dX_m = P(X_{	ext{obs}} | Y) \int P(X_m | Y) dX_m = P(X_{	ext{obs}} | Y) (1)$. Missing features simply drop out of the log-likelihood sum.
23.
```python
class GaussianNB:

  def fit(self, X, y):
    self.classes = np.unique(y)
    self.means = np.array([X[y == c].mean(axis=0) for c in self.classes])
    self.vars = np.array([X[y == c].var(axis=0) for c in self.classes])
    self.priors = np.array([np.mean(y == c) for c in self.classes])

  def predict(self, X):
    log_posts = []
    for i, c in enumerate(self.classes):
      log_prior = np.log(self.priors[i])
      log_lik = -0.5 * np.sum(
          np.log(2 * np.pi * self.vars[i])
          + ((X - self.means[i]) ** 2) / self.vars[i],
          axis=1,
      )
      log_posts.append(log_prior + log_lik)
    return self.classes[np.argmax(np.array(log_posts), axis=0)]
```
