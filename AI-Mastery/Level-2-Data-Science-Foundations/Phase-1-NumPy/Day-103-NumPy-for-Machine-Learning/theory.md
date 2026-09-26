# Day 103 Theory: NumPy for Machine Learning

### 1. What Is It?
NumPy for Machine Learning is the application of vectorized array algebra to implement ML mathematical foundations—prediction forward passes, activations, loss functions, and gradient descent—without third-party ML frameworks.

### 2. Why Does It Exist?
High-level libraries like Scikit-Learn hide mathematical implementation details. Building algorithms in raw NumPy builds fundamental engineering mastery of tensor transformations and vector calculus.

### 3. Intuition
Imagine learning how a car engine works. Using Scikit-Learn is driving the car. Implementing algorithms in NumPy is taking the engine apart and building it from pistons and gears.

### 4. Syntax
```python
import numpy as np

# Forward Pass: y_pred = X @ W + b
y_pred = X @ W + b

# Loss: MSE = mean((y_pred - y)^2)
loss = np.mean((y_pred - y) ** 2)

# Gradient: dW = (2 / N) * X.T @ (y_pred - y)
dW = (2 / len(X)) * X.T @ (y_pred - y)

# Weight Update: W = W - lr * dW
W -= learning_rate * dW
```

### 5. Parameters
- `learning_rate` ($\eta$): Step size multiplier controlling weight update magnitude.
- `epochs`: Number of full training iterations over the dataset.

### 6. How It Works
1. Forward Pass: Compute predictions $\hat{y} = X W + b$.
2. Loss Calculation: Measure discrepancy $L(\hat{y}, y)$.
3. Gradient Calculation: Compute partial derivative $rac{\partial L}{\partial W} = rac{2}{N} X^T (\hat{y} - y)$.
4. Gradient Descent: Update parameters $W \leftarrow W - \eta rac{\partial L}{\partial W}$.

### 7. Simple Example
```python
import numpy as np
x = np.array([1.0, 2.0, 3.0])
w = 0.5
y_pred = x * w
print("Predictions:", y_pred)
```

### 8. Intermediate Example
```python
import numpy as np
# Vectorized Sigmoid
def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

logits = np.array([-1.0, 0.0, 2.0])
print("Sigmoid Probabilities:", sigmoid(logits))
```

### 9. Output Interpretation
`sigmoid(z)` maps unconstrained linear activation logits into bounded probability values between 0.0 and 1.0.

### 10. Common Mistakes
- Mismatching dimensions during gradient matrix multiplication ($X^T @ 	ext{error}$).
- Forgetting to divide gradients by batch size $N$, leading to learning rates scaling with dataset size.

### 11. Data Science Connection
Extracting feature arrays `X = df.values` from Pandas DataFrames to feed into custom NumPy model pipelines.

### 12. AI/ML Connection
This exact tensor matrix math is executed inside PyTorch `autograd` and CUDA GPU kernels during deep learning backpropagation.

### 13. Interview Insight
Question: "Derive the vectorized weight gradient for Linear Regression with MSE loss."
Answer: Loss $L = rac{1}{N} \|X W - y\|^2 = rac{1}{N} (X W - y)^T (X W - y)$. Taking derivative wrt $W$: $
abla_W L = rac{2}{N} X^T (X W - y) = rac{2}{N} X^T (\hat{y} - y)$.

### 14. Summary
Machine Learning models consist of matrix forward passes, loss functions, and gradient updates. All can be cleanly implemented in raw vectorized NumPy.
