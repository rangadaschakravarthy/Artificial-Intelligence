# Solutions — Linear Algebra AI Mini-Project

## Level 1 — Basic Understanding Solutions
### Question 1
1. To build a complete Semantic Vector Search Engine using pure Linear Algebra and NumPy.
### Question 2
2. Cosine Similarity (normalized dot product between query and document vectors).
### Question 3
3. Raw word counts over-weight non-informative common words like 'the', 'is', 'and'. TF-IDF scales down common words and scales up rare informative words.
### Question 4
4. SVD compresses high-dimensional sparse TF-IDF word matrices into dense low-dimensional latent topic spaces, uncovering semantic relationships.
### Question 5
5. $[0, 1]$ for non-negative text feature embeddings (or $[-1, 1]$ in general vector spaces).

## Level 2 — Calculation Solutions
### Question 1
1. $\text{TF} = 3 / 50 = 0.06$.
### Question 2
2. $\text{IDF}(\text{'the'}) = \log(10 / 10) = \log(1) = 0.0$. Common word gets 0 weight!
### Question 3
3. $\text{IDF}(\text{'quantum'}) = \log(10 / 1) = \log(10) \approx 2.302$. High informative weight!
### Question 4
4. Vectors are parallel ($\mathbf{d} = 2\mathbf{q}_k$). Cosine similarity $= 1.0$ (perfect match!).
### Question 5
5. If pre-normalized, cosine similarity reduces to a simple dot product $\mathbf{q} \cdot \mathbf{d}$, eliminating division operations and accelerating search.

## Level 3 — Conceptual Solutions
### Question 1
1. SVD projects words onto shared latent topic dimensions $U_k$. Synonyms ('car', 'automobile') frequently co-occur with similar context words, causing their left singular vectors to align in topic space.
### Question 2
2. Project new document TF-IDF vector $\mathbf{d}_{new}$ onto existing latent topic space: $\mathbf{d}_{k, new} = \mathbf{\Sigma}_k^{-1} \mathbf{U}_k^T \mathbf{d}_{new}$ (Folding-In technique).
### Question 3
3. Document length variations alter Euclidean distance but do not change the relative proportion of topic words (direction). Cosine similarity measures direction, ignoring length.
### Question 4
4. Query vector $Q$ acts as search query, Key vectors $K$ act as document index. $Q K^T$ computes dot-product similarity scores between queries and keys.
### Question 5
5. Brute-force linear scan takes $O(N \cdot d)$ operations.

## Level 4 — AI/ML Application Solutions
### Question 1
1. User-Movie rating matrix $R_{users \times movies}$. SVD factorization $R \approx U \Sigma V^T$. User recommendation score for unrated movie $j$ is dot product $\mathbf{u}_i^T \mathbf{v}_j$.
### Question 2
2. HNSW constructs a multi-layer graph where top layers have long-distance links for fast routing, and lower layers have short-distance links for fine-grained k-NN search, reducing query complexity to $O(\log N)$.
### Question 3
3. L2 normalization projects topic vectors onto the unit hypersphere, making all document vectors equal length so dot product matches cosine similarity directly.

## Level 5 — Interview Questions Solutions
### Question 1
1. LSA uses linear algebraic term frequency statistics (SVD on TF-IDF). DPR uses deep non-linear Transformer encoders (BERT) trained via contrastive loss to capture complex syntax, word order, and context.
### Question 2
2. Bi-Encoders compute query and document embeddings independently offline, reducing search to fast dot product $\mathbf{q}^T \mathbf{d}$. Cross-Encoders concatenate query and document `[CLS] Q [SEP] D [SEP]` passing through 12 Transformer layers per pair, which is accurate but 1000x slower.
### Question 3
3. $\text{MRR} = \frac{1}{|Q|} \sum_{i=1}^{|Q|} \frac{1}{\text{rank}_i}$. $\text{NDCG@K} = \frac{\text{DCG@K}}{\text{IDCG@K}}$ where $\text{DCG@K} = \sum_{i=1}^K \frac{2^{rel_i}-1}{\log_2(i+1)}$.
### Question 4
4. Product Quantization (PQ) splits $d$-dimensional vector into $m$ sub-vectors, clusters each sub-space into 256 centroids using K-Means, and stores 1-byte centroid indices instead of 32-bit floats (32x compression).
### Question 5
5. GPU vector search uses massive parallel CUDA threads to compute matrix-matrix dot products $Q D^T$ across thousands of queries and millions of document vectors in high-speed HBM memory.
