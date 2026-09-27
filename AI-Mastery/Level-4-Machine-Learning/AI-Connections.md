# Prerequisite Connections: Levels 1–3 to Level 4 Machine Learning

```
LEVEL 1: Mathematics for AI
  ├── Linear Algebra  ──► Feature Matrices X, Dot Products, OLS Normal Equation, PCA Eigenvalues
  ├── Calculus        ──► Gradients ∇L, Loss Minimization, Sigmoid Derivatives, Gradient Descent
  ├── Probability     ──► Naive Bayes Classifier, Maximum Likelihood, Sigmoid Probabilities
  └── Statistics      ──► Covariance, Mean/Variance Scaling, Hypothesis Testing, R-Squared
        │
LEVEL 2: Data Science Foundations
  ├── NumPy           ──► Matrix Operations, Array Vectorization, Distance Computations
  ├── Pandas          ──► Data Loading, Categorical Encoding, Handling Missing Values, EDA
  └── Preprocessing   ──► Train/Test Splitting, StandardScaler, MinMax, Data Leakage Prevention
        │
LEVEL 3: AI Fundamentals
  ├── Intelligent Agents ──► Perception-Action Loop, State-Space Formulations, Goal Criteria
  └── Search & Planning  ──► Grid Search Optimization, Dynamic Programming, MDPs, Game Trees
        │
        ▼
LEVEL 4: MACHINE LEARNING (Supervised, Unsupervised, Workflow, RL, Explainability)
```

## Detailed Module Bridge

### 1. Mathematics for AI (Level 1) $\to$ ML Models
- **Linear Algebra**: The feature design matrix $X \in \mathbb{R}^{n \times d}$ and target vector $y \in \mathbb{R}^n$ form the mathematical language of all ML algorithms.
- **Calculus**: Gradient descent parameter updates $\boldsymbol{\theta} \leftarrow \boldsymbol{\theta} - \alpha \nabla \mathcal{L}$ directly apply partial derivatives from Level 1 Calculus.
- **Probability & Statistics**: Bayes theorem directly powers Naive Bayes classifiers; probability calibration evaluates logistic regression outputs.

### 2. Data Science Foundations (Level 2) $\to$ ML Preprocessing
- **NumPy & Pandas**: DataFrames provide the raw features transformed into NumPy arrays for scikit-learn estimation.
- **Data Leakage**: Preprocessing routines (e.g. `StandardScaler`) must learn parameters ($\mu, \sigma$) strictly from $X_{\text{train}}$ to avoid test data contamination.

### 3. AI Fundamentals (Level 3) $\to$ ML Paradigms
- **State-Space Search**: Hyperparameter tuning via Grid Search applies classical systematic search trees to optimization spaces.
- **Agent Loops**: Reinforcement Learning unifies Level 3 Intelligent Agent frameworks with temporal difference Q-learning updates.
