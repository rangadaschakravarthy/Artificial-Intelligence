# Day 158 Solutions: One-Hot Encoding

## Level 1 — Basic
1. $K$ columns.
2. Perfect multi-collinearity caused by including all $K$ dummy columns, making the sum of dummy columns equal to 1 (the constant intercept).
3. It transforms unseen category levels into rows containing all zeros across dummy columns instead of raising an error.

## Level 2 — Coding
1. `df_encoded = pd.get_dummies(df, columns=['CatCol'], drop_first=True, dtype=int)`

## Level 3 — Data Analysis
1. `OneHotEncoder` fits on training data and stores learned category levels statefully, ensuring test sets are transformed into identical column structures without feature misalignment. `pd.get_dummies()` is stateless and can produce mismatched columns if categories differ between train and test sets.
