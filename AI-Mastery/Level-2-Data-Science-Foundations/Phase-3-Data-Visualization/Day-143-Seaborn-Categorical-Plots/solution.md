# Day 143 Solutions: Seaborn Categorical Plots

## Level 1 — Basic
1. A Violin plot combines box plot quartiles with a smooth Kernel Density Estimate (KDE), revealing bimodal or multimodal distribution shapes.
2. `sns.countplot()`.
3. `split=True`.

## Level 2 — Coding
1. `sns.countplot(data=df, x='Customer_Segment')`
2. `sns.boxplot(data=df, x='Cat', y='Val'); sns.stripplot(data=df, x='Cat', y='Val', color='black', alpha=0.3)`

## Level 3 — Data Analysis
1. `boxenplot()` (Letter-value plot) is designed for large datasets ($N > 10,000$), providing more precise quartile tail detail than standard boxplots.
