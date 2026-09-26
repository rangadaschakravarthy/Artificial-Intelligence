import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def main():
    print("=== Day 170: Preprocessing Pipelines Demonstration ===")
    
    X = pd.DataFrame({
        'Age': [25.0, np.nan, 45.0],
        'City': ['NY', 'SF', 'NY']
    })
    
    preprocessor = ColumnTransformer(transformers=[
        ('num', Pipeline([('imp', SimpleImputer(strategy='mean')), ('scale', StandardScaler())]), ['Age']),
        ('cat', OneHotEncoder(drop='first', sparse_output=False), ['City'])
    ])
    
    X_proc = preprocessor.fit_transform(X)
    print("Pipeline Output Array:
", X_proc.round(3))

if __name__ == "__main__":
    main()
