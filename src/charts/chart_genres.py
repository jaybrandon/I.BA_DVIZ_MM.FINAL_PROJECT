import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.data_loader import get_hit_threshold
from src.style.style import genre_colors

def plot_top_genres(df):
    hit_threshold = get_hit_threshold(df)

    total_per_genre = df.groupby('playlist_genre').size().rename('total_songs')

    hits_per_genre = df[df['is_hit'] == True].groupby('playlist_genre').size().rename('hit_songs')

    genre_stats = pd.concat([total_per_genre, hits_per_genre], axis=1).fillna(0)
    genre_stats['hit_ratio'] = (genre_stats['hit_songs'] / genre_stats['total_songs']) * 100

    genre_stats = genre_stats.sort_values(by='hit_ratio', ascending=False).reset_index()

    f, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(x='playlist_genre', y='hit_ratio', data=genre_stats, hue='playlist_genre', palette=genre_colors, legend=False, ax=ax)

    ax.set_xticklabels(genre_stats['playlist_genre'], ha='center', fontsize=14)
    ax.set_title('Percentage of successful songs per genre (top 5% popularity)'.format(hit_threshold), pad=20)
    ax.set_xlabel('Genre')
    ax.set_ylabel('Percentage of successful songs (%)')

    f.tight_layout()
    return f
