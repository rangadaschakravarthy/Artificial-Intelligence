# Solutions — Bernoulli and Binomial Statistical Foundations

## Level 1
1. $\hat{p} = \frac{X}{n}$.
2. $SE(\hat{p}) = \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$.
3. $n p \ge 10$ and $n(1-p) \ge 10$.
4. To bridge discrete integer count steps (Binomial) with continuous integration boundaries (Normal PDF) by adjusting limits $\pm 0.5$.
5. Because $SE = \sqrt{\frac{p(1-p)}{n}}$ has $n$ in the denominator; larger samples shrink estimation error by factor $1/\sqrt{n}$.

## Level 2
6. $\hat{p} = \frac{250}{1000} = 0.25$. $SE(\hat{p}) = \sqrt{\frac{0.25(0.75)}{1000}} = \sqrt{\frac{0.1875}{1000}} = \sqrt{0.0001875} pprox 0.01369$.
7. $\mu = n p = 100(0.4) = 40.0$; $\sigma = \sqrt{100(0.4)(0.6)} = \sqrt{24} pprox 4.899$.
8. $SE = \sqrt{\frac{0.5(0.5)}{400}} = \sqrt{\frac{0.25}{400}} = \frac{0.5}{20} = 0.025$. Margin of Error $= 1.96 	imes 0.025 = 0.049 = 4.9\%$.
9. $SE = \sqrt{\frac{0.10(0.90)}{900}} = \sqrt{\frac{0.09}{900}} = \frac{0.3}{30} = 0.010$.
10. $n p = 200(0.08) = 16 \ge 10$; $n(1-p) = 200(0.92) = 184 \ge 10$. Valid!

## Level 3
11. $X = \sum_{i=1}^n I_i$ where $E[I_i] = p$. $E[\hat{p}] = E\left[\frac{1}{n}\sum I_i
ight] = \frac{1}{n} \sum E[I_i] = \frac{n p}{n} = p$.
12. Since $I_i$ are independent, $	ext{Var}(X) = \sum 	ext{Var}(I_i) = n p(1-p)$. $	ext{Var}(\hat{p}) = 	ext{Var}(X/n) = \frac{1}{n^2} 	ext{Var}(X) = \frac{n p(1-p)}{n^2} = \frac{p(1-p)}{n}$.
13. Let $f(p) = p - p^2$. Take derivative: $f'(p) = 1 - 2p = 0 \implies p = 0.50$. Second derivative $f''(p) = -2 < 0$ confirms maximum at $p=0.50$.
14. When $p$ is near 0 or 1, the Binomial distribution is highly skewed, making symmetric Normal distribution confidence intervals produce invalid bounds (such as CI lower bound $< 0$).
15. $E = Z_{lpha/2} \sqrt{\frac{p(1-p)}{n}} \implies E^2 = Z^2 \frac{0.25}{n} \implies n = \frac{1.96^2 	imes 0.25}{0.03^2} = \frac{3.8416 	imes 0.25}{0.0009} = \frac{0.9604}{0.0009} pprox 1067.11 \implies n = 1068$.

## Level 4
16. `from statsmodels.stats.proportion import proportion_confint; ci = proportion_confint(12, 100, method='wilson')`
17. `x = np.random.binomial(100, 0.5, 10000); plt.hist(x, density=True); t = np.linspace(30,70,100); plt.plot(t, stats.norm.pdf(t, 50, 5))`
18. Pooled proportion $\hat{p}_{pool} = \frac{100 + 130}{1000 + 1000} = \frac{230}{2000} = 0.115$. Pooled $SE = \sqrt{0.115(0.885) \left(\frac{1}{1000} + \frac{1}{1000}
ight)} = \sqrt{0.101775 	imes 0.002} = \sqrt{0.00020355} pprox 0.014267$.
19. $Z = \frac{\hat{p}_B - \hat{p}_A}{SE_{pool}} = \frac{0.13 - 0.10}{0.014267} = \frac{0.03}{0.014267} pprox +2.1028$.
20. Calculating sample size beforehand ensures sufficient statistical power ($1-eta \ge 0.80$) to detect true treatment lift without running costly tests indefinitely or stopping prematurely.

## Level 5
21. Substitute Stirling's expansion $n! pprox \sqrt{2\pi n} (n/e)^n$ into $inom{n}{k} p^k (1-p)^{n-k}$, expand $\ln P(X=k)$ via Taylor series around $\mu = np$, yielding Gaussian quadratic exponential exponent $-\frac{(k-np)^2}{2np(1-p)}$.
22. Start from Margin of Error $E = Z_{lpha/2} \sqrt{\frac{p(1-p)}{n}}$. Square both sides: $E^2 = Z_{lpha/2}^2 \frac{p(1-p)}{n}$. Rearranging for $n$ gives $n = \frac{Z_{lpha/2}^2 p (1-p)}{E^2}$.
23. `from statsmodels.stats.proportion import proportions_ztest; z_stat, p_val = proportions_ztest([130, 100], [1000, 1000])`.
