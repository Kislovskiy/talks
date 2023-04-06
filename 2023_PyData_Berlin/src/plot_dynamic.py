import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patheffects import Stroke, Normal

fig = plt.figure(figsize=(12, 5))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xticklabels([])
ax.set_yticklabels([])
plt.tick_params(
    axis="both", which="both", bottom=False, top=False, left=False, right=False
)
# family = "Pacifico"
size = 100
cmap = plt.cm.terrain
text = "Dynamic"

for x in np.linspace(0, 1, 10):
    lw, color = x * 225, cmap(1 - x)
    t = ax.text(
        0.5,
        0.45,
        text,
        size=size,
        color="none",
        weight="bold",
        va="center",
        ha="center",
        # family=family,
        zorder=-lw,
    )
    t.set_path_effects([Stroke(linewidth=lw + 1, foreground="black")])
    t = ax.text(
        0.5,
        0.45,
        text,
        size=size,
        color="black",
        weight="bold",
        va="center",
        ha="center",
        # family=family,
        zorder=-lw + 1,
    )
    t.set_path_effects([Stroke(linewidth=lw, foreground=color)])

plt.show()
fig.savefig("../../results/dynamic.pdf", dpi=300)
