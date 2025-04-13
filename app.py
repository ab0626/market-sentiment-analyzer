# app.py

import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="Market Sentiment Analyzer", layout="wide")

# ---- Sidebar ----
st.sidebar.title("📈 Market Sentiment Analyzer")
ticker = st.sidebar.text_input("Enter Stock Ticker (e.g. AAPL)", "AAPL")
start_date = st.sidebar.date_input("Start Date", datetime.now() - timedelta(days=7))
end_date = st.sidebar.date_input("End Date", datetime.now())

# ---- Main Content ----
st.title("🔍 Sentiment Analysis Dashboard")
st.write(f"Analyzing sentiment for **{ticker.upper()}** from **{start_date}** to **{end_date}**")

st.info("Data loading and sentiment analysis will show up here once implemented.")

# Placeholder columns for graphs and visuals
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Sentiment Over Time")
    st.empty()

with col2:
    st.subheader("☁️ Word Cloud")
    st.empty()
