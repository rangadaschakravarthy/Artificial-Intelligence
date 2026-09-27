# Machine Learning Concept Map — Level 4

```
                                MACHINE LEARNING
                                       │
       ┌───────────────────┬───────────┼───────────┬───────────────────┐
       ▼                   ▼           ▼           ▼                   ▼
  SUPERVISED          UNSUPERVISED   SEMI-SUP    SELF-SUP       REINFORCEMENT
       │                   │           │           │                   │
  ┌────┴────┐         ┌────┴────┐      │           │              ┌────┴────┐
  ▼         ▼         ▼         ▼      ▼           ▼              ▼         ▼
Regression Classif. Cluster. Dim.Red. Pseudo-   Pretext        Agent      Q-Table
Linear    Logistic  K-Means  PCA      Labeling  Contrastive    Env        Bellman
Ridge/Lasso Decision Tree DBSCAN t-SNE             LLM Pretrain   Reward     MDP
  │         Random Forest    UMAP                                 Policy    Exploration
  └─────────┬───────────┘
            ▼
    ML WORKFLOW & PIPELINES
  (Data Prep, Cross-Val, Tuning, Metrics, Explainability)
```

## Paradigm Taxonomy & Architecture Overview
1. **Supervised Learning**: Maps input feature matrix $X$ to continuous output $y$ (Regression) or discrete categories $y$ (Classification).
2. **Unsupervised Learning**: Uncovers structural groupings (Clustering), low-dimensional manifolds (Dimensionality Reduction), or rule associations (Apriori) from unlabeled $X$.
3. **Semi-Supervised & Self-Supervised**: Combines small labeled datasets with large unlabeled datasets (Semi-Supervised) or constructs autonomous pretext supervision directly from unlabeled data (Self-Supervised).
4. **Reinforcement Learning**: Optimizes dynamic policy $\pi(a|s)$ through continuous trial-and-error environment interactions, rewards, and Bellman temporal difference updates.
5. **ML Engineering Workflow**: Combines preprocessing, cross-validation, hyperparameter tuning, evaluation metrics, and explainability into robust production pipelines.
