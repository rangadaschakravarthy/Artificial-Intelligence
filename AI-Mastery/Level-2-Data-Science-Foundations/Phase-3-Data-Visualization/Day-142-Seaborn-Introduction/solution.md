# Day 142 Solutions: Seaborn Introduction

## Level 1 — Basic
1. Matplotlib.
2. `hue`.
3. `'darkgrid'`, `'whitegrid'`, `'ticks'`.

## Level 2 — Coding
1. `sns.set_theme(style='darkgrid', palette='muted')`
2. `sns.scatterplot(data=df, x='Height', y='Weight', hue='Gender')`

## Level 3 — Data Analysis
1. Raw Matplotlib requires writing custom `for` loops over category groups to assign colors. Seaborn handles category grouping, color mapping, and legend generation automatically in a single function call.
