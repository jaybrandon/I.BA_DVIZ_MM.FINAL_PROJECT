import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.data_loader import load_dataframe, get_hit_threshold
from src.charts.chart_dance_energy import plot_dance_vs_energy
from src.charts.chart_genres import plot_top_genres
from src.charts.chart_popularity import plot_popularity_distribution
from src.charts.chart_general_corr import plot_general_corr
from src.charts.chart_genre_corr import plot_genre_corr
from src.style.style import apply_theme

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

apply_theme()

# --- Load Data ---

df = load_data()

# --- Main App ---
st.title("Anatomy of a Hit Song: Can Audio Features Predict Popularity")

st.header("Why do some songs go viral?")

st.markdown("""
            Spotify has millions of songs but only few of them are truly successful.
            Is it all marketing and luck or does the sound of a song make a difference? In this project we explore the sound
            signature of around 26'000 songs on spotify to answer this question.
""")

st.markdown("""
            The dataset comes from [Tidy Tuesday](https://github.com/rfordatascience/tidytuesday/tree/main/data/2020/2020-01-21)
            and was originaly made using Spotify's API. The dataset is from 2020-01 so it only contains songs available at that time.
            While trends in music may evolve, the goal of this project is to understand the general characteristics that made songs popular at that time.
""")

# --- Charts ---
st.header("What is popularity on spotify?")
st.markdown("""
            The popularity score on spotify is a score given to every song and even artists to define their
            popularity compared to others. It mainly reflects how often a song gets streamed and how recent those
            streams are.
""")
st.pyplot(plot_popularity_distribution(df))

st.markdown("""
            The vast majority of tracks hover near 0 popularity, while only a small fraction achieve truly high popularity scores.
            This raises the question: what makes those outliers different?
            """)

st.header("Do audio features explain popularity?")

st.pyplot(plot_general_corr(df))

st.markdown("""
            Across the entire dataset, no audio feature (like energy, valence, or danceability) shows meaningful linear correlation with popularity.
            All correlation values fall in the “very weak” range, suggesting that if these features matter, the relationship isn't simple.
            """)

st.header("Are certain genres more favourable?")
st.pyplot(plot_top_genres(df))

st.pyplot(plot_genre_corr(df))

st.header("What really makes a popular song?")
# Conlusion / Key takeaways