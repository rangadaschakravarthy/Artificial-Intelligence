# Theory — Statistics for Machine Learning

## 1. Overview
Statistics integrates into 4 major machine learning lifecycle stages:
1. **Exploratory Data Analysis (EDA)**: Skewness normalization, outlier filtering ($1.5 	imes IQR$, $Z > 3$).
2. **Feature Engineering & Selection**: ANOVA $F$-test (`f_classif`, `f_regression`) for continuous features; Chi-Square (`chi2`) for categorical features.
3. **Model Validation**: Paired $t$-tests over cross-validation folds; $95\%$ confidence intervals for test metrics.
4. **Production Monitoring**: A/B testing and 2-sample KS tests for detecting Data Drift / Covariate Shift.

## 2. Statistical Feature Selection Metrics
- **ANOVA $F$-Score (`f_classif`)**: Computes ratio of between-class variance to within-class variance:
  $$F = rac{	ext{Between-Class Variance}}{	ext{Within-Class Variance}}$$
  High $F$-score $\implies$ Feature mean differs significantly across classes (High predictive signal!).
- **Chi-Square Score (`chi2`)**: Measures dependency between categorical feature $X$ and target $Y$.

## 3. Multiple Testing Correction
When evaluating $m$ features simultaneously:
- **Bonferroni Correction**: $lpha_{	ext{adj}} = rac{lpha}{m}$ (Very conservative).
- **Benjamini-Hochberg (FDR)**: Sort $p$-values $p_{(1)} \le \dots \le p_{(m)}$ and find largest $k$ where $p_{(k)} \le rac{k}{m} q^*$.

## 4. Summary
Statistical feature selection (ANOVA/Chi-Square) and A/B testing provide mathematical rigor across ML model training and deployment.
