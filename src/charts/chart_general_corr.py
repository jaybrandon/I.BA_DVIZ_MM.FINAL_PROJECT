import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_general_corr(df: pd.DataFrame):
    df = df.corr(numeric_only=True).drop(['track_popularity', 'is_hit'], axis=0)['track_popularity']

    f, ax = plt.subplots(figsize=(10, 8))

    sns.barplot(df, ax=ax)

    ax.axhspan(0.3, 0.5, color='green', alpha=0.05, label='Moderate Positive')
    ax.axhspan(0.1, 0.3, color='gray', alpha=0.03)
    ax.axhspan(-0.1, 0.1, color='gray', alpha=0.1, label='Very Weak')
    ax.axhspan(-0.3, -0.1, color='gray', alpha=0.03)
    ax.axhspan(-0.5, -0.3, color='blue', alpha=0.05, label='Moderate Negative')

    ax.set_ylabel("Correlation to popularity")

    ax.legend(fontsize=14, loc=(0.65, 0.61))

    return f