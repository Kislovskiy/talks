from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt


def plot_sin():
    plt.xkcd()
    fig, ax = plt.subplots()
    fnc = "sin"
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    ax.plot(x, getattr(np, fnc)(x))

    ax.set_yticks([-1, 1])
    ax.set_yticklabels(["-1", "+1"])

    ax.set_xticks([-np.pi, -np.pi / 2, np.pi / 2, np.pi])
    ax.set_xticklabels(["π-", "π-/2", "π+/2", "π+"])

    ax.set_title(f"{fnc}")

    ax.spines[["bottom", "left"]].set_position(("data", 0))
    ax.spines[["top", "right"]].set_visible(False)

    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False, zorder=10)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False, zorder=10)
    
    return fig


if __name__ == "__main__":
    results_dir = Path(__file__).resolve().parent.parent.joinpath("results")
    results_dir.mkdir(parents=True, exist_ok=True)
    fig = plot_sin()
    fig.savefig(
        f"{results_dir}/sin.svg", format="svg", bbox_inches="tight", pad_inches=0.5
    )
