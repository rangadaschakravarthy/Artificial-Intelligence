# Examples — Calculus for Neural Networks

## Example 1 — Very Easy
Forward Pass Layer 1: $\mathbf{z}^{(1)} = \mathbf{W}^{(1)} \mathbf{x} + \mathbf{b}^{(1)}, \mathbf{a}^{(1)} = \text{ReLU}(\mathbf{z}^{(1)})$.

## Example 2 — Beginner
Forward Pass Layer 2: $\mathbf{z}^{(2)} = \mathbf{W}^{(2)} \mathbf{a}^{(1)} + \mathbf{b}^{(2)}, \mathbf{a}^{(2)} = \text{Softmax}(\mathbf{z}^{(2)})$.

## Example 3 — Intermediate
Output Error Delta: $\mathbf{\delta}^{(2)} = \mathbf{a}^{(2)} - \mathbf{y}$.

## Example 4 — AI/ML Example
Backward Hidden Delta: $\mathbf{\delta}^{(1)} = (\mathbf{W}^{(2)T} \mathbf{\delta}^{(2)}) \odot \text{ReLU}'(\mathbf{z}^{(1)})$.

## Example 5 — Real-World Interpretation
Weight Gradient 1: $\frac{\partial L}{\partial \mathbf{W}^{(1)}} = \mathbf{\delta}^{(1)} \mathbf{x}^T$.
