import streamlit as st
import pandas as pd
from transformers import pipeline                                                                  
# Initialize sentiment analysis model                                    
classifier_sentiment = pipeline("sentiment-analysis")                  
# Initialize sentiment analysis model
classifier_sentiment = pipeline("sentiment-analysis")

st.title("Sentiment Analysis from Emoji Reviews")
st.markdown("Upload emoji review files for Jumia, Kilimall, or Jiji to view sentiment trends.")

# Platform selector
platform = st.selectbox("Select the platform", ["Jumia", "Kilimall", "Jiji"])

# File uploader
uploaded_file = st.file_uploader(f"Upload your {platform} dataset (CSV)", type="csv")

if uploaded_file:
    try:
        # Read the uploaded CSV
        df = pd.read_csv(uploaded_file)

        # Check for required column
        if "extracted_emojis" not in df.columns:
            st.error("Error: Column 'extracted_emojis' not found in the uploaded CSV.")
        else:
            with st.spinner("Performing sentiment analysis..."):
                df["sentiment"] = df["extracted_emojis"].apply(
                    lambda x: classifier_sentiment(x)[0]["label"] if isinstance(x, str) else "UNKNOWN"
                )

                # Get top 10 positive and negative reviews
                positive_reviews = df[df["sentiment"] == "POSITIVE"].head(10)
                negative_reviews = df[df["sentiment"] == "NEGATIVE"].head(10)

                # Display results
                st.subheader(f"Top 10 Positive Reviews - {platform}")
                st.write(positive_reviews[['extracted_emojis', 'sentiment']])

                st.subheader(f"Top 10 Negative Reviews - {platform}")
                st.write(negative_reviews[['extracted_emojis', 'sentiment']])

    except Exception as e:
        st.error(f"Something went wrong while processing your file: {e}")
else:
    st.info(f"Upload a CSV file for {platform} with a column named 'extracted_emojis'.")

