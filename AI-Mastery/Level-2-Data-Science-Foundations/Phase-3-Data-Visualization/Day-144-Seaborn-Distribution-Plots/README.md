# Day 144 — Seaborn Distribution Plots

## Learning Objectives
- Visualize continuous univariate and bivariate distributions using `displot()`, `histplot()`, `kdeplot()`, and `ecdfplot()`.
- Compute Kernel Density Estimates (KDE) and Cumulative Distribution Functions (ECDF).
- Analyze joint and marginal distributions using `jointplot()`.

## Prerequisites
- Day 137: Histograms
- Day 142: Seaborn Introduction

## Topics Covered
- Modern distribution API: `sns.displot()`, `sns.histplot()`, `sns.kdeplot()`, `sns.ecdfplot()`
- Kernel Density Estimation (KDE) smoothing bandwidth (`bw_adjust`)
- Empirical Cumulative Distribution Function (`sns.ecdfplot()`)
- Joint distributions and marginal axes using `sns.jointplot()` (kind=`'kde'`|`'scatter'`|`'hex'`)
- Multi-subplot distribution grids using `displot(col='group')`

## Why This Matters
Distribution inspection is essential for verifying normality assumptions, identifying skewness, and tuning ML data scaling.

## Practical Work
- Plot a joint distribution of Height vs Weight with marginal KDE curves using `sns.jointplot()`.

## Difficulty
Intermediate
