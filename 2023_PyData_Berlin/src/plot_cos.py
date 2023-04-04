from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt


def plot_cos():
    fig, ax = plt.subplots()
    fnc = "cos"
    x = np.linspace(0, 10, 100)
    ax.plot(x, getattr(np, fnc)(x))
    ax.set_title(f"{fnc}")
    return fig


if __name__ == "__main__":
    results_dir = Path(__file__).resolve().parent.parent.joinpath("results")
    results_dir.mkdir(parents=True, exist_ok=True)
    fig = plot_cos()
    fig.savefig(
        f"{results_dir}/cos.svg", format="svg", bbox_inches="tight", pad_inches=0.5
    )
