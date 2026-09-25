# Solutions — Calculus with Python

## Level 1 — Basic Understanding Solutions
### Question 1
1. 1) Symbolic Differentiation (SymPy), 2) Numerical Differentiation (SciPy/NumPy), 3) Automatic Differentiation (PyTorch/JAX).
### Question 2
2. SymPy (`import sympy as sp`).
### Question 3
3. `requires_grad=True`.
### Question 4
4. Because PyTorch ACCUMULATES (adds) gradients into `.grad` buffers on every backward call. Failing to zero gradients causes old gradients to pollute new updates.
### Question 5
5. `loss.backward()`.

## Level 2 — Calculation Solutions
### Question 1
1. `x = sp.Symbol('x'); f = x**4 + 3*x**2 - 5; sp.diff(f, x, 2)` $\implies 12x^2 + 6$.
### Question 2
2. `from scipy.optimize import minimize; res = minimize(lambda x: (x-4)**2 + 3, x0=0); print(res.x)` $\implies [4.0]$.
### Question 3
3. `x = torch.tensor(2.0, requires_grad=True); y = 3*x**2 + 5*x + 2; y.backward(); print(x.grad)` $\implies 17.0$.
### Question 4
4. Deactivates autograd engine tracking, reducing VRAM memory usage and speeding up forward pass computation during model validation/inference.
### Question 5
5. Computes `rel_error = norm(g_auto - g_num) / (norm(g_auto) + norm(g_num))`. If `rel_error < 1e-7`, gradient implementation is correct.

## Level 3 — Conceptual Solutions
### Question 1
1. As PyTorch code runs, autograd records operations in a dynamic Directed Acyclic Graph (DAG). Nodes are operations, edges are tensor inputs/outputs. `backward()` traverses graph backward executing recorded gradient closures.
### Question 2
2. Forward-mode AD: $O(N_{inputs})$ passes, efficient when $N_{inputs} \ll N_{outputs}$. Reverse-mode AD: $O(N_{outputs})$ passes, efficient when $N_{outputs} \ll N_{inputs}$ (e.g. 1 scalar Loss $L$).
### Question 3
3. Repeated application of product and quotient rules in symbolic math expands expressions exponentially (e.g. differentiating a 50-step function creates millions of duplicate symbolic terms).
### Question 4
4. JAX uses functional transformations: `jax.grad()` transforms a Python function into its exact gradient function using reverse AD, and `jax.jit()` compiles it into optimized GPU XLA machine code.
### Question 5
5. PyTorch throws `RuntimeError: grad can be implicitly created only for scalar outputs`. Must pass gradient tensor matching output shape: `y.backward(gradient=torch.ones_like(y))`.

## Level 4 — AI/ML Application Solutions
### Question 1
1. Script loops over all parameters $\mathbf{w}_i$, computes autograd gradient $\mathbf{g}_{auto}$, computes central difference $\mathbf{g}_{num} = \frac{L(w_i+\epsilon) - L(w_i-\epsilon)}{2\epsilon}$, calculates relative norm error, and asserts `< 1e-7`.
### Question 2
2. Inspecting `y.grad_fn` prints operation node type (e.g. `<AddBackward0>`, `<MulBackward0>`). `y.grad_fn.next_functions` points to parent input nodes, visualizing computation graph.
### Question 3
3. Setting `create_graph=True` in `torch.autograd.grad(loss, w, create_graph=True)` builds a backward computational graph for first derivatives, allowing calling `.backward()` again to compute 2nd derivatives and Hessian products.

## Level 5 — Interview Questions Solutions
### Question 1
1. Build class `Value`: tracks `data`, `grad`, `_prev` set of parents, `_op` string. Define `__add__` and `__mul__` with local backward closures. `backward()` performs topological sort on graph and executes `_backward()` closures.
### Question 2
2. Dual number $x = a + b\epsilon$ where $\epsilon^2 = 0$. Taylor expansion $f(a + b\epsilon) = f(a) + f'(a)b\epsilon$. Real part stores function value, dual part stores exact derivative in 1 forward pass without subtraction error!
### Question 3
3. Vector-Jacobian Product: `torch.autograd.grad(outputs=Y, inputs=X, grad_outputs=v)` evaluates $v^T J$, multiplying gradient vector $v$ by Jacobian matrix of mapping $Y = f(X)$.
### Question 4
4. `jax.vmap(jax.grad(f))` applies automatic differentiation across an entire mini-batch in parallel, compiling batch Jacobian computation into vectorized XLA GPU instructions.
### Question 5
5. PyTorch defines subgradients for non-smooth ops: `torch.max(0, x)` sets gradient to 1 for $x > 0$, 0 for $x < 0$, and 0 at $x = 0$. `torch.abs(x)` sets gradient to $\text{sign}(x)$ and 0 at $x=0$.
