# Day 184 Theory: Generative AI

### 1. What Is It?
Generative AI (GenAI) is a branch of Artificial Intelligence and Deep Learning that focuses on generating new, original synthetic content—such as text, images, audio, video, synthetic data, or code—that mimics the structural distribution of training data.

### 2. Discriminative vs Generative Paradigm
- **Discriminative Model**: Learns the decision boundary between classes to estimate conditional probability $P(Y \mid X)$. Used for classification and regression.
- **Generative Model**: Learns the underlying joint probability distribution $P(X, Y)$ or data distribution $P(X)$ to generate novel plausible samples $x_{\text{new}} \sim P(X)$.

### 3. Key Generative Model Families
1. **Generative Adversarial Networks (GANs)**: Generator vs Discriminator zero-sum game for photorealistic images.
2. **Diffusion Models**: Iteratively removes Gaussian noise from latent states to synthesize high-resolution images/video (e.g. Stable Diffusion).
3. **Transformer LLMs**: Autoregressive next-token prediction modeling $P(w_t \mid w_1, \dots, w_{t-1})$.

### 4. Summary
Generative AI uses deep learning probability distributions $P(X)$ to generate new synthetic text, images, audio, and multimodal content.
