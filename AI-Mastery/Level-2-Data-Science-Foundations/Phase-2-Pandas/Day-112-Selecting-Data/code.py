import pandas as pd
import numpy as np

def main():
    # 1. Sample DataFrame
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'Score': [88, 92, 79, 95],
        'Target': [1, 0, 1, 0]
    }, index=['r0', 'r1', 'r2', 'r3'])
    
    print("DataFrame:
", df)
    
    # 2. Column Selection (Series vs DataFrame)
    print("
Series df['Age'] shape:", df['Age'].shape)
    print("DataFrame df[['Age']] shape:", df[['Age']].shape)
    
    # 3. loc (Label-based) vs iloc (Positional)
    print("
.loc['r0':'r1', 'Name':'Age'] (Inclusive):
", df.loc['r0':'r1', 'Name':'Age'])
    print("
.iloc[0:2, 0:2] (Exclusive):
", df.iloc[0:2, 0:2])
    
    # 4. Fast Scalar Access
    print("
.at['r1', 'Score']:", df.at['r1', 'Score'])
    print(".iat[1, 2]:", df.iat[1, 2])
    
    # 5. ML Feature/Target Separation
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    print("
X (Features) shape:", X.shape)
    print("y (Target) shape:", y.shape)

if __name__ == "__main__":
    main()
