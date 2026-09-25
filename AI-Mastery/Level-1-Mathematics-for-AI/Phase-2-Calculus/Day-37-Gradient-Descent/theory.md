# Theory — Gradient Descent

### 1. Simple Definition
Gradient Descent is an iterative optimization algorithm that takes small steps downhill along the loss surface by subtracting the gradient vector $\nabla L$ scaled by a learning rate $\eta$.

### 2. Intuition
Imagine walking down a foggy mountain in the dark. At each step, you feel around with your feet to find the steepest downhill slope, then take one small step in that direction. Repeating this gets you to the valley bottom!

### 3. Mathematical Definition
Given objective function $L(\mathbf{w})$, Gradient Descent updates parameter vector $\mathbf{w} \in \mathbb{R}^d$ iteratively:
$$\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \nabla L(\mathbf{w}_t)$$
where $\eta > 0$ is the learning rate hyperparameter.

### 4. Notation
$\mathbf{w}_t$: Weights at iteration $t$. $\eta$: Learning rate. $\nabla L(\mathbf{w}_t)$: Gradient vector.

### 5. Formula
$$\text{Batch GD: } \mathbf{w}_{t+1} = \mathbf{w}_t - \eta \frac{1}{N} \sum_{i=1}^N \nabla L_i(\mathbf{w}_t)$$
$$\text{SGD: } \mathbf{w}_{t+1} = \mathbf{w}_t - \eta \nabla L_i(\mathbf{w}_t)$$
$$\text{Mini-Batch: } \mathbf{w}_{t+1} = \mathbf{w}_t - \eta \frac{1}{B} \sum_{i \in B} \nabla L_i(\mathbf{w}_t)$$

### 6. Symbol-by-Symbol Explanation
- $N$: Full dataset size
- $B$: Mini-batch size (e.g. 32, 64, 128)
- $\eta$: Learning rate scalar step size

### 7. Step-by-Step Calculation
Optimize $L(w) = w^2$ starting at $w_0 = 4.0$ with learning rate $\eta = 0.1$:
1. Derivative $L'(w) = 2w$.
2. Step 1: $L'(4) = 8.0 \implies w_1 = 4.0 - 0.1(8.0) = 4.0 - 0.8 = 3.2$.
3. Step 2: $L'(3.2) = 6.4 \implies w_2 = 3.2 - 0.1(6.4) = 3.2 - 0.64 = 2.56$.
4. Step 3: $w_3 = 2.56 - 0.1(5.12) = 2.048$. Weight rapidly approaches minimum $w^* = 0$!

### 8. Second Example
Multi-variable step for $L(w_1, w_2) = w_1^2 + 2w_2^2$ starting at $\mathbf{w}_0 = [2.0, 3.0]^T, \eta = 0.1$:
$\nabla L = [2w_1, 4w_2]^T = [4.0, 12.0]^T$.
$\mathbf{w}_1 = \begin{bmatrix} 2.0 \\ 3.0 \end{bmatrix} - 0.1 \begin{bmatrix} 4.0 \\ 12.0 \end{bmatrix} = \begin{bmatrix} 1.6 \\ 1.8 \end{bmatrix}$.

### 9. Common Mistakes
Adding the gradient instead of subtracting it (causes gradient ASCENT toward infinite loss!); confusing Epochs (full dataset passes) with Iterations (batch parameter updates).

### 10. AI Connection
Mini-batch SGD ($B=32..256$) is the universal standard for deep learning. It balances GPU SIMD parallel memory utilization with stochastic gradient noise for escaping saddle points.

### 11. Algorithm Connection
Batch Gradient Descent, SGD, Mini-Batch SGD, PyTorch `optimizer.step()`, TensorFlow `apply_gradients()`.

### 12. Practical Interpretation
An Epoch is 1 complete pass through all $N$ dataset samples. Number of iterations per epoch $= \frac{N}{B}$.

### 13. Interview Insight
Q: 'Why is Mini-Batch SGD preferred over pure Batch GD for deep learning?' A: 1) Batch GD requires computing gradients over millions of samples before 1 update (extremely slow and RAM intensive). 2) Mini-batch SGD provides frequent weight updates and SIMD GPU efficiency. 3) Mini-batch noise helps escape saddle points.

### 14. Summary
Gradient Descent updates parameters downhill: $\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \nabla L(\mathbf{w}_t)$. Mini-batch SGD balances GPU parallelization speed and stochastic noise.
