# Day 116 Solutions: Handling Missing Values

## Level 1 — Basic
1. `df.dropna()`
2. `df.fillna()`
3. `.ffill()` (or `.fillna(method='ffill')`).
4. `subset=['col1', 'col2']`
5. False (Median imputation is preferred for skewed data containing outliers).

## Level 2 — Coding
6. `df_clean = df.dropna(subset=['Salary'])`
7. `df['Age'] = df['Age'].fillna(df['Age'].median())`
8. `df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])`
9. `s_clean = s.ffill().bfill()`
10. `df_clean = df.dropna(thresh=int(0.70 * len(df)), axis=1)`

## Level 3 — Data Analysis
11. `how='all'` requires every column entry in the row to be `NaN`. If even 1 column contains a valid value, the row is retained.
12. Outliers distort the mean, causing imputed values to be unrepresentatively high or low, corrupting the feature distribution.
13. Index 0 becomes `10.0` (from bfill), index 1 is `10.0`, index 2 becomes `10.0` (from ffill).
14. Group-based imputation accounts for category-specific baseline differences (e.g. Data Scientist vs Intern salaries).
15. `-1.0`

## Level 4 — Debugging
16. Impute columns individually by type: numeric columns with median, categorical columns with mode or string `'Missing'`.
17. `.mode()` returns a Series (since multi-modal distributions have multiple modes). Access the first mode via `.mode()[0]`.
18. Compute imputation statistics (mean/median) **only** on the training set, then use those fixed training values to fill both train and test sets.

## Level 5 — AI/ML Application
19. 
```python
num_cols = df.select_dtypes(include=np.number).columns
cat_cols = df.select_dtypes(include='object').columns
for c in num_cols: df[c] = df[c].fillna(df[c].median())
for c in cat_cols: df[c] = df[c].fillna(df[c].mode()[0])
```
20. Binary missing indicators explicitly inform the ML model that a feature value was missing, capturing valuable predictive pattern information.
21. Constant imputation artificially reduces feature variance (shrinks std dev). Adding missingness indicators preserves model awareness of original variance bounds.

## Level 6 — Interview Solutions
22. Forward fill only uses past historical observations $t-1, t-2$ to fill $t$, guaranteeing no future data from $t+1$ leaks into historical states.
23. Single imputation fills missing slots once with a fixed value, underestimating variance. Multiple Imputation (MICE) models missing values stochastically over $D$ iterations, preserving uncertainty.
24. Computing `df['col'].mean()` on the whole dataset incorporates test set target values into the mean statistic, leaking test set information into training features.
25. `from sklearn.impute import KNNImputer; imputer = KNNImputer(n_neighbors=5); X_imp = imputer.fit_transform(X)`
26. `dropna` reduces sample size $N$ (increasing standard errors). `fillna` with constant mean artificially reduces variance $\sigma^2$ (underestimating uncertainty).
