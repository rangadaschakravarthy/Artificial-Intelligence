# Solutions — Gradient Descent

## Level 1 — Basic Understanding Solutions
### Question 1
1. $\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \nabla L(\mathbf{w}_t)$.
### Question 2
2. Batch GD uses 100% of dataset per update. SGD uses 1 sample per update. Mini-Batch GD uses a subset ($B=32..256$) per update.
### Question 3
3. An Epoch is 1 complete pass through the entire dataset.
### Question 4
4. An Iteration is 1 single parameter update step using 1 batch.
### Question 5
5. $\lceil 1000 / 32 \rceil = 32$ iterations per epoch.

## Level 2 — Calculation Solutions
### Question 1
1. $L'(w) = 2(w-5)$. Step 1: $L'(1) = 2(-4) = -8 \implies w_1 = 1 - 0.2(-8) = 2.6$. Step 2: $L'(2.6) = 2(-2.4) = -4.8 \implies w_2 = 2.6 - 0.2(-4.8) = 3.56$. Approaching $w=5$!
### Question 2
2. \nabla L = [6w_1, 2w_2]^T. At (1, 2), \nabla L = [6, 4]^T. 

$$\mathbf{w}_1 = \begin{bmatrix} 1 \\ 2 \end{bmatrix} - 0.05 \begin{bmatrix} 6 \\ 4 \end{bmatrix} = \begin{bmatrix} 0.7 \\ 1.8 \end{bmatrix}$$

.
### Question 3
3. Because each individual sample (or small mini-batch) gradient is an imperfect noisy approximation of the true full-dataset population gradient.
### Question 4
4. $\lceil 60,000 / 128 \rceil = 469$ iterations per epoch.
### Question 5
5. Mini-Batch GD becomes identical to Batch GD.

## Level 3 — Conceptual Solutions
### Question 1
1. $w_{t+1} = w_t - \eta (a w_t) = (1 - \eta a) w_t$. For $w_t \to 0$ as $t \to \infty$, contraction factor must satisfy $|1 - \eta a| < 1 \implies -1 < 1 - \eta a < 1 \implies 0 < \eta a < 2 \implies 0 < \eta < \frac{2}{a}$.
### Question 2
2. Random mini-batch sampling fluctuations introduce stochastic noise. This noise continuously shakes weights out of sharp narrow local minima that tend to overfit training data, driving parameters toward wider flatter minima.
### Question 3
3. Batch GD requires loading full 100GB dataset into RAM/VRAM to compute 1 gradient. Mini-Batch GD loads only 64MB per batch, fitting easily inside GPU VRAM.
### Question 4
4. DataLoader shuffles sample indices at start of every epoch, ensuring mini-batches contain random uncorrelated samples and preventing cyclic gradient bias.
### Question 5
5. Polyak averaging computes running average of weight history $\bar{\mathbf{w}}_T = \frac{1}{T} \sum_{t=1}^T \mathbf{w}_t$, smoothing out SGD stochastic noise and achieving faster theoretical convergence.

## Level 4 — AI/ML Application Solutions
### Question 1
1. Mini-Batch SGD loops over epochs, shuffles data, splits into batches $B$, computes $\nabla L = \frac{2}{B} X_b^T (X_b w - y_b)$, updates $w = w - \eta \nabla L$. Loss decays smoothly over epochs.
### Question 2
2. Hardware SIMD execution units on NVIDIA GPUs operate in warps of 32 threads. Tensor Cores require matrix dimensions to be multiples of 8 or 16 for hardware parallel alignment.
### Question 3
3. Plain SGD oscillates sideways in 2D Rosenbrock valley. Momentum smooths oscillations, accelerating downhill. Adam scales step sizes adaptively per dimension, reaching minimum fastest.

## Level 5 — Interview Questions Solutions
### Question 1
1. Batch GD on $L$-smooth $m$-strongly convex function achieves linear convergence $L(w_t) - L^* = O(c^t)$ with rate $c < 1$. SGD with noisy gradients $\sigma^2 > 0$ requires decaying learning rate $\eta_t = O(1/t)$, yielding sublinear convergence rate $O(1/\sqrt{t})$.
### Question 2
2. Robbins-Monro conditions: $\sum \eta_t = \infty$ guarantees step sizes accumulate to infinite distance, allowing weights to reach far-away global minimum. $\sum \eta_t^2 < \infty$ guarantees step variance shrinks to 0, ensuring exact convergence without perpetual oscillation.
### Question 3
3. Hogwild! algorithm allows multiple parallel CPU worker threads to read/write to shared memory weight vector $\mathbf{w}$ without lock synchronization. Works because sparse updates mutate different weight indices with minimal overwrite conflict.
### Question 4
4. Gradient Accumulation computes forward/backward passes for $K$ micro-batches of size $B_{micro}$, accumulating gradients in `.grad` buffer (`loss.backward()`) without calling `optimizer.step()`. Calls `optimizer.step()` and `zero_grad()` every $K$ steps, simulating effective batch size $B_{effective} = K \times B_{micro}$.
### Question 5
5. PyTorch DDP spawns 1 process per GPU. Each GPU computes local mini-batch gradients independently. Ring-AllReduce algorithm communicates gradients across GPUs via ring topology, computing exact global average gradient in $2(K-1)$ transfer steps before calling optimizer step.
