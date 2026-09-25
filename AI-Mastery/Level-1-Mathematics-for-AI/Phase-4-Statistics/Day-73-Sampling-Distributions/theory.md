# Day 73 Theory: Sampling Distributions

### 1. Simple Definition
A sampling distribution is the probability distribution of a sample statistic (such as sample mean x_bar) obtained by repeatedly taking samples of size n from a population.

### 2. Intuition
If you take 1,000 different samples of size 50 from a population and compute 1,000 sample means, those 1,000 sample means will form their own distribution! That meta-distribution is the sampling distribution.

### 3. Mathematical Definition
Let X_1, X_2, ..., X_n be i.i.d. random variables with mean μ and variance σ^2.
Sample Mean: X_bar = (1/n) sum_{i=1}^n X_i.
Expected Value: E[X_bar] = μ.
Variance: Var(X_bar) = σ^2 / n.
Standard Error: SE(X_bar) = σ / sqrt(n).

### 4. Mathematical Notation
- SE: Standard Error of the statistic
- X_bar ~ N(μ, σ^2 / n) (for normal populations or large n)

### 5. Formula
Standard Error of Mean:
SE = σ / sqrt(n)

Standard Error of Proportion:
SE_p = sqrt( p(1-p) / n )

### 6. Symbol Explanation
- σ: Population standard deviation
- n: Sample size
- p: Population proportion

### 7. Step-by-Step Calculation
Population μ = 100, σ = 15. Sample size n = 25.
Step 1: Compute SE = 15 / sqrt(25) = 15 / 5 = 3.0.
Step 2: Sampling distribution of sample mean is X_bar ~ N(100, 3^2).
Interpretation: A single sample mean of size 25 has 95% probability of falling between 100 ± 2(3) = [94, 106].

### 8. Second Concrete Example
Quadrupling sample size from n=25 to n=100:
SE_100 = 15 / sqrt(100) = 15 / 10 = 1.5.
Doubling sample size precision requires 4x more data!

### 9. Common Mistakes
- Confusing Standard Error (SE) with Standard Deviation (SD). SD measures spread of individual population points; SE measures precision of sample mean!
- Thinking SE increases with sample size (SE shrinks as n grows!).

### 10. AI Connection
In Bootstrapping and Cross-Validation, sample statistics across folds form a sampling distribution used to estimate model performance stability.

### 11. Algorithm Connection
- Bagging (Bootstrap Aggregating) reduces model prediction variance by averaging models trained over samples drawn from the sampling distribution.
- Monte Carlo simulations sample repeatedly to estimate output expectation distributions.

### 12. Practical Interpretation
Standard error measures the margin of uncertainty when generalizing from a sample to the population.

### 13. Interview Insight
Question: What happens to the Standard Error of the mean if you increase sample size by a factor of 100?
Answer: Since SE = σ / sqrt(n), increasing n by 100 reduces SE by sqrt(100) = 10. The sample mean becomes 10 times more precise!

### 14. Summary
Sampling distributions describe how sample estimates vary; Standard Error shrinks at rate 1 / sqrt(n).
