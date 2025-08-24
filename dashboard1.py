import streamlit as st
import pandas as pd
import plost

st.title("Sales Data Dashboard")
st.set_page_config(layout="wide", initial_sidebar_state="expanded")

st.sidebar.title("Dashboard")

st.subheader("Heat Map Parameter")
time_hist_color = st.sidebar.selectbox("Color by: ", ('temp_min', "temp_max"))