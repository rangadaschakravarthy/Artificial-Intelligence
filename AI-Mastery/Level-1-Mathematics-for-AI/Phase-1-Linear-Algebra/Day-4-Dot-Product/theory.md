# Theory — Dot Product

### 1. Simple Definition
The dot product takes two vectors of equal length, multiplies corresponding components together, and sums the results to produce a single scalar number.

### 2. Intuition
Imagine evaluating a job candidate across 3 skills (coding=9, comms=7, leadership=6) given job priority weights (coding=0.5, comms=0.3, leadership=0.2). The dot product sums up score $\times$ weight to give a single overall candidate score!

### 3. Mathematical Definition
For $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$, the dot product $\mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^n u_i v_i = \mathbf{u}^T \mathbf{v}$. Geometrically, $\mathbf{u} \cdot \mathbf{v} = ||\mathbf{u}||_2 ||\mathbf{v}||_2 \cos(\theta)$, where $\theta$ is the angle between them.

### 4. Notation
$\mathbf{u} \cdot \mathbf{v}$, $\langle \mathbf{u}, \mathbf{v} \rangle$, or $\mathbf{u}^T \mathbf{v}$. Result is a scalar $\in \mathbb{R}$.

### 5. Formula
$$\mathbf{u} \cdot \mathbf{v} = u_1 v_1 + u_2 v_2 + \dots + u_n v_n = \sum_{i=1}^n u_i v_i$$

### 6. Symbol-by-Symbol Explanation
- $\mathbf{u}, \mathbf{v}$: Vectors in $\mathbb{R}^n$
- $u_i, v_i$: $i$-th component of vectors
- $n$: Dimension of vector space

### 7. Step-by-Step Calculation
Given $\mathbf{u} = [2, 3]^T$, $\mathbf{v} = [4, -1]^T$:
$$\mathbf{u} \cdot \mathbf{v} = (2 \times 4) + (3 \times -1) = 8 + (-3) = 5$$

### 8. Second Example
Given $\mathbf{x} = [1, 0, 2]^T$ and $\mathbf{w} = [-2, 3, 1]^T$:
$$\mathbf{w}^T \mathbf{x} = (-2)(1) + (3)(0) + (1)(2) = -2 + 0 + 2 = 0$$
Since dot product is 0, $\mathbf{w}$ and $\mathbf{x}$ are orthogonal (perpendicular)!

### 9. Common Mistakes
Returning a vector instead of a scalar; computing dot product on vectors of unequal dimension.

### 10. AI Connection
Neuron activation pre-state $z = \mathbf{w}^T \mathbf{x} + b$. Transformer Self-Attention similarity score $S = Q K^T$. Convolution operations are dot products over sliding image patches.

### 11. Algorithm Connection
Perceptrons, Dense Neural Layers, Support Vector Machines (Kernel Tricks), Dot-Product Attention in LLMs.

### 12. Practical Interpretation
Positive dot product $\Rightarrow$ vectors point in generally similar directions. Zero $\Rightarrow$ perpendicular (independent). Negative $\Rightarrow$ opposing directions.

### 13. Interview Insight
Q: 'Why is dot product used to measure similarity in recommendation systems?' A: Because it measures the magnitude of vector projection—how much one vector points in the direction of another.

### 14. Summary
Dot product maps two vectors to a scalar: $\mathbf{u}^T \mathbf{v} = \sum u_i v_i$. It is the fundamental building block of weighted sums and similarity metrics in AI.
