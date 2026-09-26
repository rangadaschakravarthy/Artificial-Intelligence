# Day 158 — One-Hot Encoding

## Learning Objectives
- Convert nominal categorical variables to binary indicator vectors using One-Hot Encoding.
- Master `pd.get_dummies()` and `sklearn.preprocessing.OneHotEncoder`.
- Prevent multi-collinearity by dropping the first dummy column (`drop='first'`).

## Prerequisites
- Day 156: Encoding
- Day 157: Label Encoding

## Topics Covered
- One-Hot Encoding definition and binary basis vector representation
- `pd.get_dummies()` vs `sklearn.preprocessing.OneHotEncoder`
- Dummy Variable Trap and multi-collinearity prevention (`drop_first=True`)
- Handling unseen categories during test set transformation (`handle_unknown='ignore'`)
- Managing sparse matrix outputs (`sparse_output=True`)

## Practical Work
- Compare `pd.get_dummies(drop_first=True)` with `OneHotEncoder(drop='first')` on a multi-category dataset.

## Difficulty
Intermediate
