import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.data_loader import get_hit_threshold


def plot_dance_vs_energy(df: pd.DataFrame):
    f, ax = plt.subplots()

    sns.scatterplot(
        data=df[df["is_hit"] == False],
        x="danceability",
        y="energy",
        color="blue",
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
        color="orange",
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