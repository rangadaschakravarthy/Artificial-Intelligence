# Solutions — Norms and Distances

## Level 1 — Basic Understanding Solutions
### Question 1
1. $|3| + |-2| + |5| = 3 + 2 + 5 = 10$.
### Question 2
2. $\sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10$.
### Question 3
3. $\max(|-10|, |4|, |7|) = 10$.
### Question 4
4. $d = \sqrt{(4-1)^2 + (5-1)^2} = \sqrt{3^2 + 4^2} = \sqrt{25} = 5$.
### Question 5
5. A unit vector is a vector with length (L2 norm) equal to 1.0.

## Level 2 — Calculation Solutions
### Question 1
1. $||\mathbf{v}||_2 = \sqrt{5^2 + 12^2} = \sqrt{169} = 13$. Unit vector $\hat{\mathbf{v}} = [5/13, 12/13]^T \approx [0.385, 0.923]^T$.
### Question 2
2. $d_1 = |5-2| + |1 - (-3)| + |-2 - 4| = 3 + 4 + 6 = 13$.
### Question 3
3. $c\mathbf{v} = [-9, -12]^T$. $||c\mathbf{v}||_2 = \sqrt{81+144} = \sqrt{225} = 15$. $|c|||\mathbf{v}||_2 = |-3| \times 5 = 15$. Equal!
### Question 4
4. $\mathbf{u} + \mathbf{v} = [5, 4]^T$. $||\mathbf{u}+\mathbf{v}||_2 = \sqrt{25+16} = \sqrt{41} \approx 6.403$. $||\mathbf{u}||_2 = \sqrt{5} \approx 2.236, ||\mathbf{v}||_2 = \sqrt{20} \approx 4.472$. Sum $= 6.708$. Indeed $6.403 \le 6.708$.
### Question 5
5. $||\mathbf{v}||_2^2 = \mathbf{v} \cdot \mathbf{v} = 2(2) + (-1)(-1) + 3(3) = 4 + 1 + 9 = 14$.

## Level 3 — Conceptual Solutions
### Question 1
1. $|u + v| \le |u| + |v|$. For real scalars, if $u,v$ have same sign $|u+v| = |u|+|v|$; if opposite signs $|u+v| < |u|+|v|$.
### Question 2
2. Since $(\sum |v_i|)^2 = \sum v_i^2 + 2 \sum_{i \neq j} |v_i v_j| \ge \sum v_i^2$, taking square root yields $||\mathbf{v}||_1 \ge ||\mathbf{v}||_2$.
### Question 3
3. L1 unit circle is a diamond ($|x|+|y|=1$). L2 unit circle is a smooth circle ($x^2+y^2=1$). $L_\infty$ unit circle is a square ($\max(|x|,|y|)=1$).
### Question 4
4. $||0 \mathbf{v}|| = |0| ||\mathbf{v}|| = 0$. The norm becomes 0.
### Question 5
5. Larger scale features dominate squared differences in Euclidean distance. E.g., income in $ vs age in years.

## Level 4 — AI/ML Application Solutions
### Question 1
1. $||\mathbf{w}||_2^2 = 0.6^2 + (-0.8)^2 = 0.36 + 0.64 = 1.0$. Penalty $= \lambda ||\mathbf{w}||_2^2 = 0.5(1.0) = 0.5$.
### Question 2
2. $||\mathbf{w}||_1 = |0.6| + |-0.8| = 1.4$. Penalty $= \lambda ||\mathbf{w}||_1 = 0.5(1.4) = 0.7$.
### Question 3
3. $\hat{\mathbf{a}} = [3/3, 0/3]^T = [1, 0]^T$. $||\mathbf{b}||_2 = \sqrt{4+4} = \sqrt{8} = 2\sqrt{2}$. $\hat{\mathbf{b}} = [2/2\sqrt{2}, 2/2\sqrt{2}]^T = [1/\sqrt{2}, 1/\sqrt{2}]^T \approx [0.707, 0.707]^T$.

## Level 5 — Interview Questions Solutions
### Question 1
1. L1 loss contour is diamond-shaped with vertices on coordinate axes. Level sets of MSE loss touch these sharp diamond corners first, setting non-axis weights directly to zero.
### Question 2
2. $d(\mathbf{u},\mathbf{v}) = ||\mathbf{u}-\mathbf{v}||_2 = \sqrt{\sum (u_i-v_i)^2} = \sqrt{\sum (-(v_i-u_i))^2} = \sqrt{\sum (v_i-u_i)^2} = d(\mathbf{v},\mathbf{u})$.
### Question 3
3. Minkowski distance: $D(\mathbf{x}, \mathbf{y}) = (\sum_{i=1}^n |x_i - y_i|^p)^{1/p}$. For $p=1$ it is Manhattan, $p=2$ Euclidean, $p \rightarrow \infty$ Chebyshev (Infinity norm).
### Question 4
4. As dimension $n \rightarrow \infty$, ratio of distance to nearest vs farthest point approaches 1, reducing contrast between distances in high dimensions.
### Question 5
5. Batch norm subtracts feature mean $\mu$ and divides by standard deviation $\sigma = \sqrt{\frac{1}{m} ||\mathbf{x} - \mu||_2^2 + \epsilon}$, normalizing vectors to zero mean and unit L2 variance.
