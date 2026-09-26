import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def main():
    print("=== Day 133: Introduction to Data Visualization ===")
    
    # Dataset
    df = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        'Revenue': [100, 120, 140, 130, 170],
        'Expenses': [80, 85, 90, 95, 100]
    })
    
    # Matplotlib Plot
    plt.figure(figsize=(8, 4))
    plt.plot(df['Month'], df['Revenue'], marker='o', label='Revenue', color='blue')
    plt.plot(df['Month'], df['Expenses'], marker='s', label='Expenses', color='red')
    plt.title("Financial Overview (Matplotlib)")
    plt.xlabel("Month")
    plt.ylabel("Amount ($)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("day133_matplotlib_overview.png")
    plt.close()
    print("Saved day133_matplotlib_overview.png")
    
    # Seaborn Plot
    sns.set_theme(style='whitegrid')
    plt.figure(figsize=(8, 4))
    sns.barplot(data=df, x='Month', y='Revenue', palette='Blues_d')
    plt.title("Monthly Revenue (Seaborn)")
    plt.tight_layout()
    plt.savefig("day133_seaborn_overview.png")
    plt.close()
    print("Saved day133_seaborn_overview.png")

if __name__ == "__main__":
    main()
