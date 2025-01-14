import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Import data
df = pd.read_csv("epa-sea-level.csv")

# Draw plot
def draw_plot():
    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label="Data", color='blue', alpha=0.6)

    # Create first line of best fit using all data
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred1 = pd.Series(range(1880, 2051))
    y_pred1 = slope * x_pred1 + intercept
    plt.plot(x_pred1, y_pred1, 'r', label='Best Fit Line (All Data)', linewidth=2)

    # Create second line of best fit using data from 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(
        df_recent['Year'], df_recent['CSIRO Adjusted Sea Level']
    )
    x_pred2 = pd.Series(range(2000, 2051))
    y_pred2 = slope_recent * x_pred2 + intercept_recent
    plt.plot(x_pred2, y_pred2, 'green', label='Best Fit Line (2000 onwards)', linewidth=2)

    # Add labels, title, and legend
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.legend()
    plt.grid(True)

    # Save plot
    plt.savefig('sea_level_plot.png')
    return plt.gca()
