# Practice Exercises — Linear Algebra AI Mini-Project

## Level 1 — Basic Understanding
1. What is the main goal of the Phase 1 Mini-Project?
2. What mathematical operation is used to measure document-query similarity?
3. Why do we use TF-IDF weighting instead of raw word counts?
4. What role does SVD play in Latent Semantic Analysis (LSA)?
5. What is the range of cosine similarity scores in vector search?

## Level 2 — Calculation
1. Compute Term Frequency (TF) for word 'AI' appearing 3 times in a 50-word document.
2. Compute Inverse Document Frequency (IDF) for word 'the' appearing in all 10 documents ($N=10, \text{df}=10$).
3. Compute IDF for rare word 'quantum' appearing in 1 out of 10 documents ($N=10, \text{df}=1$).
4. If query embedding is $\mathbf{q}_k = [3, 4]^T$ and document embedding is $\mathbf{d} = [6, 8]^T$, compute cosine similarity.
5. What happens to document rankings if all embedding vectors are pre-normalized to unit L2 length?

## Level 3 — Conceptual
1. Derive how SVD Latent Semantic Analysis resolves the polysemy (words with multiple meanings) and synonymy problems in search.
2. Explain how to update the document vector index when a new document is added without recomputing full SVD.
3. Why is Cosine Similarity preferred over Euclidean Distance in text vector retrieval?
4. Explain how the dot product $Q K^T$ in Transformer Self-Attention is mathematically identical to query-document vector search.
5. What is the computational complexity of querying a vector index of $N$ documents with $d$ dimensions?

## Level 4 — AI/ML Application
1. Modify the mini-project pipeline to implement a Content-Based Movie Recommender system (User Rating Matrix SVD Factorization).
2. Explain how Vector Databases (e.g. Pinecone, Milvus, Qdrant) use Hierarchical Navigable Small World (HNSW) graphs to accelerate k-NN cosine similarity search from $O(N)$ to $O(\log N)$.
3. How does adding an L2 normalization layer after SVD topic projection impact vector search accuracy?

## Level 5 — Interview Questions
1. Explain the mathematical differences between classical LSA (SVD on TF-IDF) and modern Dense Passage Retrieval (DPR using Transformer BERT embeddings).
2. How does Asymmetric Query-Document embedding (Bi-Encoders) optimize search speed compared to Cross-Encoders?
3. Write the complete mathematical formulation for evaluating Mean Reciprocal Rank (MRR) and Normalized Discounted Cumulative Gain (NDCG@K) in vector search engines.
4. Explain how Quantization (e.g. Product Quantization PQ or Scalar Quantization SQ8) compresses 768D float32 embeddings to 8-bit integers with minimal loss of search recall.
5. Describe how GPU-accelerated vector search (NVIDIA RAFT / Faiss-GPU) executes millions of cosine similarity queries per second.
