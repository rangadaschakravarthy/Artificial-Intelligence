# Day 131 Worked Examples: Pandas for Machine Learning

## Example 1 — Beginner: Separating X and y
```python
import pandas as pd

df = pd.DataFrame({
    'Feature_1': [1.0, 2.5, 3.2],
    'Feature_2': [10, 20, 30],
    'Target_Label': [0, 1, 0]
})

# Feature Matrix X (2D DataFrame without target)
X = df.drop(columns=['Target_Label'])

# Target Vector y (1D Series)
y = df['Target_Label']

print("Feature Matrix X shape:", X.shape)
print("Target Vector y shape:  ", y.shape)
```

## Example 2 — Practical: Basic One-Hot Encoding with pd.get_dummies
```python
import pandas as pd

df = pd.DataFrame({
    'Gender': ['Male', 'Female', 'Female', 'Male'],
    'Plan': ['Basic', 'Premium', 'Basic', 'Standard'],
    'Spend': [50, 120, 45, 80]
})

# One-Hot Encode all categorical columns
df_encoded = pd.get_dummies(df, columns=['Gender', 'Plan'], drop_first=True, dtype=int)
print("One-Hot Encoded DataFrame:
", df_encoded)
```

## Example 3 — Intermediate: Handling Train-Test Column Alignment
```python
import pandas as pd

# Training set has 3 cities
train_df = pd.DataFrame({'City': ['NY', 'SF', 'LA'], 'Val': [1, 2, 3]})
# Test set has only 2 cities
test_df = pd.DataFrame({'City': ['NY', 'SF'], 'Val': [4, 5]})

# Encode train and test
X_train = pd.get_dummies(train_df, columns=['City'], dtype=int)
X_test = pd.get_dummies(test_df, columns=['City'], dtype=int)

# Align test set to match training set columns exactly
X_test = X_test.reindex(columns=X_train.columns, fill_value=0)
print("Aligned Test Feature Matrix:
", X_test)
```

## Example 4 — Real Dataset: Preparing Customer Churn ML Matrix
```python
import pandas as pd

churn_raw = pd.DataFrame({
    'Tenure': [12, 24, 6],
    'Contract': ['Month-to-Month', 'Two-Year', 'Month-to-Month'],
    'PaymentMethod': ['Electronic', 'CreditCard', 'Electronic'],
    'Churn': ['No', 'No', 'Yes']
})

# Convert target label to binary integer 0/1
y = (churn_raw['Churn'] == 'Yes').astype(int)

# Prepare Feature Matrix X
X_raw = churn_raw.drop(columns=['Churn'])
X = pd.get_dummies(X_raw, drop_first=True, dtype=int)

print("ML-Ready Feature Matrix X:
", X)
print("
Target Vector y:
", y.values)
```

## Example 5 — AI/ML Application: Exporting Prepared Datasets to Parquet/CSV
```python
import pandas as pd
import numpy as np

# Final clean feature matrix and target
X = pd.DataFrame({'F1': np.random.randn(5), 'F2': np.random.randn(5)})
y = pd.Series([0, 1, 0, 1, 0], name='target')

# Combine for export
ml_export = pd.concat([X, y], axis=1)

# Export clean dataset to CSV
ml_export.to_csv('clean_ml_dataset.csv', index=False)
print("Successfully exported clean_ml_dataset.csv with shape:", ml_export.shape)
```
