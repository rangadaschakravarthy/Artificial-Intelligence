# Theory — Statistics with Python

## 1. Overview
Python statistical computing relies on two core complementary libraries:
1. `scipy.stats`: High-level distribution objects, hypothesis tests, and summary metrics.
2. `statsmodels`: Full statistical modeling, linear models (OLS, GLM), ANOVA tables, and comprehensive summary reports.

## 2. Key Elements of Statsmodels OLS Summary Table
- **$R^2$ (Coefficient of Determination)**: Proportion of variance in target $Y$ explained by features ($0 \le R^2 \le 1$).
- **Adjusted $R^2$**: Penalizes addition of non-informative features:
  $$R_{	ext{adj}}^2 = 1 - \left[ (1 - R^2) rac{N - 1}{N - k - 1} ight]$$
- **$F$-statistic & Prob ($F$-statistic)**: Tests $H_0: eta_1 = eta_2 = \dots = eta_k = 0$ (Overall model significance).
- **coef, std err, t, P>|t|**: Individual feature coefficient significance tests ($H_0: eta_j = 0$).
- **[0.025, 0.975]**: $95\%$ Confidence intervals for feature weights.

## 3. Summary
`statsmodels` provides academic-grade statistical summary tables detailing fit quality ($R^2$), overall model significance ($F$-test), and feature-level significance ($t$-tests).
