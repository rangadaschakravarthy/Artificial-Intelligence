# Theory — Linear Algebra AI Mini-Project

### 1. Simple Definition
In this mini-project, we build a Semantic Vector Search Engine that converts text documents into numerical vectors, compresses them using SVD, and matches queries using Cosine Similarity.

### 2. Intuition
Imagine representing books as points in a 3D topic room. Science fiction books cluster near one wall, history books near another. When a user enters a query, we convert it to a point in the same room and find the nearest books using cosine similarity!

### 3. Mathematical Definition
Pipeline: 1) Term-Document Matrix $\mathbf{A}_{v \times d}$. 2) TF-IDF weighting $W_{i,j} = \text{tf}_{i,j} \times \log\left(\frac{N}{\text{df}_i}\right)$. 3) Truncated SVD $\mathbf{W} \approx \mathbf{U}_k \mathbf{\Sigma}_k \mathbf{V}_k^T$. 4) Query vector $\mathbf{q} \in \mathbb{R}^v$ projected to latent space $\mathbf{q}_k = \mathbf{\Sigma}_k^{-1} \mathbf{U}_k^T \mathbf{q}$. 5) Similarity scores $\mathbf{s} = \text{cos\_sim}(\mathbf{q}_k, \mathbf{V}_k^T)$.

### 4. Notation
$\mathbf{W}$: TF-IDF Matrix ($v$ words $\times d$ docs). $\mathbf{U}_k$: Latent Topic Space ($v \times k$). $\mathbf{V}_k$: Document Embeddings ($d \times k$). $\mathbf{q}$: Query Vector.

### 5. Formula

$$
\text{Similarity}(\mathbf{q}_k, \mathbf{d}_j) = \frac{\mathbf{q}_k \cdot \mathbf{d}_j}{||\mathbf{q}_k||_2 ||\mathbf{d}_j||_2}
$$

### 6. Symbol-by-Symbol Explanation
- $\mathbf{q}_k$: $k$-dimensional latent query embedding vector
- $\mathbf{d}_j$: $k$-dimensional latent document embedding vector
- $||\cdot||_2$: L2 Euclidean norm

### 7. Step-by-Step Calculation
Projecting query vector onto 2D latent topic space:
Query \mathbf{q} = [1, 0, 1]^T. Top 2 Left Singular Vectors 

$$
\mathbf{U}_2 = \begin{bmatrix} 0.8 & 0.1 \\ 0.2 & 0.9 \\ 0.6 & 0.3 \end{bmatrix}
$$

.
Latent Query 

$$
\mathbf{q}_k = \mathbf{U}_2^T \mathbf{q} = \begin{bmatrix} 0.8(1)+0.2(0)+0.6(1) \\ 0.1(1)+0.9(0)+0.3(1) \end{bmatrix} = \begin{bmatrix} 1.4 \\ 0.4 \end{bmatrix}
$$

.

### 8. Second Example
Compare $\mathbf{q}_k = [1.4, 0.4]^T$ with Doc 1 embedding $\mathbf{d}_1 = [1.0, 0.2]^T$:
$\mathbf{q}_k \cdot \mathbf{d}_1 = 1.4(1.0) + 0.4(0.2) = 1.48$.
$||\mathbf{q}_k||_2 = \sqrt{1.96+0.16} = 1.456$. $||\mathbf{d}_1||_2 = \sqrt{1.04} = 1.0198$.
$\text{Cosine Similarity} = \frac{1.48}{1.456 \times 1.0198} \approx 0.9967$ (Extremely High Match!).

### 9. Common Mistakes
Forgetting to normalize query and document vectors before computing cosine similarity.

### 10. AI Connection
This exact mathematical pipeline powers modern RAG (Retrieval-Augmented Generation) systems, Pinecone/Faiss vector search engines, and Google Search document ranking algorithms.

### 11. Algorithm Connection
Latent Semantic Analysis (LSA), Vector Search Engines, RAG Systems, Recommendation Engines.

### 12. Practical Interpretation
By compressing high-dimensional sparse word counts into low-dimensional dense SVD embeddings, the search engine matches documents based on underlying MEANING rather than exact keyword matches.

### 13. Interview Insight
Q: 'How does your Mini-Project handle synonyms like 'car' and 'automobile'?' A: SVD topic reduction maps co-occurring words 'car' and 'automobile' onto the same latent singular vectors in $\mathbf{U}_k$, yielding high cosine similarity even if the exact keyword differs.

### 14. Summary
Phase 1 Mini-Project synthesizes vectors, TF-IDF matrices, SVD latent space projection, and cosine similarity into a functional semantic vector search engine.
