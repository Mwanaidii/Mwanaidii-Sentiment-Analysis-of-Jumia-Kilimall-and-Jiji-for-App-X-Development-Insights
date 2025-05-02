import streamlit as st

st.title("Sentiment Analysis Dashboard")
st.write("This is a simple Streamlit app showing customer sentiment analysis for Jumia, Kilimall, and Jiji.")

# Load and display your results
import pandas as pd

df = pd.read_csv("your_file.csv")  # Replace with your actual file
st.dataframe(df)

# Sentiment distribution
st.bar_chart(df['sentiment'].value_counts())
