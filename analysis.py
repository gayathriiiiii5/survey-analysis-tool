import pandas as pd
from sentiment import analyze_sentiment


def process_data(df):
    df.columns = df.columns.str.strip()

    if 'Feedback' in df.columns:
        df['Feedback'] = df['Feedback'].astype(str).str.lower()
        df['Sentiment'] = df['Feedback'].apply(analyze_sentiment)

    return df


def get_summary(df):
    summary = {}

    summary['Average Rating'] = round(df['Rating'].mean(), 2)
    summary['Total Responses'] = len(df)

    sentiment_counts = df['Sentiment'].value_counts()

    summary['Positive'] = sentiment_counts.get('Positive', 0)
    summary['Negative'] = sentiment_counts.get('Negative', 0)
    summary['Neutral'] = sentiment_counts.get('Neutral', 0)

    return summary