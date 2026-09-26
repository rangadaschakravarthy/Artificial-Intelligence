import pandas as pd
import numpy as np

def main():
    print("=== Capstone Project 1: Sales Data Analysis ===")
    df = pd.DataFrame({'Branch': ['East', 'West', 'East'], 'Sales': [1000, 1500, 1200]})
    print(df.groupby('Branch')['Sales'].sum())

if __name__ == '__main__':
    main()
