# Examples — Singular Value Decomposition

## Example 1 — Very Easy
Diagonal SVD: 

$$\mathbf{A} = \begin{bmatrix} 5 & 0 \\ 0 & 2 \end{bmatrix} \implies \mathbf{U}=\mathbf{I}_2, \mathbf{\Sigma}=\begin{bmatrix}5&0\\0&2\end{bmatrix}, \mathbf{V}=\mathbf{I}_2$$

.

## Example 2 — Beginner
Singular Values of Vector: $\mathbf{x} = [3, 4]^T \implies \sigma_1 = \sqrt{3^2+4^2} = 5$.

## Example 3 — Intermediate
Truncated SVD Image Compression: Keeping top 20 singular values of a 500x500 image.

## Example 4 — AI/ML Example
Latent Semantic Analysis (LSA): Term-Document matrix SVD factorization into word topic vectors.

## Example 5 — Real-World Interpretation
Pseudoinverse via SVD: $\mathbf{A}^+ = \mathbf{V} \mathbf{\Sigma}^+ \mathbf{U}^T$.
