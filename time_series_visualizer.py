import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
import numpy as np

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df=pd.read_csv("fcc-forum-pageviews.csv",parse_dates=['date'])

# Clean data
df=df[(df['value']>=df["value"].quantile(0.025)) & (df["value"]<=df["value"].quantile(0.975))]


def draw_line_plot():
    df_line=df.copy()
    df_line=df_line.set_index('date')
    # Draw line plot
    fig, ax = plt.subplots(figsize=(20,6))


    ax.plot(df_line["value"],c="red")

    ax.set(xlabel="Date",
        ylabel="Page Views",
        title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    date_form = DateFormatter("%Y-%m")
    ax.xaxis.set_major_formatter(date_form)
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=6))
   





    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    
    
    #df_bar.reset_index(inplace=True)
    #df_bar['year'] = [d.year for d in df_bar.date]
    #df_bar['month'] = [d.strftime('%b') for d in df_bar.date]
    #df_bar = df.copy()
    #df_bar['day'] = df_bar["date"].day
    df_bar['month'] = df_bar["date"].dt.month
    
    df_bar['year'] = df_bar["date"].dt.year
   

    month_name_raw={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
    df_bar["Months"]=df_bar["month"].map(month_name_raw)

    print(df_bar)
    

    df_bar_pivot=pd.pivot_table(df_bar,index='year',
                                 columns="Months",
                                values="value",
                                aggfunc=np.mean)
   
    # Draw bar plot
    ax = df_bar_pivot.plot(kind="bar")
    fig=ax.get_figure()
    fig.set_size_inches(6.5,6.5)
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")

    

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
    fig, axes = plt.subplots(1,2,figsize=(20,6))
    sns.set_style("whitegrid")


    ax=sns.boxplot(data= df_box,x='year',y='value',ax=axes[0])
    ax.set(xlabel="Year",
            ylabel="Page Views",
            title='Year-wise Box Plot (Trend)')
    ax=sns.boxplot(data= df_box,x='month',y='value',ax=axes[1],order=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    ax.set(xlabel="Month",
            ylabel="Page Views",
            title='Month-wise Box Plot (Trend)')




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
