import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_popularity_distribution(df: pd.DataFrame):
    # Create figure and axis
    f, ax = plt.subplots(figsize=(14, 8))

    # Histogram
    sns.histplot(
        data=df,
        x='track_popularity',
        bins=30,
        kde=False,
        alpha=0.8,
        edgecolor='black',
        linewidth=0.5,
        ax=ax
    )

    # Set titles and labels
    ax.set_title('Popularity Distribution of All Songs')
    ax.set_xlabel('Popularity')
    ax.set_ylabel('Frequency')

    # Customize tick labels
    ax.set_xticks(range(0, 101, 10))

    # Customize grid
    ax.grid(axis='y')

    # Apply tight layout
    f.tight_layout()

    return f
