# Day 64 Solutions: Data Types

## Level 1: Basic Concepts
1. Nominal, Ordinal, Interval, Ratio.
2. Nominal (numbers are arbitrary labels).
3. Weight, Height, Income, Distance.
4. Education Level (Bachelors, Masters, PhD).
5. Strictly no (median or mode is appropriate).

## Level 2: Calculation
6. Red=[1,0,0], Green=[0,1,0], Blue=[0,0,1], Red=[1,0,0].
7. Low=0, Medium=1, High=2 => [0, 2, 1, 0].
8. [0.0, 0.25, 0.5, 0.75, 1.0].
9. [-1.0, 0.0, 1.0].
10. Kelvin is Ratio (absolute zero); Celsius is Interval.

## Level 3: Conceptual
11. Kelvin has a true physical absolute zero (0 K = no thermal energy).
12. Categorical strings cannot be subtracted numerically.
13. Including all k one-hot categories creates perfect multicollinearity (sum to 1); drop one category (k-1).
14. Discrete because whole numbers; ratio because 0 means zero occurrences.
15. One-hot encoding 10,000 zip codes adds 10,000 sparse columns.

## Level 4: AI Applications
16. Replaces category with target mean, keeping 1 column.
17. Min-Max or Standard Scaling (so large-scale features don't dominate distance).
18. Embeddings learn dense continuous representations (e.g. 768-D) instead of huge sparse 50,000-D vectors.
19. Ordinal: Mode / Missing Category; Continuous: Median / Mean.
20. Split criteria depends on rank order of values, not absolute scale.

## Level 5: Interview Solutions
21. Identify types -> Impute missing -> OneHot/Target encode Nominal -> Label encode Ordinal -> Scale Continuous -> Concatenate.
22. Transform periodic features (e.g. hours 0-23) using sin(2pi*t/24) and cos(2pi*t/24) to preserve continuity across midnight.
23. Ratio has a non-arbitrary absolute zero point allowing multiplication/division; interval lacks true zero.
