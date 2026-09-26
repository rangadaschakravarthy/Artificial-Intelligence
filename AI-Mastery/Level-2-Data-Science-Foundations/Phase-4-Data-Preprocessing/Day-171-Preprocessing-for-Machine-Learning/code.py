import pandas as pd
from sklearn.preprocessing import StandardScaler

def main():
    print("=== Day 171: Preprocessing for Machine Learning Demonstration ===")
    
    df = pd.DataFrame({
        'Age': [20, 30, 40],
        'Income': [30000, 60000, 90000],
        'Tier': ['Basic', 'Medium', 'High']
    })
    
    # Linear Preprocessing
    X_linear = pd.get_dummies(df, columns=['Tier'], drop_first=True, dtype=float)
    scaler = StandardScaler()
    X_linear[['Age', 'Income']] = scaler.fit_transform(X_linear[['Age', 'Income']])
    
    print("Preprocessed Matrix for Linear Models:
", X_linear.round(3))

if __name__ == "__main__":
    main()
