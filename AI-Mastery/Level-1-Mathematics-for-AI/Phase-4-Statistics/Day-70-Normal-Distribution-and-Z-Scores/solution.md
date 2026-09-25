# Solutions — Normal Distribution and Z-Scores

## Level 1
1. $Z = rac{X - \mu}{\sigma}$.
2. Mean $= 0.0$, Variance $= 1.0$.
3. $\mu \pm 1\sigma pprox 68.27\%$; $\mu \pm 2\sigma pprox 95.45\%$; $\mu \pm 3\sigma pprox 99.73\%$.
4. $|Z| > 3.0$.
5. $\phi(z) = rac{1}{\sqrt{2\pi}} e^{-z^2/2}$.

## Level 2
6. $\sigma = \sqrt{16} = 4$. $Z = rac{108 - 100}{4} = rac{8}{4} = +2.0$.
7. $P(Z > 2.0) = 1 - \Phi(2.0) = 1 - 0.9772 = 0.0228 = 2.28\%$.
8. $P(-1 \le Z \le 1) = \Phi(1) - \Phi(-1) = 0.8413 - 0.1587 = 0.6826 = 68.26\%$.
9. $x = \mu + Z \sigma = 50 + (-2.5)(10) = 50 - 25 = 25.0$.
10. $\mu = 4, s = 2$. $z = \left[ rac{2-4}{2}, rac{4-4}{2}, rac{6-4}{2} ight] = [-1.0, 0.0, 1.0]$.

## Level 3
11. $E[Z] = E\left[rac{X-\mu}{\sigma}ight] = rac{E[X]-\mu}{\sigma} = rac{\mu-\mu}{\sigma} = 0$. $	ext{Var}(Z) = 	ext{Var}\left(rac{X-\mu}{\sigma}ight) = rac{1}{\sigma^2}	ext{Var}(X-\mu) = rac{\sigma^2}{\sigma^2} = 1$.
12. Set 2nd derivative $f''(x) = 0$. $f''(x) = f(x) \left[ rac{(x-\mu)^2 - \sigma^2}{\sigma^4} ight] = 0 \implies (x-\mu)^2 = \sigma^2 \implies x = \mu \pm \sigma$.
13. Exponent $-rac{(x-\mu)^2}{2\sigma^2} \le 0$, achieving maximum $0$ at $x = \mu$, so $e^0 = 1 \implies f(\mu) = rac{1}{\sigma\sqrt{2\pi}}$.
14. Unscaled features create elongated elliptical loss contours, causing gradient descent updates to oscillate wildly. Standardizing shapes contours into circular bowls, enabling direct gradient convergence.
15. Distance metrics ($d(\mathbf{a}, \mathbf{b}) = \sqrt{\sum (a_i - b_i)^2}$) are dominated by features with large raw numerical scales (e.g. Income in $100,000s vs Age in 10s). Standardization gives equal weight to all features.

## Level 4
16. `class ScratchStandardScaler: fit(X): self.mu = X.mean(0); self.std = X.std(0); transform(X): return (X - self.mu)/self.std`
17. `z_scores = np.abs((df - df.mean()) / df.std()); clean_df = df[(z_scores < 3.0).all(axis=1)]`
18. $\mathcal{N}(\mathbf{x}; oldsymbol{\mu}_k, oldsymbol{\Sigma}_k) = rac{1}{(2\pi)^{d/2} |oldsymbol{\Sigma}_k|^{1/2}} \exp\left(-rac{1}{2} (\mathbf{x}-oldsymbol{\mu}_k)^T oldsymbol{\Sigma}_k^{-1} (\mathbf{x}-oldsymbol{\mu}_k)ight)$.
19. $\sigma = 10$. `val = stats.norm.ppf(0.90, loc=50, scale=10)` $pprox 50 + 1.28155(10) = 62.8155$.
20. $\sigma = \sqrt{2/512} = \sqrt{1/256} = 0.0625$. $Z = rac{0.10 - 0}{0.0625} = 1.60$.

## Level 5
21. Let $I = \int_{-\infty}^{\infty} e^{-z^2/2} dz$. $I^2 = \int\int e^{-(x^2+y^2)/2} dx dy = \int_0^{2\pi} d	heta \int_0^{\infty} r e^{-r^2/2} dr = 2\pi [-e^{-r^2/2}]_0^{\infty} = 2\pi (1) = 2\pi \implies I = \sqrt{2\pi}$. Dividing by $\sqrt{2\pi}$ gives integral 1.
22. `StandardScaler` preserves outliers and shape ($E=0, 	ext{Var}=1$), preferred for Gaussian features and linear/neural models; `MinMaxScaler` squashes features strictly into $[0, 1]$, preferred for bounded image pixels and algorithms sensitive to non-negative inputs.
23. `z = (x - np.mean(x))/np.std(x); outliers = np.where(np.abs(z) > 3.0); clean_x = x[np.abs(z) <= 3.0]`.
