# Solutions — Cosine Similarity

## Level 1 — Basic Understanding Solutions
### Question 1
1. $[-1, 1]$ (or $[0, 1]$ when vector components are strictly non-negative).
### Question 2
2. $\mathbf{u}\cdot\mathbf{v} = 15, ||\mathbf{u}||=3, ||\mathbf{v}||=5 \implies \text{sim} = 15 / (3 \times 5) = 1.0$.
### Question 3
3. $\mathbf{a}\cdot\mathbf{b} = 0 \implies \text{sim} = 0.0$.
### Question 4
4. $d_{cos} = 1 - 0.8 = 0.2$.
### Question 5
5. Word frequency vectors contain only non-negative numbers ($v_i \ge 0$). Dot product is $\ge 0$, so cosine of angle cannot be negative (angle between $0^\circ$ and $90^\circ$).

## Level 2 — Calculation Solutions
### Question 1
1. $\mathbf{y} = 2\mathbf{x}$. Since vectors are parallel, $\text{sim}(\mathbf{x}, \mathbf{y}) = 1.0$.
### Question 2
2. $\mathbf{u}\cdot\mathbf{v} = 1$, $||\mathbf{u}||=\sqrt{2}$, $||\mathbf{v}||=1 \implies \text{sim} = 1 / \sqrt{2} \approx 0.7071$.
### Question 3
3. $\text{sim}(c\mathbf{u}, \mathbf{v}) = \frac{c\mathbf{u}\cdot\mathbf{v}}{||c\mathbf{u}|| ||\mathbf{v}||} = \frac{c (\mathbf{u}\cdot\mathbf{v})}{c ||\mathbf{u}|| ||\mathbf{v}||} = \text{sim}(\mathbf{u}, \mathbf{v})$.
### Question 4
4. $\theta = 180^\circ$ (pi radians), pointing in exactly opposite directions.
### Question 5
5. $\text{sim}(\hat{\mathbf{u}}, \hat{\mathbf{v}}) = \hat{\mathbf{u}} \cdot \hat{\mathbf{v}}$.

## Level 3 — Conceptual Solutions
### Question 1
1. $\frac{\mathbf{u} \cdot \mathbf{v}}{||\mathbf{u}|| ||\mathbf{v}||} = (\frac{\mathbf{u}}{||\mathbf{u}||}) \cdot (\frac{\mathbf{v}}{||\mathbf{v}||}) = \hat{\mathbf{u}} \cdot \hat{\mathbf{v}}$.
### Question 2
2. Doubling word counts doubles vector magnitude $||2\mathbf{v}|| = 2||\mathbf{v}||$, increasing Euclidean distance. Cosine similarity divides out magnitude, remaining scale-invariant.
### Question 3
3. When all vectors are normalized to unit L2 length ($||v||_2 = 1$).
### Question 4
4. Standard Cosine Distance $1 - \text{sim}(u, v)$ does NOT satisfy the triangle inequality. Angular Cosine Distance $\frac{\arccos(\text{sim})}{\pi}$ is a valid metric.
### Question 5
5. Zero-centering converts Cosine Similarity into Pearson Correlation Coefficient.

## Level 4 — AI/ML Application Solutions
### Question 1
1. $\mathbf{q}\cdot\mathbf{d} = 0.6(0.8) + 0.8(0.6) = 0.96$. $||\mathbf{q}||=1, ||\mathbf{d}||=1 \implies \text{sim} = 0.96$. $d_{cos} = 1 - 0.96 = 0.04$.
### Question 2
2. $\mathbf{u}\cdot\mathbf{m} = 4(5) + 5(4) + 1(0) = 40$. $||\mathbf{u}|| = \sqrt{16+25+1} = \sqrt{42} \approx 6.48$. $||\mathbf{m}|| = \sqrt{25+16} = \sqrt{41} \approx 6.40$. Score $= 40 / (6.48 \times 6.40) = 40 / 41.47 \approx 0.9645$.
### Question 3
3. If database vectors are pre-normalized during indexing, computing cosine similarity reduces to a single matrix-vector dot product operation $X q$, enabling massive SIMD acceleration.

## Level 5 — Interview Questions Solutions
### Question 1
1. $|\hat{\mathbf{u}} - \hat{\mathbf{v}}||^2 = ||\hat{\mathbf{u}}||^2 + ||\hat{\mathbf{v}}||^2 - 2(\hat{\mathbf{u}} \cdot \hat{\mathbf{v}}) = 1 + 1 - 2 \text{sim}(\mathbf{u}, \mathbf{v}) = 2 (1 - \text{sim}(\mathbf{u}, \mathbf{v}))$.
### Question 2
2. Pre-normalizing embedding vectors allows client software to use ultra-fast dot product instructions directly without computing expensive square roots at query time.
### Question 3
3. Cosine similarity measures angle from origin. Pearson correlation centers vectors by subtracting means first, measuring linear correlation of feature variations.
### Question 4
4. In high dimensions, random independent vectors become nearly orthogonal ($cos(\theta) \approx 0$), concentrating similarity scores tightly around 0.
### Question 5
5. Temperature $T$ scales similarity logits $S / T$. Lower $T$ sharpens softmax distribution output, making model predictions more confident.
