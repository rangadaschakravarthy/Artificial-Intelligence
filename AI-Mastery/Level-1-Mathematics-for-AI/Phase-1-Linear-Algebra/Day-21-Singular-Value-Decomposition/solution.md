# Solutions — Singular Value Decomposition

## Level 1 — Basic Understanding Solutions
### Question 1
1. $\mathbf{A}_{m \times n} = \mathbf{U}_{m \times m} \mathbf{\Sigma}_{m \times n} \mathbf{V}^T_{n \times n}$.
### Question 2
2. $\mathbf{U}$ is $100 \times 100$, $\mathbf{\Sigma}$ is $100 \times 20$, $\mathbf{V}^T$ is $20 \times 20$.
### Question 3
3. Yes! SVD applies to ANY $m \times n$ rectangular matrix.
### Question 4
4. Singular values are square roots of eigenvalues of $\mathbf{A}^T \mathbf{A}$: $\sigma_i = \sqrt{\lambda_i(\mathbf{A}^T \mathbf{A})}$.
### Question 5
5. No. Singular values are ALWAYS real and non-negative ($\sigma_i \ge 0$).

## Level 2 — Calculation Solutions
### Question 1
1. $\mathbf{A}^T \mathbf{A} = \text{diag}(9, 16) \implies \lambda_1 = 16, \lambda_2 = 9 \implies \sigma_1 = 4, \sigma_2 = 3$.
### Question 2
2. 

$$
\mathbf{A}^T \mathbf{A} = \begin{bmatrix} 1 & 1 \\ 1 & 2 \end{bmatrix}
$$

. Characteristic equation (1-\lambda)(2-\lambda)-1 = 0 \implies \lambda^2 - 3\lambda + 1 = 0 \implies \lambda = \frac{3 \pm \sqrt{5}}{2}. \sigma_1 = \sqrt{\frac{3+\sqrt{5}}{2}} \approx 1.618, \sigma_2 = \sqrt{\frac{3-\sqrt{5}}{2}} \approx 0.618.
### Question 3
3. Exactly $r = 3$ non-zero singular values.
### Question 4
4. Eckart-Young theorem states that the best rank-$k$ approximation $\mathbf{A}_k$ minimizing $||\mathbf{A} - \mathbf{A}_k||_F$ is obtained by truncating SVD sum to top $k$ singular values: $\mathbf{A}_k = \sum_{i=1}^k \sigma_i \mathbf{u}_i \mathbf{v}_i^T$.
### Question 5
5. Truncated SVD retains only the top $k \ll r$ largest singular values and corresponding vectors, discarding smaller noise components.

## Level 3 — Conceptual Solutions
### Question 1
1. $\mathbf{A}\mathbf{A}^T = (\mathbf{U}\mathbf{\Sigma}\mathbf{V}^T)(\mathbf{V}\mathbf{\Sigma}^T \mathbf{U}^T) = \mathbf{U}\mathbf{\Sigma}\mathbf{I}\mathbf{\Sigma}^T \mathbf{U}^T = \mathbf{U}\mathbf{\Sigma}^2 \mathbf{U}^T$. Thus $\mathbf{U}$ contains eigenvectors of $\mathbf{A}\mathbf{A}^T$.
### Question 2
2. $\mathbf{A}^T\mathbf{A} = (\mathbf{V}\mathbf{\Sigma}^T \mathbf{U}^T)(\mathbf{U}\mathbf{\Sigma}\mathbf{V}^T) = \mathbf{V}\mathbf{\Sigma}^2 \mathbf{V}^T$. Thus $\mathbf{V}$ contains eigenvectors of $\mathbf{A}^T\mathbf{A}$.
### Question 3
3. For real symmetric $\mathbf{A} = \mathbf{A}^T$ with $\lambda_i \ge 0$, eigendecomposition is $\mathbf{A} = \mathbf{Q}\mathbf{\Lambda}\mathbf{Q}^T$. Comparing with $\mathbf{U}\mathbf{\Sigma}\mathbf{V}^T$, $\mathbf{U}=\mathbf{Q}, \mathbf{V}=\mathbf{Q}, \mathbf{\Sigma}=\mathbf{\Lambda}$.
### Question 4
4. Pseudoinverse $\mathbf{A}^+ = \mathbf{V} \mathbf{\Sigma}^+ \mathbf{U}^T$, where $\mathbf{\Sigma}^+$ inverts non-zero singular values ($1/\sigma_i$) and transposes shape.
### Question 5
5. Frobenius norm squared equals sum of squared singular values: $||\mathbf{A}||_F^2 = \text{Tr}(\mathbf{A}^T \mathbf{A}) = \sum_{i=1}^r \sigma_i^2$.

## Level 4 — AI/ML Application Solutions
### Question 1
1. Storing truncated $U_k (1000 \times 50)$, $\Sigma_k (50)$, $V_k^T (50 \times 1000)$ takes $1000(50) + 50 + 50(1000) = 100,050$ floats. Storage is reduced from 1,000,000 to 100,050 $\implies \approx 90\%$ reduction (10x compression!).
### Question 2
2. Left singular matrix $U_{10000 \times 20}$ represents 10,000 users in 20 latent movie preference dimensions. Right singular matrix $V_{5000 \times 20}$ represents 5,000 movies in 20 latent genre dimensions. User $i$ predicted rating for movie $j$ is dot product $\mathbf{u}_i^T \mathbf{v}_j$.
### Question 3
3. LSA computes SVD on Term-Document matrix $X_{words \times docs} = U \Sigma V^T$. Columns of $U_k$ form latent semantic topic vectors, mapping synonyms into shared topic spaces.

## Level 5 — Interview Questions Solutions
### Question 1
1. Spectral norm $||\mathbf{A}||_2 = \max_{\mathbf{x} \neq 0} \frac{||\mathbf{A}\mathbf{x}||_2}{||\mathbf{x}||_2} = \max_{\mathbf{x}} \frac{||\mathbf{U}\mathbf{\Sigma}\mathbf{V}^T\mathbf{x}||_2}{||\mathbf{x}||_2}$. Since $U, V$ are isometric orthogonal rotations, max is achieved along 1st singular vector yielding $||\mathbf{A}||_2 = \sigma_1$.
### Question 2
2. Randomized SVD projects $\mathbf{A}$ onto random Gaussian matrix $\mathbf{\Omega}_{n \times (k+p)}$, computes QR factorization $Y = A \Omega = Q R$, then computes exact SVD on small matrix $B = Q^T A$ ($O(mn \log k)$ speed).
### Question 3
3. Standard OLS assumes error only in target $y$. Total Least Squares assumes noise in both input features $X$ and targets $y$, finding best fit hyperplanes via smallest singular vector of augmented matrix $[X \mid y]$.
### Question 4
4. Computing $\mathbf{A}^T \mathbf{A}$ explicitly squares matrix condition number $\kappa(\mathbf{A}^T \mathbf{A}) = \kappa(\mathbf{A})^2$, causing severe floating-point precision loss. SVD computes singular values directly without matrix squaring.
### Question 5
5. For mean-centered dataset matrix $\mathbf{X}_{n \times p}$, covariance matrix $\mathbf{\Sigma} = \frac{1}{n-1}\mathbf{X}^T \mathbf{X}$. SVD of $\mathbf{X} = \mathbf{U}\mathbf{\Sigma}_{svd}\mathbf{V}^T \implies \mathbf{V}$ are PCA principal components, and $\lambda_{pca} = \frac{\sigma_i^2}{n-1}$.
