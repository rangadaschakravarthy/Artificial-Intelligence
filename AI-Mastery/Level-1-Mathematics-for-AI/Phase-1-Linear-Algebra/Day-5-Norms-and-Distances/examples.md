# Examples — Norms and Distances

## Example 1 — Very Easy
L1 Norm Calculation: $\mathbf{v} = [-5, 2, -1]^T \implies ||\mathbf{v}||_1 = |-5| + |2| + |-1| = 5 + 2 + 1 = 8$.

## Example 2 — Beginner
L2 Norm Calculation: $\mathbf{v} = [1, 2, 2]^T \implies ||\mathbf{v}||_2 = \sqrt{1^2 + 2^2 + 2^2} = \sqrt{1 + 4 + 4} = \sqrt{9} = 3$.

## Example 3 — Intermediate
Infinity Norm: $\mathbf{v} = [2, -9, 4]^T \implies ||\mathbf{v}||_\infty = \max(|2|, |-9|, |4|) = 9$.

## Example 4 — AI/ML Example
Vector Normalization (Unit Vector): $\mathbf{v} = [3, 4]^T$, $||\mathbf{v}||_2 = 5$. Unit vector $\hat{\mathbf{v}} = [3/5, 4/5]^T = [0.6, 0.8]^T$. Verify $||\hat{\mathbf{v}}||_2 = \sqrt{0.36 + 0.64} = 1.0$.

## Example 5 — Real-World Interpretation
k-NN Distance Evaluation: Query point $Q=[2,3]$, Neighbor $N=[5,7]$. Euclidean $d = \sqrt{(5-2)^2 + (7-3)^2} = \sqrt{9+16} = 5$.
