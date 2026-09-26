# Day 112 — Selecting Data

## Learning Objectives
- Master label-based selection (`df.loc[]`) and integer-based selection (`df.iloc[]`).
- Understand bracket column selection (`df['col']` vs `df[['col1', 'col2']]`).
- Extract rows, columns, single scalar cells (`at`, `iat`), and sub-tables cleanly.

## Prerequisites
- Day 108: DataFrames
- Day 109: Index and Columns

## Topics Covered
1. Column Selection (`df['col']` vs `df[['col']]`)
2. Label-based Indexing (`df.loc[row_label, col_label]`)
3. Positional Integer Indexing (`df.iloc[row_idx, col_idx]`)
4. Fast Scalar Access (`df.at[row_label, col_label]` and `df.iat[row_idx, col_idx]`)
5. View vs Copy rules during DataFrame selection

## Why This Matters
Data selection is performed in every step of data preparation—from picking feature columns to accessing specific data cells.

## Real-World Usage
Extracting feature columns $X = 	ext{df.loc[:, 'feat1':'feat10']}$ and target vector $y = 	ext{df.loc[:, 'target']}$.

## Study Order
1. Read `theory.md`.
2. Review `examples.md`.
3. Complete `practice.md`.
4. Verify using `solution.md`.
5. Run `code.py`.

## Completion Checklist
- [ ] I can select single and multiple columns using bracket notation.
- [ ] I understand the difference between `.loc[]` (label-based) and `.iloc[]` (positional).
- [ ] I can use `.at[]` and `.iat[]` for fast single-cell lookup.
- [ ] I can debug indexing errors and SettingWithCopyWarning.

## Difficulty
Beginner
