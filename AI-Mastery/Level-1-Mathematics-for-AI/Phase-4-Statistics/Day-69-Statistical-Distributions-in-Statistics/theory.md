# Theory — Statistical Distributions in Statistics

## 1. Simple Definition
Statistical distributions provide parametric mathematical models that describe population data behaviors, enabling hypothesis testing, confidence interval construction, and predictive modeling.

## 2. Parametric vs Non-Parametric Framework
- **Parametric Methods**: Assume data follows a specific parametric distribution (e.g. Gaussian $\mathcal{N}(\mu, \sigma^2)$). High statistical power when assumptions hold, but unreliable if assumptions are violated.
- **Non-Parametric Methods**: Make no strict distributional shape assumptions (distribution-free). Use ranks or empirical counts. Robust to severe non-normality and outliers.

## 3. Distribution Hierarchy in Inferential Statistics
- **Gaussian Normal $\mathcal{N}(\mu, \sigma^2)$**: Primary sampling distribution for large samples (CLT).
- **Student's $t$**: Used for sample means when population variance $\sigma^2$ is unknown and sample size $N$ is small ($N < 30$).
- **Chi-Square $\chi^2$**: Sum of squared standard normal variables; used for variance testing and categorical independence.
- **F-Distribution**: Ratio of two independent Chi-Square variables; used in ANOVA variance ratio tests.

## 4. Goodness-of-Fit Tests
1. **Shapiro-Wilk Test**: Tests null hypothesis that sample data came from a Normal distribution ($p > 0.05 \implies$ Normal).
2. **Kolmogorov-Smirnov (KS) Test**: Compares empirical sample distribution against theoretical distribution.

## 5. Summary
Statistical distributions form the backbone of parametric inferential tests. Normality testing determines whether parametric or non-parametric tests must be used.
