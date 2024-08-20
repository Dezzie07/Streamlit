import streamlit as st
import pandas as pd

st.title("Simple Data App")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Here is the data you uploaded:")
    st.dataframe(df)

    st.write("Summary statistics:")
    st.write(df.describe())

    st.write("Line chart:")
    st.line_chart(df)
