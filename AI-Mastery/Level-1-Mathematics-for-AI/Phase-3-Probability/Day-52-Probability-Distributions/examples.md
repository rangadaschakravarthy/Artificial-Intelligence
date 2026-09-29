# Worked Examples — Probability Distributions

## Example 1: Bernoulli Distribution
**Problem**: A binary classification model predicts fraud with $p = 0.05$. State $E[X]$ and $	ext{Var}(X)$.
**Solution**:
1. $E[X] = p = 0.05$.
2. $	ext{Var}(X) = p(1-p) = 0.05(0.95) = 0.0475$.

## Example 2: Binomial Distribution (Batch Accuracy)
**Problem**: A classifier has single-sample accuracy $p = 0.90$. Evaluate a batch of $n = 20$ samples. Find expected correct predictions and standard deviation.
**Solution**:
1. Expected correct $= E[X] = n p = 20 	imes 0.90 = 18$.
2. Variance $= 	ext{Var}(X) = n p (1-p) = 20 (0.90)(0.10) = 1.8$.
3. Standard Deviation $= \sqrt{1.8} pprox 1.3416$.

## Example 3: Poisson Call Arrival
**Problem**: An AI customer bot receives $\lambda = 5$ calls per minute. Compute $P(X = 2)$.
**Solution**:
1. $P(X = 2) = \frac{5^2 e^{-5}}{2!} = \frac{25 	imes 0.006738}{2} = \frac{0.16845}{2} pprox 0.0842 = 8.42\%$.

## Example 4: Uniform Weight Initialization (Xavier Uniform)
**Problem**: Weights are initialized $W \sim 	ext{Uniform}(-a, a)$ with $a = \sqrt{\frac{6}{d_{in} + d_{out}}}$. For $d_{in}=100, d_{out}=100$, compute $a$ and weight variance.
**Solution**:
1. $a = \sqrt{\frac{6}{200}} = \sqrt{0.03} pprox 0.1732$.
2. $	ext{Var}(W) = \frac{(a - (-a))^2}{12} = \frac{(2a)^2}{12} = \frac{4 a^2}{12} = \frac{a^2}{3} = \frac{0.03}{3} = 0.01$.

## Example 5: Gaussian Empirical Rule
**Problem**: Model weights $W \sim \mathcal{N}(0, 4)$ (so $\mu=0, \sigma=2$). Find interval containing $95.45\%$ of weights.
**Solution**:
1. By Gaussian empirical rule, $95.45\%$ lies within $\mu \pm 2\sigma$.
2. $\mu - 2\sigma = 0 - 2(2) = -4$.
3. $\mu + 2\sigma = 0 + 2(2) = +4$.
4. Interval is $[-4, 4]$.
