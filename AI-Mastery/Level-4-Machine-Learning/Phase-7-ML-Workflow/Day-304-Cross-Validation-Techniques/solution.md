# Practice Solutions — Day 304

## Basic Solutions
1. Cross-Validation Techniques organizes data processing, training, cross-validation, and model evaluation into reproducible pipelines.
2. `ColumnTransformer` applies separate preprocessing pipelines to specified sub-arrays of numerical and categorical columns.
3. $K$-Fold CV splits data into $K$ equal folds, iteratively training on $K-1$ folds and validating on 1 fold to estimate performance variance.

## Conceptual Solutions
4. Fitting a scaler on the whole dataset uses global mean and standard deviation from test samples, leaking test distribution information into training.
5. `GridSearchCV` exhaustively tests all parameter combinations; `RandomizedSearchCV` samples a fixed number of parameter combinations randomly from distribution spaces.
6. High Bias: Training and validation errors are both high and close together. High Variance: Large gap between low training error and high validation error.

## Calculation Solutions
7. Combinations $= 3 \times 4 = 12$. Total fits $= 12 \times 5 \text{ folds} = 60$ model fits.
8. $\text{Mean} = (0.80 + 0.82 + 0.84 + 0.78 + 0.81) / 5 = 4.05 / 5 = 0.81$ (81.0%).

## Implementation Solutions
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

# 9. Pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', Ridge())
])

# 10. Grid Search
param_grid = {'model__alpha': [0.1, 1.0, 10.0]}
grid = GridSearchCV(pipeline, param_grid, cv=5)
```

## ML Reasoning Solutions
11. Underfitting (High Bias). Solution: Increase model capacity, engineer more informative features, or reduce regularization constraints.
12. Evaluating permutation importance on training data can overestimate features that the model overfitted noise onto; test evaluation measures true predictive value.

## Dataset Questions
13. Numerical: Impute missing with median $\to$ `StandardScaler`. Categorical: Impute with most frequent $\to$ `OneHotEncoder(handle_unknown='ignore')`.

## Interview Solutions
14. `fit()` computes internal parameters (e.g. mean, std); `transform()` applies learned parameters to data; `fit_transform()` performs both sequentially for efficiency on training data.
15. Raw Data Ingest $\to$ Data Cleaning $\to$ Stratified Train/Test Split $\to$ `ColumnTransformer` Preprocessing Pipeline $\to$ Estimator $\to$ Cross-Validation & Grid Tuning $\to$ Test Evaluation $\to$ Model Serialization.
