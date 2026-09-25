# Practice Exercises — Cosine Similarity

## Level 1 — Basic Understanding
1. What is the range of Cosine Similarity?
2. Compute Cosine Similarity for $\mathbf{u} = [3, 0]^T$ and $\mathbf{v} = [5, 0]^T$.
3. Compute Cosine Similarity for $\mathbf{a} = [1, 0]^T$ and $\mathbf{b} = [0, 1]^T$.
4. What is the Cosine Distance if Cosine Similarity is 0.8?
5. Why is cosine similarity between two non-negative word frequency vectors always between 0 and 1?

## Level 2 — Calculation
1. Compute Cosine Similarity between $\mathbf{x} = [1, 2, 3]^T$ and $\mathbf{y} = [2, 4, 6]^T$.
2. Calculate Cosine Similarity between $\mathbf{u} = [1, 1]^T$ and $\mathbf{v} = [1, 0]^T$.
3. Show that scaling $\mathbf{u}$ by constant $c=5$ does not change $\text{sim}(\mathbf{u}, \mathbf{v})$.
4. If $\text{sim}(\mathbf{a}, \mathbf{b}) = -1$, what is the angle between $\mathbf{a}$ and $\mathbf{b}$?
5. Given unit vectors $\hat{\mathbf{u}}$ and $\hat{\mathbf{v}}$, write the simplified formula for Cosine Similarity.

## Level 3 — Conceptual
1. Prove that $\text{sim}(\mathbf{u}, \mathbf{v}) = \hat{\mathbf{u}} \cdot \hat{\mathbf{v}}$ where $\hat{\mathbf{u}}, \hat{\mathbf{v}}$ are normalized unit vectors.
2. Explain why Euclidean distance changes when document word counts double, but cosine similarity remains constant.
3. Under what condition does Euclidean distance monotonic ordering match Cosine distance ordering?
4. Is Cosine Distance a true mathematical metric? (Check triangle inequality).
5. How does zero-centering feature vectors affect Cosine Similarity?

## Level 4 — AI/ML Application
1. A search engine embeds query as $\mathbf{q} = [0.6, 0.8]^T$ and candidate document as $\mathbf{d} = [0.8, 0.6]^T$. Compute cosine similarity and cosine distance.
2. User preference vector $\mathbf{u} = [4, 5, 1]^T$ (ratings for Action, Comedy, Drama). Movie profile $\mathbf{m} = [5, 4, 0]^T$. Calculate recommendation score via cosine similarity.
3. Explain how Vector Databases (Pinecone/Milvus) use normalized vector dot products to compute fast k-NN search.

## Level 5 — Interview Questions
1. Derive the relationship: $||\hat{\mathbf{u}} - \hat{\mathbf{v}}||_2^2 = 2 (1 - \text{sim}(\mathbf{u}, \mathbf{v}))$.
2. Why do modern LLM embeddings (e.g. OpenAI text-embedding-3) output pre-normalized vectors?
3. Compare Cosine Similarity vs Pearson Correlation Coefficient.
4. What happens to cosine similarity in extremely high-dimensional spaces (vector orthogonality phenomenon)?
5. How does temperature scaling affect cosine similarity logits in Softmax classification?
