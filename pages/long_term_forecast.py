"""
streamlit run app.py
""" 
import streamlit as st
from datetime import datetime
from methods.vis_utils import plot_combined_growth,sizeof_fmt

my_age = 30

# st.set_page_config(layout="wide")

title_row = st.columns([1,5,1])
title_row[1].title("🔭 Long Term Forecast")

# st.subheader("Theoretical Financial Forecast")
st.markdown("**suggested use cases:**")
st.markdown("a. compare buying a house vs. investing\
            \nb. estimate duration to buy a house or retire")
choice = st.columns(4)
age =  choice[0].number_input("Age now", value=my_age,step=1, placeholder="Type a number...")
saving_duration =  choice[1].number_input("Saving duration (Years)", value=64-age,step=1,placeholder="Type a number...")
pension_duration =  choice[2].number_input("Pension Duration (Years)", value=26, placeholder="Type a number...",help="how long you expect to live after retirement")
inv_growth =  choice[3].number_input("Investments Growth %", value=15, placeholder="Type a number...")

with st.expander("Forecast Details"):
    cl = st.columns(3)
    with cl[0]:
        st.subheader("Savings")
        with st.container(border=True,height=40):
            st.write("")
        initial =  st.number_input("Initial Investment", value=300000, placeholder="Type a number...")
        monthly =  st.number_input("Monthly Investment", value=5000,step=1000, placeholder="Type a number...")
        annual_rev =  st.number_input("Estimated Mean Annual Revenue %", value=inv_growth, placeholder="Type a number...")/100
        duration =  st.number_input("Investment duration (Years)", value=saving_duration, placeholder="Type a number...")
        monthly_rev = (1+annual_rev)**(1/12)-1
        invested = initial + monthly*12*duration
        total = initial * (1 +monthly_rev)**(12*duration)+ monthly * ((1 + monthly_rev)**(12*duration) - 1 )/ monthly_rev
        post_taxes = 0.75*(total-invested)+invested
    
    with cl[1]:
        st.subheader("Housing")
        st.link_button("Real-Estate growth","https://www.mako.co.il/news-money/real_estate/Article-1e1141aae341a71027.htm")
        init_price =  st.number_input("Initial House Price", value=8*10**6, placeholder="Type a number...",help="in today's terms")
        expns =  st.number_input("Annual House Price Growth %", value=5, placeholder="Type a number...",help="mean of 2011-2021 data - [14,1,9,8,4,7,4,0,1,3,5]")/100
        house_duration =  st.number_input("House saving duration (Years)", value=saving_duration, placeholder="Type a number...")
        price = init_price* (1 + expns)**house_duration
        # container = st.container(border=True)
        # container.write(" ")
        # container.write(" ")
        # container.write(" ")
        
    
    with cl[2]:
        st.subheader("Expenses")
        st.link_button("Inflation rate","https://www.macrotrends.net/global-metrics/countries/USA/united-states/inflation-rate-cpi")
        init_lvng =  st.number_input("Monthly Expenses", value=10**4, placeholder="Type a number...",help="in today's terms, may include rent if not buying a house")
        lvn_expns =  st.number_input("Annual Expenses Growth %", value=4, placeholder="Type a number...")/100
        lvng_duration =  st.number_input("Duration till retirement (Years)", value=saving_duration, placeholder="Type a number...")
        pension_years =  st.number_input("Pension Duration In Years", value=pension_duration, placeholder="Type a number...",help="how long you expect to live after retirement")
        lvng_price = init_lvng* (1 + lvn_expns)**(lvng_duration+pension_years) - init_lvng* (1 + lvn_expns)**lvng_duration
        spare_years = post_taxes/(lvng_price*12)
        age_spare = spare_years+lvng_duration+my_age
    # st.write("first year is summed but not invested")

with st.expander("Reality at retirement"):
    age_at = saving_duration+age
    st.metric("Age to be",sizeof_fmt(age_at))

    st.subheader("Savings at retirement")
    mt_cols = st.columns(3)
    mt_cols[0].metric("Invested",sizeof_fmt(invested)) 
    mt_cols[1].metric("Total Value",sizeof_fmt(total)) 
    mt_cols[2].metric("Total Value Post Taxes",sizeof_fmt(post_taxes),help="25% tax rate") 
    st.subheader("Price levels at retirement")
    monthly_row = st.columns(3)
    monthly_row[0].metric("House Price",sizeof_fmt(price))
    monthly_row[1].metric("Monthly Expenses",sizeof_fmt(lvng_price))
    monthly_row[2].metric("Age Spare Years",sizeof_fmt(age_spare),help=f"{spare_years:,.0f} years spare at what's currently {init_lvng:,} monthly expenses - inflation adjusted")

fig = plot_combined_growth(init_price=init_price, expns=expns, initial_invest=initial,
                            living=init_lvng, living_gr=lvn_expns, pension_years=pension_years,
                            monthly_invest=monthly, annual_rev=annual_rev, duration=duration+5)
st.plotly_chart(fig)

st.write("**OS made**, 2024")
#%%

