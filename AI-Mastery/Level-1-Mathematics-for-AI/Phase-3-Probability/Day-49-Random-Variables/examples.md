# Worked Examples — Random Variables

## Example 1: Defining Discrete RV (Coin Tossing)
**Problem**: Flip a coin 3 times. Let $X$ be the number of Heads. List all values of $X(\omega)$ for each $\omega \in \Omega$.
**Solution**:
- $\Omega = \{TTT, TTH, THT, HTT, THH, HHT, HTH, HHH\}$.
- $X(TTT) = 0$.
- $X(TTH) = X(THT) = X(HTT) = 1$.
- $X(THH) = X(HHT) = X(HTH) = 2$.
- $X(HHH) = 3$.
- Range of $X$ is $\{0, 1, 2, 3\}$.

## Example 2: Continuous RV (Server Latency)
**Problem**: An API response time $T$ is measured in milliseconds. State whether $T$ is discrete or continuous, and specify its range.
**Solution**:
- $T$ can take any positive real number value (e.g. 12.345 ms).
- $T$ is a continuous random variable.
- Range / Support: $S_T = [0, \infty) \subset \mathbb{R}$.

## Example 3: Indicator Random Variable (Machine Learning)
**Problem**: Define an indicator random variable $I_A$ for event $A$: "Email contains word 'free'". Write $I_A(\omega)$.
**Solution**:
$$I_A(\omega) = egin{cases} 1 & 	ext{if } \omega \in A 	ext{ (word 'free' present)} \ 0 & 	ext{if } \omega 
otin A 	ext{ (word 'free' absent)} \end{cases}$$

## Example 4: Linear Transformation of RV
**Problem**: Let temperature $C$ in Celsius be a random variable with mean $20^\circ	ext{C}$. Let $F = 1.8 C + 32$ be Fahrenheit. If $C = 25$, what is $F$?
**Solution**:
- $F(25) = 1.8(25) + 32 = 45 + 32 = 77^\circ	ext{F}$.

## Example 5: Multidimensional RV (Computer Vision)
**Problem**: An RGB image pixel is represented as a random vector $\mathbf{X} = [R, G, B]^T$. If values are 8-bit integers, specify support of $\mathbf{X}$.
**Solution**:
- Each channel $R, G, B \in \{0, 1, \dots, 255\}$.
- Support $S_{\mathbf{X}} = \{0, 1, \dots, 255\}^3$, discrete vector random variable with $256^3 = 16,777,216$ possible states.
