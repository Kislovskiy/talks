from matplotlib import pyplot as plt
from pathlib import Path
import numpy as np

from plotting_utils import (
    despine,
    remove_ticks,
    add_arrows_to_axis,
    add_labels_to_lines,
)


def y(x):
    return x + np.sin(x * x * 8) / 4


def plot_common_chart():
    plt.xkcd()
    fig, ax = plt.subplots(figsize=(6, 4))

    ax.set_title("Title", loc="left", fontweight="bold", fontsize=18, pad=20)

    ax.set_ylabel(
        "y-label", fontsize=12, labelpad=10, rotation=0, loc="top", fontstyle="italic"
    )
    ax.set_xlabel("x-label", fontsize=12, labelpad=10, loc="right", fontstyle="italic")

    x = np.linspace(0, 1, 100)
    ax.plot(x, y(x), linewidth=4, color="black", label="label 1")
    ax.plot(x, x, linewidth=4, color="lightsteelblue", label="label 2")

    ax.set_ylim(bottom=0)
    ax.set_xlim(left=0, right=1)

    ax.scatter(0.5, y(0.5), s=100, color="indianred", zorder=10)
    ax.annotate(
        "Data Point",
        xy=(0.5, y(0.5)),
        xytext=(0.5, y(0.5) + 0.1),
        arrowprops=dict(arrowstyle="->"),
        zorder=11,
    )

    add_labels_to_lines(ax, "label 1")
    add_labels_to_lines(ax, "label 2")
    despine(ax)
    add_arrows_to_axis(ax)
    remove_ticks(ax)

    ax.text(
        x=0,
        y=-0.2,
        s="Notes/Sources/Credits:_________",
        fontsize=12,
        ha="left",
        transform=ax.transAxes,
    )

    fig.tight_layout()

    return fig


if __name__ == "__main__":
    results_dir = Path(__file__).resolve().parent.parent.joinpath("results")
    results_dir.mkdir(parents=True, exist_ok=True)
    fig = plot_common_chart()
    save_path = results_dir.joinpath("common_chart.pdf")
    fig.savefig(f"{save_path}", format="pdf", bbox_inches="tight", pad_inches=0.5)
