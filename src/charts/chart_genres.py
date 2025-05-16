import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Definition für Hits
HIT_THRESHOLD = 80

def plot_top_genres(df):
    # Nur Hits (>80 Popularität) berücksichtigen
    data = df[df['track_popularity'] > HIT_THRESHOLD]
    genre_popularity = data.groupby('playlist_genre')['track_popularity'].mean().reset_index()
    genre_popularity = genre_popularity.sort_values(by='track_popularity', ascending=False)

    # Diagramm erstellen
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(x='playlist_genre', y='track_popularity', data=genre_popularity, palette='RdGy', ax=ax)
    
    # Achsenbeschriftungen und Titel
    ax.set_xticklabels(genre_popularity['playlist_genre'], rotation=0, ha='center', fontsize=14, fontweight='bold')
    ax.set_title('Durchschnittliche Popularität nach Genre (Hits > 80)', fontsize=20, fontweight='bold', pad=20)
    ax.set_xlabel('Genre', fontsize=16, fontweight='bold', labelpad=15)
    ax.set_ylabel('Durchschnittliche Popularität', fontsize=16, fontweight='bold', labelpad=15)
    plt.tight_layout()

    return fig
