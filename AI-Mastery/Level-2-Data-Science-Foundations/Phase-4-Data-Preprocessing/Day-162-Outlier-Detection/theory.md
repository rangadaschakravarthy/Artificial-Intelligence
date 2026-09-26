# Day 162 Theory: Outlier Detection

### 1. What Is It?
An Outlier is an observation point that deviates significantly from the remaining data points, potentially distorting statistical estimates and ML model parameters.

### 2. Detection Methods
- **IQR Method**:
  

$$
ext{Lower Bound} = Q_1 - 1.5 	imes 	ext{IQR}
$$

  

$$
ext{Upper Bound} = Q_3 + 1.5 	imes 	ext{IQR}
$$

- **Z-Score Method**:
  $$	ext{Outlier if } |Z| = \left|rac{x - \mu}{\sigma}
ight| > 3.0$$

### 3. Summary
IQR is non-parametric (robust to non-Gaussian data), while Z-Score assumes an underlying normal distribution.
