# Theory — Calculus for Neural Networks

### 1. Simple Definition
Calculus for neural networks uses the chain rule to pass error signals backward from the final loss output through each layer, telling every weight matrix how to adjust to reduce overall error.

### 2. Intuition
Think of a relay race in reverse. The final output judge reports how much error occurred. Layer 2 receives the error signal, adjusts its weights, and passes the remaining error signal back to Layer 1.

### 3. Mathematical Definition
Layer $l$ Forward: $\mathbf{z}^{(l)} = \mathbf{W}^{(l)} \mathbf{a}^{(l-1)} + \mathbf{b}^{(l)}$, $\mathbf{a}^{(l)} = \sigma(\mathbf{z}^{(l)})$.
Error Delta: $\mathbf{\delta}^{(l)} = \frac{\partial L}{\partial \mathbf{z}^{(l)}}$.
Backward Recurrence: $\mathbf{\delta}^{(l)} = (\mathbf{W}^{(l+1)T} \mathbf{\delta}^{(l+1)}) \odot \sigma'(\mathbf{z}^{(l)})$.
Gradients: $\frac{\partial L}{\partial \mathbf{W}^{(l)}} = \mathbf{\delta}^{(l)} (\mathbf{a}^{(l-1)})^T$, $\frac{\partial L}{\partial \mathbf{b}^{(l)}} = \mathbf{\delta}^{(l)}$.

### 4. Notation
$\mathbf{z}^{(l)}$: Pre-activation vector. $\mathbf{a}^{(l)}$: Activated vector. $\mathbf{\delta}^{(l)}$: Error delta vector for layer $l$.

### 5. Formula
$$\mathbf{\delta}^{(L)} = (\mathbf{a}^{(L)} - \mathbf{y}) \quad \text{(Output layer delta for Cross-Entropy)}$$
$$\mathbf{\delta}^{(l)} = (\mathbf{W}^{(l+1)T} \mathbf{\delta}^{(l+1)}) \odot \sigma'(\mathbf{z}^{(l)}) \quad \text{(Hidden layer delta recurrence)}$$

### 6. Symbol-by-Symbol Explanation
- $\mathbf{\delta}^{(l+1)}$: Error delta from next layer
- $\mathbf{W}^{(l+1)T}$: Transposed weight matrix of next layer
- $\odot$: Hadamard (element-wise) product
- \sigma'(\mathbf{z}^{(l)}): Derivative of layer $l$ activation function

### 7. Step-by-Step Calculation
Compute output layer delta $\mathbf{\delta}^{(2)}$ for single output with Sigmoid Cross-Entropy loss:
Let $\hat{y} = a^{(2)} = 0.8$, target $y = 1.0$.
Output delta $\delta^{(2)} = a^{(2)} - y = 0.8 - 1.0 = -0.2$.
Let hidden activation $\mathbf{a}^{(1)} = [0.5, 0.6]^T$.
Weight gradient $\frac{\partial L}{\partial \mathbf{W}^{(2)}} = \delta^{(2)} (\mathbf{a}^{(1)})^T = -0.2 [0.5, 0.6] = [-0.10, -0.12]$.

### 8. Second Example
Propagate error delta to hidden layer $\mathbf{\delta}^{(1)}$:
Let $\mathbf{W}^{(2)} = [2.0, 1.0]$. $\mathbf{W}^{(2)T} \delta^{(2)} = \begin{bmatrix} 2.0 \\ 1.0 \end{bmatrix} (-0.2) = \begin{bmatrix} -0.4 \\ -0.2 \end{bmatrix}$.
Let $\sigma'(\mathbf{z}^{(1)}) = [0.25, 0.24]^T$.
Hidden delta $\mathbf{\delta}^{(1)} = \begin{bmatrix} -0.4 \\ -0.2 \end{bmatrix} \odot \begin{bmatrix} 0.25 \\ 0.24 \end{bmatrix} = \begin{bmatrix} -0.100 \\ -0.048 \end{bmatrix}$.

### 9. Common Mistakes
Forgetting element-wise Hadamard product $\odot$ when applying activation derivative $\sigma'(\mathbf{z}^{(l)})$; getting weight gradient matrix order reversed.

### 10. AI Connection
This 4-equation calculus framework powers all Backpropagation engines in PyTorch, TensorFlow, Caffe, and JAX.

### 11. Algorithm Connection
Backpropagation Algorithm, Multi-Layer Perceptrons (MLPs), PyTorch Autograd, Deep Learning.

### 12. Practical Interpretation
Error delta $\mathbf{\delta}^{(l)}$ summarizes all downstream error responsibility for node $l$. Computing deltas recursively avoids duplicate derivative evaluations.

### 13. Interview Insight
Q: 'Write down the 4 fundamental equations of Backpropagation.' A: 1) Output delta $\mathbf{\delta}^{(L)} = \nabla_{\mathbf{a}} L \odot \sigma'(\mathbf{z}^{(L)})$, 2) Hidden delta $\mathbf{\delta}^{(l)} = (\mathbf{W}^{(l+1)T} \mathbf{\delta}^{(l+1)}) \odot \sigma'(\mathbf{z}^{(l)})$, 3) Bias gradient $\frac{\partial L}{\partial \mathbf{b}^{(l)}} = \mathbf{\delta}^{(l)}$, 4) Weight gradient $\frac{\partial L}{\partial \mathbf{W}^{(l)}} = \mathbf{\delta}^{(l)} (\mathbf{a}^{(l-1)})^T$.

### 14. Summary
Calculus for neural networks propagates error deltas backward: $\mathbf{\delta}^{(l)} = (\mathbf{W}^{(l+1)T} \mathbf{\delta}^{(l+1)}) \odot \sigma'(\mathbf{z}^{(l)})$. Weight gradients equal outer product of layer delta and previous activation: $\mathbf{\delta}^{(l)} (\mathbf{a}^{(l-1)})^T$.
