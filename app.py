import streamlit as st
import pandas as pd
import numpy as np

# Assuming you've already done your sentiment analysis and have the following DataFrames:
# Jumia_positive_reviews, Jumia_negative_reviews
# Kilimall_positive_reviews, Kilimall_negative_reviews
# Jiji_positive_reviews, Jiji_negative_reviews

# Displaying the title of the Streamlit app
st.title("Sentiment Analysis of Reviews")
st.markdown("This app shows the sentiment analysis for reviews from Jumia, Kilimall, and Jiji.")

# Option to display top reviews based on platform
platform = st.selectbox("Choose a platform", ["Jumia", "Kilimall", "Jiji"])

# Display the top 10 positive and negative reviews based on the selected platform
if platform == "Jumia":
    st.subheader("Top 10 Positive Reviews from Jumia:")
    st.write(Jumia_positive_reviews[['extracted_emojis', 'sentiment']].head(10))

    st.subheader("Top 10 Negative Reviews from Jumia:")
    st.write(Jumia_negative_reviews[['extracted_emojis', 'sentiment']].head(10))

elif platform == "Kilimall":
    st.subheader("Top 10 Positive Reviews from Kilimall:")
    st.write(Kilimall_positive_reviews[['extracted_emojis', 'sentiment']].head(10))

    st.subheader("Top 10 Negative Reviews from Kilimall:")
    st.write(Kilimall_negative_reviews[['extracted_emojis', 'sentiment']].head(10))

else:  # Jiji platform
    st.subheader("Top 10 Positive Reviews from Jiji:")
    st.write(Jiji_positive_reviews[['extracted_emojis', 'sentiment']].head(10))

    st.subheader("Top 10 Negative Reviews from Jiji:")
    st.write(Jiji_negative_reviews[['extracted_emojis', 'sentiment']].head(10))

# Optionally, you can also show a sample of the entire dataset or statistics
st.subheader("Review Dataset Sample:")
st.write(df.head())  # Display a sample of your full dataset if needed

# Or display summary statistics for sentiment (optional)
st.subheader("Sentiment Summary Statistics:")
sentiment_summary = {
    "Positive Reviews": len(Jumia_positive_reviews),
    "Negative Reviews": len(Jumia_negative_reviews),
    "Total Reviews": len(Jumia_positive_reviews) + len(Jumia_negative_reviews),
}
st.write(sentiment_summary)
