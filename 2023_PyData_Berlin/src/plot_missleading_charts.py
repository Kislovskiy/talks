from matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec
from pathlib import Path
from plotting_utils import format_yticklabels_with_celsius, despine
import pandas as pd


def visualize_global_temp(ax):
    global_temp_path = (
        Path(__file__)
        .resolve()
        .parent.parent.joinpath("data", "global_temperature.txt")
    )

    pd.read_csv(
        global_temp_path,
        sep=" " * 5,
        skiprows=6,
        skipinitialspace=True,
        names=["year", "temp", "5-year-average"],
        engine="python",
    ).plot(
        ax=ax,
        x="year",
        y=["temp", "5-year-average"],
        legend=False,
        color=["dimgray", "black"],
    )

    despine(ax)

    ax.hlines(
        0, 1880, 2022, linestyles="dashed", color="lightgray", alpha=0.5, zorder=0
    )
    ax.set_xlim(1880, 2022)
    ax.set_xlabel("Year", fontsize=12, color="gray")

    return ax


def plot_missleading_chart():
    fig, ax = plt.subplots()
    visualize_global_temp(ax)
    ax.set_title(
        "Global Temperature Change, 1880-2022 (NASA/GISS)",
        loc="left",
        pad=10,
        fontsize=14,
        fontweight="bold",
        color="dimgray",
    )
    ax.set_ylabel(
        "Change relative to 1951-80 average (°C)", fontsize=12, color="dimgray"
    )

    fig = plt.figure(figsize=(14, 14))
    plt.xkcd()
    gspec = gridspec.GridSpec(nrows=12, ncols=12, figure=fig, hspace=40, wspace=40)

    ax1 = fig.add_subplot(gspec[:5, :8])
    visualize_global_temp(ax1)
    ax1.set_title(
        "Global Temperature Change, 1880-2022 (NASA/GISS)",
        loc="left",
        fontsize=20,
        pad=10,
        color="grey",
    )
    ax1.set_ylabel("Change relative to 1951-80 average (°C)", fontsize=12, color="grey")
    format_yticklabels_with_celsius(ax1)

    ax2 = fig.add_subplot(gspec[5:10, :8])
    visualize_global_temp(ax2)
    ax2.set_ylim(-5, 5)
    ax2.text(
        1885,
        5,
        "Misleading chart (1)",
        fontsize=12,
        color="red",
        ha="left",
        va="top",
        fontweight="bold",
    )
    format_yticklabels_with_celsius(ax2)

    ax3 = fig.add_subplot(gspec[10:, :])
    visualize_global_temp(ax3)
    ax3.text(
        1882,
        1.2,
        "Misleading chart (2)",
        fontsize=12,
        color="red",
        ha="left",
        va="top",
        fontweight="bold",
    )
    format_yticklabels_with_celsius(ax3)

    ax4 = fig.add_subplot(gspec[:10, 8:])
    visualize_global_temp(ax4)
    ax4.text(
        1885,
        1.2,
        "Misleading chart (3)",
        fontsize=12,
        color="red",
        ha="left",
        va="top",
        fontweight="bold",
    )
    format_yticklabels_with_celsius(ax4)

    return fig


if __name__ == "__main__":
    results_dir = Path(__file__).resolve().parent.parent.joinpath("results")
    results_dir.mkdir(parents=True, exist_ok=True)
    fig = plot_missleading_chart()
    save_path = results_dir.joinpath("missleading_charts.svg")
    fig.savefig(f"{save_path}", format="svg", bbox_inches="tight", pad_inches=0.5)
