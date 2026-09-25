# Practice Exercises — Loss Functions

## Level 1 — Basic Understanding
1. What is the difference between a Loss Function and a Cost Function?
2. State the formula for Mean Squared Error (MSE).
3. State the formula for Binary Cross-Entropy (BCE).
4. Why is MSE sensitive to outliers?
5. Which loss function is standard for multi-class classification with Softmax?

## Level 2 — Calculation
1. Compute MSE loss for dataset with true values $[3, 5, 8]$ and predictions $[2, 6, 7]$.
2. Compute MAE loss for the dataset above.
3. Compute BCE loss for sample with true label $y = 0$ and prediction $\hat{y} = 0.2$.
4. Compute derivative of MSE loss $L(y, \hat{y}) = (y - \hat{y})^2$ with respect to prediction $\hat{y}$.
5. Evaluate Huber Loss for outlier error $d = 4.0$ with threshold $\delta = 1.0$.

## Level 3 — Conceptual
1. Prove that Binary Cross-Entropy loss is derived from Maximum Likelihood Estimation (MLE) under a Bernoulli distribution.
2. Prove that Mean Squared Error loss is derived from Maximum Likelihood Estimation (MLE) under a Gaussian noise distribution $y \sim \mathcal{N}(\hat{y}, \sigma^2)$.
3. Show that gradient of Log-Loss $L = -y \ln(\hat{y}) - (1-y)\ln(1-\hat{y})$ w.r.t pre-activation logit $z$ (where $\hat{y} = \sigma(z)$) simplifies cleanly to $\frac{\partial L}{\partial z} = \hat{y} - y$.
4. Compare L1 loss vs L2 loss in terms of gradient magnitude and stability at $y = \hat{y}$.
5. What is Focal Loss and how does it address extreme class imbalance in object detection (RetinaNet)?

## Level 4 — AI/ML Application
1. Implement a custom PyTorch/NumPy Huber Loss function and compare its loss curve against MSE for errors $d \in [-5, 5]$.
2. In Multi-Label Classification where a sample can belong to multiple classes simultaneously, which loss function should be applied across output nodes? (BCE or CCE?).
3. Explain Contrastive Loss and Triplet Loss $L = \max(0, d(a, p) - d(a, n) + \text{margin})$ in Metric Learning (Siamese Networks).

## Level 5 — Interview Questions
1. Derive Categorical Cross-Entropy gradient w.r.t logit vector $\mathbf{z}$: $\nabla_{\mathbf{z}} L = \text{Softmax}(\mathbf{z}) - \mathbf{y}$.
2. Explain Kullback-Leibler (KL) Divergence $D_{KL}(P \parallel Q) = \sum P(x) \ln\left(\frac{P(x)}{Q(x)}\right)$ and its relation to Cross-Entropy $H(P, Q) = H(P) + D_{KL}(P \parallel Q)$.
3. Explain Wasserstein Distance (Earth Mover's Distance) loss in WGANs and why it provides continuous non-vanishing gradients even when distributions do not overlap.
4. What is Label Smoothing in Cross-Entropy loss $\mathbf{y}_{smooth} = (1-\epsilon)\mathbf{y} + \frac{\epsilon}{C}$ and how does it prevent model overconfidence?
5. Explain Cosine Margin Loss (ArcFace / CosFace) for deep face recognition feature embeddings.
