import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def main():
    print("=== Day 158: One-Hot Encoding Demonstration ===")
    
    df = pd.DataFrame({'Color': ['Red', 'Green', 'Blue', 'Red']})
    
    # Scikit-Learn OneHotEncoder
    ohe = OneHotEncoder(drop='first', sparse_output=False)
    encoded_arr = ohe.fit_transform(df[['Color']])
    
    encoded_df = pd.DataFrame(encoded_arr, columns=ohe.get_feature_names_out())
    print("One-Hot Encoded DataFrame (drop='first'):
", encoded_df)

if __name__ == "__main__":
    main()
