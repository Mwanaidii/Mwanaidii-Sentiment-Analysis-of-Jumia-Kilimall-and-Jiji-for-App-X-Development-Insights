import streamlit as st
import pandas as pd
import plotly.express as px

# Load your cleaned sentiment output
df = pd.read_csv("cleaned_reviews.csv")  # update with your real file

# App title
st.title("Sentiment Analysis Dashboard - App X Insights")

# Sentiment distribution
sentiment_counts = df["sentiment"].value_counts()
fig = px.pie(names=sentiment_counts.index, values=sentiment_counts.values, title="Sentiment Distribution")
st.plotly_chart(fig)

# Display sample reviews
st.subheader("Sample Reviews")
st.dataframe(df[['review', 'sentiment']].sample(5))
