import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def run_visual_eda(df):
    print("Generating Visual EDA Diagnostics...")
    
    # 1. Missing Value Matrix Plot
    fig, ax = plt.subplots(figsize=(7, 3))
    sns.heatmap(df.isnull(), cbar=False, cmap='viridis', yticklabels=False, ax=ax)
    ax.set_title("Missing Data Null Matrix")
    fig.savefig("eda_missing_matrix.png", bbox_inches='tight')
    plt.close(fig)
    
    # 2. Correlation Heatmap
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.heatmap(df.corr(numeric_only=True), annot=True, fmt='.2f', cmap='coolwarm', ax=ax)
    ax.set_title("Feature Correlation Heatmap")
    fig.savefig("eda_correlation_heatmap.png", bbox_inches='tight')
    plt.close(fig)
    
    print("Visual EDA Complete! Saved diagnostic plots.")

def main():
    print("=== Day 151: Visualization for EDA Demonstration ===")
    np.random.seed(42)
    df = pd.DataFrame({
        'Age': [25, np.nan, 35, 45, 50, 23],
        'Income': [50000, 60000, np.nan, 90000, 110000, 42000],
        'Score': [70, 80, 85, 90, 95, 65]
    })
    run_visual_eda(df)

if __name__ == "__main__":
    main()
