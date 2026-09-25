# Solutions — Introduction to Linear Algebra

## Level 1 — Basic Understanding Solutions
### Question 1
A scalar is a single real number representing magnitude only (e.g. temperature = 30°C, speed = 60 mph).
### Question 2
A vector is a 1D array of numbers representing magnitude and direction (or a point in space). A matrix is a 2D grid of numbers organized in rows and columns.
### Question 3
A 28x28 grayscale image is represented as a 2D matrix of shape (28, 28) with entries ranging from 0 to 255.
### Question 4
$\mathbf{x} \in \mathbb{R}^4$ means $\mathbf{x}$ is a vector containing 4 real-numbered components.
### Question 5
1. Linear Regression, 2. Principal Component Analysis (PCA), 3. Convolutional Neural Networks (CNNs).

## Level 2 — Calculation Solutions
### Question 1
1. Feature vector $\mathbf{x} = [180, 75, 25]^T \in \mathbb{R}^3$.
### Question 2
2. The dataset matrix $\mathbf{X}$ has 5 rows (samples) and 4 columns (features), so its shape is $5 \times 4$.
### Question 3
3. Weight matrix $\mathbf{W}$ must have dimensions $5 \times 10$ (or $10 \times 5$ depending on multiplication convention $\mathbf{W}\mathbf{x}$ vs $\mathbf{x}\mathbf{W}$). For $\mathbf{y} = \mathbf{W}\mathbf{x}$, shape is $5 \times 10$.
### Question 4
4. Given $w=3.5, x=4.0, b=1.2$: $y = (3.5 \times 4.0) + 1.2 = 14.0 + 1.2 = 15.2$.
### Question 5
5. An RGB image of size 64x64 has 3 color channels, so its tensor shape is $(64, 64, 3)$ or $(3, 64, 64)$.

## Level 3 — Conceptual Solutions
### Question 1
1. Raw text consists of discrete characters/words with no innate numerical arithmetic. ML algorithms require numerical matrices to perform gradient descent optimization.
### Question 2
2. Geometric intuition: A vector with $n$ entries corresponds to a point or directional arrow in $n$-dimensional space. Distance between points measures similarity.
### Question 3
3. A 1D tensor is a vector (single axis/list of numbers). A 2D tensor is a matrix (two axes: rows and columns).
### Question 4
4. Vectorization uses CPU/GPU SIMD (Single Instruction Multiple Data) registers to execute operations on entire data blocks in parallel instead of sequential CPU cycles.
### Question 5
5. Multiplying a feature vector by a diagonal scaling matrix scales each feature independently by the corresponding diagonal element.

## Level 4 — AI/ML Application Solutions
### Question 1
1. Email feature vector $\mathbf{x} = [150, 12, 1]^T$.
### Question 2
2. Users vs Movies matrix has Users as rows and Movies as columns. Matrix cell $(i, j)$ contains User $i$'s rating for Movie $j$. Matrix factorization breaks this matrix down to discover latent preferences.
### Question 3
3. Given $\mathbf{x} = [2, 3]^T, \mathbf{w} = [0.5, -1.0]^T, b = 2.0$:
$$\mathbf{w}^T \mathbf{x} = (0.5 \times 2) + (-1.0 \times 3) = 1.0 - 3.0 = -2.0$$
$$y = -2.0 + 2.0 = 0.0$$

## Level 5 — Interview Questions Solutions
### Question 1
1. GPUs contain thousands of lightweight cores designed to execute millions of matrix multiplications in parallel, matching the mathematical structure of neural network operations.
### Question 2
2. Linear transformation is like stretching, rotating, or scaling a geometric grid while keeping lines straight and the origin fixed.
### Question 3
3. High dimensionality increases search space volume exponentially ('curse of dimensionality'), requiring more data and computational memory to avoid overfitting.
### Question 4
4. Element-wise operations apply arithmetic independently to corresponding positions ($a_i + b_i$). Matrix transformations map input vectors to new coordinate spaces via dot products.
### Question 5
5. The bias term $b$ allows the linear decision boundary/hyperplane to translate (shift) away from the origin, enabling models to fit data not centered at zero.
