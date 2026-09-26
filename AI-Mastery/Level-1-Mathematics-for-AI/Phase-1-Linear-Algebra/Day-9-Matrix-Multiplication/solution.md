# Solutions — Matrix Multiplication

## Level 1 — Basic Understanding Solutions
### Question 1
1. Yes, inner dimensions match ($4 = 4$). Output shape is $3 \times 2$.
### Question 2
2. No. Inner dimensions $(2 \neq 3)$ do not match.
### Question 3
3. 

$$\begin{bmatrix} 1(2)+2(1) & 1(0)+2(3) \\ 3(2)+4(1) & 3(0)+4(3) \end{bmatrix} = \begin{bmatrix} 4 & 6 \\ 10 & 12 \end{bmatrix}$$

.
### Question 4
4. 

$$\begin{bmatrix} 3(2)+1(4) \\ 2(2)+5(4) \end{bmatrix} = \begin{bmatrix} 10 \\ 24 \end{bmatrix}$$

.
### Question 5
5. $\mathbf{A}\mathbf{I} = \mathbf{A}$ (Identity element).

## Level 2 — Calculation Solutions
### Question 1
1. 

$$\mathbf{A}\mathbf{B} = \begin{bmatrix} 1(3)+0(2)+2(1) & 1(1)+0(1)+2(0) \\ -1(3)+3(2)+1(1) & -1(1)+3(1)+1(0) \end{bmatrix} = \begin{bmatrix} 5 & 1 \\ 4 & 2 \end{bmatrix}_{2 \times 2}$$

.
### Question 2
2. $\mathbf{B}\mathbf{A}$ yields shape $3 \times 3$. Clearly $\mathbf{A}\mathbf{B} \neq \mathbf{B}\mathbf{A}$ (they don't even have the same shape!).
### Question 3
3. Weight matrix $\mathbf{W}$ must have shape $50 \times 10$ so that $(100 \times 50) \cdot (50 \times 10) = (100 \times 10)$.
### Question 4
4. 

$$\mathbf{A}^2 = \begin{bmatrix} 2 & 1 \\ 0 & 3 \end{bmatrix} \begin{bmatrix} 2 & 1 \\ 0 & 3 \end{bmatrix} = \begin{bmatrix} 4 & 5 \\ 0 & 9 \end{bmatrix}$$

.
### Question 5
5. Proof via element summation: $((\mathbf{A}+\mathbf{B})\mathbf{C})_{i,j} = \sum (a_{i,k}+b_{i,k})c_{k,j} = \sum a_{i,k}c_{k,j} + \sum b_{i,k}c_{k,j} = (\mathbf{A}\mathbf{C} + \mathbf{B}\mathbf{C})_{i,j}$.

## Level 3 — Conceptual Solutions
### Question 1
1. Associative law states $(\mathbf{A}\mathbf{B})\mathbf{C} = \mathbf{A}(\mathbf{B}\mathbf{C})$. Parenthesization order can change, but left-to-right sequence of matrices MUST be preserved.
### Question 2
2. Column $j$ of $\mathbf{C} = \mathbf{A}\mathbf{B}$ is $\mathbf{c}_j = b_{1,j}\mathbf{a}_1 + b_{2,j}\mathbf{a}_2 + \dots + b_{k,j}\mathbf{a}_k$, a linear combination of columns of $\mathbf{A}$.
### Question 3
3. Row $i$ of $\mathbf{C}$ is a linear combination of rows of $\mathbf{B}$ weighted by row $i$ of $\mathbf{A}$.
### Question 4
4. Complexity is $O(m \cdot k \cdot n)$ scalar multiplications.
### Question 5
5. Yes! 

$$\mathbf{A} = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}, \mathbf{B} = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} \implies \mathbf{A}\mathbf{B} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$$

.

## Level 4 — AI/ML Application Solutions
### Question 1
1. 

$$\mathbf{X}\mathbf{W} = \begin{bmatrix} 1(1)+0(2)+2(0) & 1(-1)+0(0)+2(1) \\ 0(1)+3(2)+1(0) & 0(-1)+3(0)+1(1) \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 6 & 1 \end{bmatrix}$$

. Adding bias [1, 2]: 

$$\mathbf{Z} = \begin{bmatrix} 2 & 3 \\ 7 & 3 \end{bmatrix}$$

.
### Question 2
2. Transpose $K^T$ has shape $B \times D \times S$. Matrix product $Q K^T$ yields shape $B \times S \times S$ (Sequence Length $\times$ Sequence Length self-attention grid).
### Question 3
3. Storing weights as `(out_features, in_features)` allows computing $x W^T$ directly, keeping memory continuous along output feature channels.

## Level 5 — Interview Questions Solutions
### Question 1
1. Strassen's algorithm uses 7 matrix multiplications instead of 8 for $2 \times 2$ blocks, reducing complexity from $O(n^3) \approx O(n^{3.0})$ to $O(n^{\log_2 7}) \approx O(n^{2.807})$.
### Question 2
2. Tensor Cores execute $4 \times 4$ matrix multiply-accumulate $D = A \cdot B + C$ in a single clock cycle using FP16 inputs and FP32 accumulation.
### Question 3
3. $\text{Tr}(\mathbf{A}\mathbf{B}) = \sum_i (\mathbf{A}\mathbf{B})_{i,i} = \sum_i \sum_j a_{i,j} b_{j,i} = \sum_j \sum_i b_{j,i} a_{i,j} = \sum_j (\mathbf{B}\mathbf{A})_{j,j} = \text{Tr}(\mathbf{B}\mathbf{A})$.
### Question 4
4. A square matrix $\mathbf{N}$ is nilpotent if $\mathbf{N}^k = \mathbf{0}$ for some positive integer $k$.
### Question 5
5. Dynamic programming finds optimal parenthesization for matrix chain multiplication, minimizing total scalar operations (e.g. $(A_{10 \times 100} B_{100 \times 5}) C_{5 \times 50}$ vs $A (B C)$).
