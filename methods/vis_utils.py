import seaborn as sns
import pandas as pd
import streamlit as st

import plotly.express as px
import numpy as np
import plotly.graph_objs as go
import plotly.express as px

def create_correlation_chart(df_view, ticker1, ticker2, window_size):
    """
    Creates a plotly chart showing stock prices and rolling correlation.
    
    Args:
        df_view: DataFrame with price data and rolling correlation
        ticker1: First ticker symbol
        ticker2: Second ticker symbol  
        window_size: Rolling window size for correlation calculation
        
    Returns:
        plotly.graph_objs.Figure: The configured chart
    """
    fig = go.Figure()

    # Add first ticker price (left y-axis)
    fig.add_trace(go.Scatter(
        x=df_view.index, y=df_view[ticker1], mode='lines', name=ticker1, yaxis='y1'
    ))
    # Add second ticker price (left y-axis)
    fig.add_trace(go.Scatter(
        x=df_view.index, y=df_view[ticker2], mode='lines', name=ticker2, yaxis='y1'
    ))
    # Add rolling correlation (right y-axis)
    fig.add_trace(go.Scatter(
        x=df_view.index, y=df_view['Rolling Correlation'],
        mode='lines', name=f'Rolling Correlation ({window_size}-day)',
        line=dict(dash='dot', color='grey'),
        yaxis='y2'
    ))

    fig.update_layout(
        title=f"Stock Prices and Rolling Correlation ({window_size}-day)",
        xaxis_title="Date",
        yaxis=dict(
            title="Price",
            side="left"
        ),
        yaxis2=dict(
            title="Rolling Correlation",
            overlaying="y",
            side="right",
            range=[-1, 1]
        ),
        legend=dict(
            orientation="h",
            yanchor="top",
            y=1.08,
            xanchor="center",
            x=0.5
        )
    )
    
    return fig

def pension_expenses(duration, pension_years, living, expns):
    

    durations = np.arange(duration+pension_years)    
    yearly_living_prices = 12*living * (1 + expns) ** durations

    yearly_living_prices = pd.Series(yearly_living_prices)
    indexer = pd.api.indexers.FixedForwardWindowIndexer(window_size = pension_years)
    coming_living_prices = yearly_living_prices.rolling(window=indexer,
                                                            min_periods=pension_years).sum().dropna()
    return coming_living_prices

def plot_combined_growth(init_price: float, expns: float, living:float, living_gr:float, pension_years:float,
                         initial_invest: float, monthly_invest: float, annual_rev: float, duration: int = 30):
    
    # Example usage:
    # plot_combined_growth(init_price=100000, expns=0.03, initial_invest=10000, monthly_invest=500, annual_rev=0.08)

    # Create array of durations
    durations = np.arange(duration + 1)
    # Calculate house prices
    house_prices = init_price * (1 + expns) ** durations
    coming_living_prices = pension_expenses(duration, pension_years, living, living_gr)
    
    # Calculate investment values
    values = []
    for d in durations:
        monthly_rev = (1 + annual_rev)**(1/12) - 1
        total = initial_invest * (1 + monthly_rev)**(12*d) + monthly_invest * ((1 + monthly_rev)**(12*d) - 1) / monthly_rev
        invested = initial_invest + monthly_invest*12*d
        post_taxes = 0.75*(total-invested) + invested

        values.append(post_taxes)
    
    # Create DataFrame for plotting
    df = pd.DataFrame({
        'Duration (Years)': durations,
        'House Price': house_prices,
        'Investment Value': values,
        f'Next {pension_years} Years Expenses': coming_living_prices
    })
    
    # Create interactive line plot
    fig = px.line(df, 
                  x='Duration (Years)', 
                  y=['House Price', 'Investment Value',f'Next {pension_years} Years Expenses'],
                  title=f'Price & Investment Growth - House: ${init_price:,.0f} ({expns:.1%}), Investment: ${initial_invest:,.0f} + ${monthly_invest:.0f}/mo ({annual_rev:.1%})')
    
    # Update layout
    fig.update_layout(
        yaxis_title="Amount (ILS)",
        hovermode='x'
    )
    
    return fig


def sizeof_fmt(num, suffix=""):
    if num == None:
        return num
    for unit in ("", "K", "M"):
        if abs(num) < 1000:
            if unit=="":
                return f"{num:3.0f}{unit}{suffix}"
            else:
                return f"{num:3.1f}{unit}{suffix}"
        num /= 1000
    return f"{num:.1f}Yi{suffix}"

def make_pretty(styler):
    cm = sns.light_palette("green", as_cmap=True)
    styler.format(precision=0, thousands=",", decimal=".")
    # styler.format("{:,.2f}".format)
    # styler.format({"count": "{:,.0f}".format,"DurationDelta": "{:,.0f}".format})
    styler.background_gradient(cmap=cm)
    return styler

def make_action_pretty(styler):
    cm = sns.light_palette("green", as_cmap=True)
    styler.format({"priority": "{:,.0f}","allocate [%]": "{:,.1f} %",
                  "current [%]": "{:,.1f} %", "allocation value":"{:,.0f}"})
    styler.background_gradient(cmap=cm)
    return styler

def night_day(ms):
    """ Simplistic option which sometimes work...
    if st.toggle("Dark Mode", value=True) is False:
          st._config.set_option(f'theme.base', "light")
    else:
          st._config.set_option(f'theme.base', "dark")
    if st.button("Refresh"):
          st.rerun()
    """
    if "themes" not in ms: 
        ms.themes = {"current_theme": "light",
                        "refreshed": True,
                        
                        "light": {"theme.base": "dark",
                                #   "theme.backgroundColor": "black",
                                #   "theme.primaryColor": "#c98bdb",
                                #   "theme.secondaryBackgroundColor": "#5591f5",
                                #   "theme.textColor": "white",
                                #   "theme.textColor": "white",
                                "button_face": "🌜"},

                        "dark":  {"theme.base": "light",
                                #   "theme.backgroundColor": "white",
                                #   "theme.primaryColor": "#5591f5",
                                #   "theme.secondaryBackgroundColor": "#82E1D7",
                                #   "theme.textColor": "#0a1464",
                                "button_face": "🌞"},
                        }
    

    def ChangeTheme():
        previous_theme = ms.themes["current_theme"]
        tdict = ms.themes["light"] if ms.themes["current_theme"] == "light" else ms.themes["dark"]
        for vkey, vval in tdict.items(): 
            if vkey.startswith("theme"): st._config.set_option(vkey, vval)

        ms.themes["refreshed"] = False
        if previous_theme == "dark": ms.themes["current_theme"] = "light"
        elif previous_theme == "light": ms.themes["current_theme"] = "dark"


    btn_face = ms.themes["light"]["button_face"] if ms.themes["current_theme"] == "light" else ms.themes["dark"]["button_face"]
    st.button(btn_face, on_click=ChangeTheme)

    if ms.themes["refreshed"] == False:
        ms.themes["refreshed"] = True
        st.rerun()