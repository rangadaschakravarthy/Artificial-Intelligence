import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

def main():
    print("=== Day 157: Label & Ordinal Encoding Demonstration ===")
    
    df = pd.DataFrame({
        'Customer_ID': [101, 102, 103, 104],
        'Satisfaction': ['Dissatisfied', 'Neutral', 'Satisfied', 'Very Satisfied']
    })
    
    # Explicit Mapping
    sat_map = {'Dissatisfied': 0, 'Neutral': 1, 'Satisfied': 2, 'Very Satisfied': 3}
    df['Sat_Code'] = df['Satisfaction'].map(sat_map)
    
    print("Ordinal Encoded Dataset:
", df)

if __name__ == "__main__":
    main()
