import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def main():
    print("=== Day 143: Seaborn Categorical Plots Demonstration ===")
    
    np.random.seed(42)
    df = pd.DataFrame({
        'Tier': np.random.choice(['Basic', 'Premium', 'Enterprise'], 150),
        'Monthly_Usage_Hrs': np.random.exponential(25, 150),
        'Region': np.random.choice(['US', 'EU'], 150)
    })
    
    sns.set_theme(style='whitegrid')
    fig, ax = plt.subplots(figsize=(8.5, 4.5))
    
    sns.violinplot(data=df, x='Tier', y='Monthly_Usage_Hrs', hue='Region', split=True, inner='quartile', palette='Pastel1', ax=ax)
    sns.stripplot(data=df, x='Tier', y='Monthly_Usage_Hrs', hue='Region', dodge=True, color='black', alpha=0.3, size=4, ax=ax)
    
    ax.set_title("Customer Usage Hours by Tier & Region (Violin + Strip)", fontsize=13)
    
    fig.tight_layout()
    fig.savefig("day143_categorical_plot.png", bbox_inches='tight')
    plt.close(fig)
    print("Saved day143_categorical_plot.png")

if __name__ == "__main__":
    main()
