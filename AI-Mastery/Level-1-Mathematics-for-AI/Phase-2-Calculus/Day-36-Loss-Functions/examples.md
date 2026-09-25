# Examples — Loss Functions

## Example 1 — Very Easy
MSE Loss: True $y=10$, Pred $\hat{y}=7 \implies L_{MSE} = (10-7)^2 = 9$.

## Example 2 — Beginner
MAE Loss: True $y=10$, Pred $\hat{y}=7 \implies L_{MAE} = |10-7| = 3$.

## Example 3 — Intermediate
BCE Confident Correct: True $y=1$, Pred $\hat{y}=0.99 \implies L = -\ln(0.99) \approx 0.0101$ (Low Loss).

## Example 4 — AI/ML Example
BCE Confident Wrong: True $y=1$, Pred $\hat{y}=0.01 \implies L = -\ln(0.01) \approx 4.605$ (High Loss Penalty!).

## Example 5 — Real-World Interpretation
Categorical Cross-Entropy 3-Class: True $\mathbf{y} = [0, 1, 0]$, Pred $\hat{\mathbf{y}} = [0.1, 0.7, 0.2] \implies L = -\ln(0.7) \approx 0.3567$.
