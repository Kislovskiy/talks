from matplotlib import pyplot as plt


def despine(axis: plt.Axes):
    return axis.spines[["top", "right"]].set_visible(False)


def remove_ticks(axis: plt.Axes):
    axis.tick_params(axis="both", which="both", length=0)
    axis.set_xticks([])
    axis.set_yticks([])
    return axis


def add_arrows_to_axis(axis: plt.Axes):
    xmin, xmax = axis.get_xlim()
    ymin, ymax = axis.get_ylim()
    axis.plot(
        xmin, ymax, "^k", transform=axis.get_yaxis_transform(), clip_on=False, zorder=10
    )
    axis.plot(
        xmax, ymin, ">k", transform=axis.get_xaxis_transform(), clip_on=False, zorder=10
    )
    return axis


def add_labels_to_lines(
    axis: plt.Axes, label: str, x_delta: float = 0.02, y_delta: float = 0
):
    for line in axis.lines:
        if line.get_label().startswith(label):
            latest_x, latest_y = line.get_data()

    axis.text(
        latest_x[-1] + x_delta,
        latest_y[-1] + y_delta,
        label,
        ha="left",
        va="center",
        fontsize=12,
    )

    return axis
