# Examples — Dot Product

## Example 1 — Very Easy
Basic 2D Dot Product: $[3, 4]^T \cdot [1, 2]^T = 3(1) + 4(2) = 3 + 8 = 11$.

## Example 2 — Beginner
Neuron Forward Pass: Input $\mathbf{x} = [0.8, 0.2, 0.5]^T$, weights $\mathbf{w} = [2.0, -1.0, 3.0]^T$, bias $b = 0.5$.
$z = \mathbf{w}^T \mathbf{x} + b = (0.8)(2) + (0.2)(-1) + (0.5)(3) + 0.5 = 1.6 - 0.2 + 1.5 + 0.5 = 3.4$.

## Example 3 — Intermediate
Orthogonal Check: $\mathbf{a} = [1, 2]^T, \mathbf{b} = [-2, 1]^T$. $\mathbf{a} \cdot \mathbf{b} = 1(-2) + 2(1) = 0$. $\theta = 90^\circ$.

## Example 4 — AI/ML Example
Transformer Query-Key Attention Score: Query $Q = [1, 0, 1]^T$, Key $K = [0.5, 0.5, 0.0]^T$.
$Score = Q \cdot K = 1(0.5) + 0(0.5) + 1(0) = 0.5$.

## Example 5 — Real-World Interpretation
Feature Selection Weighting: Customer profile dot product with product preference vector.
