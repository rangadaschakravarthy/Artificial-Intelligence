# Day 130 Theory: Exploratory Data Analysis

### 1. What Is It?
Exploratory Data Analysis (EDA) is an investigative analytical approach that uses summary statistics and numerical metrics to understand data structure, uncover patterns, test hypotheses, and detect anomalies.

### 2. Why Does It Exist?
Jumping straight into modeling without understanding data distributions leads to selecting wrong algorithms, ignoring data flaws, and building biased models.

### 3. Intuition
EDA is detective work: interviewing witnesses (univariate variables), examining relationships between suspects (bivariate correlation), and assembling the complete crime story (multivariate analysis).

### 4. Syntax
```python
# Univariate Numerical:
df['Col'].describe()
skewness = df['Col'].skew()

# Univariate Categorical:
freq = df['Cat'].value_counts(normalize=True)

# Bivariate Correlation Matrix:
corr_matrix = df.corr(numeric_only=True)

# Bivariate Grouped Comparison:
grp_summary = df.groupby('Category')['Target'].describe()
```

### 5. Parameters
- `numeric_only` (in `df.corr()`): bool. If `True`, calculates correlation only for numeric columns.
- `normalize` (in `value_counts()`): bool. If `True`, returns relative frequencies (proportions) instead of raw counts.

### 6. How It Works
EDA computes statistical moments (Mean, Variance, Skewness, Kurtosis) and pairwise mathematical covariance matrices to summarize dataset geometry.

### 7. Simple Example
```python
import pandas as pd
df = pd.DataFrame({'Age': [20, 25, 30, 80], 'Income': [30000, 40000, 50000, 150000]})
print(df.corr())
```

### 8. Intermediate Example
```python
import pandas as pd
df = pd.DataFrame({
    'Tier': ['Free', 'Free', 'Paid', 'Paid'],
    'Usage_Hrs': [5, 8, 25, 30],
    'Churn': [1, 1, 0, 0]
})
print("Tier Churn Proportions:
", df.groupby('Tier')['Churn'].mean())
```

### 9. Output Interpretation
- Correlation values range from `-1.0` (perfect negative correlation) to `+1.0` (perfect positive correlation). `0.0` indicates no linear relationship.
- Positive skewness (> 0) indicates a right-tailed distribution (e.g. income).

### 10. Common Mistakes
- Confusing correlation with causation.
- Relying solely on mean values without inspecting standard deviation or skewness (e.g. mean is heavily distorted by outliers).

### 11. Data Science Connection
Formulating business strategy, discovering customer segments, and validating analytical assumptions.

### 12. AI/ML Connection
Feature selection (removing collinear features), identifying targets for non-linear feature transformation, and informing model choice.

### 13. Interview Insight
Question: "What steps do you take when performing EDA on a new dataset?"
Answer: 1) Structural audit (`shape`, `dtypes`, `nulls`), 2) Univariate summary (distributions, skewness), 3) Bivariate correlation & group metrics, 4) Feature interaction analysis, 5) Insight synthesis.

### 14. Summary
EDA systematically inspects univariate distributions, bivariate correlations, and group-wise statistics to uncover hidden data patterns.
