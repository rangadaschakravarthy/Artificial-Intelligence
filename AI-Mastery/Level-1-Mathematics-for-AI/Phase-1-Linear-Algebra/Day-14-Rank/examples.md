# Examples — Rank

## Example 1 — Very Easy
Full Rank 2x2 Matrix: 

$$\begin{bmatrix} 1 & 0 \\ 0 & 2 \end{bmatrix} \implies \text{Rank} = 2$$

.

## Example 2 — Beginner
Rank Deficient 2x2 Matrix: 

$$\begin{bmatrix} 1 & 3 \\ 2 & 6 \end{bmatrix} \implies \text{Rank} = 1$$

 (Row 2 = 2 * Row 1).

## Example 3 — Intermediate
Outer Product Rank: $\mathbf{u} \mathbf{v}^T$ for any non-zero vectors $\mathbf{u}, \mathbf{v}$ ALWAYS has Rank = 1.

## Example 4 — AI/ML Example
Dataset Redundancy: 100 samples x 4 features where Feature 4 = Feature 1 + Feature 2 $\implies \text{Rank} = 3$.

## Example 5 — Real-World Interpretation
LoRA Memory Savings: Updating $4096 \times 4096$ matrix using rank $r=4$ factorization.
