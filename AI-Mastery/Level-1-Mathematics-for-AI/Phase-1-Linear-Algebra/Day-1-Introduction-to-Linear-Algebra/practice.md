# Practice Exercises — Introduction to Linear Algebra

## Level 1 — Basic Understanding
1. Define what a scalar is and give 2 real-world examples.
2. What is the mathematical difference between a vector and a matrix?
3. How is a 28x28 grayscale image represented in Linear Algebra?
4. What does the notation $\mathbf{x} \in \mathbb{R}^4$ mean?
5. Name 3 machine learning algorithms that rely heavily on Linear Algebra.

## Level 2 — Calculation
1. Convert the following item properties into a feature vector: height=180cm, weight=75kg, age=25.
2. Given a dataset of 5 patients with 4 health measurements each, what are the dimensions of the dataset matrix $\mathbf{X}$?
3. If a neural network layer takes a vector of size 10 and outputs a vector of size 5, what are the dimensions of the weight matrix $\mathbf{W}$?
4. Calculate the output $y = w \cdot x + b$ for scalar values $w = 3.5$, $x = 4.0$, $b = 1.2$.
5. If an RGB image has resolution 64x64, what shape is its tensor representation?

## Level 3 — Conceptual
1. Why can't computers process raw text directly without Linear Algebra?
2. Explain the geometric intuition of representing data points as vectors in space.
3. What is the difference between a 1D tensor and a 2D tensor?
4. How does vectorization improve computational efficiency compared to Python `for` loops?
5. What happens to a feature vector when we multiply it by a diagonal scaling matrix?

## Level 4 — AI/ML Application
1. A spam detector uses 3 features: word count, uppercase letter count, contains '$' symbol (1 or 0). Construct the feature vector for an email with 150 words, 12 uppercase letters, and 1 '$' symbol.
2. Explain how recommendation systems (like Netflix) use a matrix of Users vs Movies.
3. Given an input $\mathbf{x} = [2, 3]^T$, compute linear model output $y = \mathbf{w}^T \mathbf{x} + b$ where $\mathbf{w} = [0.5, -1.0]^T$ and $b = 2.0$.

## Level 5 — Interview Questions
1. Why is GPU hardware uniquely suited for Linear Algebra operations in deep learning?
2. Explain the concept of linear transformation high-level to a non-technical stakeholder.
3. How does data dimensionality impact computational complexity in machine learning?
4. What is the difference between element-wise operations and matrix transformations?
5. Why do we add a bias term $b$ to linear transformation $\mathbf{W}\mathbf{x}$?
