# Examples — Day 276: What is Classification?

## Example 1 — Extremely Simple
Binary decision: `if prob > 0.5: predict 1 else: predict 0`.

## Example 2 — Basic Numerical Example
Computing Gini Impurity for a set of 10 items containing 7 Class A and 3 Class B:

$$
\text{Gini} = 1 - \left[\left(\frac{7}{10}\right)^2 + \left(\frac{3}{10}\right)^2\right] = 1 - (0.49 + 0.09) = 1 - 0.58 = 0.42
$$

## Example 3 — Real Dataset Example (Iris Species Classification)
Multiclass classification of 3 iris species using sepal/petal measurements.

## Example 4 — Machine Learning Pipeline Example
`StandardScaler` + `LogisticRegression` / `RandomForestClassifier` with Cross-Validation.

## Example 5 — Real-World Scenario (Fraud Detection)
Tuning classification decision threshold to $0.15$ to maximize Recall for rare fraud transactions.

## Example 6 — Interview-Style Example
Explaining why Support Vector Machines maximize margin $\frac{2}{\|\mathbf{w}\|}$ and how the kernel trick computes scalar products in high-dimensional feature spaces implicitly.
