# Day 17 Practice Questions: Gram-Schmidt Process

## Level 1: Basic Concept Questions
1. What is the primary objective of the Gram-Schmidt process?
2. What formula computes the vector projection of v onto u?
3. If v1 and v2 are already orthogonal, what does Gram-Schmidt output for u2?
4. How do you convert an orthogonal basis into an orthonormal basis?
5. Does the Gram-Schmidt process change the subspace spanned by the vectors?

## Level 2: Calculation & Operations
6. Apply Gram-Schmidt to v1 = [0, 4]^T and v2 = [3, 3]^T.
7. Normalize the resulting orthogonal vectors from Question 6.
8. Perform Gram-Schmidt on 3D vectors v1 = [1, 1, 0]^T, v2 = [1, 0, 1]^T.
9. Given u1 = [1, 0]^T and v2 = [2, 5]^T, compute proj_{u1}(v2) and u2.
10. Verify that u1 and u2 from Question 9 are orthogonal.

## Level 3: Conceptual & Proof Reasoning
11. Prove that u2 = v2 - proj_{u1}(v2) is orthogonal to u1.
12. Explain why Gram-Schmidt requires the input vectors to be linearly independent.
13. If v_k is in span({v1, ..., v_{k-1}}), what happens when computing u_k?
14. Show how matrix A can be factored as A = QR using Gram-Schmidt outputs.
15. Compare Classical Gram-Schmidt (CGS) vs. Modified Gram-Schmidt (MGS).

## Level 4: AI & ML Application Scenarios
16. How is Gram-Schmidt used to solve linear least squares problems A x = b?
17. In Principal Component Analysis (PCA), how are Gram-Schmidt projections related to principal axes?
18. Why is QR decomposition preferred over computing inverse matrix (A^T A)^(-1) in linear regression?
19. How does Gram-Schmidt help in constructing orthogonal polynomial features?
20. Why do numerical rounding errors cause loss of orthogonality in CGS?

## Level 5: Interview-Style Technical Questions
21. "Implement Gram-Schmidt in Python without using `np.linalg.qr`."
22. "Given matrix A of shape (m, n) with rank n, what are the dimensions of Q and R in QR decomposition?"
23. "Derive R_ij in terms of vector dot products from the Gram-Schmidt process."
