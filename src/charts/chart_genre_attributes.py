import matplotlib.pylab as plt
import seaborn as sns
import pandas as pd
from src.style.style import genre_colors


def plot_genre_attributes(df: pd.DataFrame):

    attributes = ["danceability", "energy", "valence"]

    f, ax = plt.subplots(3, 1, figsize=(10, 14))

    f.tight_layout()

    for i, attr in enumerate(attributes):
        sns.boxplot(data=df, ax=ax.flat[i], x="playlist_genre", hue='playlist_genre', palette=genre_colors, y=attr)
        ax.flat[i].set_xlabel("")

    return f