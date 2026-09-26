import pandas as pd
import numpy as np

def main():
    print("=== Day 156: Encoding Concepts Demonstration ===")
    
    df = pd.DataFrame({'Device': ['Mobile', 'Desktop', 'Mobile', 'Tablet', 'Desktop', 'Mobile']})
    
    # Frequency Encoding
    freq_map = df['Device'].value_counts(normalize=True).to_dict()
    df['Device_Freq'] = df['Device'].map(freq_map)
    
    print("Raw and Frequency Encoded Features:
", df)

if __name__ == "__main__":
    main()
