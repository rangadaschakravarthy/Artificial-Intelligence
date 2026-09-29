# Day 161 Theory: Standardization

### 1. What Is It?
Standardization (Z-Score Normalization) rescales numerical features so that they have a mean of $0$ ($\mu = 0$) and a standard deviation of $1$ ($\sigma = 1$).

### 2. Formula

$$
z = \frac{x - \mu}{\sigma}
$$

where $\mu = \frac{1}{N}\sum x_i$ is the feature mean, and $\sigma = \sqrt{\frac{1}{N}\sum (x_i - \mu)^2}$ is the standard deviation.

### 3. Normalization vs Standardization Comparison
| Attribute | Normalization (Min-Max) | Standardization (Z-Score) |
|---|---|---|
| **Formula** | $\frac{x - x_{\min}}{x_{\max} - x_{\min}}$ | $\frac{x - \mu}{\sigma}$ |
| **Output Range** | Fixed $[0, 1]$ | Unbounded $(-\infty, +\infty)$ |
| **Mean / Std** | Varies | Mean = 0, Std = 1 |
| **Outlier Sensitivity** | High | Moderate (preserves outlier variance) |
| **Primary Use Cases** | Neural Networks, Pixel Arrays | Logistic Regression, SVM, PCA, Linear ML |

### 4. Summary
Standardization centers features around $0$ with unit variance, offering robustness against extreme outliers.
