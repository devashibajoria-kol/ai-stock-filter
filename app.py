import streamlit as st
import pandas as pd

st.set_page_config(page_title="Indian Stock Universe", layout="wide")

st.title("📊 Indian Stock Universe (Stage 2)")

st.markdown("""
This page confirms that your app is successfully loading **all Indian stocks**
from your uploaded dataset.
""")

@st.cache_data
def load_data():
    return pd.read_csv("stocks.csv")

df = load_data()

st.subheader("✅ Universe Loaded")

st.write(f"Total stocks in universe: **{len(df)}**")

st.dataframe(df.head(50))
