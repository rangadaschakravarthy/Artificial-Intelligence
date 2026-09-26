# Theory — Linear Algebra for Machine Learning

### 1. Simple Definition
Machine learning algorithms are simply structured sequences of linear algebra operations (vector products, matrix transformations, projections) optimized to minimize prediction error.

### 2. Intuition
Every ML model is a geometric machine: feature vectors position data points in space, weight matrices rotate and scale space, dot products measure alignment, and loss functions compute vector distance errors.

### 3. Mathematical Definition
Linear Model: $f(\mathbf{x}) = \mathbf{w}^T \mathbf{x} + b$. OLS Parameter Matrix: $\mathbf{w}^* = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$. Neural Network Layer $l$: $\mathbf{H}^{(l)} = \sigma(\mathbf{H}^{(l-1)} \mathbf{W}^{(l)} + \mathbf{b}^{(l)})$.

### 4. Notation
$\mathbf{X}_{N \times d}$: Data matrix. $\mathbf{w}_{d \times 1}$: Model parameter weight vector. $\mathbf{y}_{N \times 1}$: Target label vector.

### 5. Formula
$$\mathbf{w}^* = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y} \quad \text{(Closed-form OLS Solution)}$$

### 6. Symbol-by-Symbol Explanation
- $\mathbf{X}$: $N \times d$ dataset design matrix
- $\mathbf{X}^T \mathbf{X}$: $d \times d$ Gram matrix
- $\mathbf{y}$: Target vector of $N$ values
- $\mathbf{w}^*$: Optimal weight vector

### 7. Step-by-Step Calculation
Compute OLS weights for 2 samples: $x_1=1, y_1=2; x_2=2, y_2=3$:
1. Augmented design matrix 

$$\mathbf{X} = \begin{bmatrix} 1 & 1 \\ 1 & 2 \end{bmatrix}$$

 (col 1 is bias 1s).
2. 

$$\mathbf{X}^T \mathbf{X} = \begin{bmatrix} 2 & 3 \\ 3 & 5 \end{bmatrix}$$

.
3. Inverse 

$$(\mathbf{X}^T \mathbf{X})^{-1} = \begin{bmatrix} 5 & -3 \\ -3 & 2 \end{bmatrix}$$

.
4. 

$$\mathbf{X}^T \mathbf{y} = \begin{bmatrix} 1 & 1 \\ 1 & 2 \end{bmatrix} \begin{bmatrix} 2 \\ 3 \end{bmatrix} = \begin{bmatrix} 5 \\ 8 \end{bmatrix}$$

.
5. 

$$\mathbf{w}^* = \begin{bmatrix} 5 & -3 \\ -3 & 2 \end{bmatrix} \begin{bmatrix} 5 \\ 8 \end{bmatrix} = \begin{bmatrix} 25-24 \\ -15+16 \end{bmatrix} = \begin{bmatrix} 1 \\ 1 \end{bmatrix} \implies y = 1x + 1$$

.

### 8. Second Example
SVM Hyperplane decision boundary: $\mathbf{w}^T \mathbf{x} + b = 0$. Distance from point $\mathbf{x}_i$ to hyperplane is $\frac{|\mathbf{w}^T \mathbf{x}_i + b|}{||\mathbf{w}||_2}$. Margin $= \frac{2}{||\mathbf{w}||_2}$.

### 9. Common Mistakes
Thinking neural networks are magic black boxes rather than nested linear algebra operations ($W x + b$) separated by non-linear activation functions.

### 10. AI Connection
Complete ML Pipeline: Raw data $\rightarrow$ Vectorization $\rightarrow$ Standard Normalization $\rightarrow$ PCA Dimensionality Reduction $\rightarrow$ Matrix Linear Layer Transformation $\rightarrow$ Output Prediction.

### 11. Algorithm Connection
Linear Regression, Logistic Regression, Support Vector Machines, PCA, Neural Networks, Transformers.

### 12. Practical Interpretation
Every ML model learns a weight matrix $\mathbf{W}$ that transforms input feature space into an output prediction space.

### 13. Interview Insight
Q: 'How does Linear Algebra unify Linear Regression, PCA, and Neural Networks?' A: Linear Regression uses matrix transpose and inverse to find optimal projections. PCA uses eigendecomposition of covariance matrix. Neural Networks stack matrix multiplications with non-linear activation functions.

### 14. Summary
Machine Learning is applied Linear Algebra. Data is represented as feature matrices; models learn weight matrices $\mathbf{W}$; predictions are computed via dot products and matrix transformations.
