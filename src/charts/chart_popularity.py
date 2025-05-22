import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_popularity_distribution(df: pd.DataFrame):
    # Stil setzen
    sns.set_style("whitegrid")
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

    # Hintergrund entfernen
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_color("#ddd")
    plt.gca().spines['bottom'].set_color("#ddd")
    
    # Gitterlinien anpassen
    plt.grid(axis='y', linestyle='--', alpha=0.6, color="#ddd")

    # Layout verbessern
    plt.tight_layout()

    return plt
