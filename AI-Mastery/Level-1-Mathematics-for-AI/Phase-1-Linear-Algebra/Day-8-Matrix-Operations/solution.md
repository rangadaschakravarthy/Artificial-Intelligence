# Solutions — Matrix Operations

## Level 1 — Basic Understanding Solutions
### Question 1
1. 

$$\begin{bmatrix} 2+5 & 4+1 \\ 1+0 & 3+2 \end{bmatrix} = \begin{bmatrix} 7 & 5 \\ 1 & 5 \end{bmatrix}$$

.
### Question 2
2. 

$$\begin{bmatrix} 4(1) & 4(-2) \\ 4(3) & 4(0) \end{bmatrix} = \begin{bmatrix} 4 & -8 \\ 12 & 0 \end{bmatrix}$$

.
### Question 3
3. 

$$\begin{bmatrix} 3(2) & 2(0) \\ 1(-1) & 4(5) \end{bmatrix} = \begin{bmatrix} 6 & 0 \\ -1 & 20 \end{bmatrix}$$

.
### Question 4
4. No. Matrix addition requires identical shapes ($m \times n$). $3 \times 2 \neq 2 \times 3$.
### Question 5
5. The zero matrix $\mathbf{0}_{m \times n}$.

## Level 2 — Calculation Solutions
### Question 1
1. 

$$2\begin{bmatrix}1&2\\0&4\end{bmatrix} - 3\begin{bmatrix}3&-1\\2&1\end{bmatrix} = \begin{bmatrix}2&4\\0&8\end{bmatrix} - \begin{bmatrix}9&-3\\6&3\end{bmatrix} = \begin{bmatrix}-7&7\\-6&5\end{bmatrix}$$

.
### Question 2
2. 

$$\mathbf{X} = \begin{bmatrix} 4-1 & 5-3 \\ 1-2 & 2-0 \end{bmatrix} = \begin{bmatrix} 3 & 2 \\ -1 & 2 \end{bmatrix}$$

.
### Question 3
3. 

$$\text{ReLU}(\mathbf{Z}) = \begin{bmatrix} \max(0, 2.5) & \max(0, -1.2) \\ \max(0, -0.5) & \max(0, 3.0) \end{bmatrix} = \begin{bmatrix} 2.5 & 0.0 \\ 0.0 & 3.0 \end{bmatrix}$$

.
### Question 4
4. The resulting broadcasted shape is $4 \times 3$.
### Question 5
5. $(\mathbf{A} + \mathbf{B})_{i,j} = a_{i,j} + b_{i,j} = b_{i,j} + a_{i,j} = (\mathbf{B} + \mathbf{A})_{i,j}$ (by commutativity of real numbers).

## Level 3 — Conceptual Solutions
### Question 1
1. Closure: $\mathbf{A}+\mathbf{B} \in \mathbb{R}^{m \times n}$. Assoc: $(\mathbf{A}+\mathbf{B})+\mathbf{C} = \mathbf{A}+(\mathbf{B}+\mathbf{C})$. Comm: $\mathbf{A}+\mathbf{B}=\mathbf{B}+\mathbf{A}$. Identity: $\mathbf{A}+\mathbf{0}=\mathbf{A}$. Inverse: $\mathbf{A}+(-\mathbf{A})=\mathbf{0}$.
### Question 2
2. $c(\mathbf{A}+\mathbf{B})_{i,j} = c(a_{i,j} + b_{i,j}) = c a_{i,j} + c b_{i,j} = (c\mathbf{A} + c\mathbf{B})_{i,j}$.
### Question 3
3. The zero matrix $\mathbf{0}$ of shape $m \times n$ filled entirely with zeros.
### Question 4
4. Compare shapes from right to left: Axis 1 ($4=4$ match), Axis 0 ($3$ vs $1$: dimension 1 is stretched to 3). Result shape: $(3, 4)$.
### Question 5
5. Element-wise operations are embarrassingly parallel across millions of GPU CUDA threads executing identical instructions simultaneously.

## Level 4 — AI/ML Application Solutions
### Question 1
1. 

$$\mathbf{W}_{new} = \begin{bmatrix} 0.5 & 1.0 \\ -0.2 & 0.8 \end{bmatrix} - 0.1 \begin{bmatrix} 2.0 & -1.0 \\ 0.5 & 4.0 \end{bmatrix} = \begin{bmatrix} 0.5-0.2 & 1.0+0.1 \\ -0.2-0.05 & 0.8-0.4 \end{bmatrix} = \begin{bmatrix} 0.3 & 1.1 \\ -0.25 & 0.4 \end{bmatrix}$$

.
### Question 2
2. Broadcast \mathbf{b} to each row: 

$$\begin{bmatrix} 1.0+0.5 & 2.0-0.5 \\ 3.0+0.5 & 4.0-0.5 \\ 5.0+0.5 & 6.0-0.5 \end{bmatrix} = \begin{bmatrix} 1.5 & 1.5 \\ 3.5 & 3.5 \\ 5.5 & 5.5 \end{bmatrix}$$

.
### Question 3
3. Random binary mask matrix $\mathbf{M} \sim \text{Bernoulli}(p)$ has same shape as activation matrix $\mathbf{H}$. Output $\mathbf{H}_{drop} = \mathbf{H} \odot \mathbf{M}$ zeroes out random features.

## Level 5 — Interview Questions Solutions
### Question 1
1. Verification of 8 vector space axioms: Closed under addition, associative, commutative, zero element exists, additive inverse exists, scalar multiplication distributive over matrix and scalar addition, scalar multiplication associative.
### Question 2
2. Two dimensions are compatible for broadcasting if they are equal, or if one of them is 1.
### Question 3
3. Layer norm computes mean $\mu$ and variance $\sigma^2$ across feature dimensions, then applies element-wise subtraction and division: $\hat{\mathbf{X}} = (\mathbf{X} - \mu) \oslash \sqrt{\sigma^2 + \epsilon}$.
### Question 4
4. Explicit expansion allocates new RAM copying array data. Strided broadcasting sets array byte stride to 0 for length-1 dimensions, performing zero-copy virtual expansion.
### Question 5
5. Schur Product Theorem proves that the entrywise product of two positive semi-definite matrices $\mathbf{A} \odot \mathbf{B}$ remains positive semi-definite.
