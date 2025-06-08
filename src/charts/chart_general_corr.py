import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.style.style import spotify_palette

def plot_general_corr(df: pd.DataFrame):
    # Prepare dataframe for correlations
    df = df.corr(numeric_only=True).drop(['track_popularity', 'is_hit'], axis=0)['track_popularity']

    f, ax = plt.subplots(figsize=(10, 8))

    sns.barplot(df, ax=ax)

    # Add colored zones to plot
    ax.axhspan(0.3, 0.5, color='green', alpha=0.05, label='Moderate Positive')
    ax.axhspan(0.1, 0.3, color='gray', alpha=0.03)
    ax.axhspan(-0.1, 0.1, color='gray', alpha=0.1, label='Very Weak')
    ax.axhspan(-0.3, -0.1, color='gray', alpha=0.03)
    ax.axhspan(-0.5, -0.3, color='blue', alpha=0.05, label='Moderate Negative')

    # Set label
    ax.set_ylabel("Correlation to popularity")

    # Index of last color in palette
    last_col = len(spotify_palette) - 1

    # Text annotation
    ax.annotate('Longer bars = stronger correlation\n(positive or negative)', xy=(1.5, -0.1),
            xytext=(1.4, -0.18), arrowprops=dict(arrowstyle='->', color=spotify_palette[last_col]), fontsize=9, color=spotify_palette[last_col])

    # Move Legend
    ax.legend(fontsize=14, loc=(0.65, 0.61))

    return f