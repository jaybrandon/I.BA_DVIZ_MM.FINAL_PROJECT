import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.data_loader import load_dataframe
from src.charts.chart_dance_energy import plot_dance_vs_energy

# --- Page Config ---
st.set_page_config(
    page_title="Anatomy of a Hit Song",
    layout="centered",
    initial_sidebar_state="auto",
)

# --- Load Data ---
@st.cache_data
def load_data():
    return load_dataframe()

# --- Apply Global Style ---
plt.style.use('style/style.mplstyle')

# --- Main App ---
st.title("Anatomy of a Hit Song")
st.markdown("""
Explore what makes a song popular on Spotify by diving into audio features like danceability, energy,
and more. Based on a dataset of over 30,000 tracks.
""")

df = load_data()

# preview
st.header("Data Preview")
st.dataframe(df.head())

# charts
st.header("Danceability vs Energy")
st.pyplot(plot_dance_vs_energy(df))

st.header("More visualizations coming soon... (This is a header)")
st.markdown("This is a markdown")
