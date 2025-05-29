import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_genre_corr(df: pd.DataFrame):

    f, ax = plt.subplots(figsize=(12, 8))

    genre_corrs = (
    df.groupby("playlist_genre")[["energy", "valence", "danceability", "tempo", "speechiness"] + ["track_popularity"]]
      .apply(lambda g: g.corr(numeric_only=True)["track_popularity"]
             .drop("track_popularity"))
    )[["energy", "valence", "danceability", "tempo", "speechiness"]]

    sns.heatmap(genre_corrs.T, annot=True, center=0, ax=ax)

    ax.set_title("Correlations to popularity")
    ax.set_ylabel("Characteristics")
    ax.set_xlabel("Genre")

    #ax.legend(fontsize=16)

    return f