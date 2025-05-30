import matplotlib.pylab as plt
import seaborn as sns
import pandas as pd


def plot_genre_attributes(df: pd.DataFrame):

    attributes = ["danceability", "energy", "valence"]

    f, ax = plt.subplots(3, 1, figsize=(7, 12))

    f.tight_layout()

    for i, attr in enumerate(attributes):
        sns.boxplot(data=df, ax=ax.flat[i], x="playlist_genre", y=attr)
        ax.flat[i].set_xlabel("")

    return f