import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patheffects import Stroke
from pathlib import Path
from plotting_utils import despine, remove_ticks


def draw_text(axis, text, cmap):
    family = "Pacifico"
    size = 100

    for x in np.linspace(0, 1, 15):
        lw, color = x * 225, cmap(1 - x)
        t = axis.text(
            0.5,
            0.45,
            text,
            size=size,
            color="none",
            weight="bold",
            va="center",
            ha="center",
            family=family,
            zorder=-lw,
        )
        t.set_path_effects([Stroke(linewidth=lw + 1, foreground="black")])
        t = axis.text(
            0.5,
            0.45,
            text,
            size=size,
            color="black",
            weight="bold",
            va="center",
            ha="center",
            family=family,
            zorder=-lw + 1,
        )
        t.set_path_effects([Stroke(linewidth=lw, foreground=color)])
    return axis


def save_word(word, cmap):
    fig, ax = plt.subplots(figsize=(8, 6), frameon=False)
    draw_text(axis=ax, text=f"{word}", cmap=cmap)
    despine(ax, which_spines=["top", "left", "bottom", "right"])
    remove_ticks(ax)
    static_path = Path(__file__).parent.parent.joinpath("results", f"{word}.pdf")
    fig.savefig(static_path)


def plot_static_word():
    fig, ax = plt.subplots(figsize=(8, 6), frameon=False)
    draw_text(axis=ax, text="static", cmap=plt.cm.twilight)
    despine(ax, which_spines=["top", "left", "bottom", "right"])
    remove_ticks(ax)
    return fig


def plot_dynamic_word():
    fig, ax = plt.subplots(figsize=(8, 6), frameon=False)
    draw_text(axis=ax, text="dynamic", cmap=plt.cm.terrain)
    despine(ax, which_spines=["top", "left", "bottom", "right"])
    remove_ticks(ax)
    return fig


if __name__ == "__main__":
    fig = plot_static_word()
    static_path = Path(__file__).parent.parent.joinpath("results", "static.svg")
    fig.savefig(static_path)

    fig = plot_dynamic_word()
    dynamic_path = Path(__file__).parent.parent.joinpath("results", "dynamic.svg")
    fig.savefig(dynamic_path)
