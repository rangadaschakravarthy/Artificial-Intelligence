# Day 151 Solutions: Visualization for EDA

## Level 1 — Basic
1. Summary statistics can be identical for datasets with completely different visual distributions (Anscombe's Quartet).
2. Binary black/white grid mapping (`cmap='binary'`).

## Level 2 — Coding
1.
```python
def plot_num_hist(df):
    num_cols = df.select_dtypes(include='number').columns
    for col in num_cols:
        fig, ax = plt.subplots(figsize=(6, 3))
        sns.histplot(df[col], kde=True, ax=ax)
        fig.savefig(f'hist_{col}.png')
        plt.close(fig)
```

## Level 3 — Data Analysis
1. Linear models assume linear feature-target relationships. Visual scatter plots reveal quadratic or non-linear curves, prompting necessary feature transformations before modeling.
