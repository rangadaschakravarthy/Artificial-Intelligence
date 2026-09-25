# Practice Exercises — Calculus with Python

## Level 1 — Basic Understanding
1. What are the 3 main types of differentiation in Python?
2. Which Python library is used for symbolic calculus?
3. Which PyTorch flag enables gradient tracking on a tensor?
4. Why must you call `optimizer.zero_grad()` before calling `loss.backward()` in PyTorch?
5. What PyTorch method computes gradients backward along the computational graph?

## Level 2 — Calculation
1. Use SymPy to compute the 2nd derivative of $f(x) = x^4 + 3x^2 - 5$.
2. Use SciPy `scipy.optimize.minimize` to find the minimum of $f(x) = (x - 4)^2 + 3$.
3. Write PyTorch code to compute derivative of $y = 3x^2 + 5x + 2$ at $x = 2.0$.
4. Explain what `with torch.no_grad():` does during PyTorch inference.
5. Write a Python function that performs a Gradient Check between Autograd and Central Difference gradients.

## Level 3 — Conceptual
1. Explain how PyTorch builds the dynamic execution graph during forward execution (Tape-based Automatic Differentiation).
2. Compare Forward-Mode AD vs Reverse-Mode AD in terms of input vs output dimensions.
3. Why does SymPy suffer from Expression Explosion when differentiating deep composite functions?
4. Explain how JAX uses `jax.grad()` and `jax.jit()` XLA compilation for ultra-fast GPU differentiation.
5. What happens if you try to compute `.backward()` on a non-scalar PyTorch tensor without specifying `gradient` argument?

## Level 4 — AI/ML Application
1. Write a complete Python script implementing a Gradient Checker for a custom 2-layer neural network class. Verify relative error $< 10^{-7}$.
2. Demonstrate PyTorch Autograd gradient tracking visualization using `torchviz` or inspecting `grad_fn` pointers.
3. Explain how higher-order derivatives (e.g. Hessian-vector products) are computed in PyTorch using `torch.autograd.grad(create_graph=True)`.

## Level 5 — Interview Questions
1. Implement a minimal Automatic Differentiation Engine (Micrograd-style `Value` class) in 50 lines of pure Python supporting `+`, `*`, `relu`, and `backward()`.
2. Explain Dual Numbers ($a + b \epsilon$ where $\epsilon^2 = 0$) and how they implement Forward-Mode AD natively in programming languages.
3. Explain Vector-Jacobian Product (VJP) in PyTorch autograd engine: $\mathbf{v}^T \mathbf{J} = \text{torch.autograd.grad}(outputs, inputs, grad_outputs=v)$.
4. How does JAX `vmap` (vectorized map) combine with `jax.grad` to compute batch Jacobians efficiently?
5. Explain how PyTorch handles non-differentiable ops (e.g. `torch.max()`, `torch.abs()`) using subgradients during Autograd.
