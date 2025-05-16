import pandas as pd
import matplotlib.pyplot as plt
from src.data_loader import get_hit_threshold


def plot_dance_vs_energy(df: pd.DataFrame):
    hit_threshold = get_hit_threshold(df)
    df_pop = df[df['track_popularity'] >= hit_threshold]
    df_upop = df[df['track_popularity'] < hit_threshold]

    size = 0.5
    f, ax = plt.subplots()
    ax.scatter(df_upop['danceability'], df_upop['energy'], s=size)
    ax.scatter(df_pop['danceability'], df_pop['energy'], s=size)
    ax.set_title('Danceability vs Energy')
    ax.set_xlabel('Danceability')
    ax.set_ylabel('Energy')

    return f