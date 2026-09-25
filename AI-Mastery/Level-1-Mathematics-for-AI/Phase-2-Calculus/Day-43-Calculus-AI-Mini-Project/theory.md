# Theory — Calculus AI Mini-Project

### 1. Simple Definition
In this Phase 2 Mini-Project, we build a multi-layer neural network framework from scratch using pure calculus equations (forward activations, cross-entropy loss, backpropagation error deltas, and SGD updates).

### 2. Intuition
Building a neural framework from scratch is like building a car engine from raw metal parts. Once you assemble the cylinders (layers), spark plugs (activations), and transmission (backprop), you truly understand how deep learning works!

### 3. Mathematical Definition
Architecture: $Input (2D) \rightarrow Dense(4, ReLU) \rightarrow Dense(1, Sigmoid)$.
Forward: $\mathbf{Z}_1 = \mathbf{X}\mathbf{W}_1^T + \mathbf{b}_1, \mathbf{A}_1 = \text{ReLU}(\mathbf{Z}_1), \mathbf{Z}_2 = \mathbf{A}_1\mathbf{W}_2^T + \mathbf{b}_2, \mathbf{A}_2 = \sigma(\mathbf{Z}_2)$.
Backward: $\mathbf{\Delta}_2 = \mathbf{A}_2 - \mathbf{Y}, \mathbf{\Delta}_1 = (\mathbf{\Delta}_2 \mathbf{W}_2) \odot \text{ReLU}'(\mathbf{Z}_1)$.
Updates: $\mathbf{W}_1 \leftarrow \mathbf{W}_1 - \eta \frac{1}{B} \mathbf{\Delta}_1^T \mathbf{X}$, $\mathbf{W}_2 \leftarrow \mathbf{W}_2 - \eta \frac{1}{B} \mathbf{\Delta}_2^T \mathbf{A}_1$.

### 4. Notation
$\mathbf{X}_{B \times 2}$: Input batch. $\mathbf{W}_1_{4 \times 2}, \mathbf{W}_2_{1 \times 4}$: Weight matrices. $\mathbf{\Delta}_1_{B \times 4}, \mathbf{\Delta}_2_{B \times 1}$: Error delta matrices.

### 5. Formula
$$\mathbf{\Delta}_1 = (\mathbf{\Delta}_2 \mathbf{W}_2) \odot \text{ReLU}'(\mathbf{Z}_1) \quad \text{(Matrix Backprop Delta)}$$

### 6. Symbol-by-Symbol Explanation
- $\mathbf{\Delta}_2$: Output layer error delta ($B \times 1$)
- $\mathbf{W}_2$: Output layer weight matrix ($1 \times 4$)
- $\text{ReLU}'(\mathbf{Z}_1)$: Derivative of ReLU ($B \times 4$)
- $\odot$: Hadamard element-wise product

### 7. Step-by-Step Calculation
XOR Non-linear problem dataset:
Inputs $X = [[0,0], [0,1], [1,0], [1,1]]$. Targets $Y = [[0], [1], [1], [0]]$.
A single linear model CANNOT solve XOR (accuracy stuck at 50%). Our 2-layer calculus neural network folds space and solves XOR with 100% accuracy!

### 8. Second Example
Gradient Check Verification: For every weight $W_{i,j}$, verify $|g_{backprop} - g_{numerical}| < 10^{-7}$.

### 9. Common Mistakes
Initializing weights to all zeros (causes symmetric hidden neurons that receive identical gradients and fail to learn distinct features); initialize with He Normal random weights!

### 10. AI Connection
This mini-project recreates the core functionality of PyTorch `nn.Module`, `nn.Linear`, `nn.ReLU`, `nn.BCELoss`, and `torch.optim.SGD`.

### 11. Algorithm Connection
Deep Neural Networks, Backpropagation, Multi-Layer Perceptrons, Artificial Intelligence Frameworks.

### 12. Practical Interpretation
He Initialization $W \sim \mathcal{N}(0, \sqrt{2/n_{in}})$ prevents vanishing/exploding gradients at iteration 0.

### 13. Interview Insight
Q: 'Why can a 2-layer neural network solve XOR while a single perceptron cannot?' A: A single linear perceptron can only draw 1 straight line decision boundary in 2D space. Hidden layer ReLU neurons transform 2D space non-linearly, making XOR linearly separable in 4D hidden activation space.

### 14. Summary
Phase 2 Mini-Project combines multi-variable calculus, loss derivatives, chain rule error deltas, and SGD parameter updates to build a functional Deep Learning framework in pure NumPy.
