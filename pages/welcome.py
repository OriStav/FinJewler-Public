"""
streamlit run app.py
📉🔗📑🧮🪙
#TODO: consider deletation of redundant methods from stemmed from FinStory
""" 
#%%
import streamlit as st
from datetime import datetime

# Page configuration


# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        transition: transform 0.2s;
    }
    .feature-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
    .coming-soon {
        opacity: 0.7;
        background: #f8f9fa;
    }
    .section-header {
        color: #2c3e50;
        border-bottom: 3px solid #667eea;
        padding-bottom: 0.5rem;
        margin-bottom: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Main header with gradient background
st.markdown("""
<div class="main-header">
    <h1>🪙 FinJeweler</h1>
    <h3>Personal Finance Dashboard</h3>
    <p>Comprehensive financial analysis and management toolbox for informed decision-making</p>
</div>
""", unsafe_allow_html=True)


# Available Tools Section
st.markdown("## 🎯 Available Tools")
st.markdown("Ready-to-use financial analysis tools to help you make informed decisions.")
st.markdown("#### 💼 Personal Finance")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h4>🔭 Long Term Forecast</h4>
        <p>Plan your financial future with advanced forecasting tools and scenario analysis.</p>
    </div>
    """, unsafe_allow_html=True)
    # st.page_link("pages/🔭_Long_Term_Forecast.py", label="Launch Long Term Forecast", use_container_width=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h4>💰 Emergency Fund</h4>
        <p>Calculate and recommended emergency fund and visualize its timeline.</p>
    </div>
    """, unsafe_allow_html=True)
    # st.page_link("pages/💰_Emergency_Fund.py", label="Launch Emergency Fund", use_container_width=True)

with col3:

    st.markdown("""
    <div class="feature-card">
        <h4>🏖️ Postponed Investments</h4>
        <p>Calculate the cost of postponing an investment for a certain period of time.</p>
    </div>
    """, unsafe_allow_html=True)
    # st.page_link("pages/💰_Emergency_Fund.py", label="Launch Emergency Fund", use_container_width=True)

st.markdown("---")

# Investment Analysis Section
st.markdown("#### 📈 Investments Analysis")
st.markdown("Advanced tools for analyzing investment opportunities and market correlations.")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h4>🧮 Correlations</h4>
        <p>Analyze relationships between different financial instruments.</p>
    </div>
    """, unsafe_allow_html=True)
    # st.page_link("pages/🧮 _Correlations.py", label="Launch Correlations", use_container_width=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h4>🏦 Mortgage</h4>
        <p>Estimate the cost/profit of a mortgage and its impact on your financial plan.</p>
    </div>
    """, unsafe_allow_html=True)
    # st.page_link("pages/🏦_Mortgage.py", label="Launch Mortgage", use_container_width=True)

st.markdown("---")

# Coming Soon Section
st.markdown("### 🔜 Coming Soon")
st.markdown("Specialized tools for advanced financial planning and analysis.")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card coming-soon">
        <h4>📊 Historical Analysis</h4>
        <p>Deep dive into historical market data and performance analytics.</p>
        <small>🚧 Coming Soon</small>
    </div>
    """, unsafe_allow_html=True)
    # st.page_link("pages/📊_Historical_Analysis.py", label="Historical Analysis (Coming Soon)", use_container_width=True, disabled=True)


with col2:
    st.markdown("""
    <div class="feature-card coming-soon">
        <h4>📑 ETFs & Leverage</h4>
        <p>ETF comparison and leveraged investment strategies.</p>
        <small>🚧 Coming Soon</small>
    </div>
    """, unsafe_allow_html=True)
    # st.page_link("pages/📑_ETFs_and_Leverage.py", label="ETFs & Leverage (Coming Soon)", use_container_width=True, disabled=True)

with col3:
    st.markdown("""
    <div class="feature-card coming-soon">
        <h4>🪙 Trades Analysis</h4>
        <p>Track trade performance and portfolio optimization tools.</p>
        <small>🚧 Coming Soon</small>
    </div>
    """, unsafe_allow_html=True)
    # st.page_link("pages/🪙_Trades_Analysis.py", label="Trades Analysis (Coming Soon)", use_container_width=True, disabled=True)

st.markdown("---")

# Getting Started Section
st.markdown("### 🚀 Getting Started")
st.markdown("""
1. **Choose a tool** from the sections above that matches your current financial needs
2. **Input your data** using the intuitive forms and calculators
3. **Analyze results** with interactive charts and detailed insights
4. **Make informed decisions** based on comprehensive financial analysis

**💡 Tip**: Start with the Emergency Fund calculator to establish your financial foundation, then explore forecasting tools for long-term planning.
""")

# Footer with current date
st.markdown("---")
st.markdown(f"*Last updated: {datetime.now().strftime('%B %d, %Y')}*")
