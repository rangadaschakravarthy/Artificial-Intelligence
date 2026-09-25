# Examples — Cosine Similarity

## Example 1 — Very Easy
Parallel Vectors: $\mathbf{u} = [1, 2]^T, \mathbf{v} = [3, 6]^T \implies \text{sim} = \frac{3+12}{\sqrt{5}\sqrt{45}} = \frac{15}{15} = 1.0$ (0 degrees).

## Example 2 — Beginner
Orthogonal Vectors: $\mathbf{u} = [1, 0]^T, \mathbf{v} = [0, 5]^T \implies \text{sim} = \frac{0}{1 \times 5} = 0.0$ (90 degrees).

## Example 3 — Intermediate
Opposite Vectors: $\mathbf{u} = [2, 3]^T, \mathbf{v} = [-4, -6]^T \implies \text{sim} = \frac{-8-18}{\sqrt{13}\sqrt{52}} = \frac{-26}{26} = -1.0$ (180 degrees).

## Example 4 — AI/ML Example
TF-IDF Document Comparison: Doc1='cat food' $[1, 1, 0]^T$, Doc2='dog food' $[0, 1, 1]^T$. $\text{sim} = \frac{1}{\sqrt{2}\sqrt{2}} = 0.5$.

## Example 5 — Real-World Interpretation
LLM Query Matching: User query vector vs candidate answer vector cosine similarity score thresholding.
