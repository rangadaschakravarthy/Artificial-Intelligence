import pandas as pd
import numpy as np
import plotly.graph_objects as go

def main():
    print("=== Day 148: Interactive Charts Demonstration ===")
    
    dates = pd.date_range('2023-01-01', periods=10)
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(x=dates, y=[10, 12, 14, 13, 15, 18, 20, 19, 22, 25], name='Stock A'))
    fig.add_trace(go.Scatter(x=dates, y=[25, 24, 22, 20, 21, 19, 18, 17, 15, 14], name='Stock B'))
    
    fig.update_layout(
        title="Interactive Portfolio Performance Comparison",
        xaxis=dict(rangeslider=dict(visible=True)),
        template='plotly_white'
    )
    
    fig.write_html("day148_interactive_portfolio.html")
    print("Saved day148_interactive_portfolio.html")

if __name__ == "__main__":
    main()
