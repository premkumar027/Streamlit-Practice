import streamlit as st
import pandas as pd

st.title("Data Display Example")

file = st.file_uploader("Upload a CSV file", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)

if file:
    st.subheader("Statistical Summary")
    st.write(df.describe())

if file:
    cgpa = df['cgpa'] > 7.0
    st.subheader("CGPA > 7.0")
    st.write(df[cgpa])