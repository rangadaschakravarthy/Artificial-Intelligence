# Day 145 — Seaborn Relationship Plots

## Learning Objectives
- Visualize continuous relationships using `relplot()`, `scatterplot()`, and `lineplot()`.
- Perform automated linear regression modeling visualization using `regplot()` and `lmplot()`.
- Master Pair Plots (`sns.pairplot()`) for pairwise feature matrix exploration.

## Prerequisites
- Day 138: Scatter Plots
- Day 142: Seaborn Introduction

## Topics Covered
- Relational plots API: `sns.relplot()`, `sns.scatterplot()`, `sns.lineplot()`
- Regression plots: `sns.regplot()` vs `sns.lmplot()`
- Logistic / Polynomial regression fits in `lmplot()`
- Pairwise feature exploration using `sns.pairplot()`
- Faceting relationship plots across grid columns (`col='group'`)

## Why This Matters
Pair plots (`pairplot()`) and regression plots (`lmplot()`) provide rapid multi-feature correlation exploration for machine learning feature selection.

## Practical Work
- Generate a `sns.pairplot()` across 4 numeric features colored by target class.

## Difficulty
Intermediate
