# Day 156 Theory: Encoding

### 1. What Is It?
Encoding is the mathematical transformation of non-numeric categorical labels into real-valued numeric vectors or scalar codes suitable for Machine Learning models.

### 2. Theoretical Encoding Spectrum
- **Ordinal Encoding**: Maps ordered categories to sequential integers ($0, 1, 2, \dots, K-1$).
- **One-Hot Encoding**: Maps $K$ categories to $K$ mutually orthogonal binary unit vectors ($\mathbf{e}_1, \mathbf{e}_2, \dots, \mathbf{e}_K$).
- **Frequency Encoding**: Maps each category to its relative occurrence frequency in the dataset ($rac{	ext{Count}(C)}{N}$).
- **Target Encoding**: Maps each category to the mean target value for that subgroup ($\mathbb{E}[y \mid X = C]$).

### 3. Summary
Selecting the correct encoding strategy preserves category relationships while avoiding dimensional inflation.
