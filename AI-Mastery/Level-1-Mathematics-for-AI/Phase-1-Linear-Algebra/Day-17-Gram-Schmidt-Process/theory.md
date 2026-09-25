# Day 17 Theory: Gram-Schmidt Process

### 1. Simple Definition
The Gram-Schmidt process is a step-by-step method that takes a set of linearly independent vectors and constructs a set of mutually orthogonal (or orthonormal) vectors that span the exact same vector space.

### 2. Intuition
Imagine building coordinate axes step-by-step:
- Take the first vector v1 as your first direction u1.
- Take the second vector v2 and subtract its projection along u1. What remains is perpendicular to u1!
- Take the third vector v3 and subtract its projections along both u1 and u2. What remains is perpendicular to both!
- Normalize all u_i to get an orthonormal set e_i.

### 3. Mathematical Definition
Given linearly independent set {v_1, v_2, ..., v_k}:

1. u_1 = v_1
2. u_2 = v_2 - proj_{u_1}(v_2)
3. u_k = v_k - sum_{j=1}^{k-1} proj_{u_j}(v_k)

Orthonormal vectors: e_i = u_i / ||u_i||.

### 4. Mathematical Notation
proj_u(v) = ( (u^T v) / (u^T u) ) u
e_i = u_i / ||u_i||_2

### 5. Formula
Orthogonalization step:
u_k = v_k - sum_{j=1}^{k-1} ( (u_j^T v_k) / (u_j^T u_j) ) u_j

If u_j are already unit vectors e_j:
u_k = v_k - sum_{j=1}^{k-1} (e_j^T v_k) e_j

### 6. Symbol Explanation
- v_k: k-th input vector to be orthogonalized
- u_k: k-th unnormalized orthogonal vector
- e_k: k-th normalized unit orthogonal vector
- proj_u(v): Vector projection of v onto u

### 7. Step-by-Step Calculation
Perform Gram-Schmidt on v1 = [1, 1]^T and v2 = [1, 0]^T.

Step 1: Set u1 = v1 = [1, 1]^T.
||u1||^2 = 1^2 + 1^2 = 2.

Step 2: Compute projection of v2 onto u1
u1^T v2 = (1)(1) + (1)(0) = 1.
proj_{u1}(v2) = (1 / 2) [1, 1]^T = [0.5, 0.5]^T.

Step 3: Subtract projection from v2
u2 = v2 - proj_{u1}(v2) = [1, 0]^T - [0.5, 0.5]^T = [0.5, -0.5]^T.

Step 4: Check orthogonality of u1 and u2
u1 . u2 = (1)(0.5) + (1)(-0.5) = 0.5 - 0.5 = 0. Perfect!

Step 5: Normalize to get orthonormal basis
e1 = u1 / sqrt(2) = [1/sqrt(2), 1/sqrt(2)]^T.
e2 = u2 / sqrt(0.5) = [1/sqrt(2), -1/sqrt(2)]^T.

### 8. Second Concrete Example
Given 3D vectors v1 = [1, 0, 0]^T, v2 = [1, 1, 0]^T, v3 = [1, 1, 1]^T:
u1 = [1, 0, 0]^T (e1 = [1, 0, 0]^T).
proj_{e1}(v2) = (e1^T v2) e1 = 1 * [1, 0, 0]^T = [1, 0, 0]^T.
u2 = [1, 1, 0]^T - [1, 0, 0]^T = [0, 1, 0]^T (e2 = [0, 1, 0]^T).
u3 = v3 - (e1^T v3) e1 - (e2^T v3) e2 = [1, 1, 1]^T - [1, 0, 0]^T - [0, 1, 0]^T = [0, 0, 1]^T (e3 = [0, 0, 1]^T).
Output: Standard Cartesian basis e1, e2, e3!

### 9. Common Mistakes
- Subtracting projection of v_k onto v_j instead of onto previously computed u_j.
- Numerical drift in Classical Gram-Schmidt (CGS) due to floating-point precision error accumulation. (Solution: Use Modified Gram-Schmidt MGS).

### 10. AI Connection
Gram-Schmidt computes the QR decomposition (A = QR). QR decomposition is used in Least Squares Regression, Eigenvalue Computation (QR algorithm), and Orthogonal Projections in AI model quantization.

### 11. Algorithm Connection
- QR Decomposition: A = QR. The columns of Q are the Gram-Schmidt orthonormal vectors of A's columns!
- Householder Transformations: A more numerically stable algorithm for QR decomposition used internally by NumPy and PyTorch (`torch.linalg.qr`).

### 12. Practical Interpretation
Gram-Schmidt distills a noisy set of feature direction vectors into clean, uncorrelated orthogonal axes without losing any spanned subspace information.

### 13. Interview Insight
Question: Why is Modified Gram-Schmidt (MGS) preferred over Classical Gram-Schmidt (CGS)?
Answer: In standard CGS, round-off errors cause loss of orthogonality when working with high-dimensional matrices. MGS updates the remaining vectors immediately after finding each orthogonal vector, maintaining numerical orthogonality much better.

### 14. Summary
Gram-Schmidt systematically removes parallel vector components to construct orthogonal bases. It forms the foundation of QR decomposition, least-squares solvers, and stable gradient methods in ML.
