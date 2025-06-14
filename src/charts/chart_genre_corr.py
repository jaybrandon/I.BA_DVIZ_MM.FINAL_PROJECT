import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.style.style import correlation_cmap

def plot_genre_corr(df: pd.DataFrame):

    f, ax = plt.subplots(figsize=(12, 8))

    # Create dataframe with correlation matrix
    genre_corrs = (
        df.groupby("playlist_genre")[["energy", "valence", "danceability", "tempo", "speechiness", "track_popularity"]]
          .apply(lambda g: g.corr(numeric_only=True)["track_popularity"]
              .drop("track_popularity"))
    )

    sns.heatmap(genre_corrs.T, annot=True, center=0, vmin=-1, vmax=1, cmap=correlation_cmap, ax=ax)

    # Add vertical lines to separate genres
    ax.vlines([1, 2, 3, 4, 5], *ax.get_ylim(), colors='#474747', linestyles='solid', linewidth=1)

    # Set labels
    ax.set_title("Correlations to popularity")
    ax.set_ylabel("Audio feature")
    ax.set_xlabel("Genre")

    return f