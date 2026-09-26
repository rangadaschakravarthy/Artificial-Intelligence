# Theory — Backpropagation Mathematics

### 1. Simple Definition
Backpropagation is an efficient application of the chain rule that calculates the exact gradient of a neural network's loss function with respect to every weight in the network by propagating error signals backward from output to input.

### 2. Intuition
Imagine a relay team passing a torch backward. The judge at the finish line calculates the total error score. Each athlete receives the error signal, determines how much their stride contributed to the mistake, adjusts their technique, and hands the error signal back to the previous runner.

### 3. Mathematical Definition
For an $L$-layer neural network with activations $\mathbf{a}^{(l)} = \sigma(\mathbf{z}^{(l)})$ and $\mathbf{z}^{(l)} = \mathbf{W}^{(l)} \mathbf{a}^{(l-1)} + \mathbf{b}^{(l)}$:
1. $\mathbf{\delta}^{(L)} = \nabla_{\mathbf{a}} L \odot \sigma'(\mathbf{z}^{(L)})$
2. $\mathbf{\delta}^{(l)} = ((\mathbf{W}^{(l+1)})^T \mathbf{\delta}^{(l+1)}) \odot \sigma'(\mathbf{z}^{(l)})$
3. $\frac{\partial L}{\partial \mathbf{b}^{(l)}} = \mathbf{\delta}^{(l)}$
4. $\frac{\partial L}{\partial \mathbf{W}^{(l)}} = \mathbf{\delta}^{(l)} (\mathbf{a}^{(l-1)})^T$.

### 4. Notation
$\mathbf{\delta}^{(l)} = \frac{\partial L}{\partial \mathbf{z}^{(l)}} \in \mathbb{R}^{n_l}$. $\mathbf{\Sigma}'(\mathbf{z}^{(l)}) = \text{diag}(\sigma'(\mathbf{z}^{(l)}))$.

### 5. Formula

$$
\mathbf{\delta}^{(l)} = ((\mathbf{W}^{(l+1)})^T \mathbf{\delta}^{(l+1)}) \odot \sigma'(\mathbf{z}^{(l)}) \quad \text{(Equation 2 Recurrence)}
$$

### 6. Symbol-by-Symbol Explanation
- $\mathbf{\delta}^{(l+1)}$: Error vector from layer $l+1$
- $\mathbf{W}^{(l+1)T}$: Transposed weight matrix mapping layer $l$ to $l+1$
- $\odot$: Hadamard element-wise vector product
- $\sigma'(\mathbf{z}^{(l)})$: Vector of activation derivatives at layer $l$

### 7. Step-by-Step Calculation
Proof of Equation 2 (Hidden Layer Delta Recurrence):
By multi-variable chain rule: $\delta_i^{(l)} = \frac{\partial L}{\partial z_i^{(l)}} = \sum_k \frac{\partial L}{\partial z_k^{(l+1)}} \frac{\partial z_k^{(l+1)}}{\partial z_i^{(l)}} = \sum_k \delta_k^{(l+1)} \frac{\partial z_k^{(l+1)}}{\partial z_i^{(l)}}$.
Since $z_k^{(l+1)} = \sum_j W_{k,j}^{(l+1)} a_j^{(l)} + b_k^{(l+1)}$ and $a_i^{(l)} = \sigma(z_i^{(l)})$, we have:
$\frac{\partial z_k^{(l+1)}}{\partial z_i^{(l)}} = \frac{\partial z_k^{(l+1)}}{\partial a_i^{(l)}} \frac{\partial a_i^{(l)}}{\partial z_i^{(l)}} = W_{k,i}^{(l+1)} \sigma'(z_i^{(l)})$.
Substitute back: $\delta_i^{(l)} = \sum_k \delta_k^{(l+1)} W_{k,i}^{(l+1)} \sigma'(z_i^{(l)}) = \left(\sum_k W_{k,i}^{(l+1)} \delta_k^{(l+1)}\right) \sigma'(z_i^{(l)})$.
In vector matrix notation: $\mathbf{\delta}^{(l)} = ((\mathbf{W}^{(l+1)})^T \mathbf{\delta}^{(l+1)}) \odot \sigma'(\mathbf{z}^{(l)})$. Q.E.D.!

### 8. Second Example
Numerical verification of 4 equations on 1-neuron input $\rightarrow$ 1-neuron hidden $\rightarrow$ 1-neuron output network.

### 9. Common Mistakes
Forgetting that backpropagation computes exact analytical gradients via chain rule (it is NOT an approximation like finite differences!).

### 10. AI Connection
Backpropagation allows deep neural networks with billions of parameters (e.g. GPT-4, LLaMA-3) to compute exact loss gradients in a single reverse pass.

### 11. Algorithm Connection
Backpropagation, Reverse-Mode Automatic Differentiation, PyTorch Autograd, TensorFlow.

### 12. Practical Interpretation
Backpropagation converts what would be an impossible $O(M \cdot N)$ gradient computation into a simple $O(M)$ matrix-vector multiplication pass.

### 13. Interview Insight
Q: 'Prove Equation 2 of backpropagation on the whiteboard.' A: Write $\delta_i^{(l)} = \frac{\partial L}{\partial z_i^{(l)}}$, expand using chain rule over all layer $l+1$ nodes $k$, substitute $\frac{\partial z_k^{(l+1)}}{\partial a_i^{(l)}} = W_{k,i}^{(l+1)}$ and $\frac{\partial a_i^{(l)}}{\partial z_i^{(l)}} = \sigma'(z_i^{(l)})$, then convert to matrix form $(\mathbf{W}^{(l+1)T} \mathbf{\delta}^{(l+1)}) \odot \sigma'(\mathbf{z}^{(l)})$.

### 14. Summary
Backpropagation computes exact parameter gradients $\frac{\partial L}{\partial \mathbf{W}^{(l)}} = \mathbf{\delta}^{(l)} (\mathbf{a}^{(l-1)})^T$ using 4 fundamental equations, propagating deltas backward via $\mathbf{\delta}^{(l)} = (\mathbf{W}^{(l+1)T} \mathbf{\delta}^{(l+1)}) \odot \sigma'(\mathbf{z}^{(l)})$.
