from google_play_scraper import Sort, reviews
import pandas as pd

def scrape_reviews(platform_id, count=1000):
    """
    Scrapes reviews from Google Play Store using google_play_scraper.
    platform_id: the app's identifier (e.g., 'com.jumia.android')
    count: number of reviews to fetch
    """
    reviews_data, continuation_token = reviews(
        platform_id,
        sort=Sort.MOST_RELEVANT,  # Sort by most relevant
        count=count,
        filter_score_with=None  # Fetch all reviews, not just specific scores
    )
    
    # Convert the reviews to a pandas DataFrame
    reviews_df = pd.DataFrame(reviews_data)
    
    return reviews_df
