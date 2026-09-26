# Common Mistakes in Data Science & Preprocessing

This document catalogs frequent beginner mistakes, explains why they fail, and provides the correct code solution.

---

## 1. NumPy Mistakes
### Mistake: Modifying Sliced Arrays Unintentionally
- **Wrong**: `sub = arr[0:5]; sub[0] = 999` (Modifies original `arr` because slicing creates a view!).
- **Correct**: `sub = arr[0:5].copy(); sub[0] = 999`

---

## 2. Pandas Mistakes
### Mistake: Chained Assignment Triggering `SettingWithCopyWarning`
- **Wrong**: `df[df['Age'] > 30]['Status'] = 'Senior'`
- **Correct**: `df.loc[df['Age'] > 30, 'Status'] = 'Senior'`

### Mistake: Forgetting `axis=1` in `df.apply()`
- **Wrong**: `df.apply(lambda r: r['A'] + r['B'])` (Raises `KeyError` because `axis=0` passes column Series).
- **Correct**: `df.apply(lambda r: r['A'] + r['B'], axis=1)`

---

## 3. Preprocessing & Leakage Mistakes
### Mistake: Scaling Full Dataset Before Train/Test Split
- **Wrong**: `X_scaled = scaler.fit_transform(X); X_tr, X_te = train_test_split(X_scaled)`
- **Correct**: `X_tr, X_te = train_test_split(X); X_tr_s = scaler.fit_transform(X_tr); X_te_s = scaler.transform(X_te)`

### Mistake: Omission of `drop_first=True` in One-Hot Encoding
- **Wrong**: `pd.get_dummies(df)` (Triggers Dummy Variable Trap in linear models due to multi-collinearity).
- **Correct**: `pd.get_dummies(df, drop_first=True)`
