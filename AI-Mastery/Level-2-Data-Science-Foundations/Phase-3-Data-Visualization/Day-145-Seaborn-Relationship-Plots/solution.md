# Day 145 Solutions: Seaborn Relationship Plots

## Level 1 — Basic
1. `sns.pairplot()`.
2. `corner=True`.
3. `sns.lmplot()` (or `sns.regplot()`).

## Level 2 — Coding
1. `sns.pairplot(df, hue='Outcome')`
2. `sns.lmplot(data=df, x='Age', y='Salary', col='Gender')`

## Level 3 — Data Analysis
1. Pair plots display all pairwise numerical relationships simultaneously, enabling instant identification of multi-collinear feature pairs, target-separating features, and non-linear patterns.
