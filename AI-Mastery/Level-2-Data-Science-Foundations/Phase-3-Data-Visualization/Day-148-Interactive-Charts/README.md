# Day 148 — Interactive Charts

## Learning Objectives
- Construct advanced interactive charts using Plotly Graph Objects (`plotly.graph_objects`).
- Build interactive 3D scatter plots, financial candlestick charts, and multi-trace overlays.
- Customize layout controls, update menus, and range sliders.

## Prerequisites
- Day 147: Plotly Introduction

## Topics Covered
- Low-level `plotly.graph_objects` (`go`) module architecture
- Multi-trace overlays (`fig.add_trace()`)
- Financial Candlestick charts (`go.Candlestick()`)
- Interactive 3D Scatter plots (`go.Scatter3d()`)
- Adding range sliders (`rangeslider=dict(visible=True)`) and dropdown menus

## Why This Matters
Complex custom dashboards (e.g. financial trading charts, 3D spatial embeddings) require the fine-grained control of `plotly.graph_objects`.

## Practical Work
- Construct an interactive financial Candlestick chart with a range slider.

## Difficulty
Intermediate
