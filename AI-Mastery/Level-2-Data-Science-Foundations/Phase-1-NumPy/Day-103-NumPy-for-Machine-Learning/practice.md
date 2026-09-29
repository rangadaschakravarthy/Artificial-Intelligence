# Day 103 Practice Questions: NumPy for Machine Learning

## Level 1 — Basic
1. What formula represents the forward pass of a linear model with weights $W$ and bias $b$?
2. What activation function bounds values between $0.0$ and $1.0$?
3. What function converts raw logits into a multi-class probability distribution summing to $1.0$?
4. What is the derivative of ReLU $f(x) = \max(0, x)$ for $x > 0$?
5. What loss function is standard for multi-class classification models?

## Level 2 — Coding
6. Write a pure NumPy function for ReLU activation `relu(x)` and its gradient `relu_grad(x)`.
7. Implement Mean Squared Error loss function `mse(y_true, y_pred)`.
8. Write code to convert target vector `y = np.array([0, 1, 2])` to a one-hot encoded matrix.
9. Implement a Single Layer Perceptron forward pass: $	ext{output} = 	ext{sigmoid}(X W + b)$.
10. Implement L2 Regularization penalty loss: $\frac{\lambda}{2} \sum W^2$.

## Level 3 — Data Analysis
11. Predict output shape of prediction $X W$ for $X$ of shape `(100, 10)` and $W$ of shape `(10, 5)`.
12. Why do we add epsilon `1e-15` inside `np.log(y_prob)` when computing Cross-Entropy loss?
13. Explain why gradient $dW = \frac{2}{N} X^T (\hat{y} - y)$ requires transposing $X$.
14. Predict output of `relu(np.array([-5, 0, 5]))`.
15. Predict output of `sigmoid(0.0)`.

## Level 4 — Debugging
16. Fix error: `ValueError: shapes (100,10) and (100,5) not aligned` during linear forward pass $X W$.
17. Fix bug where weights blew up to `inf`/`nan` during Gradient Descent due to high learning rate.
18. Fix error when computing Cross-Entropy loss where zero probability caused `log(0) = -inf`.

## Level 5 — AI/ML Application
19. Implement Logistic Regression forward pass and loss: $\hat{y} = \sigma(X W + b)$, $	ext{Loss} = 	ext{BCE}(\hat{y}, y)$.
20. Implement Logistic Regression gradient updates: $dW = \frac{1}{N} X^T (\hat{y} - y)$, $db = \frac{1}{N} \sum (\hat{y} - y)$.
21. Connect raw NumPy tensor operations to PyTorch `torch.nn.Linear` layers.

## Level 6 — Interview Questions
22. Derive the gradient of MSE loss with respect to weight matrix $W$: $
abla_W \frac{1}{N} \|X W - y\|^2$.
23. Explain how numerical stability subtraction $\exp(z - \max(z))$ prevents overflow in Softmax.
24. What is the difference between Batch Gradient Descent, Stochastic Gradient Descent (SGD), and Mini-Batch SGD?
25. Demonstrate how to implement a complete 2-layer Neural Network forward pass in pure NumPy.
26. How do tensor memory strides impact matrix multiplication speed during forward propagation?
