# Day 25 — Linear Algebra AI Mini-Project
# AI Semantic Search Engine using Pure Linear Algebra & NumPy

import numpy as np

# 1. Corpus of Documents
documents = [
    "Deep learning neural networks process data using matrix multiplication.",
    "Linear algebra vectors and matrices are essential for machine learning.",
    "Convolutional networks process image pixels for computer vision.",
    "Natural language processing uses word embeddings and transformer models.",
    "Cooking recipes require fresh ingredients, flour, sugar, and baking powder."
]

# Vocabulary extraction
vocab = sorted(list(set(" ".join(documents).lower().replace(".", "").replace(",", "").split())))
word2idx = {w: i for i, w in enumerate(vocab)}
v_dim = len(vocab)
d_num = len(documents)

print(f"Corpus: {d_num} documents, Vocabulary size: {v_dim} unique words")

# 2. Build Term-Document Matrix A (shape v_dim x d_num)
A = np.zeros((v_dim, d_num))
for doc_idx, doc in enumerate(documents):
    words = doc.lower().replace(".", "").replace(",", "").split()
    for w in words:
        A[word2idx[w], doc_idx] += 1.0

# 3. Apply TF-IDF Weighting
# TF = count / doc_len
doc_lens = np.sum(A, axis=0)
TF = A / doc_lens

# IDF = log(N / df)
df = np.sum(A > 0, axis=1)
IDF = np.log((d_num + 1.0) / (df + 1.0)) + 1.0  # Smoothed IDF

TFIDF = TF * IDF[:, np.newaxis]
print(f"TF-IDF Matrix shape: {TFIDF.shape}")

# 4. Latent Semantic Analysis (LSA) via Truncated SVD (k = 2 topics)
U, S, Vt = np.linalg.svd(TFIDF, full_matrices=False)
k = 2
U_k = U[:, :k]         # Word topic space (v_dim x 2)
S_k = np.diag(S[:k])   # Singular values (2 x 2)
V_k = Vt[:k, :].T      # Document Embeddings (d_num x 2)

print(f"Compressed Document Embeddings V_k shape: {V_k.shape}")

# 5. Semantic Search Query Processor
def search(query_str, top_n=2):
    # Vectorize query
    q_vec = np.zeros(v_dim)
    q_words = query_str.lower().split()
    for w in q_words:
        if w in word2idx:
            q_vec[word2idx[w]] += 1.0
            
    # Project Query into Latent SVD Topic Space: q_k = U_k^T * q
    q_k = U_k.T @ q_vec
    
    # Compute Cosine Similarity between q_k and all Document Embeddings V_k
    scores = []
    q_norm = np.linalg.norm(q_k)
    if q_norm == 0:
        return []
        
    for doc_idx in range(d_num):
        d_vec = V_k[doc_idx]
        d_norm = np.linalg.norm(d_vec)
        sim = np.dot(q_k, d_vec) / (q_norm * d_norm) if d_norm > 0 else 0.0
        scores.append((sim, doc_idx))
        
    # Sort by highest similarity score
    scores.sort(key=lambda x: x[0], reverse=True)
    return scores[:top_n]

# Test Queries
query1 = "neural network matrices"
print(f"\n--- Query: '{query1}' ---")
results1 = search(query1)
for rank, (score, idx) in enumerate(results1, 1):
    print(f"Rank {rank} (Score: {score:.4f}): '{documents[idx]}'")

query2 = "baking ingredients"
print(f"\n--- Query: '{query2}' ---")
results2 = search(query2)
for rank, (score, idx) in enumerate(results2, 1):
    print(f"Rank {rank} (Score: {score:.4f}): '{documents[idx]}'")
