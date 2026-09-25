# Day 17 Solutions: Gram-Schmidt Process

## Level 1: Basic Concepts
1. To transform a set of linearly independent vectors into an orthonormal basis spanning the same space.
2. proj_u(v) = ((u^T v) / (u^T u)) u.
3. u2 = v2 (since proj_{u1}(v2) = 0).
4. Divide each orthogonal vector by its L2 norm: e_i = u_i / ||u_i||.
5. No. span({e1, ..., ek}) = span({v1, ..., vk}).

## Level 2: Calculation
6. u1 = [0, 4]^T. proj_{u1}(v2) = (12/16) [0, 4]^T = [0, 3]^T. u2 = [3, 3]^T - [0, 3]^T = [3, 0]^T.
7. ||u1|| = 4 => e1 = [0, 1]^T. ||u2|| = 3 => e2 = [1, 0]^T.
8. u1 = [1, 1, 0]^T, ||u1||^2 = 2. proj_{u1}(v2) = (1/2) [1, 1, 0]^T = [0.5, 0.5, 0]^T. u2 = [1, 0, 1]^T - [0.5, 0.5, 0]^T = [0.5, -0.5, 1]^T.
9. proj_{u1}(v2) = (2/1) [1, 0]^T = [2, 0]^T. u2 = [2, 5]^T - [2, 0]^T = [0, 5]^T.
10. u1 . u2 = 1(0) + 0(5) = 0. Confirmed.

## Level 3: Conceptual & Proofs
11. u1^T u2 = u1^T (v2 - (u1^T v2 / u1^T u1) u1) = u1^T v2 - (u1^T v2 / u1^T u1) (u1^T u1) = u1^T v2 - u1^T v2 = 0.
12. If vectors are linearly dependent, some v_k lies in the span of previous vectors, resulting in u_k = 0, which cannot be normalized (division by zero).
13. u_k becomes the zero vector.
14. Let A = [v1 | v2 | ... | vn]. We can write v_j = sum_{i=1}^j r_ij e_i. Matrix form: A = Q R, where Q has orthonormal columns e_i and R is upper triangular with r_ij = e_i^T v_j.
15. CGS subtracts projections from original v_k. MGS updates v_k step-by-step using newly computed e_j, reducing floating-point error accumulation.

## Level 4: AI Applications
16. A x = b => Q R x = b => R x = Q^T b. Since R is upper triangular, x is solved instantly via back-substitution.
17. They find successive orthogonal axes of maximum remaining variance.
18. Computing A^T A squares the condition number, causing severe numerical instability. QR avoids forming A^T A.
19. Ensures polynomial feature columns (1, x, x^2, x^3) are orthogonalized to prevent multi-collinearity.
20. Small arithmetic rounding errors accumulate across projections, causing e_k to lose orthogonality with early e_1.

## Level 5: Interview Solutions
21. See `code.py` implementation.
22. Q is m x n (or m x m full QR), R is n x n upper triangular.
23. R_ii = ||u_i|| (norm of orthogonal vector), R_ij = e_i^T v_j for i < j, R_ij = 0 for i > j.
