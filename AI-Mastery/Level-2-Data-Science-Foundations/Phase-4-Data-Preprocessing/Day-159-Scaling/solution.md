# Day 159 Solutions: Scaling

## Level 1 — Basic
1. Unscaled features with large numerical ranges dominate Euclidean distance calculations, rendering small-scale features irrelevant.
2. Scaling turns elongated loss surface contours into spherical circles, allowing gradient descent steps to converge straight toward the global minimum in fewer iterations.
3. Decision Trees and Random Forests (or XGBoost / Gradient Boosting Trees).

## Level 2 — Coding
1. `dist = np.linalg.norm(vec1 - vec2)`

## Level 3 — Data Analysis
1. Decision Trees select split thresholds on individual features independently ($x_i \ge c$). Scaling or transforming $x_i$ monotonically does not alter the relative ordering of data points, leaving optimal split locations unchanged.
