import streamlit as st
from src.data_loader import load_dataframe, calc_r2_scores
from src.charts.chart_genre_attributes import plot_genre_attributes
from src.charts.chart_genres import plot_top_genres
from src.charts.chart_popularity import plot_popularity_distribution
from src.charts.chart_general_corr import plot_general_corr
from src.charts.chart_genre_corr import plot_genre_corr
from src.charts.chart_rf_regression import plot_rfr_results
from src.style.style import apply_theme

# --- Page Config ---
st.set_page_config(
    page_title="Anatomy of a Hit Song",
    layout="centered",
    initial_sidebar_state="auto",
)

# --- Cache Data ---
@st.cache_data
def load_data():
    return load_dataframe()

@st.cache_data
def load_r2_scores(df):
    return calc_r2_scores(df)

# --- Apply Global Style ---

apply_theme()

# --- Load Data ---

df = load_data()
r2 = load_r2_scores(df)

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
            popularity compared to others. It mainly reflects user engagement and listening trends.
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
            All correlation values fall in the “very weak” range, suggesting that if these features matter, the relationship isn't linear.
            """)

st.header("Maybe it depends on the genre?")

st.pyplot(plot_top_genres(df))

st.markdown("""
            Genres like Pop and Latin produce more “hits” than others like EDM or Rock.
            This would suggest that popularity might be genre dependent. Since genres generally categorize different sounds, it
            is also expected that these genres differ in sound features.
            """)

st.pyplot(plot_genre_attributes(df))

st.markdown("""
            These boxplots show how audio characteristics like danceability, energy, and valence vary across genres. 
            For example, Latin music is typically more danceable and positive, while Rock tends to be higher energy but not really providing much danceability.
            """)

st.markdown("""
            This highlights that the genres do differ in popularity and sound profile but when we take a look
            at the correlations within each genre, we still cant find any indication that audio features can predict popularity.
            """)

st.pyplot(plot_genre_corr(df))

st.markdown("""
            Most correlations are weak, some genres like rap and r&b show slight associations with features like danceability or valence. 
            These differences suggest that popular songs may share certain audio features, but those features do not strongly define what makes a song a hit.
            """)

st.header("What about nonlinear relations?")

st.pyplot(plot_rfr_results(r2))

st.markdown("""
            Even advanced non linear models like random forests fail to predict popularity using audio features. 
            For each genre, R² values are very low, often near or below zero. Majority are even performing worse than a
            dummy model using averages. This confirms that the popularity cant be predicted based on these features.
            """)

st.header("What really makes a popular song?")

st.markdown("""
            While popular songs share some of these audio features like slightly higher danceability in the rap genre,
            these characteristics do not predict popularity at all.

            Attempts to model popularity based on audio features result in low predictive power. Even when separated by genre or exploring more complex patterns, 
            audio alone does not tell the full story.

            This means that other factors like artist reputation, marketing, social media and playlist placement likely play a far greater role in song popularity on Spotify.
            """)