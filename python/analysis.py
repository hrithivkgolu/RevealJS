# marimo
# NOTEBOOK: Interactive Data Exploration
# Author email: 24f2000717@ds.study.iitm.ac.in

import marimo

app = marimo.App()

# --------------------------------------------------------------------
# CELL 1 — Import libraries and generate synthetic data
# --------------------------------------------------------------------
# Data flow:
#   - `x` and `noise` feed into Cell 2
#   - Cell 2 uses the slider to dynamically compute `y`
# --------------------------------------------------------------------
@app.cell
def __():
    import numpy as np
    import pandas as pd

    # Synthetic dataset
    np.random.seed(42)
    x = np.linspace(0, 10, 200)
    noise = np.random.normal(scale=1.5, size=200)

    df = pd.DataFrame({"x": x, "noise": noise})
    df.head()
    return df, x, noise, np, pd


# --------------------------------------------------------------------
# CELL 2 — Interactive slider controls the slope coefficient
# --------------------------------------------------------------------
# Data flow:
#   - This slider value feeds into Cell 3
#   - Changing slider re-triggers dependent cells automatically
# --------------------------------------------------------------------
@app.cell
def __():
    import marimo as mo

    slope = mo.ui.slider(0, 5, value=2, label="Slope for y = slope * x + noise")
    slope
    return slope


# --------------------------------------------------------------------
# CELL 3 — Compute dependent variable y
# --------------------------------------------------------------------
# Data flow:
#   - Uses `x`, `noise` from Cell 1 and `slope.value` from Cell 2
#   - Output is used by Cell 4 for plotting and markdown text
# --------------------------------------------------------------------
@app.cell
def __(x, noise, slope, np):
    y = slope.value * x + noise
    y[:5], slope.value
    return y


# --------------------------------------------------------------------
# CELL 4 — Dynamic Markdown + Plot
# --------------------------------------------------------------------
# Dynamically updates text and graph when the slider moves.
# --------------------------------------------------------------------
@app.cell
def __(x, y, slope):
    import marimo as mo
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.scatter(x, y, alpha=0.6)
    ax.set_title(f"Scatter Plot for y = {slope.value}·x + noise")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    dynamic_md = mo.md(f"""
    ## Relationship Overview  
    The current model uses:  
    **Slope = {slope.value}**

    Increasing the slope steepens the linear relationship between **x** and **y**.  
    This markdown updates *live* with every adjustment of the slider.
    """)

    (fig, dynamic_md)
    return fig, dynamic_md


app.run()
