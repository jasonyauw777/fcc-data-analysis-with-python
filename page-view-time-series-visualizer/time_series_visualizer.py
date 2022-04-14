import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv").set_index('date')
df.index = pd.to_datetime(df.index)

# Clean data
df = df.loc[ (df["value"] < df["value"].quantile(0.975) ) & (df["value"] > df["value"].quantile(0.025) ) ]


def draw_line_plot():
    # Draw line plot
    plt.subplots(figsize = (18, 6))
    plt.plot(df.index, df['value'], color="red")
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.show()




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = None

    # Draw bar plot
    df_bar['month'] = df_bar.index.month
    df_bar['year'] = df_bar.index.year
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df_bar['month'] = df_bar['month'].apply(lambda data: months[data-1])
    df_bar['month'] = pd.Categorical(df_bar['month'], categories = months)

    df_pivot = pd.pivot_table(
      df_bar,
      values = 'value',
      index = 'year',
      columns = 'month',
      aggfunc = np.mean
    )

    ax = df_pivot.plot(kind = 'bar')
    fig = ax.get_figure()
    fig.set_size_inches(7, 6)
      
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axs = plt.subplots(1, 2)
    fig.set_size_inches(20, 10)

    axs[0].set_title('Year-wise Box Plot (Trend)')
    axs[1].set_title('Month-wise Box Plot (Seasonality)')

    sns.boxplot(x = df_box['year'], y = df_box['value'], ax = axs[0]).set(xlabel = 'Year', ylabel = 'Page Views')
    sns.boxplot(x = df_box['month'], y = df_box['value'], 
    order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], ax = axs[1]).set(xlabel = 'Month', ylabel = 'Page Views')




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
