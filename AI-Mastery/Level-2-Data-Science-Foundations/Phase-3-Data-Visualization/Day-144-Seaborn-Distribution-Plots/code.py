import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def main():
    print("=== Day 144: Seaborn Distribution Plots Demonstration ===")
    
    np.random.seed(42)
    df = pd.DataFrame({
        'Feature_X': np.random.normal(50, 10, 250),
        'Feature_Y': np.random.normal(100, 20, 250),
        'Group': np.random.choice(['Control', 'Treatment'], 250)
    })
    
    sns.set_theme(style='white')
    g = sns.jointplot(data=df, x='Feature_X', y='Feature_Y', hue='Group', kind='kde', alpha=0.7)
    g.fig.suptitle("Joint Distribution Comparison by Group", y=1.02)
    
    g.savefig("day144_joint_distribution.png", bbox_inches='tight')
    plt.close()
    print("Saved day144_joint_distribution.png")

if __name__ == "__main__":
    main()
