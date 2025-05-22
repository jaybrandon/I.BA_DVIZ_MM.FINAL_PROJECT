import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_popularity_distribution(df: pd.DataFrame):
    plt.figure(figsize=(14, 8))

    # Histogramm mit KDE
    sns.histplot(df['track_popularity'], bins=30, kde=False, color='royalblue', alpha=0.8, edgecolor='black', linewidth=0.5)

    # Titel und Achsen
    plt.title('Popularity Distribution of All Songs', fontsize=22, fontweight='bold', color="#333")
    plt.xlabel('Popularity', fontsize=18, fontweight='bold', color="#555")
    plt.ylabel('Frequency', fontsize=18, fontweight='bold', color="#555")

    # X-Achse anpassen
    plt.xticks(range(0, 101, 10), fontsize=12, color="#666")
    plt.yticks(fontsize=12, color="#666")
    
    # Gitterlinien anpassen
    plt.grid(axis='y')

    # Layout verbessern
    plt.tight_layout()

    return plt
