"""
CRM Sentiment Link Analyzer
--------------------------
Explainable NLP-based CRM Analyzer

Pipeline:
1. Extract text from URL
2. Clean & filter content
3. Sentence-level sentiment analysis
4. Cluster similar opinions
5. Generate positive & negative insights
"""

import streamlit as st
import pandas as pd
import json
from datetime import datetime

from scraper import extract_text_from_url
from sentiment import analyze_sentiment


# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="CRM Sentiment Analyzer",
    page_icon="📊",
    layout="wide"
)

st.title("CRM Sentiment Link Analyzer")
# st.caption("Dynamic CRM Insight Generator (Explainable NLP Pipeline)")


# -----------------------------
# HISTORY STORAGE
# -----------------------------

HISTORY_FILE = "history.json"


def load_history():
    try:
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    except:
        return []


def save_history(data):
    with open(HISTORY_FILE, "w") as f:
        json.dump(data, f, indent=4)


history = load_history()


# -----------------------------
# TABS
# -----------------------------

tab1, tab2, tab3 = st.tabs(["📊 Overview", "🔍 Analyzer", "📁 History"])


# ===================================================
# TAB 1 — OVERVIEW
# ===================================================

with tab1:

    st.subheader("Project Overview")

    if history:

        df = pd.DataFrame(history)

        total = len(df)
        positive = len(df[df["sentiment"] == "POSITIVE"])
        negative = len(df[df["sentiment"] == "NEGATIVE"])

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Links", total)
        col2.metric("Positive", positive)
        col3.metric("Negative", negative)

        st.markdown("---")

        st.subheader("Recent Analysis")
        st.dataframe(df.tail(5), use_container_width=True)

    else:
        st.info("No data available. Analyze a link first.")


# ===================================================
# TAB 2 — ANALYZER
# ===================================================
with tab2:

    st.subheader("Analyze Website")

    url = st.text_input("Enter URL")

    if st.button("Analyze "):

        if not url:
            st.warning("Please enter a URL")
        else:

            with st.spinner("Extracting content..."):
                text = extract_text_from_url(url)

            # ✅ FIX 1: Always analyze (even fallback)
            if not text:
                st.warning("Limited content found, generating insights from available data...")
                text = url  # fallback input

            # ✅ ALWAYS RUN ANALYSIS
            with st.spinner("Analyzing sentiment and generating insights..."):
                result = analyze_sentiment(text)

            st.success("Analysis Completed")

            # -----------------------------
            # SENTIMENT SCORE
            # -----------------------------
            col1, col2 = st.columns(2)

            col1.metric("Overall Sentiment", result["label"])
            col2.metric("Confidence", result["score"])

            st.markdown("---")

            # -----------------------------
            # SIDE-BY-SIDE OUTPUT
            # -----------------------------
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Positive Dimensions")
                for item in result["positive_dimensions"]:
                    st.markdown(f"- {item}")

            with col2:
                st.subheader("Negative Dimensions")
                for item in result["negative_dimensions"]:
                    st.markdown(f"- {item}")

            # -----------------------------
            # SAVE HISTORY
            # -----------------------------
            record = {
                "url": url,
                "sentiment": result["label"],
                "confidence": result["score"],
                "time": str(datetime.now())
            }

            history.append(record)
            save_history(history)

            st.info("Saved to history")
# ===================================================
# TAB 3 — HISTORY
# ===================================================

with tab3:

    st.subheader("Analysis History")

    if history:

        df = pd.DataFrame(history)

        st.dataframe(df, use_container_width=True)

    else:
        st.info("No history available")