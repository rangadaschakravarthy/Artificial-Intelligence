# Day 75 Theory: Point Estimation

### 1. Simple Definition
Point estimation involves calculating a single best-guess numerical value (a statistic) from sample data to estimate an unknown population parameter.

### 2. Intuition
If you want to guess the true average height of all humans, you measure 100 people and compute their sample mean x_bar = 170 cm. That single number 170 cm is a point estimate!

### 3. Mathematical Definition
Let θ be an unknown parameter and θ_hat = T(X_1, ..., X_n) be an estimator.
- Bias: Bias(θ_hat) = E[θ_hat] - θ.
- Unbiased: Bias(θ_hat) = 0 => E[θ_hat] = θ.
- Variance: Var(θ_hat) = E[(θ_hat - E[θ_hat])^2].
- Mean Squared Error (MSE): MSE(θ_hat) = E[(θ_hat - θ)^2] = Bias(θ_hat)^2 + Var(θ_hat).

### 4. Mathematical Notation
- θ: True parameter
- θ_hat: Estimator of parameter θ
- MSE(θ_hat) = Bias^2 + Variance

### 5. Formula
Bias-Variance Decomposition of Estimator:
MSE(θ_hat) = Bias(θ_hat)^2 + Var(θ_hat)

Cramér-Rao Lower Bound (CRLB):
Var(θ_hat) >= 1 / I(θ)

### 6. Symbol Explanation
- MSE: Mean Squared Error of estimator
- I(θ): Fisher Information of sample data

### 7. Step-by-Step Calculation
Compare two estimators of μ:
Estimator 1 (x_bar): Unbiased (Bias=0), Var = σ^2 / n. MSE = σ^2 / n.
Estimator 2 (X_1): Unbiased (Bias=0), Var = σ^2. MSE = σ^2.
Since MSE(x_bar) < MSE(X_1) for n > 1, x_bar is a more efficient estimator!

### 8. Second Concrete Example
Sample Variance estimators:
S_n^2 = (1/n) sum (x_i - x_bar)^2 -> Biased! E[S_n^2] = ((n-1)/n) σ^2.
S_{n-1}^2 = (1/(n-1)) sum (x_i - x_bar)^2 -> Unbiased! E[S_{n-1}^2] = σ^2.

### 9. Common Mistakes
- Confusing an estimator (a function/formula T(X)) with an estimate (a specific calculated number like 42.5).
- Assuming unbiased estimators always have lower MSE than biased estimators (sometimes introducing small bias drastically reduces variance, lowering total MSE!).

### 10. AI Connection
Regularization in ML (L1 Lasso / L2 Ridge) deliberately introduces a small bias to shrink weights, massively reducing model variance and overall test error (Bias-Variance Tradeoff!).

### 11. Algorithm Connection
- Minimum Variance Unbiased Estimator (MVUE)
- Ridge Regression: Weight estimate w_hat = (X^T X + λ I)^(-1) X^T y.

### 12. Practical Interpretation
- Unbiasedness: Centered accurately on true parameter on average.
- Efficiency: Lowest possible variance among unbiased estimators.
- Consistency: Converges to true parameter as n -> infinity.

### 13. Interview Insight
Question: What is the Bias-Variance Tradeoff formula for an estimator?
Answer: MSE(θ_hat) = Bias(θ_hat)^2 + Var(θ_hat). Total estimation error comes from systematic bias plus sampling variance.

### 14. Summary
Point estimation provides single-value parameter estimates; MSE balances bias squared and variance.
