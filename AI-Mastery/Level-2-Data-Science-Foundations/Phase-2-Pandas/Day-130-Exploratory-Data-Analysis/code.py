import pandas as pd
import numpy as np

def main():
    print("=== Day 130: Exploratory Data Analysis Demonstration ===")
    
    # 1. Synthetic E-Commerce Customer Dataset
    np.random.seed(42)
    n = 100
    df = pd.DataFrame({
        'Tenure_Months': np.random.randint(1, 48, n),
        'Monthly_Spend': np.random.normal(75, 25, n).clip(10, 200),
        'Support_Tickets': np.random.poisson(2, n),
        'Churn': np.random.choice([0, 1], size=n, p=[0.8, 0.2])
    })
    
    # Add strong synthetic correlation: higher support tickets -> higher churn
    df.loc[df['Support_Tickets'] > 3, 'Churn'] = 1
    
    print("=== 1. STRUCTURAL AUDIT ===")
    print("Shape:", df.shape)
    print("
Data Types & Nulls:
", df.isnull().sum())
    
    print("
=== 2. UNIVARIATE ANALYSIS ===")
    print("Numerical Summary:
", df.describe().round(2))
    print("
Spend Skewness:", round(df['Monthly_Spend'].skew(), 3))
    print("
Churn Rate Proportions:
", df['Churn'].value_counts(normalize=True).round(3))
    
    print("
=== 3. BIVARIATE CORRELATION MATRIX ===")
    corr_matrix = df.corr().round(3)
    print(corr_matrix)
    
    print("
=== 4. BIVARIATE GROUP COMPARISON (Churn Drivers) ===")
    churn_drivers = df.groupby('Churn').mean().round(2)
    print(churn_drivers)

if __name__ == "__main__":
    main()
