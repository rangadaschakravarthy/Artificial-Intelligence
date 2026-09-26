# Day 183 Theory: Deep Learning

### 1. What Is It?
Deep Learning (DL) is a subset of Machine Learning based on deep Artificial Neural Networks (ANNs) with multiple hidden layers, capable of learning hierarchical feature representations automatically from raw unstructured data.

### 2. Why Does It Exist?
Classical Machine Learning algorithms require human domain experts to manually engineer numerical features (e.g. SIFT features for images or TF-IDF for text). Deep Learning eliminates manual feature engineering by learning optimal hierarchical representations directly from raw inputs.

### 3. Representation Learning Hierarchy
- **Layer 1 (Raw Pixels)**: Low-level edge and color gradient detectors.
- **Layer 2 (Middle Layers)**: Textures, corners, and simple geometric shapes.
- **Layer 3 (Deeper Layers)**: Object components (eyes, wheels, door handles).
- **Output Layer**: High-level semantic concept classification ("Cat", "Car").

### 4. Mathematical Neural Network Notation
A single artificial neuron computes a weighted sum followed by a non-linear activation function $\sigma$:
$$y = \sigma\left( \mathbf{w}^T \mathbf{x} + b \right) = \sigma\left( \sum_{i=1}^d w_i x_i + b \right)$$

### 5. Summary
Deep Learning learns hierarchical feature representations automatically from raw data using multi-layer neural networks.
