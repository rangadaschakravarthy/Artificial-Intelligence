# Examples — Calculus with Python

## Example 1 — Very Easy
SymPy Symbolic: `sp.diff(x**3 + sp.sin(x), x)` $\implies 3x^2 + \cos(x)$.

## Example 2 — Beginner
SciPy Numerical Optimization: `scipy.optimize.minimize(f, x0)` finding minimum point.

## Example 3 — Intermediate
PyTorch Autograd: `x = torch.tensor(3.0, requires_grad=True); y = x**2; y.backward(); print(x.grad)` $\implies 6.0$.

## Example 4 — AI/ML Example
Gradient Check: Comparing PyTorch `.grad` against central difference numerical gradient.

## Example 5 — Real-World Interpretation
Detached Computation: `tensor.detach()` stopping gradient flow in PyTorch.
