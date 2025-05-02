import streamlit as st
import pandas as pd

# Load CSVs
try:
    Jumia_positive_reviews = pd.read_csv("jumia_positive_reviews.csv")
    Jumia_negative_reviews = pd.read_csv("jumia_negative_reviews.csv")
    Kilimall_positive_reviews = pd.read_csv("kilimall_positive_reviews.csv")
    Kilimall_negative_reviews = pd.read_csv("kilimall_negative_reviews.csv")
    Jiji_positive_reviews = pd.read_csv("jiji_positive_reviews.csv")
    Jiji_negative_reviews = pd.read_csv("jiji_negative_reviews.csv")
except Exception as e:
    st.error(f"Failed to load one or more datasets: {e}")
    st.stop()

# Clean column names in case of spaces
for df in [Jumia_positive_reviews, Jumia_negative_reviews,
           Kilimall_positive_reviews, Kilimall_negative_reviews,
           Jiji_positive_reviews, Jiji_negative_reviews]:
    df.columns = df.columns.str.strip()

# Streamlit UI
st.title("Sentiment Insights from Jumia, Kilimall & Jiji Reviews")
platform = st.selectbox("Choose a platform to view reviews", ["Jumia", "Kilimall", "Jiji"])

def show_reviews(positive_df, negative_df):
    st.subheader("Top 10 Positive Reviews")
    try:
        st.write(positive_df[['extracted_emojis', 'sentiment']].head(10))
    except KeyError:
        st.error("Missing 'extracted_emojis' or 'sentiment' columns in positive reviews CSV.")

    st.subheader("Top 10 Negative Reviews")
    try:
        st.write(negative_df[['extracted_emojis', 'sentiment']].head(10))
    except KeyError:
        st.error("Missing 'extracted_emojis' or 'sentiment' columns in negative reviews CSV.")

# Show based on selection
if platform == "Jumia":
    show_reviews(Jumia_positive_reviews, Jumia_negative_reviews)
elif platform == "Kilimall":
