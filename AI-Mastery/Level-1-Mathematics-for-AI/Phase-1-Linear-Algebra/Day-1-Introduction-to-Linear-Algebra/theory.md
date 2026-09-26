# Theory — Introduction to Linear Algebra

### 1. Simple Definition
Linear Algebra is the branch of mathematics that deals with linear equations, linear functions, and their representations using vectors and matrices.

### 2. Intuition
Imagine you have a list of numbers representing a person's profile (age, income, credit score). Linear algebra gives us a unified mathematical language to rotate, scale, transform, and combine thousands of such lists at once.

### 3. Mathematical Definition
Linear algebra studies vector spaces $V$ over a field $F$ and linear mappings between such spaces preserving vector addition and scalar multiplication: $T(u + v) = T(u) + T(v)$ and $T(c v) = c T(v)$.

### 4. Notation
Scalars are written as lowercase italic letters ($s \in \mathbb{R}$), vectors as bold lowercase ($\mathbf{v} \in \mathbb{R}^n$), matrices as uppercase bold ($\mathbf{A} \in \mathbb{R}^{m \times n}$).

### 5. Formula

$$
\mathbf{y} = \mathbf{A}\mathbf{x} + \mathbf{b}
$$

### 6. Symbol-by-Symbol Explanation
- $\mathbf{y}$: Output vector (e.g., predicted housing prices)
- $\mathbf{A}$: Matrix of linear weights/transformations
- $\mathbf{x}$: Input feature vector (e.g., size, bedrooms, age)
- $\mathbf{b}$: Bias vector shifting the transformation

### 7. Step-by-Step Calculation
Given $x = [2000, 3]$, $A = [[100], [15000]]$, $b = [20000]$:

$$
y = (2000 \times 100) + (3 \times 15000) + 20000 = 200000 + 45000 + 20000 = 265000
$$

### 8. Second Example
Given a 2-feature input $x = [1, 2]$ transformed by weight matrix $W = [[2, 0], [0, 3]]$:

$$
y = Wx = [2(1) + 0(2), 0(1) + 3(2)] = [2, 6]
$$

### 9. Common Mistakes
Treating matrix transformation as element-wise multiplication; confusing vector dimensions with matrix ranks.

### 10. AI Connection
Used everywhere in AI: image representation (RGB grids), word embeddings (Word2Vec/Transformers), neural network layers.

### 11. Algorithm Connection
Linear Regression, Logistic Regression, Support Vector Machines (SVM), Neural Networks, Principal Component Analysis (PCA).

### 12. Practical Interpretation
Every input to an AI model is converted into a numerical vector. Model parameters are stored as matrices.

### 13. Interview Insight
Interviewer question: 'Why is linear algebra preferred over standard loops in ML software?' Answer: Vectorized operations enable hardware parallelization on GPUs.

### 14. Summary
Linear algebra translates complex real-world data into structured arrays and linear mappings that computers can compute efficiently.
