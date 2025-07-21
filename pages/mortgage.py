"""
Leverage mortgage into % Price growth -  so, First apt. up to 75% funded - 4x leverage
"""
import streamlit as st
import numpy as np
import pandas as pd

st.title("🏦 Mortgage")
st.markdown(":red-background[**demo**]")
cols = st.columns(3)
with cols[0]:
    init_payment =  st.number_input("Initial Payment", value=300000, placeholder="Type a number...",help="")
    mortgage_rate =  st.number_input("Mortgage Rate %", value=2.5, placeholder="Type a number...",help="% rate per year")/100
    mortgage_coverage =  st.number_input("Mortgage %", value=75, placeholder="Type a number...",help="% funded by mortgage")/100
    mortgage_duration =  st.number_input("Mortgage Duration (Years)", value=25, placeholder="Type a number...",help="duration of the mortgage")
    monthly_rental =  st.number_input("Estimated Mean Monthly Rental", value=2000,step=500, placeholder="Type a number...",help="in today's terms - adjusted for 4% inflation")
    growth_rate =  st.number_input("Estimated Annual House Price Growth %", value=5, placeholder="Type a number...",help="mean of 2011-2021 data - [14,1,9,8,4,7,4,0,1,3,5]")/100

house_price = init_payment/(1-mortgage_coverage)
mortgage_size = house_price*mortgage_coverage
mortgage_price = mortgage_size*(1+mortgage_rate)**mortgage_duration - mortgage_size
total_invested = mortgage_price + house_price
house_price_growth = house_price*(1+growth_rate)**mortgage_duration
monthly_payment = (mortgage_price+mortgage_size)/(mortgage_duration*12)
# Calculate rental income with 4% annual inflation adjustment
inflation_rate = 0.04

# Create monthly data
mortgage_df = pd.DataFrame(index=range(1, mortgage_duration * 12 + 1))
mortgage_df.index.name = 'payment_month'
# mortgage_df["accumulated_investment"] = mortgage_df["investment"] + (monthly_payment * mortgage_df.index)
mortgage_df["duration"] = mortgage_duration - mortgage_df.index/12 # years invested
mortgage_df["years_passed"] = np.floor(mortgage_df.index / 12)
yp = mortgage_df.index / 12
mortgage_df["rental_income"] = monthly_rental*((1 + inflation_rate) ** mortgage_df["years_passed"])# - 1)/ inflation_rate
mortgage_df["house_price"] = house_price*((1 + growth_rate) ** yp)# - 1)/ inflation_rate
if st.checkbox("Reduce rental income to monthly payment",value=True):
    mortgage_df["investment"] =monthly_payment - mortgage_df["rental_income"]
else:
    mortgage_df["investment"] =monthly_payment
mortgage_df.loc[1,"investment"] =init_payment
mortgage_df["mortgage_value"] = mortgage_size + mortgage_price - monthly_payment*mortgage_df.index
mortgage_df["accumulated_investment"] = mortgage_df["investment"].cumsum()
mortgage_df["owned_house_value"] = mortgage_df["house_price"] - mortgage_df["mortgage_value"]
mortgage_df["%_revenue"] = 100*(mortgage_df["owned_house_value"]-mortgage_df["accumulated_investment"]) / mortgage_df["accumulated_investment"]
mortgage_df["%_annualized_revenue"] = np.where(mortgage_df["%_revenue"] > -100, 
                                               ((1+(mortgage_df["%_revenue"]/100))**(1/yp)-1)*100, 
                                               None)
mortgage_df["weighted_duration"] = mortgage_df['duration']*mortgage_df['investment']/mortgage_df['investment'].sum()
# mortgage_df["return_rate"] = (house_price_growth+rental_income-mortgage_df["investment"])/mortgage_df["investment"]

rental_income = mortgage_df["rental_income"].sum()
return_rate = (house_price_growth+rental_income-total_invested)/total_invested
annualized_return_rate = ((1+return_rate)**(1/mortgage_duration)-1)*100

st.subheader("Monthly Mortgage Analysis")
st.dataframe(mortgage_df, use_container_width=True)
weighted_duration = mortgage_df["weighted_duration"].sum()
st.metric("Weighted Duration", value=f"{weighted_duration:,.1f} years", 
          help="Average duration weighted by investment amount over time")

annualized_return_rate_weighted = ((1+return_rate)**(1/weighted_duration)-1)*100

with cols[1]:
    st.metric("House Price", value=f"{house_price:,.0f}₪",help="Total cost of the house")
    st.metric("Leverage", value=f"{1/(1-mortgage_coverage):,.1f}",help="Leverage of the mortgage")
    st.metric("Mortgage Size", value=f"{mortgage_size:,.0f}₪",help="Total amount of money borrowed")
    st.metric("Mortgage Price", value=f"{mortgage_price:,.0f}₪",help="Total cost of the mortgage")
    st.metric("Total Invested", value=f"{total_invested:,.0f}₪",help="Total amount of money invested")
    st.metric("Monthly Payment", value=f"{monthly_payment:,.0f}₪",help="Monthly payment of the mortgage")
with cols[2]:
    st.metric("Expected House Value", value=f"{house_price_growth:,.0f}₪")
    st.metric("Total Rental Income", value=f"{rental_income:,.0f}₪")
    st.metric("Expected Profit", value=f"{house_price_growth+rental_income-total_invested:,.0f}₪")
    st.metric("Expected Return %", value=f"{return_rate*100:,.1f} %")
    st.metric("Expected Annualized Return %", value=f"{annualized_return_rate:,.1f} %")
    st.metric("Weighted Expected Annualized Return %", value=f"{annualized_return_rate_weighted:,.1f} %")

down_cols = st.columns(2)
down_cols[0].link_button("🧮 Simple Mortgage Evaluator", "https://www.mizrahi-tefahot.co.il/mortgages/calculator/")
down_cols[1].link_button("⚖️ Mortgage Rate Explorer", "https://www.moti.org.il/interest/main/")

# house_duration =  st.number_input("H  ouse saving duration (Years)", value=saving_duration, placeholder="Type a number...")
# price = init_price* (1 + expns)**house_duration