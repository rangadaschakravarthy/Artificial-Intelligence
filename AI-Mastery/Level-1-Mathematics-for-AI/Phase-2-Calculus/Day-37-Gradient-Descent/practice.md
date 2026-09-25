# Practice Exercises — Gradient Descent

## Level 1 — Basic Understanding
1. Write the Gradient Descent parameter update rule.
2. What is the difference between Batch GD, SGD, and Mini-Batch GD?
3. What is an Epoch?
4. What is an Iteration?
5. If dataset size $N = 1000$ and mini-batch size $B = 32$, how many iterations make up 1 epoch?

## Level 2 — Calculation
1. Perform 2 steps of GD for $L(w) = (w - 5)^2$ starting at $w_0 = 1.0$ with $\eta = 0.2$.
2. Given loss $L(w_1, w_2) = 3w_1^2 + w_2^2$, compute gradient $\nabla L$ at $\mathbf{w}_0 = [1, 2]^T$ and calculate updated weights for $\eta = 0.05$.
3. Why does SGD produce a noisy 'zig-zag' path on the loss surface compared to smooth Batch GD?
4. Calculate dataset iterations for $N = 60,000$ images (MNIST) with batch size $B = 128$.
5. What happens if mini-batch size $B = N$?

## Level 3 — Conceptual
1. Prove that for quadratic loss $L(w) = \frac{1}{2} a w^2$, Gradient Descent converges to $w^* = 0$ if and only if $0 < \eta < \frac{2}{a}$.
2. Explain why gradient noise in SGD acts as an implicit regularizer, preventing overfitting.
3. Compare memory footprint: Batch GD vs Mini-Batch GD for a 100GB dataset.
4. Explain how Data Loaders (`torch.utils.data.DataLoader`) handle dataset shuffling before each epoch in mini-batch SGD.
5. What is the Polyak-Ruppert Averaging of SGD weight trajectories?

## Level 4 — AI/ML Application
1. Write a Python function implementing Mini-Batch SGD from scratch for Linear Regression. Train for 10 epochs and plot loss decay curve.
2. Explain why GPU Tensor Cores are underutilized when mini-batch size $B < 16$ or not a multiple of 8.
3. Compare SGD vs Momentum vs Adam optimization paths on 2D Rosenbrock banana loss surface.

## Level 5 — Interview Questions
1. Derive convergence rate of Batch GD $O(1/t)$ vs SGD $O(1/\sqrt{t})$ on strongly convex functions.
2. Explain Robbins-Monro conditions for SGD learning rate decay: $\sum_{t=1}^\infty \eta_t = \infty$ and $\sum_{t=1}^\infty \eta_t^2 < \infty$.
3. Explain Asynchronous SGD (Hogwild! algorithm) for parallel multi-core gradient updates without locks.
4. What is Gradient Accumulation and how does it simulate batch size $B = 1024$ when GPU VRAM only fits $B = 32$?
5. Explain Distributed Data Parallel (DDP) All-Reduce gradient synchronization across multi-node GPU clusters.
