![Bitcoin Analysis](app/bitcoin.jpg)

# Bitcoin Sentiment and Price Analysis App

This Streamlit app analyzes the relationship between social media sentiment and Bitcoin prices. It provides visualizations to help users understand how sentiment might influence Bitcoin's market behavior.

## Features

- **Image and Title**: Displays a header image and the title of the app.
- **Data Selection**: Users can choose between two sentiment analysis models: VADER and TextBlob.
- **Date Range Selection**: Users can select a date range to filter the data.
- **Sentiment Distribution**: Visualizes the proportion of positive, negative, and neutral sentiments over time using an area chart.
- **Bitcoin Price vs. Sentiment Score**: Displays a scatter plot to show the relationship between daily average sentiment scores and Bitcoin prices.
- **Bitcoin Price vs. Trading Volume**: Combines line charts to present Bitcoin prices and trading volumes over time.
- **Crypto News**: Lists related news articles within the selected date range, with a subject filter for more precise insights.

## Hypotheses

1. **Sentiment Balance**: Positive and neutral sentiments are expected to outweigh negative sentiments due to investors' belief in Bitcoin.
2. **Sentiment Influence**: Social media sentiment may affect Bitcoin prices as people often follow trends influenced by the bandwagon effect.
3. **Market Patterns**: The Bitcoin market exhibits buy-low, sell-high patterns, with significant price swings influenced by major market players.

## Data Sources

1. [Bitcoin Tweets](https://www.kaggle.com/datasets/kaushiksuresh147/bitcoin-tweets)
2. [Bitcoin Price (2014-2023)](https://www.kaggle.com/datasets/arslanr369/bitcoin-price-2014-2023)
3. [Crypto News +](https://www.kaggle.com/datasets/oliviervha/crypto-news)

## Usage

1. Clone the repository.
2. Install the required packages.
3. Run the app using Streamlit.
4. Interact with the app by selecting data models, date ranges, and viewing the visualizations.

## Author and Copyright

Author: ChiaChi Hsu  
© 2024 All Rights Reserved

**Disclaimer**: This analysis is for practice purposes only, does not guarantee complete accuracy of the data, and does not constitute any investment advice.
