# Day 113 Solutions: Filtering Data

## Level 1 — Basic
1. `|`
2. `~`
3. `.isin()`
4. `.between()`
5. False (It returns a new filtered DataFrame copy).

## Level 2 — Coding
6. `df[df['Age'] >= 21]`
7. `df[df['City'].isin(['New York', 'London'])]`
8. `df[df['Salary'].between(50000, 100000)]`
9. `df[~(df['Department'] == 'Sales')]` (or `df[df['Department'] != 'Sales']`).
10. `df.query("Score > 80 and Status == 'Active'")`

## Level 3 — Data Analysis
11. Python bitwise operator `&` has higher operator precedence than comparison operators (`>`, `<`). Without parentheses, `10 & df['B']` evaluates first, causing syntax errors.
12. Extracts rows where `'col'` values are **NOT** contained in `vals` (negation of `.isin()`).
13. `2` (Values 20 and 30).
14. `df.query()` is cleaner and avoids verbose `df[...]` repetition. Standard boolean masking is more flexible for custom Python functions.
15. `2` (`.between()` is inclusive by default, matching 1 and 2).

## Level 4 — Debugging
16. Wrap boolean condition expressions in parentheses: `df[(df['col'] > 0)]`.
17. Add parentheses around conditions: `df[(df['A'] > 10) & (df['B'] == 'Y')]`.
18. Reference Python local variables in `query()` using `@` prefix: `min_age = 21; df.query("Age > @min_age")`.

## Level 5 — AI/ML Application
19. `clean_df = df[df['Price'] >= 0.0]`
20. `fraud_df = df[(df['Amount'] > 10000) | (df['Is_Foreign'] == True)]`
21. Filtering enables evaluating ML model precision/recall performance separately across specific demographic cohorts (e.g. `df[df['Age_Group'] == 'Senior']`).

## Level 6 — Interview Solutions
22. `numexpr` avoids creating intermediate temporary array allocations in RAM, compiling string query expressions into multithreaded CPU SIMD instructions.
23. `.str.contains()` checks if pattern exists anywhere within string. `.str.match()` checks if string starts with the regex pattern.
24. Filtering retains original row index labels. Filtered DataFrames have non-consecutive indices requiring `.reset_index(drop=True)` if consecutive integer indices are needed.
25. `df.loc[lambda d: d['Age'] > 25, ['Name', 'Salary']]` allows chaining filtering steps in pipe workflows.
26. Boolean filtering evaluates conditions into 1D `bool_` bitmasks in memory, passing bitmask pointer arrays down to C-level block selection routines.
