# Practice Questions — Day 304

## Basic Questions
1. Define Cross-Validation Techniques.
2. What is the role of `ColumnTransformer` in scikit-learn?
3. Explain $K$-Fold Cross-Validation.

## Conceptual Questions
4. Explain how performing feature scaling before `train_test_split` causes data leakage.
5. Contrast `GridSearchCV` vs `RandomizedSearchCV`.
6. How do learning curves help distinguish high bias from high variance?

## Calculation Questions
7. Calculate the total number of models trained in a 5-Fold Cross-Validation Grid Search testing 3 values of `C` and 4 values of `gamma`.
8. Given CV accuracy scores $[0.80, 0.82, 0.84, 0.78, 0.81]$, compute the mean CV score.

## Implementation Questions
9. Write a Python script constructing a scikit-learn `Pipeline` with `StandardScaler` and `Ridge`.
10. Implement `GridSearchCV` to tune `n_estimators` for a `RandomForestClassifier`.

## ML Reasoning Questions
11. If a learning curve shows training error and validation error converging at a high error rate, is the model underfitting or overfitting? What is the solution?
12. Why should Permutation Importance be evaluated on validation/test data rather than training data?

## Dataset Questions
13. Identify numerical vs categorical columns in a tabular dataset and design a preprocessing strategy.

## Interview Questions
14. Explain the difference between `fit()`, `transform()`, and `fit_transform()` in scikit-learn estimators.
15. Walk through the step-by-step pipeline design for a machine learning model going into production.
