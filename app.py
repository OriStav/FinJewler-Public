"""
streamlit run app.py
📉🔗📑🧮🪙
#TODO: consider deletation of redundant methods from stemmed from FinStory
""" 
#%%
import streamlit as st
from st_pages import get_nav_from_toml
from methods.vis_utils import night_day

# Automatically load pages from .streamlit/pages.toml
st.set_page_config(layout="centered",page_title="FinJewler")

with st.sidebar:
    night_day(st.session_state)

nav = get_nav_from_toml(".streamlit/pages.toml")
pg = st.navigation(nav)

# add_page_title(pg)

pg.run()
