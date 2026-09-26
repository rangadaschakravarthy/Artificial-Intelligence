import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def main():
    print("=== Day 172: Data Preprocessing Mini Project Capstone ===")
    
    # STAGE 1: RAW INGESTION
    np.random.seed(42)
    n = 100
    raw_df = pd.DataFrame({
        'Age': np.random.choice([25, 30, 45, np.nan, 50], n),
        'Income': np.random.exponential(50000, n),
        'City': np.random.choice(['NY', 'SF', 'LA', np.nan], n),
        'Churn': np.random.choice([0, 1], n, p=[0.8, 0.2])
    })
    
    print("Raw Dataset Ingested. Shape:", raw_df.shape)
    
    # STAGE 2: SEPARATE X AND Y
    y = raw_df['Churn']
    X = raw_df.drop(columns=['Churn'])
    
    # STAGE 3: TRAIN/TEST SPLIT FIRST (LEAKAGE BOUNDARY)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    print("Train/Test Split Completed. Train shape:", X_train.shape, "Test shape:", X_test.shape)
    
    # STAGE 4: PIPELINE PREPROCESSING
    num_cols = ['Age', 'Income']
    cat_cols = ['City']
    
    preprocessor = ColumnTransformer(transformers=[
        ('num', Pipeline([
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ]), num_cols),
        ('cat', Pipeline([
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('ohe', OneHotEncoder(drop='first', sparse_output=False))
        ]), cat_cols)
    ])
    
    # FIT ON TRAIN ONLY!
    X_train_proc = preprocessor.fit_transform(X_train)
    X_test_proc = preprocessor.transform(X_test)
    
    # STAGE 5: QUALITY ASSERTIONS
    assert np.isnan(X_train_proc).sum() == 0, "Error: Nulls remain in X_train!"
    assert np.isnan(X_test_proc).sum() == 0, "Error: Nulls remain in X_test!"
    assert X_train_proc.shape[0] == y_train.shape[0], "Error: Train row mismatch!"
    
    print("
Preprocessed X_train Array Shape:", X_train_proc.shape)
    print("Preprocessed X_test Array Shape: ", X_test_proc.shape)
    print("
=== LEVEL 2: DATA SCIENCE FOUNDATIONS CURRICULUM COMPLETE ===")

if __name__ == "__main__":
    main()
