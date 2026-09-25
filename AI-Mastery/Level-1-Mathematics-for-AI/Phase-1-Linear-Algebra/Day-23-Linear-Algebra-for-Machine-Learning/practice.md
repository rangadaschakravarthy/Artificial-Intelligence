# Practice Exercises — Linear Algebra for Machine Learning

## Level 1 — Basic Understanding
1. What linear algebra operation is used to calculate prediction $y$ in a linear regression model?
2. Write the closed-form normal equation for Linear Regression OLS parameters $\mathbf{w}^*$.
3. What is the geometric equation of an SVM decision hyperplane?
4. What linear algebra operation connects input activations to hidden nodes in a neural network layer?
5. Which linear algebra decomposition is used in PCA for feature reduction?

## Level 2 — Calculation
1. Given 2D sample $\mathbf{x} = [2, 5]^T$, weight vector $\mathbf{w} = [0.4, -0.2]^T$, and bias $b = 1.0$, calculate prediction $y = \mathbf{w}^T \mathbf{x} + b$.
2. Calculate distance from point $\mathbf{x}_0 = [3, 4]^T$ to hyperplane $3x_1 + 4x_2 - 5 = 0$ using formula $\frac{|\mathbf{w}^T \mathbf{x}_0 + b|}{||\mathbf{w}||_2}$.
3. A dataset has $N=500$ samples and $d=20$ features. What are the shapes of $\mathbf{X}$, $\mathbf{X}^T \mathbf{X}$, and $\mathbf{w}^*$ in OLS?
4. Write the matrix formula for a 3-layer neural network forward pass.
5. Explain how L2 regularization (Ridge) relates to the L2 norm of weight vector $\mathbf{w}$.

## Level 3 — Conceptual
1. Derive the OLS Normal Equation $(\mathbf{X}^T \mathbf{X}) \mathbf{w} = \mathbf{X}^T \mathbf{y}$ by setting gradient of MSE loss $\nabla_{\mathbf{w}} ||\mathbf{X}\mathbf{w} - \mathbf{y}||_2^2$ to $\mathbf{0}$.
2. Explain why SVM soft-margin optimization uses slack variables and L2 norm weight minimization $\frac{1}{2} ||\mathbf{w}||_2^2$.
3. Show that if activation functions in a deep neural network were purely linear ($f(x) = x$), a 100-layer network collapses to a single matrix multiplication.
4. How does Convolution in CNNs map to sliding dot products between kernel weight tensors and image feature patches?
5. Explain how Softmax classification converts output logit vectors into probability distribution vectors.

## Level 4 — AI/ML Application
1. Build a matrix flowchart showing data transformation from raw input $\mathbf{X}_{32 \times 784}$ to 10-class probability output $\mathbf{P}_{32 \times 10}$ in a 2-layer MLP (`Dense(128) -> ReLU -> Dense(10) -> Softmax`). Specify all matrix shapes.
2. In Linear Regression, if $\mathbf{X}^T \mathbf{X}$ is singular, explain how Ridge Regression solves the problem mathematically.
3. Explain how Attention Mechanism in Transformers computes $Q K^T V$ using matrix multiplication.

## Level 5 — Interview Questions
1. Prove that the OLS parameter vector $\mathbf{w}^* = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$ is the Unbiased Minimum Variance Linear Estimator (Gauss-Markov Theorem).
2. Explain how Singular Value Decomposition (SVD) solves total least squares and rank-deficient linear systems via Pseudoinverse $\mathbf{w} = \mathbf{X}^+ \mathbf{y}$.
3. Derive the backpropagation gradient formulas for matrix weights $\frac{\partial L}{\partial \mathbf{W}} = \mathbf{X}^T \frac{\partial L}{\partial \mathbf{Z}}$ using Matrix Calculus.
4. Explain the connection between Kernel SVM inner products $\langle \phi(x), \phi(y) \rangle$ and Mercer's Theorem on Positive Definite Kernels.
5. How does Low-Rank Adaptation (LoRA) enable parameter-efficient fine-tuning of 70B parameter LLMs?
