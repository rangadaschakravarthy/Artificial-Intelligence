import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def main():
    print("=== Day 145: Seaborn Relationship Plots Demonstration ===")
    
    np.random.seed(42)
    df = pd.DataFrame({
        'Feature_1': np.random.randn(100),
        'Feature_2': np.random.randn(100),
        'Target': np.random.choice([0, 1], 100)
    })
    df['Feature_2'] += df['Feature_1'] * 1.5
    
    sns.set_theme(style='ticks')
    g = sns.lmplot(data=df, x='Feature_1', y='Feature_2', hue='Target', palette='Set1', height=4.5, aspect=1.3)
    g.fig.suptitle("Linear Regression Trends by Target Class", y=1.03)
    
    g.savefig("day145_relationship_plot.png", bbox_inches='tight')
    plt.close()
    print("Saved day145_relationship_plot.png")

if __name__ == "__main__":
    main()
