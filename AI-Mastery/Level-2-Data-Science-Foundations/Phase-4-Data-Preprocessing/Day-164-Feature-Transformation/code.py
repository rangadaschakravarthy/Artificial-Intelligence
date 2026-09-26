import pandas as pd

def main():
    print("=== Day 164: Feature Transformation (Binning) Demonstration ===")
    
    df = pd.DataFrame({'Score': [45, 62, 78, 85, 92, 98]})
    
    df['Grade_Cut'] = pd.cut(df['Score'], bins=[0, 60, 80, 100], labels=['F', 'B', 'A'])
    df['Quartile_Qcut'] = pd.qcut(df['Score'], q=3, labels=['Low', 'Mid', 'High'])
    
    print("Discretized Scores:
", df)

if __name__ == "__main__":
    main()
