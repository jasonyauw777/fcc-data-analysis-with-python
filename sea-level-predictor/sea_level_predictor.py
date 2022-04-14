import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], color = "black")

    # Create first line of best fit
    slope, intercept, r_value, p_value, stderr = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    line_x = np.arange(df["Year"].min(), 2050)
    line_y = slope*line_x + intercept
    plt.plot(line_x, line_y)

    # Create second line of best fit
    df_2nd = df.loc[df["Year"]>=2000]

    slope2, intercept2, r_value2, p_value2, stderr2 = linregress(df_2nd["Year"], df_2nd["CSIRO Adjusted Sea Level"])

    line_x2 = np.arange(2000, 2050)
    line_y2 = slope2*line_x2 + intercept2
    plt.plot(line_x2, line_y2)

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()