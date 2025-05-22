import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.data_loader import load_dataframe, get_hit_threshold
from src.charts.chart_dance_energy import plot_dance_vs_energy
from src.charts.chart_genres import plot_top_genres

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
st.title("Anatomy of a Hit Song: What makes music popular on Spotify?")

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

df = load_data()

# preview
st.header("Data Preview")
st.markdown("Here's a preview of the dataset used for this analysis, showing the attributes provided by the Spotify API.")
st.dataframe(df.sample(5, random_state=55)[["track_name", "track_artist", "track_popularity", "playlist_genre", "danceability", "energy", "speechiness", "acousticness", "valence", "tempo"]].head())

# --- Charts ---
# Popularity chart
st.header("What is popularity on spotify?")
st.markdown("""
            The popularity score on spotify is a score given to every song and even artists to define their
            popularity compared to others. It mainly reflects how often a song gets streamed and how recent those
            streams are.
""")

st.header("How to define a hit song?")
st.markdown("To really find out what makes a hit song we first need to define what a hit song is.")
st.markdown("""
            Traditionally, a hit song is one that achieves widespread popularity. Often reaching the top of music charts, 
            going viral on social media, or dominating radio and streaming platforms.
""")
st.markdown(f"""
            For this analysis, we define a hit song as one that falls in the **top 5% of popularity scores** in our dataset.  
            This corresponds to a score of **≥ {int(get_hit_threshold(df))}**.
""")

st.header("Are certain genres more favourable?")
st.pyplot(plot_top_genres(df))


st.header("Does danceability and energy increase peoples interest?")
st.markdown("""
            A lot of people enjoy going to concerts or clubs to dance and feel the energy of music.
            This implies that hit songs would generally have high danceability and energy. 
""")
st.pyplot(plot_dance_vs_energy(df))
st.markdown("""
            Contrary to expectations, hit songs are not significantly more danceable or energetic than the general pool.
            
            The spread of hit songs is about the same as the normal spread of songs and there
            are no obvious clusters for optimal energy or danceability.
""")

st.header("Exploring mood and popularity")
st.markdown("""
            The valence attribute describes the positiveness of a track. Tracks with high valence sound more positive (e.g. happy, cheerful), 
            while tracks with low valence sound more negative (e.g. sad, depressed, angry).
""")
st.markdown("""
            People tend to share and engage more with positive content both online and socially. 
            If this trend carries into music, we would expect happier sounding songs (higher valence) to be more popular overall.
""")

st.header("Acoustic traits of a hit song")
st.markdown("""
            In an age of digitalization it is only expected that we also shifted to like music with electronical elements
            rather than pure acoustic tracks.
""")

st.header("The tempo sweet spot")

st.header("What really makes a hit song?")
# Conlusion / Key takeaways