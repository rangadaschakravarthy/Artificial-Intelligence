# Day 94 — Boolean and Fancy Indexing

## Learning Objectives
- Master Boolean Masking (`arr[mask]`) for conditional data filtering.
- Master Fancy Indexing (`arr[index_array]`) using integer arrays.
- Combine logical operators (`&`, `|`, `~`) for complex query filtering.

## Prerequisites
- Day 92: Indexing
- Day 93: Slicing

## Topics Covered
1. Boolean Masking (`arr[arr > threshold]`)
2. Bitwise Logical Operators in NumPy (`&` AND, `|` OR, `~` NOT)
3. Fancy Indexing with integer arrays/lists
4. 2D Fancy Indexing (`matrix[[r1, r2], [c1, c2]]`)
5. Difference between Views (Slicing) and Copies (Fancy/Boolean Indexing)

## Why This Matters
Filtering dataset rows based on numerical thresholds and conditions is the cornerstone of data cleaning, outlier removal, and exploratory data analysis.

## Real-World Usage
Filtering patient records where `Age > 50` AND `BP > 140` in medical datasets.

## Study Order
1. Read `theory.md`.
2. Review `examples.md`.
3. Complete `practice.md`.
4. Verify using `solution.md`.
5. Run `code.py`.

## Completion Checklist
- [ ] I can filter array elements using boolean masks.
- [ ] I know why to use `&` and `|` instead of Python `and` / `or`.
- [ ] I can select arbitrary rows using integer lists (fancy indexing).
- [ ] I understand that boolean and fancy indexing return **copies**, not views.

## Difficulty
Intermediate
