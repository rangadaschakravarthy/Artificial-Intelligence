# Day 16 Worked Examples: Orthogonality & Orthonormality

## Example 1: Very Easy — Checking 2D Orthogonality
Given u = [1, 2]^T and v = [-2, 1]^T:
u . v = (1)(-2) + (2)(1) = -2 + 2 = 0.
The vectors are orthogonal.

## Example 2: Beginner — Normalizing an Orthogonal Set
Given orthogonal vectors v1 = [2, 0]^T and v2 = [0, -3]^T:
Norms: ||v1|| = 2, ||v2|| = 3.
Orthonormal set: u1 = [1, 0]^T, u2 = [0, -1]^T.

## Example 3: Intermediate — Verifying an Orthogonal Matrix
Given Q = [[1/sqrt(2), -1/sqrt(2)], [1/sqrt(2), 1/sqrt(2)]]:
Column 1 norm: sqrt(1/2 + 1/2) = 1.
Column 2 norm: sqrt(1/2 + 1/2) = 1.
Dot product of col 1 & col 2: (1/sqrt(2))(-1/sqrt(2)) + (1/sqrt(2))(1/sqrt(2)) = -1/2 + 1/2 = 0.
Q is an orthonormal matrix.

## Example 4: AI/ML Focus — Norm Preservation in Feature Transformation
Let x = [3, 4]^T. ||x|| = 5.
Apply rotation matrix Q with θ = 90 deg: Q = [[0, -1], [1, 0]].
Qx = [[0, -1], [1, 0]] [3, 4]^T = [-4, 3]^T.
||Qx|| = sqrt((-4)^2 + 3^2) = 5.
Vector length is perfectly preserved!

## Example 5: Real-World AI — Weight Initialization in RNNs
In Recurrent Neural Networks (RNNs), repeatedly multiplying hidden state h_t by weight matrix W can lead to exploding/vanishing gradients. If W is initialized as an orthogonal matrix Q, ||Q h_t|| = ||h_t||, maintaining gradient norm equal to 1 across arbitrary sequence lengths.
