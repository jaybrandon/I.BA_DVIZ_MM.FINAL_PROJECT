import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

spotify_palette = [
    "#1ed760",
    "#3bb95c",
    "#479b58",
    "#4b7e53",
    "#4b624d",
    "#474747"
]

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
