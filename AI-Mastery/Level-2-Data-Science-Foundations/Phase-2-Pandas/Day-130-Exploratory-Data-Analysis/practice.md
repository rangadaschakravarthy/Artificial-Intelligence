# Day 130 Practice Questions: Exploratory Data Analysis

## Level 1 — Basic
1. What are the three levels of Exploratory Data Analysis (EDA)?
2. What method computes pairwise correlation coefficients across numeric columns?
3. What parameter in `.value_counts()` converts raw category counts into percentage proportions?
4. What does a Pearson correlation coefficient of `-0.85` indicate?
5. How do you measure distribution skewness in Pandas?

## Level 2 — Coding
1. Calculate mean, median, standard deviation, and skewness for `df['Revenue']`.
2. Compute relative frequencies of column `'Customer_Segment'`.
3. Generate a Pearson correlation matrix for all numeric features in `df`.
4. Group `df` by `'Education_Level'` and calculate median `'Income'` and mean `'Credit_Score'`.
5. Identify pairs of features with correlation absolute value greater than `0.80`.

## Level 3 — Data Analysis
1. Conduct complete EDA on a retail customer dataset to identify top drivers of customer spend.
2. Analyze credit default logs to identify which demographic features separate defaulters from non-defaulters.
3. Perform univariate and bivariate analysis on a medical dataset predicting hospital readmission.
4. Uncover multi-collinear feature pairs in a financial risk feature set.
5. Synthesize 3 actionable business insights from an e-commerce EDA report.

## Level 4 — Debugging
1. Fix error: `TypeError: could not convert string to float` when calling `df.corr()`.
2. Fix analytical mistake: assuming a zero Pearson correlation coefficient implies NO relationship between two variables (ignoring non-linear relationships).
3. Correct misleading mean values caused by un-analyzed extreme outliers.

## Level 5 — AI/ML Application
1. Demonstrate using correlation analysis to drop redundant collinear features before ML training.
2. How does identifying skewed continuous features during EDA inform log transformation decisions?
3. Explain how EDA prevents spurious correlations from corrupting feature selection.

## Level 6 — Interview Questions
1. How do you approach EDA when given a dataset with 200+ features?
2. What is Anscombe's Quartet, and why does it demonstrate the importance of combining summary statistics with visualization?
3. How do you distinguish between Pearson correlation and Spearman rank correlation?
4. How do you handle non-linear feature relationships discovered during EDA?
5. How do you present EDA findings to non-technical executive stakeholders?
