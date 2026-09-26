# Theory — Jacobians

### 1. Simple Definition
A Jacobian matrix is a grid that organizes all the partial derivatives of a vector function that takes multiple inputs and produces multiple outputs.

### 2. Intuition
Gradient is for 1 output. Jacobian is for MULTIPLE outputs! Row $i$ of the Jacobian is the gradient vector for output $f_i$.

### 3. Mathematical Definition
For vector-valued function $\mathbf{f}: \mathbb{R}^n \rightarrow \mathbb{R}^m$ given by $\mathbf{f}(\mathbf{x}) = [f_1(\mathbf{x}), \dots, f_m(\mathbf{x})]^T$, the Jacobian matrix $\mathbf{J}_{m \times n} \in \mathbb{R}^{m \times n}$ is:
$$\mathbf{J} = \frac{\partial \mathbf{f}}{\partial \mathbf{x}} = \begin{bmatrix} \frac{\partial f_1}{\partial x_1} & \dots & \frac{\partial f_1}{\partial x_n} \\ \vdots & \ddots & \vdots \\ \frac{\partial f_m}{\partial x_1} & \dots & \frac{\partial f_m}{\partial x_n} \end{bmatrix}$$

### 4. Notation
$\mathbf{J}$, $\frac{\partial \mathbf{f}}{\partial \mathbf{x}}$, $D \mathbf{f}(\mathbf{x})$. Shape is $m \times n$ ($m$ outputs, $n$ inputs).

### 5. Formula
$$\mathbf{J}_{i,j} = \frac{\partial f_i}{\partial x_j}$$
$$\text{Linear Approximation: } \mathbf{f}(\mathbf{x} + \Delta \mathbf{x}) \approx \mathbf{f}(\mathbf{x}) + \mathbf{J} \Delta \mathbf{x}$$

### 6. Symbol-by-Symbol Explanation
- $m$: Number of output components ($f_1, \dots, f_m$)
- $n$: Number of input components ($x_1, \dots, x_n$)
- $\mathbf{J}_{i,j}$: Partial derivative of output $i$ with respect to input $j$

### 7. Step-by-Step Calculation
Find Jacobian of 

$$\mathbf{f}(x, y) = \begin{bmatrix} x^2 y \\ x + 3y \end{bmatrix}$$

 at point (2, 1):
1. Output $f_1(x, y) = x^2 y \implies \frac{\partial f_1}{\partial x} = 2xy, \frac{\partial f_1}{\partial y} = x^2$.
2. Output $f_2(x, y) = x + 3y \implies \frac{\partial f_2}{\partial x} = 1, \frac{\partial f_2}{\partial y} = 3$.
3. Jacobian matrix: 

$$\mathbf{J} = \begin{bmatrix} 2xy & x^2 \\ 1 & 3 \end{bmatrix}$$

.
4. Evaluate at (2, 1): 

$$\mathbf{J}(2, 1) = \begin{bmatrix} 2(2)(1) & 2^2 \\ 1 & 3 \end{bmatrix} = \begin{bmatrix} 4 & 4 \\ 1 & 3 \end{bmatrix}_{2 \times 2}$$

.

### 8. Second Example
Jacobian of linear transformation $\mathbf{f}(\mathbf{x}) = \mathbf{A}\mathbf{x}$: $\mathbf{J} = \frac{\partial (\mathbf{A}\mathbf{x})}{\partial \mathbf{x}} = \mathbf{A}$. The Jacobian of a linear transform is the matrix itself!

### 9. Common Mistakes
Swapping Jacobian rows and columns (Row = Output index $i$, Column = Input index $j$); confusing Jacobian matrix (first partials) with Hessian matrix (second partials).

### 10. AI Connection
Normalizing Flows: Transform latent noise $\mathbf{z}$ to complex image data $\mathbf{x} = g(\mathbf{z})$. Change-of-variables formula requires computing Jacobian determinant $|\det \mathbf{J}_g(\mathbf{z})|$ to track probability density.

### 11. Algorithm Connection
Normalizing Flows (RealNVP, Glow), PyTorch Autograd (Jacobian-Vector Products), Robotics Kinematics, GAN Latent Mapping.

### 12. Practical Interpretation
Jacobian determinant $|\det \mathbf{J}|$ measures local volume expansion or contraction at point $\mathbf{x}$. If $|\det \mathbf{J}| = 1$, transformation is volume-preserving.

### 13. Interview Insight
Q: 'Why do Normalizing Flow architectures (like RealNVP) use Triangular Coupling Layers?' A: Because the Jacobian of a triangular transformation is a triangular matrix, making the Jacobian determinant trivial to compute in $O(n)$ as the product of diagonal entries!

### 14. Summary
Jacobian matrix $\mathbf{J}_{m \times n}$ collects all first partial derivatives $J_{i,j} = \frac{\partial f_i}{\partial x_j}$ for vector functions $\mathbf{f}: \mathbb{R}^n \rightarrow \mathbb{R}^m$. $|\det \mathbf{J}|$ scales probability density volumes.
