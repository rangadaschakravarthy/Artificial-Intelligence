import pandas as pd
import numpy as np
import plotly.express as px

def main():
    print("=== Day 147: Plotly Introduction Demonstration ===")
    
    df = pd.DataFrame({
        'Experience': [1, 2, 3, 5, 7, 8, 10],
        'Salary': [45000, 52000, 60000, 78000, 95000, 105000, 135000],
        'Role': ['Junior', 'Junior', 'Mid', 'Mid', 'Senior', 'Senior', 'Lead']
    })
    
    fig = px.scatter(df, x='Experience', y='Salary', color='Role', text='Role',
                     title="Interactive Salary vs Experience (Plotly Express)")
    
    fig.write_html("day147_plotly_interactive.html")
    print("Saved day147_plotly_interactive.html")

if __name__ == "__main__":
    main()
