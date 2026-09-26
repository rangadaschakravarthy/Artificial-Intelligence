# Day 158 Worked Examples: One-Hot Encoding

## Example 1 — Practical: Scikit-Learn OneHotEncoder with handle_unknown='ignore'
```python
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

train_df = pd.DataFrame({'City': ['NY', 'SF', 'LA']})
test_df = pd.DataFrame({'City': ['NY', 'Chicago']}) # 'Chicago' is unseen!

# Fit OneHotEncoder on training data
ohe = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
ohe.fit(train_df[['City']])

# Transform train and test
X_train_ohe = ohe.transform(train_df[['City']])
X_test_ohe = ohe.transform(test_df[['City']])

print("Encoded Train Columns:", ohe.get_feature_names_out())
print("Encoded Test Matrix (Unseen 'Chicago' becomes all 0s):
", X_test_ohe)
```
