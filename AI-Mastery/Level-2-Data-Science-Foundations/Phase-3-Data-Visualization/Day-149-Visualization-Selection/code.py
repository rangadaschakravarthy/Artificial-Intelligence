import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def main():
    print("=== Day 149: Visualization Selection Demonstration ===")
    
    # Selecting correct charts for 2 questions:
    # 1. Distribution of Customer Ages -> Histogram
    # 2. Relationship between Income and Spend -> Scatter Plot
    
    np.random.seed(42)
    ages = np.random.normal(35, 10, 200)
    income = np.random.normal(60000, 15000, 200)
    spend = income * 0.4 + np.random.normal(0, 3000, 200)
    
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    
    # Q1: Distribution -> Histogram
    sns.histplot(ages, kde=True, ax=axes[0], color='purple')
    axes[0].set_title("1. Distribution: Customer Age")
    
    # Q2: Relationship -> Scatter
    axes[1].scatter(income, spend, alpha=0.6, color='teal')
    axes[1].set_title("2. Relationship: Income vs Spend")
    
    fig.tight_layout()
    fig.savefig("day149_chart_selection.png", bbox_inches='tight')
    plt.close(fig)
    print("Saved day149_chart_selection.png")

if __name__ == "__main__":
    main()
