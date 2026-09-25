# Theory — Cosine Similarity

### 1. Simple Definition
Cosine similarity measures the angle between two vectors, ignoring their lengths. It determines whether two vectors point in roughly the same direction.

### 2. Intuition
Imagine two rays pointing out from the origin. If they overlap completely, similarity is 1 (0° angle). If perpendicular, similarity is 0 (90° angle). If pointing opposite, similarity is -1 (180° angle). It measures direction, not length!

### 3. Mathematical Definition
For non-zero vectors $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$, $\text{cos}(\theta) = \frac{\mathbf{u} \cdot \mathbf{v}}{||\mathbf{u}||_2 ||\mathbf{v}||_2} = \hat{\mathbf{u}} \cdot \hat{\mathbf{v}}$.

### 4. Notation
$\text{sim}(\mathbf{u}, \mathbf{v}) \in [-1, 1]$. Cosine distance $d_{cos}(\mathbf{u}, \mathbf{v}) = 1 - \text{sim}(\mathbf{u}, \mathbf{v}) \in [0, 2]$.

### 5. Formula
$$\text{sim}(\mathbf{u}, \mathbf{v}) = \frac{\sum_{i=1}^n u_i v_i}{\sqrt{\sum_{i=1}^n u_i^2} \sqrt{\sum_{i=1}^n v_i^2}}$$

### 6. Symbol-by-Symbol Explanation
- $\mathbf{u} \cdot \mathbf{v}$: Dot product sum of component products
- $||\mathbf{u}||_2, ||\mathbf{v}||_2$: L2 Euclidean norms
- $\theta$: Angle between vectors in vector space

### 7. Step-by-Step Calculation
Given $\mathbf{u} = [1, 1]^T$, $\mathbf{v} = [0, 2]^T$:
1. Dot product: $1(0) + 1(2) = 2$
2. L2 Norm $\mathbf{u}$: $\sqrt{1^2 + 1^2} = \sqrt{2} \approx 1.414$
3. L2 Norm $\mathbf{v}$: $\sqrt{0^2 + 2^2} = \sqrt{4} = 2$
4. $\text{sim} = \frac{2}{\sqrt{2} \times 2} = \frac{1}{\sqrt{2}} \approx 0.7071$ (Angle is $45^\circ$)

### 8. Second Example
Given scaled vector $\mathbf{w} = [2, 2]^T = 2\mathbf{u}$ and $\mathbf{v} = [0, 2]^T$:
$\mathbf{w} \cdot \mathbf{v} = 4, ||\mathbf{w}||_2 = \sqrt{8} = 2\sqrt{2}, ||\mathbf{v}||_2 = 2$.
$\text{sim}(\mathbf{w}, \mathbf{v}) = \frac{4}{2\sqrt{2} \times 2} = \frac{1}{\sqrt{2}} \approx 0.7071$. Exactly identical similarity score (Scale Invariance)!

### 9. Common Mistakes
Confusing cosine similarity with dot product (forgetting normalization denominator); confusing cosine similarity with cosine distance.

### 10. AI Connection
RAG (Retrieval-Augmented Generation) vector databases (Faiss, Pinecone) compare query embeddings against knowledge chunks using cosine similarity.

### 11. Algorithm Connection
Content-Based Recommendation Systems, Word2Vec, BERT embeddings, Vector Search Engines.

### 12. Practical Interpretation
For normalized unit vectors ($||\mathbf{u}||=1, ||\mathbf{v}||=1$), Cosine Similarity simplifies directly to the dot product $\mathbf{u} \cdot \mathbf{v}$.

### 13. Interview Insight
Q: 'Why prefer Cosine Similarity over Euclidean Distance for text document comparison?' A: A long document repeating the same words has a larger Euclidean magnitude but identical term ratios (direction). Cosine similarity correctly yields 1.0.

### 14. Summary
Cosine similarity measures vector angular alignment $\frac{\mathbf{u}\cdot\mathbf{v}}{||\mathbf{u}|| ||\mathbf{v}||}$. It is scale-invariant and crucial for semantic search.
