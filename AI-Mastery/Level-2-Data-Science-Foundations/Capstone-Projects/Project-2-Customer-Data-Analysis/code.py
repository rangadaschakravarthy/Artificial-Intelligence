import pandas as pd
import numpy as np

def main():
    print("=== Capstone Project 2: Customer Data Analysis ===")
    df = pd.DataFrame({'Tier': ['Basic', 'Premium'], 'Churn': [0.2, 0.05]})
    print(df)

if __name__ == '__main__':
    main()
