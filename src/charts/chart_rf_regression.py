import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.style.style import spotify_palette

def plot_rfr_results(df: pd.DataFrame):
    f, ax = plt.subplots(figsize=(10, 6))

    last_col = len(spotify_palette) - 1

    sns.stripplot(data=df, x='genre', y='r2', hue='model', palette=[spotify_palette[0], spotify_palette[last_col]], dodge=True, marker='o', size=8, ax=ax)

    # Add annotation lines
    ax.axhline(0, color='red', linestyle='--', label='No predictive power')

    ax.axhline(0.6, color='gray', linestyle='--', label='Good predictive power (R² > 0.6)')

    # Add annotation texts
    ax.annotate('Dummy models\npredict the average', xy=(1.23, 0.015),
            xytext=(1, 0.1), arrowprops=dict(arrowstyle='->', color=spotify_palette[last_col]), fontsize=9, color=spotify_palette[last_col])

    ax.annotate('RF performs worse\nthan baseline', xy=(1.9, -0.09),
            xytext=(2.3, -0.08), arrowprops=dict(arrowstyle='->', color=spotify_palette[last_col]), fontsize=9, color=spotify_palette[last_col])

    # Set labels
    ax.set_ylabel('R² Score')
    ax.set_xlabel('Genre')
    
    # Enable legend
    ax.legend()

    f.tight_layout()
    
    return f