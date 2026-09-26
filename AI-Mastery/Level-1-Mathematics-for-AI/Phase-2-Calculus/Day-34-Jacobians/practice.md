# Practice Exercises — Jacobians

## Level 1 — Basic Understanding
1. What is a Jacobian matrix?
2. If a vector function maps $\mathbb{R}^3 \rightarrow \mathbb{R}^2$, what are the dimensions of its Jacobian matrix?
3. Given 

$$\mathbf{f}(x, y) = \begin{bmatrix} x + y \\ 2x y \end{bmatrix}$$

, find partial derivatives for row 1 and row 2.
4. What is the Jacobian matrix of linear function $\mathbf{f}(\mathbf{x}) = \mathbf{A}\mathbf{x}$?
5. What does a Jacobian determinant $|\det(\mathbf{J})| = 1$ signify geometrically?

## Level 2 — Calculation
1. Compute Jacobian matrix for 

$$\mathbf{f}(x, y) = \begin{bmatrix} x^2 + y^2 \\ 3x y \end{bmatrix}$$

 at point (1, 2).
2. Compute Jacobian determinant $|\det(\mathbf{J})|$ for Polar Coordinate transformation $x = r \cos\theta, y = r \sin\theta$.
3. Given 

$$\mathbf{f}(x_1, x_2, x_3) = \begin{bmatrix} x_1^2 \\ x_2 x_3 \end{bmatrix}$$

, state shape and compute Jacobian matrix.
4. Compute Jacobian matrix of Softmax function for 2 outputs $S_1 = \frac{e^{z_1}}{e^{z_1}+e^{z_2}}, S_2 = \frac{e^{z_2}}{e^{z_1}+e^{z_2}}$.
5. What is the linear Taylor approximation of vector function $\mathbf{f}(\mathbf{x})$ near $\mathbf{x}_0$ using Jacobian $\mathbf{J}$?

## Level 3 — Conceptual
1. Prove that the Jacobian of composite function $\mathbf{h}(\mathbf{x}) = \mathbf{f}(\mathbf{g}(\mathbf{x}))$ satisfies $\mathbf{J}_{h}(\mathbf{x}) = \mathbf{J}_f(\mathbf{g}(\mathbf{x})) \mathbf{J}_g(\mathbf{x})$ (Vector Chain Rule).
2. Why is computing full $N \times N$ Jacobian matrices computationally expensive in deep learning when $N = 1,000,000$?
3. Explain Vector-Jacobian Product (VJP) $v^T J$ in Reverse-Mode Automatic Differentiation.
4. Explain Jacobian-Vector Product (JVP) $J v$ in Forward-Mode Automatic Differentiation.
5. Why do Normalizing Flows require invertible transformations with easily computable Jacobian determinants?

## Level 4 — AI/ML Application
1. In RealNVP Normalizing Flow, coupling layer transforms $(x_1, x_2) \to (y_1, y_2)$ via $y_1 = x_1$ and $y_2 = x_2 e^{s(x_1)} + t(x_1)$. Derive Jacobian matrix and show $\det(\mathbf{J}) = e^{s(x_1)}$.
2. Calculate Jacobian matrix of neural network layer $\mathbf{h} = \text{ReLU}(\mathbf{W}\mathbf{x} + \mathbf{b})$ with respect to input vector $\mathbf{x}$.
3. Use PyTorch `torch.autograd.functional.jacobian()` to evaluate Jacobian of a 2D neural layer.

## Level 5 — Interview Questions
1. Derive change-of-variables theorem for multi-variable continuous probability density functions: $p_{\mathbf{X}}(\mathbf{x}) = p_{\mathbf{Z}}(\mathbf{z}) \left| \det \frac{\partial g^{-1}(\mathbf{x})}{\partial \mathbf{x}} \right|$.
2. Explain Continuous Normalizing Flows (CNFs) and Neural ODEs $\frac{d z}{d t} = f(z, t)$, where log-density changes via Trace of Jacobian $\frac{d \log p(z(t))}{d t} = -\text{Tr}\left(\frac{\partial f}{\partial z}\right)$ (Liouville's Theorem / Jacobi's Formula).
3. What is a Sieve/Skyscraper Jacobian structure in autoregressive flows (e.g. MAF/IAF)?
4. Explain Jacobian Regularization for improving model robustness against adversarial perturbations ($L_{reg} = ||\mathbf{J}_f(\mathbf{x})||_F^2$).
5. How does SVD of Jacobian matrix $\mathbf{J} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^T$ characterize local geometric stretching and local principal directions of a non-linear manifold mapping?
