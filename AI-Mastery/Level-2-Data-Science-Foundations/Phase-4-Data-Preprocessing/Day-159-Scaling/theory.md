# Day 159 Theory: Scaling

### 1. What Is It?
Feature Scaling rescales numerical features into a common range or distribution scale so that no single feature dominates optimization gradients or distance calculations.

### 2. Mathematical Impact
- **Distance Metrics**: Euclidean distance $d(\mathbf{a}, \mathbf{b}) = \sqrt{\sum_{i=1}^d (a_i - b_i)^2}$. If feature 1 ranges $[0, 100000]$ and feature 2 ranges $[0, 1]$, feature 1 completely dictates distance.
- **Gradient Descent**: Loss function contours $\mathcal{L}(w_1, w_2)$ for unscaled features become highly elongated ellipses, causing gradients to oscillate wildly. Scaling transforms contours into concentric circles, enabling direct convergence.

### 3. Summary
Scaling accelerates gradient descent optimization and ensures equal feature weighting in distance-based ML algorithms.
