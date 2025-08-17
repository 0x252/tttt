import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
np.float = np.float16
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')

# Clean data
low = df['value'].quantile(0.025)
high = df['value'].quantile(0.975)
df = df[(df['value'] >= low) & (df['value'] <= high)]

def draw_line_plot():
    # Draw line plot
    fig,ax = plt.subplots(figsize=(12,6))
    #ax.plot(df.cumsum(), c='red')
    ax.plot(df, c='red')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar['month'] = [d.strftime('%B') for d in df_bar.date]
    df_bar['year'] = [d.year for d in df_bar.date]
    # Draw bar plot
    fig,ax = plt.subplots(figsize=(12,6))
    months_order = ['January', 'February', 'March', 'April', 'May', 'June',
                'July', 'August', 'September', 'October', 'November', 'December']

    df_bar['month'] = pd.Categorical(df_bar['month'], categories=months_order, ordered=True)

    df_bar_grouped = df_bar.groupby(['year','month'])['value'].mean().unstack()
    #df_bar.plot(kind='bar', ax=ax)
    df_bar_grouped.plot(kind='bar',ax=ax)
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.set_title('Page views')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    months_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    df_box['month'] = pd.Categorical(df_box['month'], categories=months_order, ordered=True)
    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(figsize=(12, 12), nrows=2)

    # Year-wise box plot
    sns.boxplot(data=df_box, x="year", y="value", ax=ax1)
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")

    # Month-wise box plot
    sns.boxplot(data=df_box, x="month", y="value", ax=ax2)
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
