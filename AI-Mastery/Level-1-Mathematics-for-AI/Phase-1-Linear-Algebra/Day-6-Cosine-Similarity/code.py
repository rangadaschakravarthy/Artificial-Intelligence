# Day 6 — Cosine Similarity
import numpy as np

u = np.array([1.0, 1.0])
v = np.array([0.0, 2.0])

# 1. Manual Cosine Similarity Calculation
dot_uv = np.dot(u, v)
norm_u = np.sqrt(np.sum(u**2))
norm_v = np.sqrt(np.sum(v**2))

cos_sim_manual = dot_uv / (norm_u * norm_v)
cos_dist_manual = 1.0 - cos_sim_manual

print(f"Manual Cosine Similarity: {cos_sim_manual:.4f}")
print(f"Manual Cosine Distance: {cos_dist_manual:.4f}")

# 2. NumPy / Unit Vector Shortcut
u_hat = u / np.linalg.norm(u)
v_hat = v / np.linalg.norm(v)

cos_sim_unit = np.dot(u_hat, v_hat)
print(f"Unit Vector Dot Product Cosine Similarity: {cos_sim_unit:.4f}")

# 3. Document Matching Example (Scale Invariance)
doc_short = np.array([2, 1, 0])      # 2 'cat', 1 'dog'
doc_long = np.array([200, 100, 0])    # 200 'cat', 100 'dog' (100x length)

sim_docs = np.dot(doc_short, doc_long) / (np.linalg.norm(doc_short) * np.linalg.norm(doc_long))
print(f"Cosine Similarity between Short and Long doc: {sim_docs:.4f} (Perfect match!)")
