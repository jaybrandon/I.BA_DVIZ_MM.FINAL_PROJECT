import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.style.style import spotify_palette

def plot_dance_vs_energy(df: pd.DataFrame):
    f, ax = plt.subplots()

    sns.scatterplot(
        data=df[df["is_hit"] == False],
        x="danceability",
        y="energy",
        color=spotify_palette[len(spotify_palette) - 1],
        alpha=0.25,
        s=12,
        edgecolor=None,
        ax=ax,
        label='False'
    )

    sns.scatterplot(
        data=df[df["is_hit"] == True],
        x="danceability",
        y="energy",
        color=spotify_palette[0],
        alpha=0.6,
        s=14,
        edgecolor=None,
        ax=ax,
        label="True"
    )
    plt.legend(title="Hit Song")
    ax.set_xlabel('Danceability')
    ax.set_ylabel('Energy')

    return f