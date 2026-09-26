# Day 156 Solutions: Encoding

## Level 1 — Basic
1. Machine learning algorithms perform matrix multiplication and distance calculations requiring numerical inputs in $\mathbb{R}^d$.
2. One-Hot Encoding.
3. Frequency Encoding replaces each category label with its proportion or frequency of occurrence in the dataset.

## Level 2 — Coding
1. `df['Count_Encoded'] = df['Cat'].map(df['Cat'].value_counts())`

## Level 3 — Data Analysis
1. One-Hot Encoding creates 1,000 new sparse columns ($N 	imes 1000$ matrix expansion). Target Encoding replaces the categorical column in-place with a single numeric mean column ($N 	imes 1$ matrix), requiring 1000x less memory.
