# Day 125 Practice Questions: Concatenation

## Level 1 — Basic
1. What parameter controls whether `pd.concat()` stacks rows or appends columns?
2. Why is `ignore_index=True` recommended for vertical concatenation?
3. What is the default join behavior (`join` parameter) in `pd.concat()`?
4. How do you append a Series `s` as a new column to a DataFrame `df`?
5. What happens when concatenating DataFrames vertically if one DataFrame contains extra columns?

## Level 2 — Coding
1. Vertically concatenate `df1` and `df2` and reset index labels.
2. Horizontally concatenate `df_left` and `df_right` using `join='inner'`.
3. Concatenate a list of 4 DataFrames `[df1, df2, df3, df4]` along `axis=0`.
4. Use the `keys` parameter to create a MultiIndex identifying source batches `['Q1', 'Q2']`.
5. Filter out non-matching columns during vertical concatenation using `join='inner'`.

## Level 3 — Data Analysis
1. Combine 12 monthly sales log DataFrames into a single yearly analysis DataFrame.
2. Stitched together 3 parallel feature extraction outputs on sample index.
3. Concatenate historical price data from 2021, 2022, and 2023.
4. Combine web-scraped search result pages into a single dataset.
5. Create a unified sensor reading dataset by stacking telemetry batches.

## Level 4 — Debugging
1. Fix memory leak / severe slowdown caused by:
   `master_df = pd.DataFrame(); for file in files: master_df = master_df.append(pd.read_csv(file))`
2. Fix duplicate index issues after vertical concat where `.loc[0]` returns multiple rows.
3. Correct row misalignment when performing horizontal concatenation (`axis=1`) on DataFrames with different row indices.

## Level 5 — AI/ML Application
1. Demonstrate using `pd.concat()` to merge train and test sets for unified one-hot encoding, then re-splitting.
2. How does row order preservation in `pd.concat()` prevent feature-target swapping in ML training pipelines?
3. Concatenate dynamic predictions from 3 ensemble models into a meta-feature matrix.

## Level 6 — Interview Questions
1. Compare computational efficiency of `pd.concat()` vs repeated `.append()` calls.
2. What is the difference between `pd.concat()` and `pd.merge()`?
3. How does `pd.concat()` manage memory during concatenation of large DataFrames?
4. How do you handle non-aligned row indices during horizontal concatenation (`axis=1`)?
5. Explain how `keys` parameter creates a MultiIndex during concatenation.
