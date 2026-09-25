# Theory — Norms and Distances

### 1. Simple Definition
A vector norm is a function that measures the length, magnitude, or size of a vector. Distance measures how far apart two vector points are.

### 2. Intuition
L2 norm is the straight-line distance as the crow flies. L1 norm is the distance walking along a grid of city blocks (Manhattan distance). Infinity norm is simply the largest single coordinate step.

### 3. Mathematical Definition
A norm $||\mathbf{v}||$ on a vector space $V$ is a function $V \rightarrow \mathbb{R}_{\ge 0}$ satisfying: 1) Non-negativity $||v|| \ge 0$, 2) Absolute homogeneity $||c v|| = |c| ||v||$, 3) Triangle inequality $||u + v|| \le ||u|| + ||v||$. General $L_p$ norm: $||v||_p = (\sum_{i=1}^n |v_i|^p)^{1/p}$.

### 4. Notation
$||v||_1$ for L1 norm, $||v||_2$ for L2 norm, $||v||_\infty$ for max norm. Distance $d(\mathbf{u}, \mathbf{v}) = ||\mathbf{u} - \mathbf{v}||$.

### 5. Formula
$$||\mathbf{v}||_1 = \sum_{i=1}^n |v_i|, \quad ||\mathbf{v}||_2 = \sqrt{\sum_{i=1}^n v_i^2}, \quad ||\mathbf{v}||_\infty = \max_{i} |v_i|$$

### 6. Symbol-by-Symbol Explanation
- $|v_i|$: Absolute value of component $i$
- $\sum$: Sum over all $n$ dimensions
- $\max$: Maximum absolute component

### 7. Step-by-Step Calculation
For vector $\mathbf{v} = [3, -4]^T$:
1. L1 Norm: $|3| + |-4| = 3 + 4 = 7$
2. L2 Norm: $\sqrt{3^2 + (-4)^2} = \sqrt{9 + 16} = \sqrt{25} = 5$
3. $L_\infty$ Norm: $\max(|3|, |-4|) = 4$

### 8. Second Example
Distance between $\mathbf{u} = [1, 2]^T$ and $\mathbf{v} = [4, 6]^T$:
Diff vector $\mathbf{d} = \mathbf{u} - \mathbf{v} = [-3, -4]^T$.
1. Euclidean distance $d_2 = ||\mathbf{d}||_2 = \sqrt{(-3)^2 + (-4)^2} = 5$
2. Manhattan distance $d_1 = ||\mathbf{d}||_1 = |-3| + |-4| = 7$

### 9. Common Mistakes
Forgetting to take absolute values in L1 norm; forgetting square root in L2 norm.

### 10. AI Connection
Regularization terms added to loss functions: $L_{total} = L_{data} + \lambda ||\mathbf{w}||_p$. L1 regularization (Lasso) drives uninformative weights to exact 0 (feature selection). L2 regularization (Ridge / Weight Decay) keeps weights small.

### 11. Algorithm Connection
Lasso Regression, Ridge Regression, k-Nearest Neighbors (k-NN), K-Means Clustering, SVMs.

### 12. Practical Interpretation
A unit vector is a vector normalized to have L2 norm equal to 1: $\hat{\mathbf{v}} = \frac{\mathbf{v}}{||\mathbf{v}||_2}$.

### 13. Interview Insight
Q: 'Why does L1 regularization encourage sparse weights while L2 does not?' A: The L1 norm geometric contour has sharp corners along coordinate axes where loss minimums frequently intersect, setting parameters to zero.

### 14. Summary
Norms quantify vector magnitude ($L_1$ sum of absolute values, $L_2$ Euclidean square root of sum of squares, $L_\infty$ maximum absolute value). Distances measure norm of vector difference.
