import streamlit as st
import pandas as pd

st.set_page_config(page_title="My AI Stock Filter", layout="wide")
st.title("📊 My AI Stock Filter (India)")

st.sidebar.header("Your Preferences")

min_roce = st.sidebar.slider("Minimum ROCE (%)", 5, 30, 15)
min_growth = st.sidebar.slider("Minimum Revenue Growth (%)", 0, 30, 8)
max_debt = st.sidebar.slider("Maximum Debt / Equity", 0.0, 2.0, 0.5)

run = st.sidebar.button("🔍 Run AI Filter")

@st.cache_data
def load_data():
    return pd.read_csv("stocks.csv")

if run:
    df = load_data()

    filtered = df[
        (df["ROCE"] >= min_roce) &
        (df["RevenueGrowth"] >= min_growth) &
        (df["DebtEquity"] <= max_debt)
    ]

    filtered["AI_Score"] = (
        filtered["ROCE"] * 0.4 +
        filtered["RevenueGrowth"] * 0.4 -
        filtered["DebtEquity"] * 10
    )

    filtered = filtered.sort_values("AI_Score", ascending=False)

    st.subheader("✅ Stocks That Match Your Criteria")
    st.dataframe(filtered.head(20))

else:
    st.info("👈 Set your preferences and click Run AI Filter")
