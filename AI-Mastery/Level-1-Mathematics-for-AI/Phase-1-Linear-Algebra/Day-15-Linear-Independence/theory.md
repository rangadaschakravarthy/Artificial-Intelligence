# Theory — Linear Independence

### 1. Simple Definition
A set of vectors is linearly independent if no vector in the set can be built as a linear combination of the other vectors.

### 2. Intuition
Imagine directions on a map. 'North' and 'East' are independent because walking North will never get you even 1 millimeter East. But 'North', 'East', and 'Northeast' are dependent because Northeast = North + East.

### 3. Mathematical Definition
A set of vectors \{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k\} \subset \mathbb{R}^n$ is linearly independent if the equation:

$$
c_1 \mathbf{v}_1 + c_2 \mathbf{v}_2 + \dots + c_k \mathbf{v}_k = \mathbf{0}
$$

has ONLY the trivial solution $c_1 = c_2 = \dots = c_k = 0$. If non-zero scalars $c_i$ exist, the vectors are linearly dependent.

### 4. Notation
$c_1 \mathbf{v}_1 + \dots + c_k \mathbf{v}_k = \mathbf{0} \implies c_i = 0 \quad \forall i$.

### 5. Formula

$$
\text{Vectors } \{\mathbf{v}_1, \dots, \mathbf{v}_n\} \in \mathbb{R}^n \text{ are Independent } \iff \det([\mathbf{v}_1 \, \mathbf{v}_2 \dots \mathbf{v}_n]) \neq 0
$$

### 6. Symbol-by-Symbol Explanation
- $\mathbf{v}_i$: Individual vectors in the set
- $c_i$: Scalar coefficients
- $\mathbf{0}$: Zero vector

### 7. Step-by-Step Calculation
Test if $\mathbf{u} = [1, 2]^T$ and $\mathbf{v} = [3, 6]^T$ are independent:
Set 

$$
c_1 \begin{bmatrix} 1 \\ 2 \end{bmatrix} + c_2 \begin{bmatrix} 3 \\ 6 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
$$

.
1. $c_1 + 3c_2 = 0 \implies c_1 = -3c_2$.
2. $2c_1 + 6c_2 = 0 \implies 2(-3c_2) + 6c_2 = 0 \implies 0 = 0$.
Since $c_1 = -3, c_2 = 1$ is a valid non-zero solution, the vectors are LINEARLY DEPENDENT! (Indeed $\mathbf{v} = 3\mathbf{u}$).

### 8. Second Example
Test $\mathbf{a} = [1, 0]^T, \mathbf{b} = [0, 1]^T$:
$c_1 [1, 0]^T + c_2 [0, 1]^T = [0, 0]^T \implies c_1 = 0, c_2 = 0$.
Only trivial solution exists $\implies$ LINEARLY INDEPENDENT!

### 9. Common Mistakes
Thinking orthogonal vectors are the only independent vectors (all orthogonal vectors are independent, but NOT all independent vectors are orthogonal!); attempting to have more than $n$ independent vectors in $\mathbb{R}^n$.

### 10. AI Connection
Feature Selection and PCA: Removing linearly dependent feature columns reduces dataset dimensions without losing predictive information. One-hot encoding creates linearly independent basis vectors.

### 11. Algorithm Connection
Principal Component Analysis (PCA), Gram-Schmidt Orthogonalization, Linear Regression, Feature Selection.

### 12. Practical Interpretation
Any set of $k > n$ vectors in $\mathbb{R}^n$ is AUTOMATICALLY linearly dependent (pigeonhole principle of linear algebra).

### 13. Interview Insight
Q: 'Can 4 vectors in $\mathbb{R}^3$ be linearly independent?' A: No! Maximum number of linearly independent vectors in $\mathbb{R}^n$ is $n$. The 4th vector MUST be a linear combination of the first 3.

### 14. Summary
Vectors are independent if none can be formed from the others ($c_1 v_1 + \dots + c_k v_k = 0 \implies c_i = 0$). Matrix of $n$ vectors in $\mathbb{R}^n$ is independent if and only if $\det \neq 0$ and $\text{Rank} = n$.
