import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

st.set_page_config(page_title="Analysis", page_icon="📈", layout="wide")

# st.image("app/bitcoin.jpg", use_container_width=True)
st.title("Social Media Sentiment and Bitcoin Price Relationship Analysis")
st.warning(":warning: This analysis is for practice purposes only, does not guarantee complete accuracy of the data, and does not constitute any investment advice.")

datasets = {
    'VADER Sentiment Analysis': 'https://drive.google.com/uc?id=1_ZbmKv33FM_au2em5f4FfCcC3LhM2ByJ',
    'TextBlob Sentiment Analysis': 'https://drive.google.com/uc?id=1pG4TRDcBzgFj1NwP4a4Jp5P4G1ysmTOk'
}

@st.cache_data
def get_data(file_url):
    # 加載 CSV 文件直接從 URL
    return pd.read_csv(file_url)

# 使用選項選擇數據集
dataset_option = st.selectbox('Select Analysis Model', list(datasets.keys()))
selected_file = datasets[dataset_option]

# 加載所選數據集
df = get_data(selected_file)
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d', errors='coerce')

min_date = df['date'].min()
max_date = df['date'].max()

date_range = st.date_input(
    "Choose date range",
    [min_date, max_date],
    min_value=min_date,
    max_value=max_date,
    format="YYYY-MM-DD"
)

if isinstance(date_range, tuple) and len(date_range) == 2:
    start_date, end_date = date_range
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    filtered_data = df[(df['date'] >= start_date) & (df['date'] <= end_date)]

    if filtered_data.empty:
        st.error("No data in selected date range.")
    else:
        # 篩選並抽樣資料
        sampled_data = filtered_data.iloc[::10, :]  # 每10天取一個資料點

        st.subheader("Sentiment Distribution")
        st.info("🤔 Hypothesis: Due to significant short-term fluctuations, positive and negative sentiments should be roughly balanced.")
        st.write('Data Visualization Types: Use an area chart to visualize the change in Bitcoin discussion volume and the proportion of each sentiment category.')
        st.write('Effectiveness Principle: Use hue to differentiate sentiment categories, with area representing the quantity of each sentiment category.')

        sentiment_counts = sampled_data.groupby(['date', 'sentiment']).size().reset_index(name='count')
        total_counts = sentiment_counts.groupby('date')['count'].transform('sum')
        sentiment_counts['proportion'] = sentiment_counts['count'] / total_counts

        color_scale = alt.Scale(
            domain=['positive', 'negative', 'neutral'],
            range=['#A7C957', '#BC4749', '#F2E8CF']
        )
        chart = alt.Chart(sentiment_counts).mark_area(opacity=0.8).encode(
            x='date:T',
            y=alt.Y('proportion:Q', title='Proportion'),
            color=alt.Color('sentiment:N', scale=color_scale),
            tooltip=['date:T', 'sentiment:N', 'count:Q', 'proportion:Q']
        ).properties(
            width=600,
            height=400
        )

        st.altair_chart(chart, use_container_width=True)

        st.success("🧐In fact, the positive and neutral sentiment significantly outweighs the negative sentiment. It might be because those who keep their eyes on Bitcoin are investing to some extent, which means they believe in the value of Bitcoin. Hence, there are more positive comments about it.")

        # 計算每日情緒與比特幣價格的關聯
        daily_sentiment = sampled_data.groupby('date')['sentiment_score'].mean().reset_index()
        daily_price = sampled_data.groupby('date')['Close'].mean().reset_index()
        daily_data = daily_price.merge(daily_sentiment, on='date')

        st.divider()
        st.subheader('Bitcoin Price vs. Daily Average Sentiment Score')
        st.info("🤔 Hypothesis: Social media sentiment can influence crowd psychology, which may affect Bitcoin prices. This is because people are susceptible to the bandwagon effect, leading them to make investment decisions based on fluctuations in social media sentiment.")
        st.write('Data Visualization Types: Use a scatter plot to visualize the relationship between the daily average sentiment score and the bitcoin price of the day.')
        st.write('Effectiveness Principle: Use tick positions to show the relationship between two variables.')
        fig = px.scatter(
            daily_data, 
            x='Close', 
            y='sentiment_score',
            hover_data={'date': True},
            labels={'Close': 'Bitcoin Price', 'sentiment_score': 'Average Sentiment Score'}
        )

        st.plotly_chart(fig)
        st.success("🧐The relationship between the bitcoin price and sentiment score in the same time period seems positively correlated, and they should have a mutual influence on each other.")

        st.divider()
        st.subheader("Bitcoin Price vs. Trading Volume")
        st.write('Data Visualization Types: Combine a line chart to provide an overview of Bitcoin prices/trading volume.')
        st.write('Effectiveness Principle: Use tick positions to show the Bitcoin prices/trading volume.')
        st.write('Sentiment Score: -1.0 (negative) ~ 1.0 (positive)') 

        price_line = alt.Chart(sampled_data).mark_line(size=5, color='#FFB703').encode(
            x='date:T',
            y=alt.Y('Close:Q', title='Bitcoin Price'),
            tooltip=['date:T', 'Close:Q']
        )

        volume_line = alt.Chart(sampled_data).mark_line(size=5, color='#A3B18A').encode(
            x='date:T',
            y=alt.Y('Volume:Q', title='Bitcoin Trading Volume'),
            tooltip=['date:T', 'Volume:Q']
        )

        combined_chart = alt.layer(price_line, volume_line).resolve_scale(
            y='independent'
        ).properties(
            width=600,  
            height=400
        )

        st.altair_chart(combined_chart, use_container_width=True)

        st.success("🧐The chart shows that the Bitcoin market, like other investment markets, has buy-low, sell-high patterns. However, Bitcoin's price swings are quite large. When influential players, like exchanges, experience big changes, it can cause the market to fluctuate wildly, heavily impacting social media sentiment and the price of Bitcoin.")
else:
    st.error("Please select a valid date range.")
