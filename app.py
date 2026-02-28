import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Stock Funnel (India)", layout="wide")
st.title("📊 AI Stock Funnel – India")

@st.cache_data
def load_data():
    return pd.read_csv("stocks.csv")

df = load_data()

st.sidebar.header("📌 Your Filters")

min_roce = st.sidebar.slider("Minimum ROCE (%)", 0, 50, 15)
min_roe = st.sidebar.slider("Minimum ROE (%)", 0, 50, 15)
min_growth = st.sidebar.slider("Minimum Revenue Growth (%)", -50, 50, 8)
max_debt = st.sidebar.slider("Maximum Debt / Equity", 0.0, 3.0, 0.5)

st.subheader("🧩 Funnel Progress")

# Stage 0 – Starting universe
st.write(f"🔹 Starting stocks: {len(df)}")

# Stage 1 – Quality
stage1 = df[
    (df["ROCE"] >= min_roce) &
    (df["ROE"] >= min_roe) &
    (df["REV growth"] >= min_growth)
]
st.write(f"🔹 After quality filter: {len(stage1)}")

# Stage 2 – Balance sheet
stage2 = stage1[
    stage1["DebtEquity"] <= max_debt
]
st.write(f"🔹 After balance sheet filter: {len(stage2)}")

# Stage 3 – Scoring
stage2 = stage2.copy()
stage2["AI_Score"] = (
    stage2["ROCE"] * 0.4 +
    stage2["ROE"] * 0.3 +
    stage2["RevenueGrowth"] * 0.3 -
    stage2["DebtEquity"] * 10
)

final = stage2.sort_values("AI_Score", ascending=False)

st.subheader("✅ Final Shortlist")
st.dataframe(
    final[
        ["Stock", "Industry Group", "ROCE", "ROE", "RevenueGrowth", "DebtEquity", "PE", "AI_Score"]
    ].head(25)
)
