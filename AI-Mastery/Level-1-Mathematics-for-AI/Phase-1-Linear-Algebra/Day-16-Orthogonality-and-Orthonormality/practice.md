# Day 16 Practice Questions: Orthogonality & Orthonormality

## Level 1: Basic Concept Questions
1. Define orthogonality in terms of dot product.
2. What additional condition makes an orthogonal set orthonormal?
3. What is the value of Q^T Q for an orthonormal matrix Q?
4. True or False: Any set of non-zero orthogonal vectors is linearly independent.
5. If u ⊥ v, what is ||u + v||^2 according to the Pythagorean theorem?

## Level 2: Calculation & Operations
6. Test if u = [2, 5]^T and v = [10, -4]^T are orthogonal.
7. Normalize vector v = [3, -4, 0]^T to form a unit vector.
8. Verify if Q = [[0.6, -0.8], [0.8, 0.6]] is an orthogonal matrix.
9. Given u = [1, 1, 1]^T, find a non-zero vector v orthogonal to u.
10. If ||u|| = 3, ||v|| = 4, and u ⊥ v, compute ||u - v||.

## Level 3: Conceptual & Proof Reasoning
11. Prove that if Q is an orthogonal matrix, det(Q) = +1 or -1.
12. Show that if u and v are orthogonal, (u + v) . (u - v) = ||u||^2 - ||v||^2.
13. Explain why the columns of an n x n orthogonal matrix form an orthonormal basis for R^n.
14. Show that ||Qx||_2 = ||x||_2 for any orthogonal matrix Q.
15. If Q1 and Q2 are orthogonal matrices, prove that their product Q1 Q2 is also orthogonal.

## Level 4: AI & ML Application Scenarios
16. Why is Q^T used as Q^(-1) in SVD (Singular Value Decomposition)?
17. Explain how orthogonal feature projections eliminate multi-collinearity in linear regression.
18. In Transformer architectures, why are orthogonal projection weights desirable for Query and Key matrices?
19. How does orthogonal weight initialization help avoid exploding gradients in deep networks?
20. Why does cosine similarity between two orthogonal embedding vectors equal 0?

## Level 5: Interview-Style Technical Questions
21. "Given a non-square matrix Q of shape (m, n) with m > n and orthonormal columns, is Q Q^T equal to I?" Explain.
22. "How would you computationally verify if a given matrix is orthogonal in NumPy?"
23. "Derive the gradient of loss L = ||Qx - y||^2 with respect to x when Q is an orthogonal matrix."
