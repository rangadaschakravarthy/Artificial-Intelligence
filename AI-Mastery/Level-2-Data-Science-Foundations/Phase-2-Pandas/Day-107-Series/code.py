import pandas as pd
import numpy as np

def main():
    # 1. Creating Series
    s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'], name='SampleSeries')
    print("Series:
", s)
    print("Underlying NumPy Array:", s.to_numpy())
    print("Index Labels:", s.index)
    
    # 2. Label Alignment Demo
    s1 = pd.Series([100, 200], index=['Apple', 'Banana'])
    s2 = pd.Series([150, 300], index=['Banana', 'Cherry'])
    print("
Series 1:
", s1)
    print("Series 2:
", s2)
    print("Sum (Auto-aligned by label):
", s1 + s2)
    
    # 3. Categorical Exploration (value_counts)
    cities = pd.Series(['NY', 'LA', 'NY', 'SF', 'NY', 'LA', np.nan])
    print("
City Counts (including NaNs):
", cities.value_counts(dropna=False))
    print("Unique Cities:", cities.unique())

if __name__ == "__main__":
    main()
