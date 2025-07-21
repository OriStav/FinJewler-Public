import streamlit as st
import yfinance as yf
import pandas as pd
from methods.vis_utils import create_correlation_chart

# App title
st.title("Stock Correlation Analysis")

# Two rows, each with two columns for inputs
row1 = st.columns(2)

ticker1 = row1[0].text_input("Enter the first ticker symbol:", "^NDX")
ticker2 = row1[1].text_input("Enter the second ticker symbol:", "ASX.AX")

row2 = st.columns(2)
start_date = row2[0].date_input("Start date:", pd.Timestamp("2020-01-01"), pd.Timestamp("1000-01-01"), pd.Timestamp("3000-01-01"))
end_date = row2[1].date_input("End date:", pd.Timestamp.today(), pd.Timestamp("1000-01-01"), pd.Timestamp("3000-01-01"))

# Fetch data and plot if both tickers are provided
# if st.button("Analyze"):
try:
    # Fetch data using yfinance
    data1 = yf.download(ticker1, start=start_date, end=end_date)['Close']
    data2 = yf.download(ticker2, start=start_date, end=end_date)['Close']

    # Combine data into a single DataFrame
    # Ensure data1 and data2 are pandas Series with proper indices before creating the DataFrame
    df = data1.merge(data2, left_index=True, right_index=True)

    # Calculate overall correlation
    overall_corr = df[ticker1].corr(df[ticker2])

    # Calculate rolling correlation
    window_size = st.slider("Window Size", min_value=1, max_value=365*4, value=100, step=10)
    df['Rolling Correlation'] = df[ticker1].rolling(window=window_size).corr(df[ticker2])
    metric_row = st.columns(2)
    metric_row[0].metric(label="Overall Correlation", value=f"{overall_corr:.2f}")

    normalize = metric_row[1].checkbox("Normalize Chart", value=True)
    if normalize:
        df_view = df.apply(lambda x: x / x.max())
    else:
        df_view = df.copy()
    # Plot both prices and rolling correlation in the same chart

    # Create and display the chart
    fig = create_correlation_chart(df_view, ticker1, ticker2, window_size)
    st.plotly_chart(fig)

except Exception as e:
    st.error(f"An error occurred: {e}")

st.write("**OS made**, 2024") 