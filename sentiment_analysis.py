import pandas as pd
import matplotlib.pyplot as plt
from transformers import pipeline
import re
from nltk.corpus import stopwords
import nltk

# Ensure stopwords are downloaded
nltk.download('stopwords')

# Initialize stopwords
stop_words = stopwords.words('english')

# Initialize sentiment analysis model
classifier_sentiment = pipeline("sentiment-analysis")

def extract_emojis(s):
    """
    Extracts emojis from review text using regex.
    """
    expe = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
    return expe.sub(r'', s)  # Removes emojis from the text

def preprocess_data(df):
    """
    Preprocesses the input DataFrame by:
    - Lowercasing the reviews.
    - Extracting emojis from the 'content' column.
    - Removing stopwords.
    Adds the cleaned data to a new 'extracted_emojis' column.
    """
    # Lowercase the reviews
    df['content'] = df['content'].apply(lambda x: x.lower())  # Lowercase all reviews
    
    # Extract emojis
    df['extracted_emojis'] = df['content'].apply(extract_emojis)  # Remove emojis
    
    # Remove stopwords
    df['extracted_emojis'] = df['extracted_emojis'].apply(lambda x: ' '.join([word for word in x.split() if word not in stop_words]))
    
    return df  # Returns the DataFrame with preprocessed data

def analyze_sentiment(df):
    """
    Analyzes sentiment for each review in the 'extracted_emojis' column.
    Assumes the DataFrame has a column named 'extracted_emojis'.
    Adds a new 'sentiment' column with 'POSITIVE' or 'NEGATIVE' labels.
    """
    df['sentiment'] = df['extracted_emojis'].apply(
        lambda x: classifier_sentiment(x)[0]['label'] if isinstance(x, str) else 'UNKNOWN'
    )
    return df  # Returns DataFrame with sentiment column

def visualize_sentiment(df):
    """
    Generates a bar chart of sentiment distribution.
    Assumes that 'sentiment' column exists in the DataFrame.
    """
    sentiment_counts = df['sentiment'].value_counts()  # Count occurrences of each sentiment

    # Plotting the sentiment distribution
    fig, ax = plt.subplots(figsize=(10, 6))
    sentiment_counts.plot(kind='bar', color=['green', 'red', 'blue'], ax=ax)
    
    ax.set_xlabel('Sentiment')
    ax.set_ylabel('Count')
    ax.set_title('Sentiment Distribution')
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    return fig  # Return the figure to be displayed in Streamlit
