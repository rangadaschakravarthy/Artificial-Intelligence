# Theory — Bernoulli and Binomial Statistical Foundations

## 1. Simple Definition
The Bernoulli distribution models a single binary success/failure trial ($p$). The Binomial distribution models total success counts $X$ across $n$ independent Bernoulli trials. The sample proportion $\hat{p} = rac{X}{n}$ measures empirical success frequency.

## 2. Intuition
In an A/B test, 1,000 website visitors see Variant A ($n = 1000$). 120 users convert ($X = 120$). The sample conversion proportion is $\hat{p} = rac{120}{1000} = 0.12$. How confident are we in this estimate? Binomial statistics calculates the standard error of this proportion.

## 3. Mathematical Statistics
- **Sample Proportion**: $\hat{p} = rac{X}{n}$
- **Expectation of $\hat{p}$**: $E[\hat{p}] = E\left[rac{X}{n}ight] = rac{n p}{n} = p$ (Unbiased!).
- **Variance of $\hat{p}$**:
  $$	ext{Var}(\hat{p}) = 	ext{Var}\left(rac{X}{n}ight) = rac{1}{n^2} 	ext{Var}(X) = rac{n p(1-p)}{n^2} = rac{p(1-p)}{n}$$
- **Standard Error of Proportion**:
  $$SE(\hat{p}) = \sqrt{rac{p(1-p)}{n}} pprox \sqrt{rac{\hat{p}(1-\hat{p})}{n}}$$

## 4. Normal Approximation Theorem (De Moivre–Laplace)
When $n p \ge 10$ and $n(1-p) \ge 10$, the discrete Binomial distribution is well approximated by a continuous Normal distribution:
$$X \sim 	ext{Bin}(n, p) pprox \mathcal{N}\left(\mu = n p, \sigma^2 = n p (1-p)ight)$$
$$\hat{p} \sim \mathcal{N}\left(\mu = p, \sigma^2 = rac{p(1-p)}{n}ight)$$

## 5. Continuity Correction
When approximating discrete $P(X = k)$ with continuous Normal integration, integrate between $k - 0.5$ and $k + 0.5$:
$$P(X = k) pprox P\left(k - 0.5 \le X_{	ext{norm}} \le k + 0.5ight)$$

## 6. AI Connection
A/B testing conversion lift analysis uses the $Z$-test for two proportions, relying directly on Normal approximation to Binomial distributions.

## 7. Summary
Sample proportions $\hat{p}$ have mean $p$ and standard error $SE = \sqrt{rac{p(1-p)}{n}}$, enabling $Z$-score inference for binary AI metrics.
