import streamlit as st
import pandas as pd

st.set_page_config(page_title="Crypto News", page_icon="📰", layout="wide")

st.image("app/bitcoin.jpg", use_container_width=True)

st.title("📰 Crypto News")

@st.cache_data
def get_news_data():
    news = pd.read_csv('app/cryptonews.csv')
    news['date'] = pd.to_datetime(news['date'], format='mixed')
    return news

news = get_news_data()

news_min_date = news['date'].min()
news_max_date = news['date'].max()

news_date_range = st.date_input(
    "Choose news date range",
    [news_min_date, news_max_date],
    min_value=news_min_date,
    max_value=news_max_date,
    format="YYYY-MM-DD"
)

if isinstance(news_date_range, tuple) and len(news_date_range) == 2:
    news_start_date, news_end_date = news_date_range

    news_start_date = pd.to_datetime(news_start_date)
    news_end_date = pd.to_datetime(news_end_date)

    filtered_news = news[(news['date'] >= news_start_date) & (news['date'] <= news_end_date)]

    subjects = filtered_news['subject'].unique()
    selected_subjects = st.multiselect('Select subjects:', subjects, default=subjects)

    final_filtered_news = filtered_news[filtered_news['subject'].isin(selected_subjects)]
    final_filtered_news['sentiment'] = final_filtered_news['sentiment'].apply(lambda x: x['class'])
    # Display the news in a table
    st.dataframe(final_filtered_news[['date','sentiment','subject','text']],use_container_width=True)

else:
    st.error("Please select a valid date range.")
