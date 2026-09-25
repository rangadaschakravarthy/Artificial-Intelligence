# Day 16 Solutions: Orthogonality & Orthonormality

## Level 1: Basic Concepts
1. Two vectors u and v are orthogonal if their dot product u . v = 0.
2. The vectors must all have unit norm (magnitude equal to 1).
3. Q^T Q = I (the Identity Matrix).
4. True. Orthogonal non-zero vectors are always linearly independent.
5. ||u + v||^2 = ||u||^2 + ||v||^2.

## Level 2: Calculation
6. u . v = (2)(10) + (5)(-4) = 20 - 20 = 0. Yes, orthogonal.
7. ||v|| = sqrt(9 + 16 + 0) = 5. Normalized v_hat = [0.6, -0.8, 0.0]^T.
8. Col 1 norm = sqrt(0.36 + 0.64) = 1. Col 2 norm = sqrt(0.64 + 0.36) = 1. Dot product = (0.6)(-0.8) + (0.8)(0.6) = 0. Yes, orthogonal matrix.
9. Need v1 + v2 + v3 = 0. E.g., v = [1, -1, 0]^T. Dot product: 1 - 1 + 0 = 0.
10. Since u ⊥ v, ||u - v||^2 = ||u||^2 + ||v||^2 = 9 + 16 = 25. Thus ||u - v|| = 5.

## Level 3: Conceptual & Proofs
11. Q^T Q = I => det(Q^T Q) = det(I) = 1 => det(Q^T) det(Q) = (det(Q))^2 = 1 => det(Q) = ±1.
12. (u + v) . (u - v) = u.u - u.v + v.u - v.v = ||u||^2 - 0 + 0 - ||v||^2 = ||u||^2 - ||v||^2.
13. The n columns are orthonormal, hence non-zero and pairwise orthogonal, making them linearly independent. n independent vectors in R^n form a basis for R^n.
14. ||Qx||^2 = (Qx)^T (Qx) = x^T Q^T Q x = x^T I x = x^T x = ||x||^2. Taking square roots gives ||Qx|| = ||x||.
15. (Q1 Q2)^T (Q1 Q2) = Q2^T Q1^T Q1 Q2 = Q2^T I Q2 = Q2^T Q2 = I. Thus Q1 Q2 is orthogonal.

## Level 4: AI Applications
16. Because Q^T Q = I implies Q^(-1) = Q^T, eliminating the need for complex matrix inversion.
17. Orthogonal features have zero correlation (covariance = 0), so each predictor provides unique variance without collinearity.
18. Preserves vector energy and angles, preventing representation collapse during attention projections.
19. Matrix multiplication by Q preserves vector norm (||Qx|| = ||x||), preventing singular values from shrinking to 0 or blowing up.
20. Cosine similarity = (u . v) / (||u|| ||v||) = 0 / (||u|| ||v||) = 0.

## Level 5: Interview Solutions
21. No. Q^T Q = I_n (n x n identity), but Q Q^T is an m x m projection matrix of rank n onto the column space of Q, not the m x m identity matrix.
22. Check `np.allclose(Q.T @ Q, np.eye(Q.shape[1]))`.
23. L = (Qx - y)^T (Qx - y) = x^T Q^T Q x - 2 y^T Q x + y^T y = x^T x - 2 y^T Q x + y^T y.
    dL/dx = 2 x - 2 Q^T y = 2(x - Q^T y).
