from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt
from plotting_utils import despine


def plot_cos():
    plt.xkcd()
    fig, ax = plt.subplots()
    fnc = "cos"
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    ax.plot(x, getattr(np, fnc)(x))
    ax.set_title(f"{fnc}")

    ax.plot(x, getattr(np, fnc)(x))

    ax.set_yticks([-1, 1])
    ax.set_yticklabels(["-1", "+1"])

    ax.set_xticks([-np.pi, -np.pi / 2, np.pi / 2, np.pi])
    ax.set_xticklabels(["π-", "π-/2", "π+/2", "π+"])

    ax.spines[["bottom", "left"]].set_position(("data", 0))
    despine(axis=ax)

    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False, zorder=10)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False, zorder=10)

    ax.set_title(f"{fnc}")

    return fig


if __name__ == "__main__":
    results_dir = Path(__file__).resolve().parent.parent.joinpath("results")
    results_dir.mkdir(parents=True, exist_ok=True)
    fig = plot_cos()
    fig.savefig(
        f"{results_dir.joinpath('cos.svg')}",
        format="svg",
        bbox_inches="tight",
        pad_inches=0.5,
    )
