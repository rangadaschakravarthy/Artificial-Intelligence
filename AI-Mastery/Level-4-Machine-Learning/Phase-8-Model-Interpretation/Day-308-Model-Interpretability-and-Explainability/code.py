# Code — Day 308: Model Interpretability & Explainability
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier

def demonstrate_workflow():
    print("--- Day 308: Model Interpretability & Explainability Demo ---")
    
    # 1. Create Mixed Dataset
    df = pd.DataFrame({
        'age': [25, 30, np.nan, 45, 35, 50, 23, 40],
        'income': [50000, 60000, 80000, np.nan, 75000, 120000, 32000, 95000],
        'city': ['NY', 'SF', 'NY', 'LA', 'SF', 'LA', 'NY', 'SF'],
        'bought': [0, 1, 0, 1, 1, 1, 0, 1]
    })
    
    X = df.drop(columns=['bought'])
    y = df['bought']
    
    # 2. Define Pipelines
    num_cols = ['age', 'income']
    cat_cols = ['city']
    
    num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])
    
    cat_pipeline = Pipeline([
        ('encoder', OneHotEncoder(handle_unknown='ignore'))
    ])
    
    preprocessor = ColumnTransformer([
        ('num', num_pipeline, num_cols),
        ('cat', cat_pipeline, cat_cols)
    ])
    
    full_pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(random_state=42))
    ])
    
    # 3. Fit Pipeline
    full_pipeline.fit(X, y)
    print("Full Pipeline Trained Successfully!")
    print("Transformed Feature Matrix Shape:", full_pipeline.named_steps['preprocessor'].transform(X).shape)

if __name__ == "__main__":
    demonstrate_workflow()
