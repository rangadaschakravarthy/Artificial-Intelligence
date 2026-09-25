# Examples — Backpropagation Mathematics

## Example 1 — Very Easy
Equation 1 (Output Delta): $\mathbf{\delta}^{(L)} = (\mathbf{a}^{(L)} - \mathbf{y})$ for Cross-Entropy.

## Example 2 — Beginner
Equation 2 (Hidden Delta): $\mathbf{\delta}^{(1)} = (\mathbf{W}^{(2)T} \mathbf{\delta}^{(2)}) \odot \sigma'(\mathbf{z}^{(1)})$.

## Example 3 — Intermediate
Equation 3 (Bias Grad): $\frac{\partial L}{\partial \mathbf{b}^{(1)}} = \mathbf{\delta}^{(1)}$.

## Example 4 — AI/ML Example
Equation 4 (Weight Grad): $\frac{\partial L}{\partial \mathbf{W}^{(1)}} = \mathbf{\delta}^{(1)} \mathbf{x}^T$.

## Example 5 — Real-World Interpretation
Numerical Hand Calculation: Step-by-step arithmetic matching Python code.
