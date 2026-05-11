# -----------------------------
# 📦 IMPORT LIBRARIES
# -----------------------------
import streamlit as st
import requests
import feedparser
import pandas as pd
from datetime import datetime
import re
import socket

from sklearn.feature_extraction.text import (
    ENGLISH_STOP_WORDS,
    TfidfVectorizer
)

from sklearn.cluster import KMeans

import matplotlib.pyplot as plt


# -----------------------------
# 🔹 PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="News NLP Analyzer",
    layout="wide"
)

st.title("📰 News Topic Discovery + Trend Analyzer")


# -----------------------------
# 🔹 SIDEBAR SETTINGS
# -----------------------------
st.sidebar.header("Settings")

num_topics = st.sidebar.slider(
    "Number of Topics",
    2,
    10,
    5
)

selected_sources = st.sidebar.multiselect(
    "Select News Sources",
    ["BBC", "The Hindu"],
    default=["BBC", "The Hindu"]
)


# -----------------------------
# 🔹 RSS FEEDS
# -----------------------------
FEEDS = {
    "BBC": "http://feeds.bbci.co.uk/news/rss.xml",
    "The Hindu": "https://www.thehindu.com/news/national/feeder/default.rss"
}


# -----------------------------
# 🔹 CHECK INTERNET CONNECTION
# -----------------------------
def internet_available():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except:
        return False


# -----------------------------
# 🔹 FETCH RSS FUNCTION
# -----------------------------
def fetch_rss(url):

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        return feedparser.parse(response.content)

    except requests.exceptions.RequestException as e:

        st.error(f"RSS Fetch Error:\n{e}")

        return feedparser.parse("")


# -----------------------------
# 🔹 FETCH NEWS ARTICLES
# -----------------------------
def fetch_news():

    articles = []

    for source in selected_sources:

        feed = fetch_rss(FEEDS[source])

        # Skip source if no entries found
        if not feed.entries:
            st.warning(f"No articles fetched from {source}")
            continue

        # Fetch first 20 articles
        for entry in feed.entries[:20]:

            title = entry.get("title", "")
            summary = entry.get("summary", "")

            text = title + " " + summary

            articles.append({
                "source": source,
                "text": text,
                "date": datetime.now()
            })

    return pd.DataFrame(articles)


# -----------------------------
# 🔹 NLP PREPROCESSING
# -----------------------------
stop_words = set(ENGLISH_STOP_WORDS)


def clean_text(text):

    # Lowercase
    text = text.lower()

    # Remove special characters
    text = re.sub(r'[^a-z\s]', '', text)

    # Tokenize
    words = text.split()

    # Remove stopwords
    words = [w for w in words if w not in stop_words]

    return " ".join(words)


# -----------------------------
# 🔹 RUN ANALYSIS BUTTON
# -----------------------------
if st.button("🚀 Run Analysis"):

    # Check internet first
    if not internet_available():

        st.error("❌ No Internet Connection!")

    else:

        # -----------------------------
        # 🔹 FETCH DATA
        # -----------------------------
        with st.spinner("Fetching news articles..."):

            df = fetch_news()

        # -----------------------------
        # 🔹 HANDLE EMPTY DATA
        # -----------------------------
        if df.empty:

            st.error("❌ No data fetched!")

        else:

            st.success(f"✅ Fetched {len(df)} articles")

            # -----------------------------
            # 🔹 CLEAN TEXT
            # -----------------------------
            df["clean_text"] = df["text"].apply(clean_text)

            # -----------------------------
            # 🔹 TF-IDF VECTORIZATION
            # -----------------------------
            vectorizer = TfidfVectorizer(
                max_features=1000
            )

            X = vectorizer.fit_transform(
                df["clean_text"]
            )

            # -----------------------------
            # 🔹 KMEANS TOPIC MODELING
            # -----------------------------
            model = KMeans(
                n_clusters=num_topics,
                random_state=42,
                n_init=10
            )

            df["topic"] = model.fit_predict(X)

            # -----------------------------
            # 🔹 DISPLAY TOPICS
            # -----------------------------
            st.subheader("📌 Topics Discovered")

            terms = vectorizer.get_feature_names_out()

            for i in range(num_topics):

                center = model.cluster_centers_[i]

                words = [
                    terms[j]
                    for j in center.argsort()[-6:][::-1]
                ]

                st.write(
                    f"### Topic {i}"
                )

                st.write(
                    ", ".join(words)
                )

            # -----------------------------
            # 🔹 TOPIC DISTRIBUTION GRAPH
            # -----------------------------
            st.subheader("📊 Topic Distribution")

            fig, ax = plt.subplots()

            df["topic"].value_counts().sort_index().plot(
                kind="bar",
                ax=ax
            )

            ax.set_xlabel("Topic")
            ax.set_ylabel("Number of Articles")
            ax.set_title("Topic Frequency")

            st.pyplot(fig)

            # -----------------------------
            # 🔹 ARTICLES TABLE
            # -----------------------------
            st.subheader("📄 Articles")

            st.dataframe(
                df[[
                    "source",
                    "topic",
                    "text"
                ]]
            )

            # -----------------------------
            # 🔹 DOWNLOAD CSV
            # -----------------------------
            csv = df.to_csv(index=False)

            st.download_button(
                label="⬇ Download Results CSV",
                data=csv,
                file_name="news_topics.csv",
                mime="text/csv"
            )