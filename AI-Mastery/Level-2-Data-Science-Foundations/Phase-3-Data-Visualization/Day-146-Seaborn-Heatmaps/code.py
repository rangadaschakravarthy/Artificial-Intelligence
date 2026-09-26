import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def main():
    print("=== Day 146: Seaborn Heatmaps Demonstration ===")
    
    np.random.seed(42)
    data = np.random.randn(100, 4)
    df = pd.DataFrame(data, columns=['Var_A', 'Var_B', 'Var_C', 'Var_D'])
    df['Var_C'] += df['Var_A'] * 2.0
    
    corr = df.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.heatmap(corr, mask=mask, annot=True, fmt='.2f', cmap='coolwarm', vmin=-1, vmax=1, linewidths=0.8, ax=ax)
    
    ax.set_title("Feature Correlation Heatmap (Upper Masked)", fontsize=13)
    
    fig.tight_layout()
    fig.savefig("day146_heatmap.png", bbox_inches='tight')
    plt.close(fig)
    print("Saved day146_heatmap.png")

if __name__ == "__main__":
    main()
