# Theory — Day 281: Random Forests & Ensemble Learning

### 6.1 Definition
Random Forests & Ensemble Learning is a foundational classification technique in Machine Learning. Bagging, bootstrap sampling, random feature sub-selection, tree aggregation, and feature importance analysis.

### 6.2 Intuition
Imagine drawing a boundary (line, curve, or decision region) in feature space that separates different discrete classes of data points (e.g., spam vs ham, cat vs dog).

### 6.3 Why It Exists
Categorical decision-making (e.g., medical diagnosis, credit approval, fraud detection) requires models that output discrete class labels or calibrated probability scores rather than unconstrained continuous numbers.

### 6.4 Real-World Analogy
Sorting mail into post office bins: Based on zip code and envelope dimensions, each letter is routed into a specific discrete bin.

### 6.5 Formal Definition
Given dataset $\mathcal{D} = \{(\mathbf{x}_i, y_i)\}_{i=1}^n$ where $y_i \in \{0, 1\}$ (binary) or $y_i \in \{1, \dots, K\}$ (multiclass), we model conditional probability $P(Y = k \mid \mathbf{X} = \mathbf{x})$.

### 6.6 Mathematical Representation
- **Sigmoid Function**:
  

$$
\sigma(z) = \frac{1}{1 + e^{-z}}, \quad \text{where } z = \mathbf{w}^T \mathbf{x} + b
$$

- **Log Loss / Binary Cross-Entropy**:
  

$$
\mathcal{L}(\mathbf{w}) = -\frac{1}{n} \sum_{i=1}^n \left[ y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i) \right]
$$

- **Entropy & Gini Impurity (Trees)**:
  

$$
\text{Entropy}(S) = -\sum_{i=1}^K p_i \log_2(p_i), \quad \text{Gini}(S) = 1 - \sum_{i=1}^K p_i^2
$$

- **Bayes Theorem**:
  

$$
P(Y = c \mid \mathbf{x}) = \frac{P(\mathbf{x} \mid Y = c) P(Y = c)}{P(\mathbf{x})}
$$

### 6.7 Worked Example
Evaluating a confusion matrix with $TP=80, TN=10, FP=5, FN=5$:
- $\text{Accuracy} = \frac{80+10}{100} = 0.90$.
- $\text{Precision} = \frac{80}{80+5} = \frac{80}{85} = 0.941$.
- $\text{Recall} = \frac{80}{80+5} = \frac{80}{85} = 0.941$.
- $\text{F1} = 2 \times \frac{0.941 \times 0.941}{0.941 + 0.941} = 0.941$.

### 6.8 ML Example
Classifying medical patient records into High Risk ($1$) vs Low Risk ($0$).

### 6.9 Python Example
Scratch NumPy algorithm implementation.

### 6.10 scikit-learn Example
`from sklearn.linear_model import LogisticRegression` / `from sklearn.tree import DecisionTreeClassifier`.

### 6.11 Common Mistakes
- Relying on accuracy for severely imbalanced datasets (e.g., 99% negative class).
- Using default 0.5 decision thresholds when precision/recall costs are asymmetric.

### 6.12 Strengths
Provides probability outputs, interpretable decision boundaries, and robust classification performance.

### 6.13 Weaknesses
Can suffer from overfitting on high-dimensional noisy features if unregularized or unpruned.

### 6.14 Real-World Applications
Spam detection, credit card fraud prevention, medical screening, sentiment analysis.

### 6.15 Interview Insight
Be ready to derive the Sigmoid derivative $\frac{d\sigma(z)}{dz} = \sigma(z)(1 - \sigma(z))$ and explain why Accuracy fails on imbalanced data.

### 6.16 Summary
Random Forests & Ensemble Learning equips Machine Learning systems with decision boundaries and probabilistic class assignments.
