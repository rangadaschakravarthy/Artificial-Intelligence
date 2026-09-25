# Examples — Vector Operations

## Example 1 — Very Easy
Adding 2D Vectors: $[1, 3]^T + [4, 2]^T = [1+4, 3+2]^T = [5, 5]^T$.

## Example 2 — Beginner
Gradient Descent Step: $\mathbf{w}_{new} = \mathbf{w}_{old} - \alpha \mathbf{g}$. If $\mathbf{w} = [1.0, 2.0]^T$, $\alpha=0.1$, $\mathbf{g}=[0.4, -0.2]^T$, then $\mathbf{w}_{new} = [1-0.04, 2-(-0.02)]^T = [0.96, 2.02]^T$.

## Example 3 — Intermediate
Linear Combination: $2[1, 0]^T + 3[0, 1]^T = [2, 0]^T + [0, 3]^T = [2, 3]^T$.

## Example 4 — AI/ML Example
Feature Masking (Hadamard): Feature vector $\mathbf{x} = [100, 50, 0.5]^T$, binary mask $\mathbf{m} = [1, 0, 1]^T$. Result $\mathbf{x} \odot \mathbf{m} = [100, 0, 0.5]^T$.

## Example 5 — Real-World Interpretation
Word Vector Arithmetic: $\text{vec('king')} - \text{vec('man')} + \text{vec('woman')} \approx \text{vec('queen')}.
