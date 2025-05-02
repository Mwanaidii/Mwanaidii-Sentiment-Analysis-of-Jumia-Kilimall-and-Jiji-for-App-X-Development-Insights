import streamlit as st
import pandas as pd

# Load data
try:
    Jumia_positive_reviews = pd.read_csv("path_to_jumia_positive_reviews.csv")
    Jumia_negative_reviews = pd.read_csv("path_to_jumia_negative_reviews.csv")
except Exception as e:
    st.error(f"Failed to load data: {e}")
    st.stop()

# Sanitize column names
Jumia_positive_reviews.columns = Jumia_positive_reviews.columns.str.strip()
Jumia_negative_reviews.columns = Jumia_negative_reviews.columns.str.strip()

# Show available columns (debug)
st.write("Jumia Positive Review Columns:", Jumia_positive_reviews.columns.tolist())

# Display data
st.subheader("Top 10 Positive Reviews from Jumia")
try:
    st.write(Jumia_positive_reviews[['extracted_emojis', 'sentiment']].head(10))
except KeyError as e:
    st.error(f"Missing expected columns: {e}")
