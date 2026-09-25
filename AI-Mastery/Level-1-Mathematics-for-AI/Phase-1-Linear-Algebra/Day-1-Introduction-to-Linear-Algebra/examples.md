# Examples — Introduction to Linear Algebra

## Example 1 — Very Easy
Scalar value: Temperature of a room $T = 25.5^\circ\text{C}$. Represented as a single real number $x \in \mathbb{R}$.

## Example 2 — Beginner
Vector representation: A 2D point representing a house with 1500 sq ft and 3 bedrooms: $\mathbf{v} = [1500, 3]^T$.

## Example 3 — Intermediate
Matrix dataset: 3 houses with 2 features each:
$$\mathbf{X} = \begin{bmatrix} 1500 & 3 \\ 2000 & 4 \\ 1200 & 2 \end{bmatrix}$$

## Example 4 — AI/ML Example
Neural network linear transformation: Transforming 2 input features to 2 output nodes using weights $W$ and bias $b$.
$$\mathbf{W} = \begin{bmatrix} 0.5 & 1.2 \\ 0.1 & 2.0 \end{bmatrix}, \quad \mathbf{x} = \begin{bmatrix} 2 \\ 1 \end{bmatrix}$$
$$\mathbf{y} = \mathbf{W}\mathbf{x} = \begin{bmatrix} 0.5(2) + 1.2(1) \\ 0.1(2) + 2.0(1) \end{bmatrix} = \begin{bmatrix} 2.2 \\ 2.2 \end{bmatrix}$$

## Example 5 — Real-World Interpretation
Image as a 2D matrix: A grayscale image of size 3x3 pixels represented as pixel intensity matrix from 0 (black) to 255 (white).
