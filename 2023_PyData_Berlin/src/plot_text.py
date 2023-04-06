import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patheffects import Stroke
from pathlib import Path


def draw_text(axis, text, cmap):
    """_summary_

    Args:
        axis (_type_): _description_
        text (_type_): _description_
        cmap (_type_): _description_

    Returns:
        _type_: _description_
    """
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


def despine_axis(axis):
    """ """
    axis.spines[["top", "right", "bottom", "left"]].set_visible(False)
    plt.tick_params(
        axis="both", which="both", bottom=False, top=False, left=False, right=False
    )
    axis.set_xticklabels([])
    axis.set_yticklabels([])

    return axis


def save_word(word, cmap):
    fig, ax = plt.subplots(figsize=(8, 6), frameon=False)
    draw_text(axis=despine_axis(ax), text=f"{word}", cmap=cmap)
    static_path = Path(__file__).parent.parent.joinpath(f"results/{word}.pdf")
    fig.savefig(static_path)


if __name__ == "__main__":
    save_word(word="static", cmap=plt.cm.twilight)
    save_word(word="dynamic", cmap=plt.cm.terrain)
