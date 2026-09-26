# Formula and Reference Sheet — Level 2 Data Science Foundations

This sheet provides quick reference mathematical formulas, code syntaxes, and usage guidelines across NumPy, Pandas, Visualization, and Preprocessing.

---

## 1. NumPy Quick Reference
- **Array Creation**: `np.array(list)`, `np.zeros(shape)`, `np.ones(shape)`, `np.arange(start, stop, step)`, `np.linspace(start, stop, num)`
- **Matrix Multiplication**: `A @ B` or `np.dot(A, B)`
- **Reshaping**: `arr.reshape(rows, cols)`, `arr.flatten()`, `arr.T`
- **Statistics**: `np.mean(arr)`, `np.median(arr)`, `np.std(arr)`, `np.var(arr)`

---

## 2. Pandas Quick Reference
- **Data Selection**: `df.loc[row_label, col_label]`, `df.iloc[row_idx, col_idx]`
- **Filtering**: `df[df['Col'] > threshold]`, `df.query("Age > 30 & Status == 'Active'")`
- **GroupBy Aggregation**: `df.groupby('Key').agg(New_Col=('Source_Col', 'mean'))`
- **Merging**: `pd.merge(df1, df2, on='Key', how='inner'|'left'|'outer')`
- **Datetime Extraction**: `df['Date'].dt.year`, `df['Date'].dt.month`, `df['Date'].dt.day_name()`

---

## 3. Statistical & Preprocessing Formulas

### Z-Score Standardization
$$z = rac{x - \mu}{\sigma}$$
Where $\mu = 	ext{mean}(x)$ and $\sigma = 	ext{std}(x)$.

### Min-Max Normalization
$$x' = rac{x - x_{\min}}{x_{\max} - x_{\min}}$$

### Interquartile Range (IQR) & Outlier Bounds
$$	ext{IQR} = Q_3 - Q_1$$
$$	ext{Lower Bound} = Q_1 - 1.5 	imes 	ext{IQR}$$
$$	ext{Upper Bound} = Q_3 + 1.5 	imes 	ext{IQR}$$

### Pearson Correlation Coefficient
$$r_{xy} = rac{\sum (x_i - ar{x})(y_i - ar{y})}{\sqrt{\sum (x_i - ar{x})^2 \sum (y_i - ar{y})^2}}$$

### Log1p Transformation
$$y = \ln(1 + x)$$
