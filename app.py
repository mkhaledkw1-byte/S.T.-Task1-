import streamlit as st
import pandas as pd

st.title("CSV Reader Task")

uploaded_file = st.file_uploader("Upload a csv file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("First 3 Rows:")
    st.dataframe(df.head(3))