# Solutions — Vector Operations

## Level 1 — Basic Understanding Solutions
### Question 1
1. $[3+2, 7+(-4)]^T = [5, 3]^T$.
### Question 2
2. $[5(-1), 5(2), 5(0)]^T = [-5, 10, 0]^T$.
### Question 3
3. $[4-1, 5-2, 6-3]^T = [3, 3, 3]^T$.
### Question 4
4. $[2 \times 4, 3 \times (-1)]^T = [8, -3]^T$.
### Question 5
5. No. Vectors must have identical dimensions to perform component-wise addition.

## Level 2 — Calculation Solutions
### Question 1
1. $[2(1)-3(0), 2(3)-3(2), 2(-2)-3(1)]^T = [2, 0, -7]^T$.
### Question 2
2. $-1 \cdot \mathbf{u} = [-5, -12]^T$. Geometrically, it has equal magnitude but opposite direction (180 degree rotation).
### Question 3
3. $\mathbf{x} = [7-2, 1-3]^T = [5, -2]^T$.
### Question 4
4. $3[2,0]^T + 4[0,3]^T = [6,0]^T + [0,12]^T = [6, 12]^T$.
### Question 5
5. $[0.5 \times 2.0, 2.0 \times 0.5, 1.5 \times 3.0]^T = [1.0, 1.0, 4.5]^T$.

## Level 3 — Conceptual Solutions
### Question 1
1. Placing vector $\mathbf{v}$ head-to-tail at the tip of $\mathbf{u}$ forms two sides of a parallelogram. The diagonal from the origin is $\mathbf{u} + \mathbf{v}$.
### Question 2
2. Proof: $\mathbf{u} + \mathbf{v} = [u_1+v_1, \dots, u_n+v_n]^T = [v_1+u_1, \dots, v_n+u_n]^T = \mathbf{v} + \mathbf{u}$ (by commutativity of real addition).
### Question 3
3. The zero vector $\mathbf{0} = [0, \dots, 0]^T \in \mathbb{R}^n$, since $\mathbf{v} + \mathbf{0} = \mathbf{v}$.
### Question 4
4. Since $\mathbf{a} + (\mathbf{b} - \mathbf{a}) = \mathbf{b}$, adding displacement $(\mathbf{b} - \mathbf{a})$ to point $\mathbf{a}$ leads to point $\mathbf{b}$.
### Question 5
5. Hadamard product results in a vector of same dimension ($[a_i b_i]$). Dot product sums the element-wise products into a single scalar ($\sum a_i b_i$).

## Level 4 — AI/ML Application Solutions
### Question 1
1. $\mathbf{\theta}_1 = [0.5, -0.5]^T - 0.01 [10.0, -5.0]^T = [0.5 - 0.1, -0.5 + 0.05]^T = [0.4, -0.45]^T$.
### Question 2
2. $\mathbf{y} = [-0.2 + 1.2, 0.5 + 0.8]^T = [1.0, 1.3]^T$.
### Question 3
3. Dropout generates a random binary vector $\mathbf{d} \in \{0, 1\}^n$ with probability $p$ of $1$s. Neurons are deactivated via element-wise multiplication $\mathbf{h}_{dropped} = \mathbf{h} \odot \mathbf{d}$.

## Level 5 — Interview Questions Solutions
### Question 1
1. $c(\mathbf{u} + \mathbf{v}) = c[u_1+v_1, \dots]^T = [c u_1 + c v_1, \dots]^T = c\mathbf{u} + c\mathbf{v}$.
### Question 2
2. A linear combination $\alpha \mathbf{u} + (1-\alpha)\mathbf{v}$ where $0 \le \alpha \le 1$. It traces the line segment connecting $\mathbf{u}$ and $\mathbf{v}$.
### Question 3
3. Semantic relations are linear displacements in embedding space. 'king' - 'man' yields a 'royalty' direction vector, which added to 'woman' yields 'queen'.
### Question 4
4. When $\mathbf{w}_1$ and $\mathbf{w}_2$ are linearly dependent (collinear vectors, $\mathbf{w}_1 = k \mathbf{w}_2$).
### Question 5
5. NumPy uses C-compiled SIMD vector instructions operating directly on contiguous memory blocks, avoiding Python interpreter overhead.
