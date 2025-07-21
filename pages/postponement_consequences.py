"""
streamlit run app.py
""" 
import streamlit as st
from datetime import datetime
import numpy as np
import plotly.graph_objs as go
import pandas as pd

st.header("🏖️ Investment Postponement Consequences")
choice_0 = st.columns(3)
inflation =  choice_0[0].number_input("Annual Inflation %", value=4, placeholder="Type a number...")/100
inv_growth =  choice_0[1].number_input("Investments Growth %", value=8, placeholder="Type a number...")/100
saving_duration =  choice_0[2].number_input("Saving duration (Years)", value=20,step=1,placeholder="Type a number...")
choice_1 = st.columns(2)
amount_to_postpone =  choice_1[0].number_input("Amount to postpone (₪)", value=10000, placeholder="Type a number...")
time_to_postpone =  choice_1[1].number_input("Time to postpone (Months)", value=1, placeholder="Type a number...")
# adjust = choice_1[2].
adjusted_growth = inv_growth - inflation

potential_investment = amount_to_postpone * (1+adjusted_growth)**saving_duration
postponed_investment = amount_to_postpone * (1+adjusted_growth)**(saving_duration-time_to_postpone/12)
cost_of_postponement = potential_investment - postponed_investment
cost_of_postponement_percent = cost_of_postponement / amount_to_postpone

metric_row = st.columns(3)
metric_row[0].metric("Cost of Postponement",f"{cost_of_postponement:,.0f} ₪",delta_color="inverse",delta = f"({cost_of_postponement_percent:.1%})", help="Difference between potential and postponed investment - in Today's ₪ terms")
metric_row[1].metric("Potential Investment",f"{potential_investment:,.0f} ₪",help="Investment if you invest now - in Today's ₪ terms")
metric_row[2].metric("Postponed Investment",f"{postponed_investment:,.0f} ₪",help="Investment if you postpone - in Today's ₪ terms")
# metric_row[2].metric("",,help="Difference between potential and postponed investment")

# Chart showing cost of postponement vs time
months_range = np.arange(1, 241)  # 1 to 120 months (10 years)
postponed_investments = amount_to_postpone * (1+adjusted_growth)**(saving_duration-months_range/12)
costs = potential_investment - postponed_investments

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=months_range, 
    y=costs,
    mode='lines',
    name='Cost of Postponement',
    line=dict(color='red', width=2)
))
fig.update_layout(
    title='Cost of Postponement vs. Time Delayed',
    xaxis_title='Months Delayed',
    yaxis_title='Cost (₪)',
    hovermode='x unified',
    height=400,
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("* *Values are inflation adjusted*")
st.markdown("* *Assuming funds are held in a money market fund to mitigate inflation's erosive effects while postponed.*")
st.write("**OS made**, 2024") 