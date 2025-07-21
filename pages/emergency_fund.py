"""
streamlit run app.py
""" 
import streamlit as st
from datetime import datetime
import numpy as np
import plotly.graph_objs as go
import pandas as pd

my_age = 30

# st.set_page_config(layout="centered")

st.markdown("<h1 style='text-align: center;'>🛟 Emergency Fund 💰</h1>", unsafe_allow_html=True)
input_row = st.columns([1,1])

monthly_salary = input_row[0].number_input("Monthly Salary", value=10000,step=1000, placeholder="Type a number...")
age =  input_row[1].number_input("Age", value=my_age, step=1, placeholder="Type a number...")
cols = st.columns([1,2])
cols[0].container(height=150,border=False)
cols[0].metric("↓ Current Value ↓",f"{monthly_salary*(age-25)/3:,.0f} ₪") 

ages = np.arange(28, 71)
emergency_funds = [monthly_salary * (a - 25) / 3 for a in ages]
emergency_funds_df = pd.DataFrame({'Age': ages, 'Emergency Fund': emergency_funds})

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=emergency_funds_df['Age'],
    y=emergency_funds_df['Emergency Fund'],
    mode='lines+markers',
    name='Emergency Fund'
))
fig.update_layout(
    title="Recommended Emergency Fund by Age",
    xaxis_title="Age",
    yaxis_title="Emergency Fund (ILS)",
    template="plotly_white"
)
cols[1].plotly_chart(fig, use_container_width=True)
st.markdown(r"""
**Emergency Fund Formula:**  
$$
\text{Emergency Fund} = 3 \times \text{Monthly Salary} \times (\text{Age} - 25)
$$
""")
link_row = st.columns([1,1])
link_row[0].link_button(icon="🧮",label="Formula Recommendation",url="https://www.calcalist.co.il/money/articles/0,7340,L-3641283,00.html",use_container_width=True) 
link_row[1].link_button(icon="🏦",label="Best kept at Money market funds",url="https://www.funder.co.il/kaspit",use_container_width=True) 

st.write("**OS made**, 2024") 
