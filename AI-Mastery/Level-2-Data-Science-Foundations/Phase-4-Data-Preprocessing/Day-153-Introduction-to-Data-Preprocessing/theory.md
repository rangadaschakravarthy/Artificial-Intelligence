# Day 153 Theory: Introduction to Data Preprocessing

### 1. What Is It?
Data Preprocessing is the systematic process of converting cleaned raw tabular data into a refined numeric matrix optimized for machine learning algorithms.

### 2. The Complete Preprocessing Flow
```
Raw Data ➔ Clean Nulls/Duplicates ➔ Encode Categoricals ➔ Detect Outliers ➔ Transform Skew ➔ Scale Features ➔ Select Features ➔ ML Ready Data
```

### 3. Connection to Mathematics for AI (Level 1)
- **Feature Scaling**: Maps feature vectors into normalized $L_2$ vector spaces or standard normal distributions $\mathcal{N}(0, 1)$.
- **Encoding**: Maps discrete categorical sets to orthogonal unit basis vectors in $\mathbb{R}^K$.
- **Outlier Detection**: Uses statistical $Z$-scores ($Z = rac{x - \mu}{\sigma}$) and Interquartile Ranges ($	ext{IQR} = Q_3 - Q_1$).

### 4. Summary
Preprocessing translates continuous and categorical variables into standardized mathematical representations for machine learning models.
