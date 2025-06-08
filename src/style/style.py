import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

spotify_palette = [
    "#1ed760",
    "#3bb95c",
    "#479b58",
    "#4b7e53",
    "#4b624d",
    "#474747"
]

genre_colors = {
    'pop': '#FF69B4',
    'rap': '#FFD700',
    'rock': '#808080',
    'latin': '#E63946',
    'r&b': '#6A5ACD',
    'edm': '#00CED1'
}

correlation_cmap = LinearSegmentedColormap.from_list(
    "correlation",
    [(0, "blue"), (0.5, "#ffffff"), (1, "#1ed760")]
)

def apply_theme():
    sns.set_theme(style="whitegrid")
    sns.set_palette(spotify_palette)

    plt.rcParams.update({
        "axes.prop_cycle": plt.cycler(color=spotify_palette),
        "axes.facecolor": "#ffffff",
        "figure.facecolor": "#ffffff",
        "text.color": "#000000",
        "axes.labelcolor": "#000000",

        "xtick.color": "#000000",
        "ytick.color": "#000000",

        "grid.color": "#cccccc",
        "grid.linestyle": "--",
        "grid.linewidth": 0.5,

        "axes.titlesize": 16,
        "axes.titleweight": "bold",
        "axes.labelsize": 13,
        "axes.labelweight": "bold",
        "axes.labelpad": 15,
        "xtick.labelsize": 11,
        "ytick.labelsize": 11,
        "legend.fontsize": 11,

        "lines.linewidth": 2,
        "lines.markersize": 6,

        "axes.spines.top": False,
        "axes.spines.right": False
    })
