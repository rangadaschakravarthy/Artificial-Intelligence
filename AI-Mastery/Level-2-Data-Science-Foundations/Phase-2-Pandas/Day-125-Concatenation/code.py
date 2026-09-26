import pandas as pd
import numpy as np

def main():
    print("=== Day 125: Concatenation Demonstration ===")
    
    # 1. Sample Batches
    batch_q1 = pd.DataFrame({
        'Region': ['East', 'West'],
        'Sales': [15000, 22000]
    })
    
    batch_q2 = pd.DataFrame({
        'Region': ['East', 'West', 'North'],
        'Sales': [18000, 24000, 12000]
    })
    
    print("Batch Q1:
", batch_q1)
    print("
Batch Q2:
", batch_q2)
    
    # 2. Vertical Concatenation (axis=0)
    print("
--- 1. Vertical Concatenation (ignore_index=True) ---")
    stacked = pd.concat([batch_q1, batch_q2], axis=0, ignore_index=True)
    print(stacked)
    
    # 3. Concatenation with Source Keys
    print("
--- 2. Vertical Concat with Source Keys ---")
    keyed_concat = pd.concat([batch_q1, batch_q2], keys=['Q1_Data', 'Q2_Data'])
    print(keyed_concat)
    
    # 4. Horizontal Concatenation (axis=1)
    print("
--- 3. Horizontal Feature Concatenation ---")
    feat_set1 = pd.DataFrame({'F1': [1, 2], 'F2': [3, 4]})
    feat_set2 = pd.DataFrame({'F3': [0.5, 0.8], 'F4': [0.1, 0.9]})
    
    combined_feats = pd.concat([feat_set1, feat_set2], axis=1)
    print(combined_feats)

if __name__ == "__main__":
    main()
