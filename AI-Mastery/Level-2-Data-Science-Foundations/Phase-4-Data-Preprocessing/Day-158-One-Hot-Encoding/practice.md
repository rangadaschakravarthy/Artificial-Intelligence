# Day 158 Practice Questions: One-Hot Encoding

## Level 1 — Basic
1. How many binary columns does One-Hot Encoding create for a feature with $K$ unique categories (without dropping first)?
2. What is the Dummy Variable Trap?
3. How does setting `handle_unknown='ignore'` handle unseen categories in Scikit-Learn's `OneHotEncoder`?

## Level 2 — Coding
1. Apply `pd.get_dummies()` with `drop_first=True` and `dtype=int`.

## Level 3 — Data Analysis
1. Why is `OneHotEncoder` preferred over `pd.get_dummies()` inside production ML pipelines?
