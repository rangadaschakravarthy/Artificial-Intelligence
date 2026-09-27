# Practice Solutions — Day 267

## Basic Solutions
1. Self-Supervised Learning is defined by its data input requirements and objective optimization formulation.
2. The learning signal ranges from explicit ground-truth targets to structural data properties or environmental rewards.
3. Industry examples depend on the paradigm (e.g., spam filtering for Supervised, customer segmentation for Unsupervised).

## Conceptual Solutions
4. Human annotation requires domain expertise and time; alternative paradigms leverage unlabeled data or self-generated supervision.
5. Supervised requires explicit $(X, y)$ pairs; other paradigms operate on $X$ alone, partial $y$, or reward feedback $r$.
6. Without explicit labels, evaluation relies on intrinsic metrics (silhouette score, perplexity, return) rather than ground-truth accuracy.

## Calculation Solutions
7. Predictions match at indices 0, 1, 3 (3 correct out of 4). Accuracy = $3/4 = 0.75$ (75%).
8. $R_t = 10 + 0.9(0) + (0.9)^2(100) = 10 + 0 + 81 = 91.0$.

## Implementation Solutions
```python
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# 9. Synthetic Data Generation
X, _ = make_blobs(n_samples=200, centers=3, random_state=42)

# 10. Unsupervised Fitting
kmeans = KMeans(n_clusters=3, random_state=42).fit(X)
print("Cluster Centers:\n", kmeans.cluster_centers_)
```

## ML Reasoning Solutions
11. Semi-Supervised or Self-Supervised Learning. Pre-train representations on all 10,000 images, then fine-tune on the 200 labeled images.
12. Reinforcement Learning via self-play (e.g., AlphaZero), learning optimal policies through state-action-reward loops.

## Dataset Questions
13. Features: input measurements $X$; Label: outcome attribute $y$.

## Interview Solutions
14. Use the comparison matrix: Supervised (labels), Unsupervised (patterns), Semi-Supervised (few labels), Self-Supervised (pretext mask), RL (rewards).
15. Self-Supervised learning scales to uncurated internet-scale text/image data without costly human annotation, building rich general representations.
