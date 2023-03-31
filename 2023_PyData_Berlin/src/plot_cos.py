from pathlib import Path
import numpy as np
from matplotlib import pyplot as plt

def plot_cos():
    results_dir = Path(__file__).resolve().parent.parent/"results"
    results_dir.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots()
    fnc = "cos"
    x = np.linspace(0, 10, 100)
    ax.plot(x, getattr(np, fnc)(x))
    ax.set_title(f"{fnc}")
    fig.savefig(
        f"{results_dir}/{fnc}.pdf", format="pdf", bbox_inches="tight", pad_inches=0.5
    )

if __name__ == "__main__":
    plot_sine()
