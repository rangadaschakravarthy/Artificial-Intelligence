# Day 103 Solutions: NumPy for Machine Learning

## Level 1 — Basic
1. $\hat{y} = X W + b$
2. Sigmoid activation function $\sigma(z) = rac{1}{1 + e^{-z}}$.
3. Softmax activation function.
4. $1.0$ (for $x > 0$; $0$ for $x < 0$).
5. Categorical Cross-Entropy Loss (or Negative Log-Likelihood).

## Level 2 — Coding
6. 
```python
def relu(x): return np.maximum(0, x)
def relu_grad(x): return (x > 0).astype(float)
```
7. `def mse(y_true, y_pred): return np.mean((y_pred - y_true)**2)`
8. 
```python
y = np.array([0, 1, 2])
one_hot = np.eye(3)[y]
```
9. 
```python
def perceptron_forward(X, W, b):
    return 1.0 / (1.0 + np.exp(-(X @ W + b)))
```
10. `l2_loss = 0.5 * lmbda * np.sum(W ** 2)`

## Level 3 — Data Analysis
11. `(100, 5)` (100 samples, 5 output classes/neurons).
12. If model predicts probability $0.0$, $\ln(0) = -\infty$, producing `nan` loss. Epsilon caps probabilities at `[1e-15, 1 - 1e-15]`.
13. Shape of $X$ is $(N, D)$ and error $(\hat{y} - y)$ is $(N, 1)$. Transposing $X^T$ to $(D, N)$ aligns inner dimension $N$, resulting in gradient shape $(D, 1)$ matching weight $W$.
14. `array([0, 0, 5])`
15. `0.5` ($rac{1}{1 + e^0} = rac{1}{2}$).

## Level 4 — Debugging
16. Match inner dimensions: Transpose $W$ or ensure $W$ has shape `(10, 5)` so `(100, 10) @ (10, 5)` evaluates to `(100, 5)`.
17. Reduce learning rate $\eta$ (e.g. from $0.1$ to $0.001$) or scale input features using Z-score standardization.
18. Clip probability predictions: `y_pred = np.clip(y_pred, 1e-15, 1 - 1e-15)`.

## Level 5 — AI/ML Application
19. 
```python
z = X @ W + b
y_hat = 1.0 / (1.0 + np.exp(-z))
y_hat_clip = np.clip(y_hat, 1e-15, 1 - 1e-15)
loss = -np.mean(y * np.log(y_hat_clip) + (1 - y) * np.log(1 - y_hat_clip))
```
20. 
```python
err = y_hat - y
dW = (1.0 / len(X)) * X.T @ err
db = (1.0 / len(X)) * np.sum(err)
W -= lr * dW; b -= lr * db
```
21. PyTorch `nn.Linear(in, out)` stores weight parameter tensor $W$ of shape `(out, in)` and computes forward pass $X W^T + b$ using identical BLAS matrix multiplication.

## Level 6 — Interview Solutions
22. $L = rac{1}{N} (X W - y)^T (X W - y)$. Taking matrix derivative $
abla_W L = rac{2}{N} X^T (X W - y)$.
23. Softmax $rac{e^{z_i}}{\sum e^{z_j}} = rac{e^{z_i - m}}{\sum e^{z_j - m}}$ where $m = \max(z)$. Shifting logits by $-m$ bounds exponents to $e^{z_i - m} \le e^0 = 1$, preventing float overflow.
24. Batch GD uses all $N$ samples per update (stable, slow). SGD uses 1 sample per update (noisy, fast). Mini-Batch SGD uses small batch $B$ (e.g., 32/64) balancing speed and stability.
25. 
```python
# Layer 1
A1 = np.maximum(0, X @ W1 + b1) # ReLU
# Layer 2
output = A1 @ W2 + b2
```
26. Contiguous memory alignment allows matrix multiplication algorithms to pre-fetch blocks into CPU L1/L2 cache registers, maximizing FLOPs/sec throughput.
