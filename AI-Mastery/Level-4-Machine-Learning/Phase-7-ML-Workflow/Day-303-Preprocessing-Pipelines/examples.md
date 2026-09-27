# Examples — Day 303: scikit-learn Preprocessing Pipelines

## Example 1 — Extremely Simple
Constructing a basic 2-step pipeline: `SimpleImputer` $\to$ `LogisticRegression`.

## Example 2 — Basic Numerical Example
Calculating Mean and Standard Deviation of cross-validation accuracy folds $[0.88, 0.90, 0.87, 0.91, 0.89]$.
- $\text{Mean} = 4.45 / 5 = 0.89$.
- $\text{Std} = \sqrt{\frac{\sum (x_i - 0.89)^2}{5}} = 0.0141$.

## Example 3 — Real Dataset Example (Titanic Survival Pipeline)
Handling numerical age imputation/scaling and categorical gender/embarked one-hot encoding.

## Example 4 — Machine Learning Grid Search Example
Tuning `n_estimators` $[50, 100, 200]$ and `max_depth` $[3, 5, 10]$ inside `GridSearchCV`.

## Example 5 — Real-World Scenario (Model Diagnostics)
Diagnosing a learning curve where training score is 0.99 and validation score is 0.65 $\implies$ High Variance (Overfitting).

## Example 6 — Interview-Style Example
Explaining why Permutation Feature Importance is superior to default Decision Tree Gini importance when features have high cardinality or collinearity.
