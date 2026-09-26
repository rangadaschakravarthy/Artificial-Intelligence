# Day 116 Practice Questions: Handling Missing Values

## Level 1 — Basic
1. What method drops rows containing missing values?
2. What method fills missing values with a specified constant or statistic?
3. What method propagates the last valid observation forward to fill `NaN`?
4. What parameter in `df.dropna()` restricts checking for missingness to specific columns?
5. True or False: Mean imputation is preferred over Median imputation for skewed feature columns.

## Level 2 — Coding
6. Drop rows from DataFrame `df` where column `'Salary'` is `NaN`.
7. Impute missing values in column `'Age'` with its column median.
8. Impute missing values in categorical column `'Gender'` with its mode value (`.mode()[0]`).
9. Perform forward fill (`ffill`) followed by backward fill (`bfill`) on Series `s`.
10. Drop columns from DataFrame `df` if they contain less than 70% non-null values using `thresh`.

## Level 3 — Data Analysis
11. Why does `df.dropna(how='all')` only drop rows where every single column is `NaN`?
12. Explain the danger of imputing missing values with the column mean when severe outliers exist.
13. Predict output of `s = pd.Series([np.nan, 10, np.nan]); print(s.ffill().bfill())`.
14. Explain why group-based median imputation `groupby('Category')['Val'].transform(...)` is superior to overall median imputation.
15. Predict output: `df = pd.DataFrame({'a': [1, np.nan]}); print(df.fillna(-1)['a'].iloc[1])`.

## Level 4 — Debugging
16. Fix bug where `df.fillna(0)` filled missing values in string/categorical columns with number `0`.
17. Fix error: `IndexError: Single bound only with an integer key` when accessing `.mode()`.
18. Fix data leakage bug where test set missing values were imputed using full dataset mean.

## Level 5 — AI/ML Application
19. How do you implement automated median imputation for numerical columns and mode imputation for categorical columns?
20. Why add a binary missingness indicator column (`df['col_isna']`) before imputing MNAR (Missing Not At Random) features?
21. Connect imputation choices to preserving training set distribution variance.

## Level 6 — Interview Questions
22. Explain how `fillna(method='ffill')` executes sequentially on time-series data without lookahead bias.
23. What is Multiple Imputation (e.g. MICE algorithm) and how does it differ from single mean/median imputation?
24. How does data leakage occur if you compute `fillna(df['col'].mean())` before splitting into train and test sets?
25. Demonstrate how `IterativeImputer` or `KNNImputer` in Scikit-Learn imputes missing features using non-missing predictor features.
26. How do dropna vs fillna operations impact dataset variance and standard errors?
