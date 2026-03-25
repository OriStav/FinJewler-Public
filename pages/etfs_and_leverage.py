import streamlit as st

st.title("🔜 Coming Soon")

st.markdown("""
## 🚧 Under Development

We're working hard to bring you more amazing features! Here's what's coming next:

### 📑 ETFs and Leverage
- ETF comparison and analysis
- Leveraged investment strategies
- Diversification recommendations

---

**Stay tuned for updates!** 🎉

*This page will be updated as new features become available.*
""")

# Add some visual elements
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Features Planned", "3+", "📈")
    
with col2:
    st.metric("Development Status", "In Progress", "⚡")
    
with col3:
    st.metric("ETA", "Coming Soon", "🎯")

# Add a progress bar for fun
st.progress(0.75)
st.caption("Development Progress: 75% Complete")

st.write("**OS made**, 2024 • Not financial advice")
