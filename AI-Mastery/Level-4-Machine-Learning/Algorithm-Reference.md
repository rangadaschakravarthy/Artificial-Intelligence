# Machine Learning Algorithm Reference Guide

| Algorithm | Learning Type | Task | Key Principle | Requires Scaling? | Strengths | Weaknesses |
| --------- | ------------- | ---- | ------------- | ----------------- | --------- | ---------- |
| **Linear Regression** | Supervised | Regression | OLS Residual Minimization | Yes (for Regularization) | Highly interpretable, fast, analytical solution | Assumes linear relationships |
| **Logistic Regression** | Supervised | Classification | Sigmoidal Log-Odds Probabilities | Yes | Probabilistic outputs, interpretable coefficients | Linear decision boundary |
| **K-Nearest Neighbors ($k$-NN)** | Supervised | Both | Distance-based majority voting | **Mandatory** | Simple, no training phase (lazy) | High inference cost $O(nd)$, memory heavy |
| **Decision Trees** | Supervised | Both | Recursive Gini/Entropy splits | No | Non-linear, highly interpretable | Prone to overfitting (high variance) |
| **Random Forest** | Supervised | Both | Bagging ensemble of trees | No | Robust, handles high dimensions, reduces variance | Less interpretable than single tree |
| **Naive Bayes** | Supervised | Classification | Bayes Theorem + Conditional Independence | No | Extremely fast, excels at text classification | Independence assumption often violated |
| **Support Vector Machines** | Supervised | Both | Maximum margin hyperplane + Kernels | **Mandatory** | Powerful in high dimensions, effective non-linear kernels | Slow on large datasets $O(n^3)$ |
| **K-Means** | Unsupervised | Clustering | Centroid distance minimization | **Mandatory** | Fast $O(nKd)$, simple implementation | Requires choosing $K$, assumes spherical clusters |
| **DBSCAN** | Unsupervised | Clustering | Density continuity & $\epsilon$-neighborhoods | **Mandatory** | Finds arbitrary cluster shapes, identifies noise | Sensitivity to $\epsilon$ and MinPts parameters |
| **PCA** | Unsupervised | Dim. Reduction | Covariance variance maximization | **Mandatory** | Linear feature compression, fast | Linear projection only |
| **Apriori** | Unsupervised | Association | Frequent itemset generation | No | Simple, interpretable association rules | Exponential candidate itemset search space |
| **Q-Learning** | Reinforcement | Control | Bellman temporal difference updates | No | Model-free control, learns optimal policy | Sample inefficient, limited to small discrete state spaces |
