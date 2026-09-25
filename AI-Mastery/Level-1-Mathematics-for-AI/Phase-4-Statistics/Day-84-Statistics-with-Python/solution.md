# Solutions — Statistics with Python

## Level 1
1. By default, Statsmodels OLS does not automatically include an intercept term $eta_0$; `sm.add_constant(X)` appends a column of 1s to represent the bias intercept.
2. The proportion of total target variance explained by the model features ($R^2 = 1 - rac{SS_{res}}{SS_{tot}}$).
3. Adjusted $R^2$ penalizes adding features that do not improve model fit more than expected by chance, preventing artificial inflation.
4. $H_0: eta_1 = eta_2 = \dots = eta_k = 0$ (Tests whether at least one feature has non-zero predictive power).
5. `scipy.stats.ttest_1samp`.

## Level 2
6. `import statsmodels.api as sm; model = sm.OLS(y, sm.add_constant(X)).fit()`
7. `cis = model.conf_int(alpha=0.05)`
8. `from statsmodels.stats.stattools import durbin_watson; dw = durbin_watson(model.resid)`
9. `sw_stat, sw_p = stats.shapiro(model.resid)`
10. `bic_val = model.bic`

## Level 3
11. Durbin-Watson statistic $d = rac{\sum (e_t - e_{t-1})^2}{\sum e_t^2} pprox 2(1 - r_1)$. When residual autocorrelation $r_1 = 0 \implies d = 2.0$; positive autocorrelation $r_1 > 0 \implies d < 2.0$.
12. Multicollinearity makes feature matrix $X^T X$ near-singular, inflating $(X^T X)^{-1}$ diagonal entries and blowing up coefficient standard errors $SE(\hat{eta}_j)$. High Condition Number ($> 30$) flags ill-conditioned feature matrices.
13. Adding a feature increases $k$. If $R^2$ increase is small, denominator term $(N-k-1)$ shrinks faster than $(1-R^2)$, causing Adjusted $R^2$ to decrease.
14. Breusch-Pagan test regresses squared residuals $e_i^2$ on independent variables $X$. A significant $p$-value ($p < 0.05$) indicates residual variance depends on $X$ (Heteroscedasticity).
15. Statsmodels prioritizes probabilistic inference, confidence intervals, $p$-values, and diagnostic tests; Scikit-Learn prioritizes predictive generalization performance, cross-validation, and pipeline integration.

## Level 4
16. `model = sm.OLS(y, sm.add_constant(X)).fit(); print(model.rsquared, model.f_pvalue)`
17. `sm.qqplot(model.resid, line='s'); plt.show()`
18. `vif = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]`
19. $VIF_j = rac{1}{1 - R_j^2}$. $VIF > 10 \implies R_j^2 > 0.90$, meaning $>90\%$ of feature $j$'s variance is explained by other input features (extreme redundancy).
20. `logit = sm.Logit(y, sm.add_constant(X)).fit(); odds_ratios = np.exp(logit.params)`

## Level 5
21. Top left: Model metadata; Top right: $R^2$, Adj $R^2$, $F$-stat & $p$-val; Middle table: Coefficients, Std Errors, t-stats, $p$-values, 95% CIs; Bottom table: Residual diagnostics (Omnibus/Jarque-Bera for normality, Durbin-Watson for autocorrelation, Cond No for collinearity).
22. Use Huber-White robust covariance estimators during fitting: `model = sm.OLS(y, X_const).fit(cov_type='HC3')`, which adjusts standard errors without altering point coefficients.
23. Complete regression diagnostic pipeline implemented in `code.py`.
