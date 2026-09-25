# Worked Examples — Bernoulli and Binomial Statistical Foundations

## Example 1: Standard Error of Proportion Calculation
**Problem**: An AI model classifies 400 test images ($n=400$), getting 320 correct ($X=320$). Compute sample accuracy $\hat{p}$ and standard error $SE(\hat{p})$.
**Solution**:
1. $\hat{p} = rac{320}{400} = 0.80$.
2. $SE(\hat{p}) = \sqrt{rac{\hat{p}(1-\hat{p})}{n}} = \sqrt{rac{0.80(0.20)}{400}} = \sqrt{rac{0.16}{400}} = \sqrt{0.0004} = 0.02$.
3. Sample accuracy is $80\% \pm 2\%$.

## Example 2: Checking Normal Approximation Conditions
**Problem**: Is Normal approximation valid for $n = 50, p = 0.05$?
**Solution**:
1. Check $n p$: $50 	imes 0.05 = 2.5$.
2. Since $2.5 < 10$, Normal approximation is NOT valid (sample size too small for rare event $p=0.05$). Exact Binomial probabilities must be used.

## Example 3: Normal Approximation Calculation
**Problem**: $n = 100, p = 0.50$. Compute $P(X \ge 60)$ using Normal approximation.
**Solution**:
1. Check conditions: $n p = 50 \ge 10, n(1-p) = 50 \ge 10$ (Valid!).
2. $\mu = n p = 50$, $\sigma = \sqrt{100(0.5)(0.5)} = \sqrt{25} = 5$.
3. Apply continuity correction for $X \ge 60 \implies X \ge 59.5$.
4. $Z = rac{59.5 - 50}{5} = rac{9.5}{5} = 1.90$.
5. $P(Z \ge 1.90) = 1 - \Phi(1.90) pprox 1 - 0.9713 = 0.0287 = 2.87\%$.

## Example 4: 95% Confidence Interval for Proportion
**Problem**: From Example 1 ($\hat{p} = 0.80, n = 400, SE = 0.02$), compute $95\%$ Confidence Interval for model accuracy.
**Solution**:
1. $Z_{0.025} = 1.96$ for $95\%$ confidence.
2. Margin of Error $= 1.96 	imes 0.02 = 0.0392$.
3. $CI = 0.80 \pm 0.0392 = [0.7608, 0.8392] = [76.08\%, 83.92\%]$.

## Example 5: Proportion Inference in SciPy
**Problem**: Compute proportion confidence interval in Python.
**Solution**:
```python
from statsmodels.stats.proportion import proportion_confint

ci_low, ci_high = proportion_confint(
    count=320, nobs=400, alpha=0.05, method='normal'
)
```
