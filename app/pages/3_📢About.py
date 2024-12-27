import streamlit as st
st.set_page_config(page_title="About", page_icon="📢", layout="wide")

st.title("📢 About")

st.markdown("""
# Bitcoin Sentiment and Price Analysis App

This Streamlit app analyzes the relationship between social media sentiment and Bitcoin prices. It provides visualizations to help users understand how sentiment might influence Bitcoin's market behavior.

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
""")
