# Day 17 Worked Examples: Gram-Schmidt Process

## Example 1: Very Easy — 2D Orthogonalization
Given v1 = [3, 0]^T and v2 = [2, 2]^T:
u1 = [3, 0]^T.
proj_{u1}(v2) = ((3*2 + 0*2) / 9) [3, 0]^T = (6/9) [3, 0]^T = [2, 0]^T.
u2 = [2, 2]^T - [2, 0]^T = [0, 2]^T.
u1 . u2 = 0.

## Example 2: Beginner — Orthonormalization in 2D
From Example 1:
||u1|| = 3 => e1 = [1, 0]^T.
||u2|| = 2 => e2 = [0, 1]^T.
Set {e1, e2} is an orthonormal basis.

## Example 3: Intermediate — 3D Vector Gram-Schmidt
v1 = [1, 0, 1]^T, v2 = [1, 1, 0]^T.
u1 = [1, 0, 1]^T, ||u1||^2 = 2.
proj_{u1}(v2) = ((1*1 + 0*1 + 1*0) / 2) [1, 0, 1]^T = 0.5 [1, 0, 1]^T = [0.5, 0, 0.5]^T.
u2 = [1, 1, 0]^T - [0.5, 0, 0.5]^T = [0.5, 1, -0.5]^T.
u1 . u2 = 1(0.5) + 0(1) + 1(-0.5) = 0.

## Example 4: AI Focus — QR Decomposition via Gram-Schmidt
Let A = [[1, 1], [1, 0]].
From Day 17 Theory calculation, Gram-Schmidt orthonormal columns give:
Q = [[1/sqrt(2), 1/sqrt(2)], [1/sqrt(2), -1/sqrt(2)]].
R = Q^T A = [[sqrt(2), 1/sqrt(2)], [0, 1/sqrt(2)]].
Verification: Q @ R = [[1, 1], [1, 0]] = A.

## Example 5: Real-World AI — Feature De-correlation
When input data features x1 and x2 are highly correlated, applying Gram-Schmidt transforms them into independent orthogonal features e1 and e2, preventing ill-conditioned covariance matrices in regression and neural networks.
