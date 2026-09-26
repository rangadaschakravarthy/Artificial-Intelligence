# Level 2 Practice Test Solutions

1. `arr[1:3, 2:4]`
2. Shapes `(3, 1)` and `(1, 4)` broadcast along single dimensions to produce output shape `(3, 4)`.
3. `df['Price'].fillna(df['Price'].median(), inplace=True); df.groupby('Region')['Revenue'].mean()`.
4. `pd.merge(orders_df, customers_df, on='CustomerID', how='left')`.
5. `sns.heatmap(df.corr(), mask=np.triu(np.ones_like(df.corr(), dtype=bool)), annot=True)`.
6. `X_tr, X_te, y_tr, y_te = train_test_split(X, y); scaler = StandardScaler(); X_tr_s = scaler.fit_transform(X_tr); X_te_s = scaler.transform(X_te)`.
