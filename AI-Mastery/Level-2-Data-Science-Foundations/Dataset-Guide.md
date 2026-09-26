# Dataset Guide — Finding and Working with Real-World Datasets

This guide explains safe sources for acquiring practice datasets and best practices for dataset inspection and quality documentation.

---

## Recommended Public Dataset Repositories
1. **Kaggle Datasets**: Excellent source for tabular CSV datasets across domain topics.
2. **UCI Machine Learning Repository**: Benchmark datasets for classification and regression tasks.
3. **Seaborn Built-in Datasets**: Clean datasets available via `sns.load_dataset('iris'|'titanic'|'tips'|'diamonds')`.
4. **Scikit-Learn Toy Datasets**: Loadable via `sklearn.datasets.load_iris()`, `load_diabetes()`.

---

## Dataset Quality Audit Checklist
- [ ] Verify dataset license and usage permissions.
- [ ] Check total row count and column data types (`df.info()`).
- [ ] Check missing value proportions per column (`df.isna().mean()`).
- [ ] Identify duplicate rows (`df.duplicated().sum()`).
- [ ] Inspect numeric range minimums and maximums (`df.describe()`).
