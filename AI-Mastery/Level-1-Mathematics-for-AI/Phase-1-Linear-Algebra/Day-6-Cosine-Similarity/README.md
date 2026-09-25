# Day 6 — Cosine Similarity

## Learning Objectives
- Understand cosine similarity as the cosine of the angle between two vectors
- Distinguish between Cosine Similarity and Cosine Distance
- Calculate cosine similarity manually and using NumPy
- Apply cosine similarity in vector search, document retrieval, and recommendation systems

## Prerequisites
Day 4 — Dot Product, Day 5 — Norms and Distances

## Topics Covered
- Geometric foundation of Cosine Similarity
- Formula: $\text{CosineSimilarity}(\mathbf{u}, \mathbf{v}) = \frac{\mathbf{u} \cdot \mathbf{v}}{||\mathbf{u}||_2 ||\mathbf{v}||_2}$
- Range of Cosine Similarity $[-1, 1]$ and $[0, 1]$ for non-negative embeddings
- Cosine Distance = $1 - \text{CosineSimilarity}$
- Scale-invariance property of cosine similarity

## Why This Matters for AI
Cosine similarity measures orientation rather than magnitude. In NLP and Semantic Search (RAG systems), document length variations shouldn't affect semantic similarity, making cosine similarity the gold standard metric.

## Study Order
1. Read theory.md
2. Study examples.md
3. Run code.py
4. Complete practice.md
5. Verify with solution.md

## Practical Work
Compute cosine similarity between word vectors / document TF-IDF vectors using NumPy and SciPy.

## Interview Preparation
Explain why Cosine Similarity is scale-invariant and when to use it over Euclidean distance.

## Completion Checklist
- [ ] I can state the formula for Cosine Similarity
- [ ] I can calculate cosine similarity step-by-step
- [ ] I understand scale invariance
- [ ] I can convert Cosine Similarity to Cosine Distance

## Estimated Difficulty
Beginner
