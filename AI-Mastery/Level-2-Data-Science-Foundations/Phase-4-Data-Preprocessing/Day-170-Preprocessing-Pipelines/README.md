# Day 170 — Preprocessing Pipelines

## Learning Objectives
- Build modular, leak-free preprocessing pipelines using Scikit-Learn `Pipeline` and `ColumnTransformer`.
- Apply distinct transformation pipelines to numerical vs categorical features simultaneously.
- Chain imputers, encoders, and scalers into single production-grade pipeline objects.

## Prerequisites
- Day 168: Data Leakage
- Day 169: Train-Test Concept

## Topics Covered
- `sklearn.pipeline.Pipeline` architecture
- `sklearn.compose.ColumnTransformer` for feature-specific transformation pipelines
- Combining `SimpleImputer`, `OneHotEncoder`, `StandardScaler`, and `MinMaxScaler`
- Fitting pipelines on `X_train` and executing `pipeline.transform(X_test)`
- Preventing manual data leakage automatically

## Practical Work
- Construct a full `ColumnTransformer` pipeline processing numeric (impute + scale) and categorical (impute + one-hot encode) features.

## Difficulty
Intermediate / Advanced
