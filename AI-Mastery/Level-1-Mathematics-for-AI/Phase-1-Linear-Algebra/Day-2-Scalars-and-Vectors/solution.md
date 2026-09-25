# Solutions — Scalars and Vectors

## Level 1 — Basic Understanding Solutions
### Question 1
Wind speed is a scalar (magnitude only, e.g. 20 mph). Wind velocity is a vector (magnitude and direction, e.g. 20 mph North).
### Question 2
$\mathbf{x} = \begin{bmatrix} 2 \\ -5 \\ 0 \end{bmatrix}$.
### Question 3
The dimension is $n = 5$ because it has 5 elements.
### Question 4
Feature vector $\mathbf{x} = [220, 4, 300]^T \in \mathbb{R}^3$.
### Question 5
$\mathbb{R}^3$ represents the 3-dimensional vector space of all ordered triples of real numbers.

## Level 2 — Calculation Solutions
### Question 1
1. $c\mathbf{v} = 3 \begin{bmatrix} 2 \\ 4 \end{bmatrix} = \begin{bmatrix} 6 \\ 12 \end{bmatrix}$.
### Question 2
2. The 3rd component $v_3 = 30$.
### Question 3
3. $m = n$ because vectors can only have equal dimensions if their component counts match.
### Question 4
4. $[1, 2, 3]^T = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$.
### Question 5
5. Each feature vector has dimension $n = 50$ (it belongs to $\mathbb{R}^{50}$).

## Level 3 — Conceptual Solutions
### Question 1
1. Scaling by $c = -2$ doubles the vector's length and reverses its direction by 180 degrees.
### Question 2
2. In tensor framework terminology, a 1D tensor is an array indexed by a single axis, which matches the definition of a mathematical vector.
### Question 3
3. A scalar zero is the number $0 \in \mathbb{R}$. A zero vector $\mathbf{0} = [0, 0, \dots, 0]^T$ is a vector where all components are zero.
### Question 4
4. Adding a constant feature increases the vector dimension from $n$ to $n+1$ (commonly used for bias terms).
### Question 5
5. Most standard ML models use real-valued vectors ($\mathbb{R}^n$), though complex-valued vectors exist in quantum ML and signal processing.

## Level 4 — AI/ML Application Solutions
### Question 1
1. $\mathbf{x} = [\text{tenure\_months}, \text{monthly\_charges}, \text{total\_support\_calls}, \text{contract\_type\_code}, \text{is\_paperless}]^T \in \mathbb{R}^5$.
### Question 2
2. The one-hot vector has dimension $n = 10,000$, with 1 at the word's index and 0 elsewhere.
### Question 3
3. A 2D grid of size $H \times W$ is flattened by concatenating rows into a single continuous 1D vector of dimension $H \times W$.

## Level 5 — Interview Questions Solutions
### Question 1
1. A point represents a fixed position in space. A vector represents a displacement (direction and magnitude) from the origin to that point.
### Question 2
2. Column vector convention ($\mathbf{y} = \mathbf{W}\mathbf{x}$) simplifies matrix calculus derivatives and matches standard linear algebra textbook notation.
### Question 3
3. Sparse vectors allow memory optimization by storing only non-zero indices and values, drastically speeding up computations.
### Question 4
4. Sparse vectors are high-dimensional with mostly 0s (e.g. bag-of-words). Dense embeddings are low-dimensional continuous real vectors containing rich contextual information.
### Question 5
5. Vastly different feature scales cause gradient descent to oscillate inefficiently, making feature scaling/normalization essential.
