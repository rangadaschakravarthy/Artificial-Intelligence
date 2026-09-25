# Worked Examples — Continuous Random Variables

## Example 1: PDF Normalization Verification
**Problem**: Find constant $c$ such that $f(x) = c x$ for $x \in [0, 2]$ (and $0$ elsewhere) is a valid PDF.
**Solution**:
1. Integral condition: $\int_0^2 c x dx = 1$.
2. $\left[ c rac{x^2}{2} ight]_0^2 = c \left( rac{4}{2} - 0 ight) = 2c = 1 \implies c = 0.5$.
3. Valid PDF is $f(x) = 0.5 x$ on $[0, 2]$.

## Example 2: CDF Derivation
**Problem**: Derive CDF $F(x)$ for the PDF $f(x) = 0.5 x$ on $[0, 2]$.
**Solution**:
1. For $x < 0$, $F(x) = 0$.
2. For $0 \le x \le 2$:
   $$F(x) = \int_0^x 0.5 t dt = \left[ 0.25 t^2 ight]_0^x = 0.25 x^2$$
3. For $x > 2$, $F(x) = 1.0$.

## Example 3: Interval Probability Calculation
**Problem**: Using $F(x) = 0.25 x^2$ on $[0, 2]$, calculate $P(1 \le X \le 1.5)$.
**Solution**:
1. $P(1 \le X \le 1.5) = F(1.5) - F(1)$.
2. $F(1.5) = 0.25 (1.5)^2 = 0.25 (2.25) = 0.5625$.
3. $F(1) = 0.25 (1)^2 = 0.25$.
4. $P = 0.5625 - 0.25 = 0.3125$.

## Example 4: Exponential PDF Latency Model
**Problem**: Response time $X$ has PDF $f(x) = 0.1 e^{-0.1 x}$ for $x \ge 0$. Find probability latency is less than 10 ms.
**Solution**:
1. $P(X < 10) = \int_0^{10} 0.1 e^{-0.1 x} dx = \left[ -e^{-0.1 x} ight]_0^{10} = -e^{-1} - (-e^0) = 1 - e^{-1} pprox 1 - 0.3679 = 0.6321$.

## Example 5: Gaussian Distribution Probability (SciPy)
**Problem**: Model parameter $W \sim \mathcal{N}(0, 1)$. Compute $P(W > 1.96)$.
**Solution**:
1. Using symmetry: $P(W > 1.96) = 1 - \Phi(1.96)$.
2. Standard Normal CDF value $\Phi(1.96) pprox 0.9750$.
3. $P(W > 1.96) = 1 - 0.9750 = 0.0250 = 2.5\%$.
