# Day 131 Practice Questions: Pandas for Machine Learning

## Level 1 — Basic
1. What mathematical shapes correspond to Feature Matrix $X$ and Target Vector $y$?
2. What function converts categorical string columns to binary dummy variables in Pandas?
3. What is the purpose of `drop_first=True` in `pd.get_dummies()`?
4. How do you convert a boolean Series (`True`/`False`) into a binary integer vector (`1`/`0`)?
5. Which Pandas export format (`.to_csv()` or `.to_parquet()`) preserves column data types natively?

## Level 2 — Coding
1. Separate `df` into $X$ (all columns except `'Price'`) and $y$ (`'Price'`).
2. Apply `pd.get_dummies()` to column `'Department'` with `drop_first=True` and `dtype=int`.
3. Convert string target labels (`'Yes'`, `'No'`) in `df['Churn']` to `1` and `0`.
4. Reindex test set columns `X_test` to align perfectly with training columns `X_train.columns`.
5. Export clean $X$ and $y$ tables as a single combined CSV file named `'processed_ml_data.csv'`.

## Level 3 — Data Analysis
1. Prepare a raw customer churn dataset into a fully numeric ML-ready feature matrix $X$ and target $y$.
2. Handle categorical attributes with missing values using `dummy_na=True` in `pd.get_dummies()`.
3. Process a multi-class target variable (`'Low'`, `'Medium'`, `'High'`) into ordinal integers (`0`, `1`, `2`).
4. Construct an ML dataset containing continuous numeric features, normalized scaling, and encoded dummies.
5. Verify that zero string or missing values remain in feature matrix $X$.

## Level 4 — Debugging
1. Fix error: `ValueError: could not convert string to float` when fitting a Scikit-Learn model on a DataFrame containing un-encoded string columns.
2. Fix feature dimension mismatch error between `X_train` (15 features) and `X_test` (12 features) after `pd.get_dummies()`.
3. Correct multi-collinearity error in linear regression caused by omitting `drop_first=True`.

## Level 5 — AI/ML Application
1. Demonstrate a complete Pandas pre-ML pipeline taking raw dirty DataFrame to numeric $X$ and $y$ matrices.
2. Why is `pd.get_dummies()` preferred for quick EDA, while Scikit-Learn's `OneHotEncoder` is preferred inside production ML pipelines?
3. Explain how target leakage can occur when encoding target-encoded features in Pandas before splitting data.

## Level 6 — Interview Questions
1. What is the Dummy Variable Trap, and how does linear algebra break if it is ignored?
2. Compare One-Hot Encoding (`pd.get_dummies()`) vs Label Encoding (`.astype('category').cat.codes`).
3. How do you handle high-cardinality categorical variables (e.g. 1,000 unique zip codes) in Pandas?
4. How do you ensure reproducible feature names when exporting Pandas DataFrames to NumPy arrays (`df.values`)?
5. What advantages does Parquet file format offer over CSV for storing preprocessed ML datasets?
