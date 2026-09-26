# Theory — Tensors

### 1. Simple Definition
A tensor is a multi-dimensional grid of numbers. It generalizes scalars (0D), vectors (1D), and matrices (2D) to 3, 4, or arbitrary dimensions.

### 2. Intuition
Think of nested boxes. A number is 0D. A row of numbers is 1D. A sheet of numbers is 2D. A stack of sheets (like a book) is a 3D tensor. A library shelf of books is a 4D tensor (Batch of image channels!).

### 3. Mathematical Definition
A tensor $\mathbf{X} \in \mathbb{R}^{n_1 \times n_2 \times \dots \times n_d}$ of rank (order) $d$ is a multi-dimensional array indexed by $d$ indices $(i_1, i_2, \dots, i_d)$ where each component $x_{i_1, i_2, \dots, i_d} \in \mathbb{R}$.

### 4. Notation
Euler script or bold letters $\mathcal{X} \in \mathbb{R}^{d_1 \times d_2 \times \dots \times d_n}$. Axis $0, 1, \dots, d-1$.

### 5. Formula

$$
\mathcal{X}_{B \times C \times H \times W} \implies \text{4D Tensor: (Batch, Channels, Height, Width)}
$$

### 6. Symbol-by-Symbol Explanation
- $B$: Batch size (number of data samples)
- $C$: Channels (e.g. 3 for RGB image, 1 for Grayscale)
- $H$: Image Height in pixels
- $W$: Image Width in pixels

### 7. Step-by-Step Calculation
Given an RGB image batch of 32 images, each 64x64 pixels:
- Rank (Order) $d = 4$
- Tensor Shape $= (32, 3, 64, 64)$
- Total numbers stored $= 32 \times 3 \times 64 \times 64 = 393,216$ floats.

### 8. Second Example
Video Tensor (5D): Batch of 16 video clips, 30 frames long, RGB 128x128 resolution $\implies$ Shape $(16, 30, 3, 128, 128)$. Total elements $= 16 \times 30 \times 3 \times 128 \times 128 = 23,592,960$.

### 9. Common Mistakes
Confusing tensor rank (number of array axes) with matrix rank (number of linearly independent rows/cols); mixing up PyTorch `(B, C, H, W)` vs TensorFlow `(B, H, W, C)` axis ordering.

### 10. AI Connection
Convolutional Networks process 4D image tensors. Transformers process 3D token batch tensors `(Batch, Seq_Len, Embed_Dim)`. LLM Key-Query attention computes 4D tensors `(Batch, Heads, Seq_Len, Head_Dim)`.

### 11. Algorithm Connection
PyTorch, TensorFlow, Convolutional Neural Networks (CNNs), Vision Transformers (ViT), Large Language Models (LLMs).

### 12. Practical Interpretation
Reshaping a tensor changes how elements are indexed across axes without altering underlying memory bytes or total element count.

### 13. Interview Insight
Q: 'What is the difference between Matrix Rank and Tensor Rank?' A: Matrix rank is the number of linearly independent rows/cols. Tensor rank in computer science usually refers to the number of axes/dimensions (order) of the array.

### 14. Summary
Tensors are $d$-dimensional arrays ($0D$ scalar, $1D$ vector, $2D$ matrix, $3D+$ high-D). Key DL shapes: NLP `(B, S, D)`, Vision `(B, C, H, W)`.
