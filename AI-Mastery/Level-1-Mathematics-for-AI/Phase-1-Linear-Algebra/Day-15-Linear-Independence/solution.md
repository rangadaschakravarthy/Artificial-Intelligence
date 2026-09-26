# Solutions — Linear Independence

## Level 1 — Basic Understanding Solutions
### Question 1
1. Linearly dependent, because $\mathbf{v} = 2\mathbf{u}$ ($[2, 6] = 2[1, 3]$).
### Question 2
2. Yes! $c_1[1,0,0]^T + c_2[0,1,0]^T + c_3[0,0,1]^T = [0,0,0]^T \implies c_1=c_2=c_3=0$.
### Question 3
3. Maximum 4 linearly independent vectors.
### Question 4
4. Linearly DEPENDENT, because setting coefficient of $\mathbf{0}$ to $c=1 \neq 0$ satisfies $1 \cdot \mathbf{0} = \mathbf{0}$.
### Question 5
5. $c_1 \mathbf{v}_1 + c_2 \mathbf{v}_2 + \dots + c_k \mathbf{v}_k = \mathbf{0} \implies c_1 = c_2 = \dots = c_k = 0$.

## Level 2 — Calculation Solutions
### Question 1
1. 

$$\det \begin{bmatrix} 1 & -1 \\ 2 & 3 \end{bmatrix} = 1(3) - (-1)(2) = 3 + 2 = 5 \neq 0$$

. Independent!
### Question 2
2. Notice $\mathbf{w} = \mathbf{u} + \mathbf{v}$ ($[1,0,1]^T + [0,1,1]^T = [1,1,2]^T$). Since $\mathbf{w}$ is a sum of others, the set is LINEARLY DEPENDENT! (Determinant $= 0$).
### Question 3
3. Yes. Scaling non-zero vectors by non-zero constants does not alter linear independence.
### Question 4
4. Two 2D vectors are dependent if and only if one is a scalar multiple of the other (parallel). Non-parallel vectors cannot be multiples, so they are independent.
### Question 5
5. Setting $2\mathbf{u} - 1\mathbf{v} - 1\mathbf{w} = \mathbf{0}$ provides a non-trivial solution with coefficients $c_1=2, c_2=-1, c_3=-1$.

## Level 3 — Conceptual Solutions
### Question 1
1. Let $\mathbf{v}_1 = \mathbf{0}$. Choose $c_1 = 1 \neq 0$ and $c_2 = c_3 = \dots = 0$. Then $1 \cdot \mathbf{0} + 0\mathbf{v}_2 + \dots = \mathbf{0}$. A non-trivial solution exists, proving dependence.
### Question 2
2. Set $c_1(\mathbf{v}_1+\mathbf{v}_2) + c_2(\mathbf{v}_1-\mathbf{v}_2) = \mathbf{0} \implies (c_1+c_2)\mathbf{v}_1 + (c_1-c_2)\mathbf{v}_2 = \mathbf{0}$. Since $\mathbf{v}_1,\mathbf{v}_2$ independent: $c_1+c_2=0$ and $c_1-c_2=0 \implies c_1=0, c_2=0$. Independent!
### Question 3
3. Matrix $\mathbf{A}_{n \times k}$ with $k > n$ has more columns than rows. Systems $\mathbf{A}\mathbf{c} = \mathbf{0}$ has at least $k - n > 0$ free variables, guaranteeing non-trivial solutions.
### Question 4
4. Column vectors are linearly independent if and only if $\text{Rank}(\mathbf{A}) = k$ (number of columns).
### Question 5
5. Let $\mathbf{v}_i \cdot \mathbf{v}_j = 0$ for $i \neq j$. Take dot product of $\sum c_i \mathbf{v}_i = \mathbf{0}$ with $\mathbf{v}_k$: $c_k (\mathbf{v}_k \cdot \mathbf{v}_k) = 0 \implies c_k = 0$ (since $\mathbf{v}_k \neq \mathbf{0}$). Thus all $c_k = 0$.

## Level 4 — AI/ML Application Solutions
### Question 1
1. $x_1 + x_2 + x_3 = 1 \cdot x_0$. Feature vector $[x_0, x_1, x_2, x_3]^T$ has linear dependency $x_1 + x_2 + x_3 - x_0 = 0$. Solution: Drop one category column (e.g. keep $k-1$ dummy variables).
### Question 2
2. No. $x_2 = 1.8 x_1 + 32 x_0$. Fahrenheit feature is an exact affine linear combination of Celsius and constant 1 bias, making features linearly dependent.
### Question 3
3. Gram-Schmidt takes independent vectors $\mathbf{v}_1, \dots, \mathbf{v}_k$ and sequentially subtracts vector projections along previous directions: $\mathbf{u}_k = \mathbf{v}_k - \sum_{j=1}^{k-1} \text{proj}_{u_j}(\mathbf{v}_k)$, then normalizes $\hat{\mathbf{u}}_k = \mathbf{u}_k / ||\mathbf{u}_k||$.

## Level 5 — Interview Questions Solutions
### Question 1
1. $\mathbf{A}\mathbf{x} = x_1 \mathbf{a}_1 + x_2 \mathbf{a}_2 + \dots + x_n \mathbf{a}_n = \mathbf{0}$. By definition of linear independence, this holds if and only if $x_1 = x_2 = \dots = x_n = 0$ (trivial solution $\mathbf{x} = \mathbf{0}$).
### Question 2
2. $\text{Span}(\mathbf{v}_1, \dots, \mathbf{v}_k)$ is the set of ALL possible linear combinations $\sum c_i \mathbf{v}_i$. If vectors are independent, adding a vector expands span dimension by 1.
### Question 3
3. A Basis of vector space $V$ is a set of vectors that is BOTH linearly independent AND spans $V$.
### Question 4
4. Linearly dependent columns $\implies \det(\mathbf{A}) = 0 \implies \prod \lambda_i = 0 \implies$ At least one eigenvalue $\lambda = 0$.
### Question 5
5. VC dimension of linear hyperplanes in $\mathbb{R}^n$ is $n+1$. Up to $n+1$ points in general position can be shattered by linear classifiers if their augmented feature vectors are linearly independent.
