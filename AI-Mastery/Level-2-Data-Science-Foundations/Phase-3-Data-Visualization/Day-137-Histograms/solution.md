# Day 137 Solutions: Histograms

## Level 1 — Basic
1. Raw count of observations falling inside that bin interval.
2. `1.0`.
3. Sturges' Rule.

## Level 2 — Coding
1. `ax.hist(data, bins=20, edgecolor='black')`
2. `ax.hist(data, bins=20, cumulative=True)`

## Level 3 — Data Analysis
1. Too few bins (undersampling) oversmoothes distributions, masking bimodal peaks. Too many bins (oversampling) creates noisy, spiky artifacts.
