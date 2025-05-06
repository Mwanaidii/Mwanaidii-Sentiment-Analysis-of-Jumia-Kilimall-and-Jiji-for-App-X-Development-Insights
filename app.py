import streamlit as st
from sentiment_analysis import analyze_sentiment, visualize_sentiment, preprocess_data
from scraping import scrape_reviews

# Streamlit Title and Description
st.title("Sentiment Analysis from Emoji Reviews")
st.markdown("Scrape reviews directly from Jumia, Kilimall, or Jiji to view sentiment trends.")

# Platform selection (dropdown)
platform = st.selectbox("Select the platform", ["Jumia", "Kilimall", "Jiji"])

# Option to scrape reviews from the platform
scrape_reviews_option = st.button("Scrape Reviews")

if scrape_reviews_option:
    # Set the platform ID based on the user's choice
    if platform == "Jumia":
        platform_id = "com.jumia.android"
    elif platform == "Kilimall":
        platform_id = "net.kilimall.shop"
    elif platform == "Jiji":
        platform_id = "com.olx.ssa.ke"
    
    # Scrape reviews from the platform
    st.write(f"Scraping reviews from {platform}...")
    df = scrape_reviews(platform_id)

    # Perform preprocessing (extract emojis and clean text)
    df = preprocess_data(df)
    
    # Perform sentiment analysis
    df = analyze_sentiment(df)

    # Display the top 10 positive and negative reviews
    st.subheader(f"Top 10 Positive Reviews for {platform}")
    top_positive_reviews = df[df['sentiment'] == 'POSITIVE'].head(10)

    # Drop unnecessary columns for positive reviews
    top_positive_reviews_cleaned = top_positive_reviews.drop(columns=['reviewId', 'userName', 'userImage', 'thumbsUpCount', 'reviewCreatedVersion', 'at', 'replyContent', 'repliedAt', 'appVersion'])

    # Display cleaned top 10 positive reviews
    st.write(top_positive_reviews_cleaned[['content', 'extracted_emojis', 'sentiment']])

    st.subheader(f"Top 10 Negative Reviews for {platform}")
    top_negative_reviews = df[df['sentiment'] == 'NEGATIVE'].head(10)

    # Drop unnecessary columns for negative reviews
    top_negative_reviews_cleaned = top_negative_reviews.drop(columns=['reviewId', 'userName', 'userImage', 'thumbsUpCount', 'reviewCreatedVersion', 'at', 'replyContent', 'repliedAt', 'appVersion'])

    # Display cleaned top 10 negative reviews
    st.write(top_negative_reviews_cleaned[['content', 'extracted_emojis', 'sentiment']])

    # Visualize sentiment distribution
    st.subheader(f"Sentiment Distribution for {platform}")
    sentiment_plot = visualize_sentiment(df)  # This will return the figure object
    st.pyplot(sentiment_plot)

