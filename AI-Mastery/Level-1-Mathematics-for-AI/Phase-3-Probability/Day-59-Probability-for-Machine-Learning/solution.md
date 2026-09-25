# Solutions — Probability for Machine Learning

## Level 1
1. Parameter estimation method that finds $	heta$ maximizing observed data probability $P(\mathcal{D}|	heta)$.
2. MLE maximizes data likelihood $P(\mathcal{D}|	heta)$; MAP incorporates a prior $P(	heta)$ over parameters: $\max P(\mathcal{D}|	heta)P(	heta)$.
3. Binary Cross-Entropy (BCE) loss.
4. Mean Squared Error (MSE) loss.
5. Discriminative models learn $P(Y|X)$; Generative models learn joint $P(X,Y)$.

## Level 2
6. $k = 4, N = 5 \implies \hat{p}_{MLE} = rac{4}{5} = 0.80$.
7. For $y=0$: BCE $= -\ln(1 - 0.90) = -\ln(0.10) pprox 2.3026$.
8. True class index 3 (value $0.80$): Loss $= -\ln(0.80) pprox 0.2231$.
9. $\hat{\mu}_{MLE} = ar{X} = rac{2 + 4 + 6}{3} = 4.0$.
10. Residuals at $\mu=4$: $(2-4)^2 + (4-4)^2 + (6-4)^2 = 4 + 0 + 4 = 8$. Log-Likelihood $= -rac{3}{2}\ln(2\pi) - rac{8}{2} = -2.7568 - 4 = -6.7568$.

## Level 3
11. $\ln L(\mu) = -rac{N}{2}\ln(2\pi\sigma^2) - rac{1}{2\sigma^2}\sum(x_i - \mu)^2$. $rac{d}{d\mu}\ln L = rac{1}{\sigma^2}\sum(x_i - \mu) = 0 \implies \sum x_i - N\mu = 0 \implies \hat{\mu} = rac{1}{N}\sum x_i$.
12. $rac{d}{d\sigma^2}\ln L = -rac{N}{2\sigma^2} + rac{1}{2(\sigma^2)^2}\sum(x_i - \mu)^2 = 0 \implies \hat{\sigma}^2_{MLE} = rac{1}{N}\sum_{i=1}^N (x_i - \mu)^2$.
13. $\hat{\mathbf{w}}_{MAP} = rg\max [ \ln P(\mathcal{D}|\mathbf{w}) + \ln P(\mathbf{w}) ]$. For Laplacian prior $P(\mathbf{w}) = \prod rac{\gamma}{2} e^{-\gamma |w_j|}$, $\ln P(\mathbf{w}) = -\gamma \sum |w_j| + 	ext{const} = -\gamma \|\mathbf{w}\|_1 + 	ext{const}$, yielding $L_1$ Lasso penalty.
14. Because $f(t) = \ln(t)$ is strictly increasing ($f'(t) = 1/t > 0$ for $t > 0$), any point $	heta$ that maximizes $L(	heta)$ simultaneously maximizes $\ln L(	heta)$.
15. ECE bins predictions by confidence (e.g. $[0.8, 0.9]$) and measures absolute difference between average confidence and true bin accuracy $|	ext{acc}(B) - 	ext{conf}(B)|$.

## Level 4
16. $rac{d\sigma}{dz} = rac{e^{-z}}{(1+e^{-z})^2} = rac{1}{1+e^{-z}} \left(1 - rac{1}{1+e^{-z}}ight) = \sigma(z)(1 - \sigma(z))$.
17. $rac{\partial L}{\partial \hat{y}} = -rac{y}{\hat{y}} + rac{1-y}{1-\hat{y}} = rac{\hat{y} - y}{\hat{y}(1-\hat{y})}$. Chain rule: $rac{\partial L}{\partial z} = rac{\partial L}{\partial \hat{y}} rac{\partial \hat{y}}{\partial z} = rac{\hat{y} - y}{\hat{y}(1-\hat{y})} [\hat{y}(1-\hat{y})] = \hat{y} - y$.
18. The derivative simplifies directly to linear error $(\hat{y} - y)$, eliminating the term $\hat{y}(1-\hat{y})$ that saturates to zero at extremes when using MSE + Sigmoid.
19. 1) Discriminative, 2) Generative, 3) Generative, 4) Discriminative.
20. Temperature $T > 1$ softens probability distribution (increases entropy, reducing overconfidence without changing class ranking $rg\max$).

## Level 5
21. $D_{KL}(p \parallel q) = \sum p(x) \log rac{p(x)}{q(x)} = \sum p(x) \log p(x) - \sum p(x) \log q(x) = -H(p) + H(p, q)$. Since target entropy $H(p)$ is constant w.r.t model parameters $q$, minimizing $H(p, q)$ is identical to minimizing $D_{KL}(p \parallel q)$.
22. Likelihood $\propto p^k (1-p)^{N-k}$. Prior $\propto p^{lpha-1} (1-p)^{eta-1}$. Posterior $\propto p^{k+lpha-1} (1-p)^{N-k+eta-1}$. Setting derivative of log-posterior to zero yields $rac{k+lpha-1}{p} = rac{N-k+eta-1}{1-p} \implies (k+lpha-1)(1-p) = (N-k+eta-1)p \implies \hat{p}_{MAP} = rac{k+lpha-1}{N+lpha+eta-2}$.
23. `from scipy.optimize import minimize; res = minimize(lambda params: -np.sum(stats.norm.logpdf(data, params[0], params[1])), [0, 1])`.
