from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path
from matplotlib.collections import LineCollection
from plotting_utils import despine, remove_ticks


def visualize_lines_with_colormap(axis, X, Y, cmap, alpha):
    P = np.array([X, Y]).T.reshape(-1, 1, 2)
    S = np.concatenate([P[:-1], P[1:]], axis=1)
    C = cmap(np.linspace(0, 1, len(S)))
    L = LineCollection(S, color=C, alpha=alpha, linewidth=2)
    axis.add_collection(L)


def visualize_curves(axis, df, cmap=plt.get_cmap("twilight")):
    num_cols_start_with_y = sum([col.startswith("Y") for col in df.columns])
    for i, alpha in enumerate(np.linspace(0, 1, num_cols_start_with_y)):
        visualize_lines_with_colormap(axis, df["X"], df[f"Y_{i}"], cmap, alpha)
    axis.set_xlim(df["X"].min(), df["X"].max())
    axis.set_ylim(-2.0, 2.0)
    despine(axis, which_spines=["top", "right", "bottom", "left"])
    remove_ticks(axis)

    return axis


def plot_cmap_waves():
    data_curves_path = (
        Path(__file__).resolve().parent.parent.joinpath("data", "data_curves.csv")
    )
    df = pd.read_csv(data_curves_path)

    fig, ax = plt.subplots(nrows=3, ncols=1, figsize=(12, 10))
    ax[0] = visualize_curves(ax[0], df, plt.get_cmap("twilight"))
    ax[0].set_title("The same curves, different colormaps\ntwilight", loc="left")

    ax[1] = visualize_curves(ax[1], df, plt.get_cmap("binary"))
    ax[1].set_title("binary", loc="left")

    ax[2] = visualize_curves(ax[2], df, plt.get_cmap("Spectral"))
    ax[2].set_title("Spectral", loc="left")

    fig.tight_layout()
    return fig


if __name__ == "__main__":
    plt.xkcd()
    results_dir = Path(__file__).resolve().parent.parent.joinpath("results")
    results_dir.mkdir(parents=True, exist_ok=True)
    fig = plot_cmap_waves()
    fig.savefig(
        f"{results_dir.joinpath('cmap_waves.pdf')}",
        format="pdf",
        bbox_inches="tight",
        pad_inches=0.5,
    )
