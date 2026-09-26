# Day 130 Solutions: Exploratory Data Analysis

## Level 1 — Basic
1. Univariate (single variable), Bivariate (two variables), Multivariate (3+ variables).
2. `df.corr(numeric_only=True)`.
3. `normalize=True`.
4. A strong negative linear relationship (as one variable increases, the other decreases).
5. `df['Col'].skew()`.

## Level 2 — Coding
1.
```python
import pandas as pd
rev = df['Revenue']
print(f"Mean: {rev.mean()}, Median: {rev.median()}, Std: {rev.std()}, Skew: {rev.skew()}")
```
2.
```python
seg_props = df['Customer_Segment'].value_counts(normalize=True)
```
3.
```python
corr_matrix = df.corr(numeric_only=True)
```
4.
```python
edu_analysis = df.groupby('Education_Level').agg({'Income': 'median', 'Credit_Score': 'mean'})
```
5.
```python
corr = df.corr(numeric_only=True)
high_corr = (corr.abs() > 0.8) & (corr != 1.0)
```

## Level 3 — Data Analysis
1.
```python
# Univariate: inspect spend distribution
print(df['Spend'].describe())
# Bivariate: correlate features with spend
print(df.corr()['Spend'].sort_values(ascending=False))
```
2.
```python
print(df.groupby('Default')['Age', 'Income', 'Debt_Ratio'].mean())
```
3.
```python
print(df['Readmitted'].value_counts(normalize=True))
print(df.groupby('Readmitted')['Days_In_Hospital'].describe())
```
4.
```python
c = df.corr().abs()
pairs = c.unstack().sort_values(ascending=False)
redundant = pairs[(pairs > 0.85) & (pairs < 1.0)]
print(redundant)
```
5. Synthesize observations into clear statements (e.g. "1) High spend strongly correlates with tenure, 2) Basic plan users exhibit 3x higher churn, 3) Income exhibits positive right-skewness").

## Level 4 — Debugging
1. Pass `numeric_only=True` to `df.corr(numeric_only=True)`.
2. Pearson correlation measures ONLY linear relationships. Variables with perfect quadratic relationships ($y = x^2$) can yield Pearson $r pprox 0$. Inspect Spearman rank correlation or scatter plots.
3. Compare mean vs median. If mean >> median, report median and IQR alongside mean to account for outlier skewness.

## Level 5 — AI/ML Application
1.
```python
corr = X_train.corr().abs()
upper = corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool))
to_drop = [col for col in upper.columns if any(upper[col] > 0.90)]
X_filtered = X_train.drop(columns=to_drop)
```
2. High positive skewness (> 1.0) distorts linear ML models. Identifying skewness during EDA flags features requiring `np.log1p()` transformation.
3. EDA audits sample sizes and domain context, helping spot spurious mathematical correlations caused by random noise or confounding variables.

## Level 6 — Interview Questions
1. 1) Audit target variable distribution, 2) Group features by domain/type, 3) Automated feature-to-target correlation ranking, 4) Dimensionality reduction (PCA / clustering) for visual exploration.
2. Anscombe's Quartet consists of 4 datasets with identical summary statistics (mean, variance, correlation) but completely different graphical distributions, proving that numerical summaries alone can mask structural patterns.
3. Pearson measures linear relationship on raw continuous values. Spearman measures monotonic relationship on ranked ordinal values (robust to non-linear monotonic trends and outliers).
4. Apply non-linear feature transformations (log, polynomial, binning) or use non-linear ML algorithms (Decision Trees, Random Forests).
5. Focus on business impact, use clean key takeaways, present top-ranked driving factors, and avoid overwhelming technical jargon.
