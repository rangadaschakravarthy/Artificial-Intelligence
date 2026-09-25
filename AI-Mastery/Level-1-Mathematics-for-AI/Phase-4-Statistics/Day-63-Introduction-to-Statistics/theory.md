# Day 63 Theory: Introduction to Statistics

### 1. Simple Definition
Statistics is the science of collecting, analyzing, interpreting, presenting, and organizing data to make informed decisions in the presence of uncertainty.

### 2. Intuition
Instead of inspecting billions of user clicks individually, statistics distills raw data into actionable summaries (like average CTR) and generalizes from samples to entire populations.

### 3. Mathematical Definition
- Population: Set N of all possible observations.
- Sample: Subset n of N chosen for measurement.
- Parameter θ: Fixed numerical summary of population.
- Statistic T(X): Function of sample data estimating θ.

### 4. Mathematical Notation
- Population mean: μ, Sample mean: x_bar
- Population variance: σ^2, Sample variance: s^2

### 5. Formula
Sample Mean:
x_bar = (1/n) sum_{i=1}^n x_i

### 6. Symbol Explanation
- n: Sample size
- x_i: Individual sample observation
- x_bar: Estimator of population mean μ

### 7. Step-by-Step Calculation
Sample: [10, 20, 30, 40, 50]
Sum = 150.
n = 5.
x_bar = 150 / 5 = 30.

### 8. Second Concrete Example
In A/B testing:
Group A conversion: 120 / 1000 = 0.12.
Group B conversion: 150 / 1000 = 0.15.
Statistics determines if B's 3% uplift is real or random noise.

### 9. Common Mistakes
- Confusing sample statistic s^2 with population parameter σ^2.
- Assuming sample statistics always equal true population parameters without error bounds.

### 10. AI Connection
Machine learning models (e.g. Linear Regression, Naive Bayes) are statistical estimators fitted on sample datasets to predict unseen population outcomes.

### 11. Algorithm Connection
- Maximum Likelihood Estimation (MLE)
- Regularization (Ridge/Lasso) as Bayesian priors
- Cross-validation for sample variance estimation

### 12. Practical Interpretation
Descriptive statistics summarizes what happened; inferential statistics predicts what will happen.

### 13. Interview Insight
Question: What is the difference between a parameter and a statistic?
Answer: A parameter is a true, fixed value summarizing an entire population (e.g. μ). A statistic is a variable computed from sample data (e.g. x_bar) to estimate the parameter.

### 14. Summary
Statistics forms the foundational language of empirical data analysis and ML inference.
