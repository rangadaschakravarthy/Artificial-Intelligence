# Theory — Scalars and Vectors

### 1. Simple Definition
A scalar is a single number representing magnitude. A vector is an ordered list of numbers representing magnitude and direction in space.

### 2. Intuition
Think of a scalar as a single measurement like your weight (70 kg). A vector is like a GPS coordinate giving your latitude, longitude, and elevation (37.77, -122.41, 15), specifying a precise spot in 3D space.

### 3. Mathematical Definition
A vector $\mathbf{v} \in \mathbb{R}^n$ is an $n$-tuple of real numbers $(v_1, v_2, \dots, v_n)$. It can be written as a column vector:
$$\mathbf{v} = \begin{bmatrix} v_1 \\ \vdots \\ v_n \end{bmatrix}$$
or as a row vector $\mathbf{v}^T = [v_1, v_2, \dots, v_n]$.

### 4. Notation
$\alpha, c \in \mathbb{R}$ for scalars. $\mathbf{v}, \vec{v}, \mathbf{x} \in \mathbb{R}^n$ for vectors. Component $i$ is denoted $v_i$.

### 5. Formula
$$\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix} \in \mathbb{R}^n$$

### 6. Symbol-by-Symbol Explanation
- $\mathbf{v}$: Vector
- $v_1, v_2, \dots, v_n$: Individual scalar components
- $\mathbb{R}^n$: $n$-dimensional real vector space

### 7. Step-by-Step Calculation
For a point $(3, 4)$ in 2D space: Component $x = 3$, component $y = 4$. Vector $\mathbf{v} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}$. Dimension $n = 2$.

### 8. Second Example
For 4D text feature vector [word_count=50, sentiment=0.8, avg_len=4.5, contains_links=1]: $\mathbf{x} = [50, 0.8, 4.5, 1.0]^T \in \mathbb{R}^4$.

### 9. Common Mistakes
Confusing vector dimension (length of array) with matrix rank or array memory size.

### 10. AI Connection
Feature vectors form the inputs to ML models. Word embeddings (e.g. 768-dimensional BERT embeddings) represent semantic word meaning as vectors.

### 11. Algorithm Connection
k-Nearest Neighbors (k-NN), Support Vector Machines, Word2Vec, Transformers.

### 12. Practical Interpretation
The dimension $n$ corresponds to the number of features describing each data instance.

### 13. Interview Insight
Q: 'What is a feature vector?' A: An $n$-dimensional vector where each element represents a measurable property of an object.

### 14. Summary
Scalars are 0D single values; vectors are 1D arrays representing points or directions in $n$-dimensional space.
