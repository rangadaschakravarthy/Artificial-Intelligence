import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def main():
    print("=== Day 142: Seaborn Introduction Demonstration ===")
    
    np.random.seed(42)
    df = pd.DataFrame({
        'Age': np.random.randint(20, 60, 50),
        'Income': np.random.normal(65000, 15000, 50),
        'Education': np.random.choice(['Bachelors', 'Masters', 'PhD'], 50)
    })
    
    sns.set_theme(style='whitegrid', palette='Set2')
    fig, ax = plt.subplots(figsize=(8, 4.5))
    
    sns.scatterplot(data=df, x='Age', y='Income', hue='Education', style='Education', s=90, ax=ax)
    
    ax.set_title("Demographic Income Distribution by Education Level", fontsize=13)
    
    fig.tight_layout()
    fig.savefig("day142_seaborn_intro.png", bbox_inches='tight')
    plt.close(fig)
    print("Saved day142_seaborn_intro.png")

if __name__ == "__main__":
    main()
